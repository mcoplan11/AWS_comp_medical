import argparse
import json
import re
from datetime import datetime
from pathlib import Path

import boto3
import pandas as pd
from numpyencoder import NumpyEncoder
from tqdm import tqdm
import post_process_results_and_analysis
from utils import list_of_lvef_entities, pre_process_text, SAVE_OUTPUT_FOLDER

parser = argparse.ArgumentParser()
parser.add_argument("dataset_file_path", required=False)
args = parser.parse_args()

date_time = datetime.now().strftime("%m_%d_%Y_%H:%M:%S")

session = boto3.Session(profile_name='mitch_test')
client = session.client(service_name='comprehendmedical', verify=False)

global output
output = {}

list_of_lvef_entities_query = [
    'LEFT VENTRICULAR EJECTION FRACTION'
    , 'LEFT VENTRICULAR EJECTION FRATION'
    , 'LVEF'
    , 'SYSTOLIC FUNCTION'
    , 'SYSTOLIC DYSFUNCTION'
    , ' EF '
    , 'LVSD'
    , 'LEFT VENTRICULAR SYSTOLIC DYSFUNCTION'
    , 'LEFT VENTRICULAR SYSTOLIC FUNCTION'
    , 'EJECTION FRACTION'
]

regex_keywords = '|'.join(f'({p})' for p in list_of_lvef_entities_query)


def extract_lvef_text(text: str = '', patient_id: int = 0):
    # result = client.detect_entities(Text=text)
    if text == '':
        print('!!! document is blank !!!')
        return
    text = pre_process_text(text)
    if text == '':
        return
    result = client.detect_entities_v2(Text=text)
    entities = result['Entities']
    data = {}
    cases = []
    for entity in entities:
        case = {}
        if entity['Text'].upper() in list_of_lvef_entities:
            if 'Attributes' in entity:
                for attrib in entity['Attributes']:
                    if attrib['Type'] == 'TEST_VALUE':
                        case['Value'] = attrib['Text']
                        case['Score'] = attrib['Score']
                        cases.append(case)
    data['cases'] = cases
    data['text'] = text
    output[patient_id] = data


if __name__ == '__main__':
    # load data
    file = '/Users/Mitchell_Coplan/PycharmProjects/AWS_comp_medical/dataset/mtsamples 2.csv'
    data = pd.read_csv(args)
    transcription = data['transcription']
    filter_text = []
    for item in transcription:
        # only process text that has keywords to save on compute
        if re.search(regex_keywords, str(item), flags=re.I):
            # excluding large notes to save compute costs
            if len(item) < 3000:
                filter_text.append(item)

    print(f'number of docs: {len(filter_text)}')

    for i, text in tqdm(enumerate(filter_text)):
        print(i)
        extract_lvef_text(text=text, patient_id=i)

    output_file = SAVE_OUTPUT_FOLDER / str(date_time + '.json')
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=4, sort_keys=True, cls=NumpyEncoder)

    #run some analysis
    post_process_results_and_analysis.run()
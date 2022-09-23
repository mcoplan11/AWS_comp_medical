import boto3
from utils import list_of_lvef_entities, pre_process_text
# from ocr_images import ocr_image
import json
from numpyencoder import NumpyEncoder
from datetime import datetime
from pathlib import Path
import argparse
from utils import SAVE_OUTPUT_FOLDER


parser = argparse.ArgumentParser()
parser.add_argument("image_file_path", required=False)
args = parser.parse_args()

date_time = datetime.now().strftime("%m_%d_%Y_%H:%M:%S")

session = boto3.Session(profile_name='mitch_test')
client = session.client(service_name='comprehendmedical', verify=False)

global output
output = {}

# SAMPLE TEXT FOR TESTING
text = '''
3. Normal LV systolic function with left ventricular ejection fration of 51%
4. LVEF is 33%
5. Systolic function of 23 percent 
2.  Mild hypertensive cardiomyopathy with an EF of 48%
'''

# Clinical logic defines minimum LVEF to be only relevant value.  This value can change over time but rarely goes up

def extract_lvef(ocr_image_path: str = 'test'):
    # result = client.detect_entities(Text=text)
    text = ''
    with open(ocr_image_path) as f:
        text = f.read()
        f.close()
    # result = client.detect_entities(Text=text)
    if text == '':
        print('!!! document is blank !!!')
        return
    text = pre_process_text(text)
    if text == '':
        return
    result = client.detect_entities_v2(Text=text)
    entities = result['Entities']
    cases = []
    for entity in entities:
        case = {}
        if entity['Text'].upper() in list_of_lvef_entities:
            if entity['Attributes']:
                for attrib in entity['Attributes']:
                    if attrib['Type'] == 'TEST_VALUE':
                        case['Value'] = float(attrib['Text'])
                        case['Score'] = attrib['Score']
                        cases.append(case)
    output[ocr_image_path] = cases


if __name__ == '__main__':
    image_path = '/Users/Mitchell_Coplan/PycharmProjects/AWS_comp_medical/image_texts/test.txt'
    #image_path = ocr_image(args)
    extract_lvef(image_path)
    print(output)
    output_file = SAVE_OUTPUT_FOLDER / str(date_time + '.json')
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=4, sort_keys=True, cls=NumpyEncoder)
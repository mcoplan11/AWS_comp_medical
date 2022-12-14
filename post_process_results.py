import glob
import json
import os
import re
from pathlib import Path
from utils import SAVE_OUTPUT_FOLDER
from numpyencoder import NumpyEncoder
from datetime import datetime
import matplotlib.pyplot as plt

date_time = datetime.now().strftime("%m_%d_%Y_%H:%M:%S")



def run():
    list_of_results_files = glob.glob(str(SAVE_OUTPUT_FOLDER) + '/[0-9]' + '*')
    latest_results_file = max(list_of_results_files, key=os.path.getctime)

    print(f'latest_results_file: {latest_results_file}')
    results_data = json.loads(Path(latest_results_file).read_text())

    # Find patients with Ejection fraction <35%
    LVEFs = {}
    for patient_id, content in results_data.items():
        # print(patient_id)
        # print(content)
        LVEF = 100
        for case in content['cases']:
            try:
                value_hold = 100
                values = re.split('-|to', case['Value'])
                for value in values:
                    value = float(re.sub('[^0-9]', '', value))
                    if value < value_hold:
                        value_hold = value
            except:
                print(f"could not convert {case['Value']} to float")
                continue
            if value < LVEF:
                LVEF = value
                LVEFs[patient_id] = LVEF

    output_file = SAVE_OUTPUT_FOLDER / str('post_process_' + date_time + '.json')
    with open(output_file, 'w') as f:
        json.dump(LVEFs, f, indent=4, sort_keys=True, cls=NumpyEncoder)

if __name__ == '__main__':
    run()
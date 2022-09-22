import glob
import json
import glob
import json
import os
import re
from datetime import datetime
from pathlib import Path
from process_image import SAVE_OUTPUT_FOLDER
import tqdm as tqdm

list_of_results_files = glob.glob(str(SAVE_OUTPUT_FOLDER) + '/*')
latest_results_file = max(list_of_results_files, key=os.path.getctime)


print(f'latest_results_file: {latest_results_file}')
results_data = json.loads(Path(latest_results_file).read_text())


#Find patients with Ejection fraction <35%
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

n = 0
ids= []
for patient_id, LVEF in LVEFs.items():
    if LVEF <= 35.0:
        n += 1
        ids.append(patient_id)

print(f'Identified {13} patients with LVEF >= 35.  These patient_ids should are recommended for clinical chart review: \n {ids}')
import glob
import json
import os
from pathlib import Path
from utils import SAVE_OUTPUT_FOLDER
import matplotlib.pyplot as plt



def run():
    list_of_results_files = glob.glob(str(SAVE_OUTPUT_FOLDER) + '/post_process' + '*')
    latest_results_file = max(list_of_results_files, key=os.path.getctime)

    print(f'latest_results_file: {latest_results_file}')
    LVEFs = json.loads(Path(latest_results_file).read_text())

    n = 0
    mild = 0
    mod = 0
    sev = 0
    ids_mod = []
    ids_sev = []
    for patient_id, LVEF in LVEFs.items():
        n+=1
        if LVEF <= 51.0 and LVEF >= 41.0:
            mild += 1
        if LVEF <= 40.0 and LVEF >= 30.0:
            mod += 1
            ids_mod.append(patient_id)
        if LVEF < 30.0:
            sev += 1
            ids_sev.append(patient_id)
    '41% to 51%	30% to 40%	Below 30%'
    # 'I50.30' #Unspecified diastolic (congestive) heart failure
    print('Scanned 5000 medical charts for LVEF')
    print(f'Found LVEF for {n} patients')
    print(f'Found LVEF for {mild} patients with mildly abnormal results (41% to 51%)')
    print(f'Found LVEF for {mod} patients with moderately abnormal results (30% to 40%)')
    print(f'Found LVEF for {sev} patients with severely abnormal results (Below 30%)')

    print(
        f'The following patients_id\'s are recommended for clinical chart review to determine if billing codes (I50.20) need to be added: \n {ids_mod}')


    print(
        f'The following patients_id\'s are recommended for clinical chart review to determine if complex cardiac implantable electronic devices needed and billing codes (I50.20) need to be added: \n {ids_sev}')



    # creating the bar plot of data
    courses = ["Mildly abnormal (symptoms with physical activity)", "Moderately abnormal", "Severely abnormal (life-threatening complications)"]
    values = [mild, mod, sev]

    fig = plt.figure(figsize=(10, 5))
    plt.bar(courses, values, color='maroon',
            width=0.4)

    # plt.xlabel("Number of Patients")
    plt.ylabel("Number of Patients")
    plt.title("Number of Patients with LVEF Identified")
    plt.show()

if __name__ == '__main__':
    run()
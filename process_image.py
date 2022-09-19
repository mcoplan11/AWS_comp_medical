import boto3
from utils import list_of_lvef_entities

session = boto3.Session(profile_name='mitch_test')
client = session.client(service_name='comprehendmedical', verify=False)

#OCR Image to get text
patient_id = 1
text = None
text = '''
3. Normal LV systolic function with left ventricular ejection fration of 51%
4. LVEF is 33%
5. Systolic function of 23 percent 
'''


# result = client.detect_entities(Text=text)
result = client.detect_entities_v2(Text=text)
output = {}
entities = result['Entities']
cases = []
for entity in entities:
    if entity['Text'].upper() in list_of_lvef_entities:
        if entity['Attributes']:
            for attrib in entity['Attributes']:
                if attrib['Type']=='TEST_VALUE':
                    cases.append(attrib['Text'])
    #TODO expand to make this more robust
    output[patient_id] = min(cases)

print(output)

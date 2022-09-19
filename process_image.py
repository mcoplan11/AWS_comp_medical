import boto3
from utils import list_of_lvef_entities

session = boto3.Session(profile_name='mitch_test')
client = session.client(service_name='comprehendmedical', verify=False)

#OCR Image to get text
text = None


result = client.detect_entities(Text=text)
entities = result['Entities']
for entity in entities:
    if entity in list_of_lvef_entities:


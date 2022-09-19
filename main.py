import boto3

session = boto3.Session(profile_name='mitch_test')
client = session.client(service_name='comprehendmedical', verify=False)
result = client.detect_entities(Text= 'LVEF 35%')
entities = result['Entities']
for entity in entities:
    print('Entity', entity)

# from botocore.session import Session
# print(Session().get_config_variable('ca_bundle'))


# import ssl
# print(ssl.get_default_verify_paths())
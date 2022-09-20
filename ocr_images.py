#modified https://github.com/aws-samples/amazon-textract-and-comprehend-medical-document-processing/blob/main/1.Data_Processing.ipynb
import boto3
import sagemaker
import trp
import color

SAVE_IMAGE_TEXTS_FOLDER = '/Users/Mitchell_Coplan/PycharmProjects/AWS_comp_medical/image_texts'
bucket = sagemaker.Session().default_bucket()



#OCR Image to get text
def ocr_image(image_path: str = '', textractObjectName: str = ''):
    # Upload medical report file
    boto3.Session().resource('s3').Bucket(bucket).Object(textractObjectName).upload_file(image_path)
    textract = boto3.client('textract')
    response = textract.start_document_analysis(
        DocumentLocation={
            'S3Object': {
                'Bucket': bucket,
                'Name': textractObjectName
            }},
        FeatureTypes=[
            'TABLES',
        ]
    )

    textractJobId = response["JobId"]
    pages = []
    response = textract.get_document_analysis(JobId=textractJobId)
    pages.append(response)
    nextToken = None
    if ('NextToken' in response):
        nextToken = response['NextToken']

    while (nextToken):
        response = textract.get_document_analysis(JobId=textractJobId, NextToken=nextToken)
        pages.append(response)
        print("Resultset page recieved: {}".format(len(pages)))
        nextToken = None
        if ('NextToken' in response):
            nextToken = response['NextToken']

    doc = trp.Document(pages)
    print("Total length of document is", len(doc.pages))
    for page in doc.pages:
        pageText = page.text
        file_output = SAVE_IMAGE_TEXTS_FOLDER / f'OCR_{image_path}_{page}.txt'
        with open(file_output, 'w') as f:
            for line in pageText:
                f.write(f"{line}\n")



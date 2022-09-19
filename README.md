# AWS_comp_medical

One of the most underutilized data assets in healthcare is free text written in clinical notes.  Developing systems to better harvest and then operationalize this natural language data could result in earlier interventions and decreased healthcare costs. While highly data rich, this text is notoriously difficult to understand and process. 

This project will utilize AWS for image OCR ([Textract](https://aws.amazon.com/textract/)) and [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/index.html) for entity recognition.


**Input:** _Sample medical chart image_
![](/Users/Mitchell_Coplan/PycharmProjects/AWS_comp_medical/Images/sample_1.png)

**Output:** _A patient's LVEF value_
![](/Users/Mitchell_Coplan/PycharmProjects/AWS_comp_medical/Images/output1.png)


To use:
Add an image to the image folder
-Run process image
-Examine the output csv data to identify if a patient's LVEF





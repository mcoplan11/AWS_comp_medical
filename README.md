# AWS_comp_medical

###Introduction
One of the most underutilized data assets in healthcare is free text written in clinical notes.  Developing systems to better harvest and then operationalize this natural language data could result in earlier interventions and decreased healthcare costs. While highly data rich, this text is notoriously difficult to understand and process. 

This project focus on identifying an essential measure of heart failure patients, left ventricular ejection fraction ([LVEF](https://my.clevelandclinic.org/health/articles/16950-ejection-fraction#:~:text=Left%20ventricular%20ejection%20fraction%20(LVEF,left%20side%20of%20the%20heart))). One study found that often times this metric is buried in free text, but with manual clinical review 27% of missed heart failure patients identified for a cardiologist consultation are eligible for complex complex cardiac implantable electronic devices.  Additionally 45% require medicines optimization, and 47% of patients audited require diagnosis codes adding to their medical record ([Kahn 2022](https://doi.org/10.1093/eurheartj/ehab629)). Identifying and treating this patients would lead to better patient outcomes and increased hostpial system revenue.

This project will utilize AWS for image OCR ([Textract](https://aws.amazon.com/textract/)) and [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/index.html) for entity recognition.

###How it works
**Input:** _Sample medical chart image (OCR boxes shown for visualization)_
![](/Users/Mitchell_Coplan/PycharmProjects/AWS_comp_medical/Images/sample_1.png)

**Output:** _A patient's LVEF value_
![](/Users/Mitchell_Coplan/PycharmProjects/AWS_comp_medical/Images/output1.png)

###How to use it
-Add an image to the image folder

-Run python `process_image.py --image_name `

-Examine the output csv data to identify if a patient's LVEF

###How it was developed
We fine tuned the data extraction based on this [synthetic dataset](https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions).  

###Citations
Matthew Kahn, Antony D Grayson, Parminder S Chaggar, Marie J Ng Kam Chuen, Alison Scott, Carol Hughes, Niall G Campbell, Primary care heart failure service identifies a missed cohort of heart failure patients with reduced ejection fraction, European Heart Journal, Volume 43, Issue 5, 1 February 2022, Pages 405–412, https://doi.org/10.1093/eurheartj/ehab629



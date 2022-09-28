# Extraction of LVEF from medical chart text

## Introduction
One of the most underutilized data assets in healthcare is free text written in clinical notes.  Developing systems to better harvest and then operationalize this natural language data could result in earlier interventions, better health outcomes, and decreased healthcare costs. While highly data rich, this text is notoriously difficult to understand and process. 

Heart failure is the leading cause of hospitalizations and costs $216 billion per year in the USA ([CDC](https://www.cdc.gov/dhdsp/)). This project focuses on identifying an essential measure of heart failure patients, left ventricular ejection fraction ([LVEF](https://my.clevelandclinic.org/health/articles/16950-ejection-fraction#:~:text=Left%20ventricular%20ejection%20fraction%20(LVEF,left%20side%20of%20the%20heart))). LVEF measures how well your heart pumps blood.  In a healthy person, the LVEF is generally in the range of 55% to 75%. 

One study found the LVEF is often buried in medical free text and which **can result in patients missing out on life-saving care** ([Chaggar 2020](https://doi.org/10.1093/europace/euaa162.332)).  Another study ([Kahn 2022](https://doi.org/10.1093/eurheartj/ehab629)) showed that a manual clinical review led to a 47% increase in the number of patients that required adding heart failure diagnosis codes to their medical record. Additionally, 27% of missed heart failure patients were eligible for [complex cardiac implantable electronic devices](https://my.clevelandclinic.org/health/treatments/16837-cardiac-implantable-electronic-device-replacement) and another 45% required medication optimization. **Identifying and treating these patients would improve patient outcomes and increase revenue for the hospital system providing care.**

Previous work to automate extraction of LVEF ([Kim 2017](https://www.sciencedirect.com/science/article/pii/S1532046417300205)) has some promising results, but further technological systems are needed to expand this commercially. This project will utilize AWS for image OCR ([Textract](https://aws.amazon.com/textract/)) and [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/index.html) for entity recognition and relationship extraction.

## What it does
### Input: 

**_Sample medical chart image (OCR boxes shown for visualization)_**

| ![Alt text](images/sample_1.png?raw=true) |
|-|

### Output:
**_A json file with all extracted patient's LVEF values_**

| ![Alt text](images/output1.png?raw=true) |
|-|

**_A summary of findings and clinical/billing implications_**


| ![Alt text](images/output_analysis.png?raw=true) |
|-|

## How to use it
Process by image:
* Add an image to the `image` folder

* Run python `process_image.py --{your_image_name}`

* Examine the output json data to identify a patient's LVEF

* Clinical evaluations for healthcare quality, billing codes, and medical interventions can be completed on the appropriate patients identified 


Process by csv:
* Add a csv to the `dataset` folder (Clinical text column must have the header `transcription`)

* Run python `process_dataset.py --{your_dataset_name}`

* Examine the output json data to identify a patient's LVEF

* Clinical evaluations for healthcare quality, billing codes, and medical interventions can be completed on the appropriate patients identified 

### How it was developed
We fine-tuned the data extraction based on this [synthetic dataset](https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions).  This dataset contains 5000 discharge summaries from various specialties. LVEF values for each patient were manually extracted by a clinical annotator.  We then created regex code and decision tree logic to augment the findings returned from [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/index.html) in order to improve our results for our specific use case.

### Citations
Matthew Kahn, Antony D Grayson, Parminder S Chaggar, Marie J Ng Kam Chuen, Alison Scott, Carol Hughes, Niall G Campbell, Primary care heart failure service identifies a missed cohort of heart failure patients with reduced ejection fraction, European Heart Journal, Volume 43, Issue 5, 1 February 2022, Pages 405–412, https://doi.org/10.1093/eurheartj/ehab629

P Chaggar, A D Grayson, N Connor, C Hughes, P1489
An audit of 215,000 patients on primary care registers using novel electronic searches to identify patients with heart failure requiring treatment optimisation and complex device therapies, EP Europace, Volume 22, Issue Supplement_1, June 2020, euaa162.332, https://doi.org/10.1093/europace/euaa162.332

Youngjun Kim, Jennifer H. Garvin, Mary K. Goldstein, Tammy S. Hwang, Andrew Redd, Dan Bolton, Paul A. Heidenreich, Stéphane M. Meystre,
Extraction of left ventricular ejection fraction information from various types of clinical reports,
Journal of Biomedical Informatics,
Volume 67,
2017,
Pages 42-48,
ISSN 1532-0464,
https://doi.org/10.1016/j.jbi.2017.01.017.

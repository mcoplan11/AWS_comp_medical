# AWS_comp_medical

### Introduction
One of the most under-utilized data assets in healthcare is free text written in clinical notes.  Developing systems to better harvest and then operationalize this natural language data could result in earlier interventions and decreased healthcare costs. While highly data rich, this text is notoriously difficult to understand and process. 

This project focus on identifying an essential measure of heart failure patients, left ventricular ejection fraction ([LVEF](https://my.clevelandclinic.org/health/articles/16950-ejection-fraction#:~:text=Left%20ventricular%20ejection%20fraction%20(LVEF,left%20side%20of%20the%20heart))). One study found that often times this metric is buried in free text, but with manual clinical review 27% of missed heart failure patients identified for a cardiologist consultation are eligible for complex complex cardiac implantable electronic devices.  Additionally 45% require medicines optimization and 47% of patients audited require diagnosis codes added to their medical record ([Kahn 2022](https://doi.org/10.1093/eurheartj/ehab629)). *Identifying and treating these patients would lead to better patient outcomes and increased hospital system revenue.*

Previous work to extract LVEF ([Kim 2017](https://www.sciencedirect.com/science/article/pii/S1532046417300205)) has some promising results, but further technological systems are needed to expand this commercially. This project will utilize AWS for image OCR ([Textract](https://aws.amazon.com/textract/)) and [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/index.html) for entity recognition and relationship extraction.

### How it works
**Input:** _Sample medical chart image (OCR boxes shown for visualization)_
![Alt text](images/sample_1.png?raw=true)

**Output:** _A patient's LVEF value_
![Alt text](images/output1.png?raw=true)

### How to use it
* Add an image to the image folder

* Run python `process_image.py --image_name`

* Examine the output json data to identify a patient's LVEF

* Clinical evaluations for healthcare quality, billing codes, and medical interventions can be completed on the appropriate patients identified 

### How it was developed
We fine tuned the data extraction based on this [synthetic dataset](https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions).  This dataset contains 5000 discharge summaries from various specialties. LVEF values for each patient were manulally extracted by a clinical annotator.  We then created regex code to augment the findings returned from [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/index.html) in order to improve our results.

### Citations
Matthew Kahn, Antony D Grayson, Parminder S Chaggar, Marie J Ng Kam Chuen, Alison Scott, Carol Hughes, Niall G Campbell, Primary care heart failure service identifies a missed cohort of heart failure patients with reduced ejection fraction, European Heart Journal, Volume 43, Issue 5, 1 February 2022, Pages 405–412, https://doi.org/10.1093/eurheartj/ehab629

Youngjun Kim, Jennifer H. Garvin, Mary K. Goldstein, Tammy S. Hwang, Andrew Redd, Dan Bolton, Paul A. Heidenreich, Stéphane M. Meystre,
Extraction of left ventricular ejection fraction information from various types of clinical reports,
Journal of Biomedical Informatics,
Volume 67,
2017,
Pages 42-48,
ISSN 1532-0464,
https://doi.org/10.1016/j.jbi.2017.01.017.

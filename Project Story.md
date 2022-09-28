## Inspiration and Introduction
I have worked in the healthcare analytics space for about 10 years.  I have experience working for a large healthcare provider in the analytics and data architecture departments and also had the opportunity to develop NLP software for providers and payers. While I have a seen a tremendous amount of progress during this time, I still see many areas where advanced analytics could be utilized to improve patient outcomes. 

One of the most underutilized data assets in healthcare is free text written in clinical notes.  Developing systems to better harvest and then operationalize this natural language data could result in earlier interventions, better health outcomes, and decreased healthcare costs. While highly data rich, this text is notoriously difficult to understand and process. 

Heart failure is the leading cause of hospitalizations and costs $216 billion per year in the USA ([CDC](https://www.cdc.gov/dhdsp/)). This project focuses on identifying an essential measure of heart failure patients, left ventricular ejection fraction ([LVEF](https://my.clevelandclinic.org/health/articles/16950-ejection-fraction#:~:text=Left%20ventricular%20ejection%20fraction%20(LVEF,left%20side%20of%20the%20heart))). LVEF measures how well your heart pumps blood.  In a healthy person, the LVEF is generally in the range of 55% to 75%. 

One study found the LVEF is often buried in medical free text and which **can result in patients missing out on life-saving care** ([Chaggar 2020](https://doi.org/10.1093/europace/euaa162.332)).  Another study ([Kahn 2022](https://doi.org/10.1093/eurheartj/ehab629)) showed that a manual clinical review led to a 47% increase in the number of patients that required adding heart failure diagnosis codes to their medical record. Additionally, 27% of missed heart failure patients were eligible for [complex cardiac implantable electronic devices](https://my.clevelandclinic.org/health/treatments/16837-cardiac-implantable-electronic-device-replacement) and another 45% required medication optimization. **Identifying and treating these patients would improve patient outcomes and increase revenue for the hospital system providing care.**

Previous work to automate extraction of LVEF ([Kim 2017](https://www.sciencedirect.com/science/article/pii/S1532046417300205)) has some promising results, but further technological systems are needed to expand this commercially. This project will utilize AWS for image OCR ([Textract](https://aws.amazon.com/textract/)) and [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/index.html) for entity recognition and relationship extraction.

## What it does
We have built a system to extract the LVEF from medical charts and then provide analytics on the findings. The product can be utilized in two ways:
1. Input medical images

2. Input a csv with one column containing text from medical notes

The output is a json file containing the extract LVEF for each patient/image and summary statistics on the results.

_Example output summary_

![Alt text](images/output_analysis.png?raw=true)


## How we built it
We utilized a rule based extraction engine paired with Amazon Medical Comprehend and Textract. For any images being process, we used Textract to OCR the image and saved the results as a text file. We then developed code to take the text data and extract the LVEF value through Amazon Medical Comprehend.  In order to evaluate the effectiveness of this solution, we tested the extraction on this [synthetic dataset](https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions) after manually labeling the correct LVEF for each patient.  We then fine-tuned our pre and post processing functions based on the results we output from the synthetic dataset. 

## Challenges we ran into
Amazon Medical Comprehend is does an excellent job at extracting information for text. However, medical charts do not contain clean text data.  They consist of duplicate (copied over from previous encounters) notes and often have informational data in the chart. For example, if a medical note contained the text `Left ventricular ejection fraction in the range of 53% to 70% is considered normal`, LVEF might be extracted as `53% to 70%`. A human annotator of this sentence would likely understand that this is referring to LVEF in general, not the specific patient.  We were able to mediate this challenge through the use of a pre-processing function where these types of sentences where filtered out.  This function utilizes regex lookup queries and was developed through the error analysis of the synthetic dataset.

## Accomplishments that we're proud of
Utilizing our synthetic dataset of 5000 patient discharges, we were able to successfully extract the LVEF for 93 patients.  Additionally, 23 of those patients had LVEF values below 40% which means they would qualify for the I50.20 ICD billing code and 7 of those patients has severely reduced LVEF and might quality for cardiac implantable electronic devices.


When the above results are extrapolated to a larger health system seeing around 250,000 patients a year assuming similar ratios to ([Kahn 2022](https://doi.org/10.1093/eurheartj/ehab629)), we can estimate this would have led to a health system and their patients:

* **~40 patients receiving life-saving surgery to get cardiac devices**   ((7/5000) X 250,000 X 27% X 47%)
* **Additional ~$4.1 million in hospital revenue** ((23/5000) X 250,000 X 47% X 240 USD) [billing codes] + ($100,000 X 40) [cardiac surgeries] ([HHS](https://aspe.hhs.gov/sites/default/files/private/pdf/252376/Table1C.pdf))



## What we learned
Amazon Medical Comprehend is a powerful tool. However, its best use cases in healthcare will require significant pre and post processing of results in order to be clinically or commercially useful.  We developed these functions based on synthetic dataset that allowed us to find the outputs of our models. Future work utilizing Amazon Medical Comprehend will need to be developed in a similar manner. 

## What's next for Extraction of LVEF from medical chart text
We recommend licensing this technology out to large providers networks.  The consolidation of the healthcare market in the past 10-20 years has led to the rise of fragmented databases and coding documentation. Unfortunately, patients have suffered from this by "slipping through the cracks" and not receiving they care they need.  This technology could be used to rapidly iterate through provider's proprietary healthcare databases to extract structured LVEF data and obtain novel insight to their heart failure patient population. A refined list of patients with LVEF values would improve billing codes and identify patients that need referral to cardiology for advanced heart failure treatment, who would otherwise be forgotten.

Advanced heart failure patients often result in complex surgical intervention which is generally how large health systems generate a large share of their revenue.  **This solution improves the quality of patient care and healthcare systems are financially incentivized to implement it.**

## Citations
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
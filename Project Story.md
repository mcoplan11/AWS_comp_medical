## Inspiration and Introduction
I have worked in the healthcare analytics space for about 10 years.  While I have a seen a tremendous amount of progress during this time, I still see many areas where advanced analytics could be utilized to improve patient outcomes.  One of the most underutilized data assets in healthcare is free text written in clinical notes.  Developing systems to better harvest and then operationalize this natural language data could result in earlier interventions and decreased healthcare costs. While highly data rich, this text is notoriously difficult to understand and process. 

Heart failure is the bad.  LVEF is an important measure that is needed to effectively treat HF patients, but it is often buried in clinical notes.

## What it does
Our product will read through medical charts and extract the LVEF of patients.  

## How we built it
We utilized a rule based extraction engine paired with AWS healthcare NLP. 

## Challenges we ran into
TBD

## Accomplishments that we're proud of
Utilizing our synthetic dataset of 5000 patient discharges, we were able to successfully extract the LVEF for 93 patients.  Additionally, 23 of those patients had LVEF values below 40% which means they would qualify for the I50.20 ICD billing code and 7 of those patients has severely reduced LVEF and might quality for cardiac implantable electronic devices.  Assuming similar ratios to ([Kahn 2022](https://doi.org/10.1093/eurheartj/ehab629)), we can estimate this would have led to an **additional ~$50,000** ([HHS](https://aspe.hhs.gov/sites/default/files/private/pdf/252376/Table1C.pdf)) billing dollars and **1-2 patients receiving needed cardiac devices** at this synthetic organization.

## What we learned
Amazon Medical Comprehend is a powerful tool. However, it's strongest use cases in healthcare will require signicant pre and post processing of results in order to be clinically or commercially useful.  We develeped these functions based on synthetic dataset that allowed us to find the outputs of our models. Future work utilizing Amazon Medical Comprehend will need to be developed in a similar manner. 

## What's next for Extraction of LVEF from medical chart text
We recommend listening this technology out to large providers networks.  This technology would give them the ability to rapidly iterate through their proprietary healthcare databases in order to extract structured LVEF data for the entire patient population.  The data could then be utilized for   A refined list of patients with LVEF within a certain range should be referred to cardiology for advanced heart failure treatment. 

Advanced heart failure patients often result in complex surgical intervention which is generally how large health systems generate a large share of their revenue.  **Not only will this solution improve quality of patient care, but healthcare systems are also financially incentivized to do this**.

## Citations

Matthew Kahn, Antony D Grayson, Parminder S Chaggar, Marie J Ng Kam Chuen, Alison Scott, Carol Hughes, Niall G Campbell, Primary care heart failure service identifies a missed cohort of heart failure patients with reduced ejection fraction, European Heart Journal, Volume 43, Issue 5, 1 February 2022, Pages 405–412, https://doi.org/10.1093/eurheartj/ehab629

import re

list_of_lvef_entities = [
    'LEFT VENTRICULAR EJECTION FRACTION'
    , 'LEFT VENTRICULAR EJECTION FRATION'
    , 'LVEF'
    , 'SYSTOLIC FUNCTION'
    , 'SYSTOLIC DYSFUNCTION'
    , 'EF'
    , 'LVSD'
    , 'LEFT VENTRICULAR SYSTOLIC DYSFUNCTION'
    , 'LEFT VENTRICULAR SYSTOLIC FUNCTION'
    , 'EJECTION FRACTION'
]

#filter out common keywords/phrases that lead to false positives
regex_keywords = [
    r'LVEF less than (\d||d\d)% is considered NYHA',
    r'normal lvef is in the 55-70%',
    r'LEFT VENTRICULAR EJECTION FRACTION in the range of 53% to 70%',
]
regex_keywords = '|'.join(f'({p})' for p in regex_keywords)

def pre_process_text(text: str = ''):
    #TODO: add a spellcorrect here
    if re.search(regex_keywords, text, flags=re.I):
        print(f'!!! Filtering out this doc: {text}')
        return ''
    else:
        return text
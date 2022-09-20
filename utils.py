import re

regex_keywords = [
    r'LVEF less than (\d||d\d)% is considered NYHA',
    r'LEFT VENTRICULAR EJECTION FRACTION in the range of 50% to 70% is normal',
]
regex_keywords = '|'.join(f'({p})' for p in regex_keywords)


list_of_lvef_entities = [
    'LEFT VENTRICULAR EJECTION FRACTION'
    , 'LVEF'
    , 'SYSTOLIC FUNCTION'
    , 'SYSTOLIC DYSFUNCTION'
    , 'EF'
    , 'LVSD'
    , 'LEFT VENTRICULAR SYSTOLIC DYSFUNCTION'
    , 'LEFT VENTRICULAR SYSTOLIC FUNCTION'
    , 'EJECTION FRACTION'
]

def pre_process_text(text: str = ''):
    if re.search(regex_keywords, text, flags=re.I):
        print(f'!!! Filtering out this doc: {text}')
        return ''
    else:
        return text
import pandas as pd

def get_gita_verse(file_path = "data/bhagavad_gita.csv"):
    
    #load the dataset
    df = pd.read_csv('data/bhagavad_gita.csv')
    
    #create empty dictionary
    gita_verse = {}
    
    for index, row in df.iterrows():
        verse_number = str(row['verse_number']).strip()
        verse_in_sanskrit = str(row['verse_in_sanskrit']).strip()
        translation_in_english= str(row['translation_in_english']).strip()
        translation_in_hindi= str(row['translation_in_hindi']).strip()
        
        reference = f"{verse_number}\n{verse_in_sanskrit}\n{translation_in_english}\n{translation_in_hindi}"
        gita_verse[verse_number] = reference
        
    return gita_verse
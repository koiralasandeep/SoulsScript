import random
import csv
import pandas as pd


def change_gita_dataset(file_path =  'data/bhagavad_gita.csv'):
    
    df = pd.read_csv('data/bhagavad_gita.csv')
    
    #create list to store data
    gita_verses = []
    
    for index, row in df.iterrows():
        verse_number = str(row['verse_number']).strip()
        verse_in_sanskrit = str(row['verse_in_sanskrit']).strip()
        translation_in_english= str(row['translation_in_english']).strip()
        translation_in_hindi= str(row['translation_in_hindi']).strip()
        
        reference = f"{verse_number}\n{verse_in_sanskrit}\n{translation_in_english}\n{translation_in_hindi}"
        gita_verses.append(reference)
    return gita_verses

    
    
#getting random verse by reading csv file
def random_gita_verse():
    gita_verses = change_gita_dataset()
    return random.choice(gita_verses)

random_gita_verse()











               


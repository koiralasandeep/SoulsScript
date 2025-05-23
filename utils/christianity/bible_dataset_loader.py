import pandas as pd

def load_bible_dataset(file_path="data/KJV.csv"):
    #load the data
    df = pd.read_csv('data/KJV.csv')

    #create list to store the data
    bible_dataset = []

    for index, row in df.iterrows():
        book = str(row['Book']).strip()
        chapter = str(row['Chapter']).strip()
        verse = str(row['Verse']).strip()
        text = str(row['Text']).strip()
        
        reference = f"{book} {chapter}:{verse}"
        
        bible_dataset.append({
            "reference": reference,
            "text": text
        })
        
    print(f"Loaded {len(bible_dataset)} verses.")
    return bible_dataset
               


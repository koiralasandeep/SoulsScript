import random
import csv

#get random verse by reading csv file
def random_bible_verse():
    with open('data/bible.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

        # skip header if present
        if data[0][0].lower() == 'book':  # optional safety check
            data = data[1:]

        random_row = random.choice(data)

        # Assuming columns = [book, chapter, verse, text]
        book = random_row[0]
        chapter = random_row[1]
        verse = random_row[2]
        text = random_row[3]

        formatted = f"{book} {chapter}:{verse} \n {text}"
        return formatted

random_bible_verse()











               


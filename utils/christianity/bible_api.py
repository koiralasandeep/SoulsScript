import requests

def get_bible_verse(reference):
    """
    Fetched a Bible verse using bible-api.com
    reference: user input like 'John 3:16' or 'Psalm 23:1'
    """
    formatted_reference = reference.replace(" ", "%20")  # URL encode spaces
    url = f"https://bible-api.com/{formatted_reference}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        verse_text = data["text"]
        verse_ref = data["reference"]
        translation = data["translation_name"]

        return f'"{verse_text.strip()}"\n\n- {verse_ref} ({translation})'
    
    except Exception as e:
        print(f"Error fetching Bible verse: {e}")
        return "Unable to fetch Bible verse at this time."

from pathlib import Path
from gtts import gTTS

BASE_DIR = Path(__file__).resolve().parent
AUDIO_DIR = BASE_DIR / "audio"

vowels = [
    {"id": "a", "letter": "अ", "roman": "a"},
    {"id": "aa", "letter": "आ", "roman": "aa"},
    {"id": "i", "letter": "इ", "roman": "i"},
    {"id": "ee", "letter": "ई", "roman": "ee"},
    {"id": "u", "letter": "उ", "roman": "u"},
    {"id": "oo", "letter": "ऊ", "roman": "oo"},
    {"id": "ri", "letter": "ऋ", "roman": "ri"},
    {"id": "e", "letter": "ए", "roman": "e"},
    {"id": "ai", "letter": "ऐ", "roman": "ai"},
    {"id": "o", "letter": "ओ", "roman": "o"},
    {"id": "au", "letter": "औ", "roman": "au"},
    {"id": "am", "letter": "अं", "roman": "am"},
    {"id": "ah", "letter": "अः", "roman": "ah"},
]

consonants = [
    {"id": "ka", "letter": "क", "roman": "ka"},
    {"id": "kha", "letter": "ख", "roman": "kha"},
    {"id": "ga", "letter": "ग", "roman": "ga"},
    {"id": "gha", "letter": "घ", "roman": "gha"},
    {"id": "nga", "letter": "ङ", "roman": "nga"},
    {"id": "cha", "letter": "च", "roman": "cha"},
    {"id": "chha", "letter": "छ", "roman": "chha"},
    {"id": "ja", "letter": "ज", "roman": "ja"},
    {"id": "jha", "letter": "झ", "roman": "jha"},
    {"id": "nya", "letter": "ञ", "roman": "nya"},
    {"id": "ta_1", "letter": "ट", "roman": "ta"},
    {"id": "tha_1", "letter": "ठ", "roman": "tha"},
    {"id": "da_1", "letter": "ड", "roman": "da"},
    {"id": "dha_1", "letter": "ढ", "roman": "dha"},
    {"id": "na_1", "letter": "ण", "roman": "na"},
    {"id": "ta_2", "letter": "त", "roman": "ta"},
    {"id": "tha_2", "letter": "थ", "roman": "tha"},
    {"id": "da_2", "letter": "द", "roman": "da"},
    {"id": "dha_2", "letter": "ध", "roman": "dha"},
    {"id": "na_2", "letter": "न", "roman": "na"},
    {"id": "pa", "letter": "प", "roman": "pa"},
    {"id": "pha", "letter": "फ", "roman": "pha"},
    {"id": "ba", "letter": "ब", "roman": "ba"},
    {"id": "bha", "letter": "भ", "roman": "bha"},
    {"id": "ma", "letter": "म", "roman": "ma"},
    {"id": "ya", "letter": "य", "roman": "ya"},
    {"id": "ra", "letter": "र", "roman": "ra"},
    {"id": "la", "letter": "ल", "roman": "la"},
    {"id": "va", "letter": "व", "roman": "va"},
    {"id": "sha_1", "letter": "श", "roman": "sha"},
    {"id": "sha_2", "letter": "ष", "roman": "sha"},
    {"id": "sa", "letter": "स", "roman": "sa"},
    {"id": "ha", "letter": "ह", "roman": "ha"},
    {"id": "ksha", "letter": "क्ष", "roman": "ksha"},
    {"id": "tra", "letter": "त्र", "roman": "tra"},
    {"id": "gya", "letter": "ज्ञ", "roman": "gya"},
]

all_items = [("vowels", vowels), ("consonants", consonants)]

for folder_name, items in all_items:
    folder = AUDIO_DIR / folder_name
    folder.mkdir(parents=True, exist_ok=True)
    for item in items:
        file_path = folder / f"{item['id']}.mp3"
        if file_path.exists():
            print(f"Skipped existing: {file_path.name}")
            continue
        tts = gTTS(text=item["letter"], lang="hi", slow=False)
        tts.save(str(file_path))
        print(f"Saved: {file_path}")

print("Done.")

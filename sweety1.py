!pip install autocorrect
from autocorrect import Speller
def autocorrect_text(text):
    spell=Speller(lang='en')
    corrected_text=spell(text)
    return corrected_text
input_text="Babi"
corrected_text=autocorrect_text(input_text)
print(corrected_text)
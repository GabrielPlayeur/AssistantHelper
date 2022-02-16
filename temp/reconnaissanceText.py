from spellchecker import SpellChecker
#indexer

spell = SpellChecker(language='fr')

misspelled = ['salu', 'sossicon', 'candier','météo']
misspelled = spell.unknown(misspelled)
for word in misspelled:
    print("original word: "+ word)
    print("corrected word: "+ spell.correction(word))

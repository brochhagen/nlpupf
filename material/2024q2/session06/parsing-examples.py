import spacy
nlp = spacy.load("en_core_web_sm")

sentence1 =  'I went up to my bedroom.'
sentence2 = 'I closed and locked the door.' 

doc = nlp(sentence2)

for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])

spacy.displacy.render(doc, style='dep')
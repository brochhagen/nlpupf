#### Book 1: Dishes made without meat by Mrs. C. S. Peel

import urllib.request #for opening/reading URLs
book_url = 'https://www.gutenberg.org/cache/epub/69346/pg69346.txt' #URL of book we want to read in

book_text = urllib.request.urlopen(book_url) #open URL as "book_text"
book_text = book_text.read()                 #returns all bytes from "book_text" 
book_text = book_text.decode("utf-8")        #decode as UTF-8

### Pre processing ###
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp(book_text) #tokenization & lemmatization using spaCy
### ### ###


### Question 1 ###
book_spacy = doc.text

import re
carrots = re.findall('[cC]arrot',book_spacy)
print(len(carrots))

###################


### Question 2 ###
chapters = re.findall('CHAPTER [A-Z]+', book_text)
chapters = list(set(chapters))
print('\n\n\n###Question 2###\n' + 'Here are the chapter numbers that were retrieved\n' + str(chapters) + '\n### ### ###\n\n\n')

###################

#############################################################
# Question 3
#############################################################
after_index = book_text.split('INDEX')[1]
matches     = re.findall(', \d+\\r\\n', after_index)
print('\n\n\n###Question 3###\n' + 'Number of recipes: ' + str(len(matches)) + '\n### ### ###\n\n\n')



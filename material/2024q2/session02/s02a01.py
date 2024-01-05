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


#############################################################
#1. How many times does the word "carrot" appear in the text?
#############################################################
import re
book_lemmas = [t.lemma_ for t in doc]
#N.B.: re.match checks if elements in book_lemma match the string 'carrot' (ignoring casing)
#      this is passed as an (anonymous) function to filter(), which processes iterables and returns matches
#      and turned into a list through list()
matches     = list(filter(lambda g: re.match('carrot', g, re.IGNORECASE),book_lemmas))
print('\n\n\n### Question 1 ###\n' + 'The word "carrot" appears ' + str(len(matches)) + ' times in the text \n(ignoring casing and after lemmatization)\n' + '### ### ###\n\n\n')
#############################################################

#############################################################
#2. How many chapters does the book have?
#############################################################

chapters = re.findall('chapter [MDCLXVI]*', book_text, re.IGNORECASE) #^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$
chapters = list(set(chapters))
chapters = [w.split(' ')[1] for w in chapters]
print('\n\n\n###Question 2###\n' + 'Here are the chapter numbers that were retrieved\n' + str(chapters) + '\n### ### ###\n\n\n')

#############################################################
#3. How many recipes does the book have?
#############################################################
after_index = book_text.split('INDEX')[1]
matches     = re.findall(', \d+\\r\\n', after_index)
print('\n\n\n###Question 3###\n' + 'Number of recipes: ' + str(len(matches)) + '\n### ### ###\n\n\n')

#############################################################
#4. Are the recipes vegan or vegetarian?
#############################################################

#some frequent non-vegan food (https://www.webmd.com/diet/vegan-diet-overview)
nonvegan_food = ['beef', 'pork', 'lamb', 'chicken', 'duck', 'fish', 'crabs', 'clams', 'mussels', 'eggs', 'cheese', 'butter', 'milk', 'honey']

for i in range(len(book_lemmas)):
	if book_lemmas[i] in nonvegan_food:
		if i - 10 >= 0: 
			lower_bound = i-10
		else:
			lower_bound = i
		if i + 10 <= len(book_lemmas)-1:
			upper_bound = i+10
		else:
			upper_bound = i
		print(' '.join(book_lemmas[lower_bound:upper_bound]))
		text = input("Press 1 if the recipe is not vegan, 0 otherwise: ")  # Python 3
		if text == '1': 
			break

if text == '1': 
	answer = 'The book is not vegan'
else:
	answer = 'The book is vegan'

print('\n\n\n###Question 4###\n' + answer + '\n### ### ###\n\n\n')


#############################################################
#5. What are the 5 most frequently mentioned ingredients?
#############################################################
from collections import Counter

nouns = [token.lemma_
         for token in doc
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN")]
noun_freq = Counter(nouns)
noun_most_freq = noun_freq.most_common(20)

print('\n\n\n###Question 5###\n' + 'Here are the 20 most common nouns')
for i in noun_most_freq: print(i[0])

print('\n\n\n###')


#############################################################
#6. How many carrots would you need to buy to make all recipes that involve carrots?
#############################################################

#Step 1: Split the document up into the different recipes
#Step 2A: For each recipe that mentions carrots, look up the immediate window of occurence and manually extract quantity
#Step 2B: For each recipe that mentions carrots, retrieve closest quantifier ("some" but also "3", "three" and "1/2 pound"). See https://spacy.io/models/en for help
#N.B.: Add measures for multiple mentions of carrots in single recipe


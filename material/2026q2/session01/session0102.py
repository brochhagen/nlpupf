#!/usr/bin/env python
# coding: utf-8

# Open in colab: https://colab.research.google.com/github/brochhagen/nlpupf/blob/main/material/2023q2/session01/session0102.ipynb
# 
# 
# # Handling text (Session 01.02)
# 
# Main contents covered:
# 
#   * Normalization
#   * Tokenization
#   * Type/token distinction
#   * Zipf's Law of Abbreviation
#   
# To distill information from textual data, chances are that you need to pre-process it first. 
# 

# In[ ]:


### This snippet reads in a text from a URL ###

import urllib.request #for opening/reading URLs
book_url = 'https://www.gutenberg.org/cache/epub/1727/pg1727.txt' #URL of book we want to read in

book_text = urllib.request.urlopen(book_url) #open URL as "book_text"
book_text = book_text.read()                 #returns all bytes from "book_text" 
book_text = book_text.decode("utf-8")        #decode as UTF-8


# <div class="alert alert-block alert-info"> <b>Discussion.</b> This is a pretty typical situation. You start with a package/module that does some pre-processing, but now you need to figure out the type of the output it gave. How do you figure out what "book_text" is?</div>

# In[ ]:


print(len(book_text))


# In[ ]:


print(book_text[1:10])


# In[ ]:


print(book_text[1:500])


# # Pre-processing 
# 
# Let's start with the question how many times each word appears in the text.
# 
# <div class="alert alert-block alert-info"> <b>Discussion.</b> Minimally, what do we need to do with "book_text" before answering this question?</div>
# 
# ## Tokenization

# In[ ]:


word_tokenized_book = book_text.split(' ') #list with elements of "book_text", split at the specified string


# In[ ]:


len(word_tokenized_book)


# In[ ]:


word_tokenized_book[1:5]


# In[ ]:


len(set(word_tokenized_book))


# <div class="alert alert-block alert-info"> <b>Discussion.</b> Can you think of other units of analysis than word-level tokenization?</div>
# 
# 
# <div class="alert alert-block alert-info"> <b>Discussion.</b> Can we now answer the question how many times each word appears in the text?</div>
# 

# In[ ]:


from collections import Counter

freq_book = Counter(word_tokenized_book)
freq_book.most_common(5)


# ## Normalization

# In[ ]:


word_tokenized_normed_book = [w.lower() for w in word_tokenized_book]
freq_book = Counter(word_tokenized_normed_book)
freq_book.most_common(5)


# <div class="alert alert-block alert-info"> <b>Discussion.</b> Look at the tokenized book. What other normalization processes can you think of?</div>

# ## Types vs. tokens
# 
# *Types* are the distinct units in a corpus (e.g., distinct words). *Tokens* are each occurence of a unit in a corpus (e.g., each word). So the number of *types* in a corpus will be equal or less than the number of *tokens*
# 
# <div class="alert alert-block alert-success"> <b>Activity.</b> How many word types are there in The Odyssey? How many word tokens?</div>
# 

# # The NLP pipeline & common tasks
# 
# ![](spacy-pipeline.svg "Spacy pipeline")
# <br>
# <div style="text-align: right"> https://spacy.io/usage/processing-pipelines </div>
# 
# 
# ### Some common tasks
# 
#   * Label prediction
#   * Q&A
#   * Information extraction
#   * Summarization
#   * Machine translation
#   * Image captioning
#   * Text generation
#   * ...
# 
# ***

# # spaCy
# 
# State of the art NLP module, interfaces with deep learning techniques and symbolic ones.
# 
# See __[https://spacy.io/](https://spacy.io/)__

# In[ ]:


import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp(book_text)
# all tokens that arent stop words or punctuations
words = [token.text
         for token in doc
         if not token.is_stop and not token.is_punct]

# noun tokens that arent stop words or punctuations
nouns = [token.text
         for token in doc
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN")]

# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(5)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(5)


# In[ ]:


common_words


# In[ ]:


common_nouns


# <div class="alert alert-block alert-success"> You can introduce spaCy to the group next week for participation credit.</div>

# ## Excursion: Zipf's Law of Abbreviation
# 
# 

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

df = pd.DataFrame.from_records(list(dict(Counter(words)).items()), columns=['word','frequency'])


# In[ ]:


df


# In[ ]:


df = df.sort_values(by=['frequency'], ascending=False)
df['rank'] = list(range(1, len(df) + 1))

df


# In[ ]:


sns.relplot(x="rank", y="frequency", data=df);
plt.show()
plt.close()


# In[ ]:


# Drop first row from data frame
df.drop(index=df.index[0], 
        axis=0, 
        inplace=True)

# Drop first row from data frame
df.drop(index=df.index[0], 
        axis=0, 
        inplace=True)

# re-do rank with new elements
df['rank'] = list(range(1, len(df) + 1)) 
df


# In[ ]:


sns.relplot(x="rank", y="frequency", data=df);
plt.show()
plt.close()


# <div class="alert alert-block alert-success"> <b>Activity.</b> Find a text that interests you.
# 
#   1. Load it
#   2. Tokenize it  (what is the unit of analysis you are interested in?)
#   3. Normalize it (what pre-processing is required?)
#   4. Diagnose it  (what is still outstanding?)
# </div>

# If you cannot think of anything, here's a collection of tweets by Donald Trump. Answer the following questions about it:
# 
#   * What is the most frequent word tweeted by D. Trump?
#       
#   * What city does he mention most often?

# In[ ]:


df_trump = pd.read_csv('https://raw.githubusercontent.com/ecdedios/into-heart-of-darkness/master/trump_20200530_clean.csv')
df_trump = df_trump.head(1000) #just the first 1000 tweets for ease of processing 


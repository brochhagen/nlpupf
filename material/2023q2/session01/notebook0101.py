#!/usr/bin/env python
# coding: utf-8

# # Natural Language Processing (Session 01.01)
# 
# ## Overview
# 
# ### Presentation
# 
# Welcome to NLP! This class gives an introduction to central aspects of natural language processing. It puts emphasis on hands-on experience with the acquisition, manipulation, curation, and processing of linguistic data. It covers both symbolic and statistical methods, from a theoretical and practical angle.
# 
# A central goal of this class is for you to acquaint yourself with state of the art techniques used in industry and academia to structure language data and extract information from it; as well as to empower you to apply this knowledge to new problems outside the scope of this class.
# 
# ***
# 
# ### Associated skills
# 
#   * python
#   * data acquisition; manipulation; curation; and processing
#   * machine learning
#   * quantitative reasoning applied to language sciences
# 
# ***
# 
# ### Prerequisites
# 
# Working knowledge of *python 3*. See the *Recommendations* section of the [specialization in Computational Linguistics of the Master's for more information](https://www.upf.edu/web/masterlinguistica/linguistica-computacional)
# 
# ***
# 
# ### Contents
# 
# Main tasks
# 
#   * Handling text
#   * Tagging
#   * Parsing
#   * Question answering
# 
# Main models & technologies
# 
#   * Rule-based systems, using [spaCy](https://spacy.io/)
#   * Learned systems, using [hugging face's transformers](https://huggingface.co/)
# 
# Associated topics
# 
#   * Data curation
#   * Data quality
#   * Fine-tuning
#   * Training and evaluation
#  
# ***
# 
# ### Evaluation
#   
#   * 20% participation in class (5% for each instance)
# 
#   * 80% exercises
#     * Exercise 1: 25% (due: DD/MM at HH:MM)
#     * Exercise 2: 25% (due: DD/MM at HH:MM)
#     * Exercise 3: 30% (due: DD/MM at HH:MM)
# 
# Participation in class can be either of two kinds:
#   1. Present a concept
#   2. Present your approach/results to a problem
# 
# Exercises can be done individually or in groups of 2
# 
# ***
# 
# 
# ### Weekly structure 
# 
# Before a session:
# 
#   * Prepare reading
#   * Make sure you have a working environment that fulfills the necessary dependencies
#   * Submit exercise (if due)
#   * Prepare your concept presentation (if you volunteered) 
# 
# The session itself:
# 
#   * Roughly half is devoted to discussing concepts from a conceptual and theoretical angle (including your mini-presentations)
#   * The other half is hands-on work (including your appraoches/solutions)
# 
# ***
# 
# ### A few recommendations
# 
#   * Do not program "heavy duty" scripts in Jupyter notebooks. Use them for dynamic presentations (or smaller scripts and collaborations)
#   * Comment your code extensively
#   * Document your choices
#   * Use (ana)conda environments
#   * Use the language that is most convenient to you whenever you can
# 
# ***
# 
# ### Short instructor bio
# 
# Thomas is a professor in computational linguistics / computational cognitive science at the UPF. He's particularly interested in the way meaning is structured across languages: why it is the way it is and how it came to be that way. To answer these questions, he sometimes gets people in the lab; sometimes he uses artificial agents to simulate language (use); and other times, he uses large-scale typological data. Besides NLP, he also employs Bayesian models; game theory; and information theory in his daily research.
# 
# Contact: thomas.brochhagen@upf.edu
# 
# Webpage: [https://brochhagen.github.io](https://brochhagen.github.io)
# 
# Main natural languages: EN, DE, ES, CAT
# 
# Main programming languages: python, R, Stan

# *** 
# 
# # Some remarks (Session 01.02)
# 
# ## What is a Jupyter notebook?
# 
# 
# It is a dynamic programming interface, a "web application for creating and sharing computational documents." See [https://jupyter.org/](https://jupyter.org/) for full documentation.

# In[ ]:


# A Jupyter notebook consists of different cells. 
# The cell above is interpreted as Markdown
# This cell is interpreted as python 3.0

print('Testing that this is, indeed, python')


# In[ ]:


# When running a python cell, you see the output just below
# For example:

4+4 


# In[ ]:


# What is the output of this cell?

for i in range(1,10):
    print(i * 2)


# In this class most of the material is made up of one or more Jupyter notebooks. You will find them in [Campus Global](www.upf.edu/intranet/campus-global),together with `.py`- and `.pdf`-versions

# ***
# 
# # What is a(n) (ana)conda environment?
# 
# 

# In[ ]:





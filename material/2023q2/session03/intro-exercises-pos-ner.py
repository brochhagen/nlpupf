import spacy

nlp = spacy.load("en_core_web_sm")



### PoS tagging ###
sentence1 = "It's no use going back to yesterday, because I was a different person then."
sentence2 = 'The best way to explain it is to do it.'
sentence3 = 'Never let anyone drive you crazy; it is nearby anyway and the walk is good for you.'

#### Example with first sentence ###
doc = nlp(sentence1)

for token in doc:
    print(token.text, token.pos_)

### Writing a function to get accuracy ###

# ground truths to test accuracy function 
true_tags1 = ['PRON', 'AUX', 'DET', 'NOUN', 'VERB', 'ADV', 'ADP', 'NOUN', 'PUNCT', 'SCONJ', 'PRON', 'AUX', 'DET', 'ADJ', 'NOUN', 'ADV', 'PUNCT']
true_tags2 = ['NOUN', 'VERB', 'DET', 'NOUN', 'VERB', 'ADV', 'ADP', 'NOUN', 'PUNCT', 'SCONJ', 'PRON', 'AUX', 'DET', 'ADJ', 'NOUN', 'ADV', 'PUNCT']
true_tags3 = ['WRONG.TAG' for _ in range(len(true_tags1))]

def eval_pos(input_sentence, true_tags):
	"""Evaluate spaCy PoS tagger, in terms of accuracy given (1) an input sentence to tag and (2) a list of true tags to evaluate against"""
	doc = nlp(input_sentence)
	predicted_tags = [token.pos_ for token in doc]
	if not len(predicted_tags) == len(true_tags): 
		return(print('Input sentence and ground truth are not of the same length'))
	out = []
	for x,y in zip(predicted_tags,true_tags):
		if x == y: 
			out.append(1)
		else:
			out.append(0)
	return(round(sum(out) / len(out), 2)) 

### NER ###

fragment = "“Who are you?” said the Caterpillar. This was not an encouraging opening for a conversation. Alice replied, rather shyly, “I—I hardly know, Sir, just at present—at least I know who I was when I got up this morning, but I think I must have been changed several times since then.” “What do you mean by that?” said the Caterpillar, sternly. “Explain yourself!” “I can’t explain myself, I’m afraid, Sir,” said Alice, “because I am not myself, you see."

doc = nlp(fragment)

### Example with fragment ###
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

### Writing a function to get F1 ###

true_ners1 = [(24, 35), (93, 98), (201, 213), (316, 327), (406, 411)]
true_ners2 = [(20, 31), (93, 98), (201, 213), (316, 327), (406, 411)]
true_ners3  = [(0,5) for _ in range(3)]
true_ners4 = [(24, 35)]
predicted_ners = [(ent.start_char, ent.end_char) for ent in doc.ents]

eval_ner_precision(predicted_ners,true_ners1)
def eval_ner_precision(predicted_ners, true_entities):
	"""Returns number of true positives divided by number of NEs recognized"""
	return(len(set(true_entities).intersection(set(predicted_ners))) / len(predicted_ners))

def eval_ner_recall(predicted_ners, true_entities):
	"""Returns number of true positives divided by number of true NEs"""
	return(len(set(true_entities).intersection(set(predicted_ners))) / len(true_entities))

def eval_ner(input_sentence, true_entities):
	"""Returns harmonic mean of precision and recall for spaCys NER, taking an input sentence and a list of true NER spans to evaluate against"""
	doc = nlp(input_sentence)
	pred_ners = [(ent.start_char, ent.end_char) for ent in doc.ents]
	precision = eval_ner_precision(pred_ners, true_entities)
	recall    = eval_ner_recall(pred_ners, true_entities)
	if (precision + recall) == 0: return 0
	return(2 * ((precision * recall)) / (precision + recall))



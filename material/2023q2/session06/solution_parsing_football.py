{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d925c6aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: spacy-transformers in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (1.1.8)\n",
      "Requirement already satisfied: spacy-alignments<1.0.0,>=0.7.2 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy-transformers) (0.8.6)\n",
      "Requirement already satisfied: torch>=1.6.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy-transformers) (1.12.1)\n",
      "Requirement already satisfied: transformers<4.22.0,>=3.4.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy-transformers) (4.21.3)\n",
      "Requirement already satisfied: srsly<3.0.0,>=2.4.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy-transformers) (2.4.4)\n",
      "Requirement already satisfied: spacy<4.0.0,>=3.4.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy-transformers) (3.4.3)\n",
      "Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (1.0.9)\n",
      "Requirement already satisfied: numpy>=1.15.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (1.23.4)\n",
      "Requirement already satisfied: jinja2 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (3.1.2)\n",
      "Requirement already satisfied: typer<0.8.0,>=0.3.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (0.4.2)\n",
      "Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.10 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (3.0.10)\n",
      "Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (2.0.8)\n",
      "Requirement already satisfied: setuptools in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (65.5.0)\n",
      "Requirement already satisfied: thinc<8.2.0,>=8.1.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (8.1.5)\n",
      "Requirement already satisfied: pydantic!=1.8,!=1.8.1,<1.11.0,>=1.7.4 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (1.9.2)\n",
      "Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (3.3.0)\n",
      "Requirement already satisfied: pathy>=0.3.5 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (0.6.2)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.13.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (2.28.1)\n",
      "Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (2.0.7)\n",
      "Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (1.0.3)\n",
      "Requirement already satisfied: wasabi<1.1.0,>=0.9.1 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (0.10.0)\n",
      "Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (4.64.1)\n",
      "Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (3.0.8)\n",
      "Requirement already satisfied: packaging>=20.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from spacy<4.0.0,>=3.4.0->spacy-transformers) (21.3)\n",
      "Requirement already satisfied: typing-extensions in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from torch>=1.6.0->spacy-transformers) (4.4.0)\n",
      "Requirement already satisfied: filelock in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from transformers<4.22.0,>=3.4.0->spacy-transformers) (3.8.0)\n",
      "Requirement already satisfied: huggingface-hub<1.0,>=0.1.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from transformers<4.22.0,>=3.4.0->spacy-transformers) (0.11.1)\n",
      "Requirement already satisfied: regex!=2019.12.17 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from transformers<4.22.0,>=3.4.0->spacy-transformers) (2022.10.31)\n",
      "Requirement already satisfied: tokenizers!=0.11.3,<0.13,>=0.11.1 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from transformers<4.22.0,>=3.4.0->spacy-transformers) (0.12.1)\n",
      "Requirement already satisfied: pyyaml>=5.1 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from transformers<4.22.0,>=3.4.0->spacy-transformers) (6.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from packaging>=20.0->spacy<4.0.0,>=3.4.0->spacy-transformers) (3.0.9)\n",
      "Requirement already satisfied: smart-open<6.0.0,>=5.2.1 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from pathy>=0.3.5->spacy<4.0.0,>=3.4.0->spacy-transformers) (5.2.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from requests<3.0.0,>=2.13.0->spacy<4.0.0,>=3.4.0->spacy-transformers) (2022.12.7)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from requests<3.0.0,>=2.13.0->spacy<4.0.0,>=3.4.0->spacy-transformers) (3.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from requests<3.0.0,>=2.13.0->spacy<4.0.0,>=3.4.0->spacy-transformers) (1.26.11)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from requests<3.0.0,>=2.13.0->spacy<4.0.0,>=3.4.0->spacy-transformers) (2.1.1)\n",
      "Requirement already satisfied: confection<1.0.0,>=0.0.1 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from thinc<8.2.0,>=8.1.0->spacy<4.0.0,>=3.4.0->spacy-transformers) (0.0.3)\n",
      "Requirement already satisfied: blis<0.8.0,>=0.7.8 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from thinc<8.2.0,>=8.1.0->spacy<4.0.0,>=3.4.0->spacy-transformers) (0.7.8)\n",
      "Requirement already satisfied: click<9.0.0,>=7.1.1 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from typer<0.8.0,>=0.3.0->spacy<4.0.0,>=3.4.0->spacy-transformers) (8.1.3)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /opt/anaconda3/envs/nlpupf/lib/python3.9/site-packages (from jinja2->spacy<4.0.0,>=3.4.0->spacy-transformers) (2.1.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install spacy-transformers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "71307f64",
   "metadata": {},
   "outputs": [],
   "source": [
    "import spacy\n",
    "nlp_trf = spacy.load('en_core_web_trf')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "04208cb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Class from: https://applied-language-technology.mooc.fi\n",
    "\n",
    "# Import the Language object under the 'language' module in spaCy,\n",
    "# and NumPy for calculating cosine similarity.\n",
    "from spacy.language import Language\n",
    "import numpy as np\n",
    "\n",
    "# We use the @ character to register the following Class definition\n",
    "# with spaCy under the name 'tensor2attr'.\n",
    "@Language.factory('tensor2attr')\n",
    "\n",
    "# We begin by declaring the class name: Tensor2Attr. The name is \n",
    "# declared using 'class', followed by the name and a colon.\n",
    "class Tensor2Attr:\n",
    "    \n",
    "    # We continue by defining the first method of the class, \n",
    "    # __init__(), which is called when this class is used for \n",
    "    # creating a Python object. Custom components in spaCy \n",
    "    # require passing two variables to the __init__() method:\n",
    "    # 'name' and 'nlp'. The variable 'self' refers to any\n",
    "    # object created using this class!\n",
    "    def __init__(self, name, nlp):\n",
    "        \n",
    "        # We do not really do anything with this class, so we\n",
    "        # simply move on using 'pass' when the object is created.\n",
    "        pass\n",
    "\n",
    "    # The __call__() method is called whenever some other object\n",
    "    # is passed to an object representing this class. Since we know\n",
    "    # that the class is a part of the spaCy pipeline, we already know\n",
    "    # that it will receive Doc objects from the preceding layers.\n",
    "    # We use the variable 'doc' to refer to any object received.\n",
    "    def __call__(self, doc):\n",
    "        \n",
    "        # When an object is received, the class will instantly pass\n",
    "        # the object forward to the 'add_attributes' method. The\n",
    "        # reference to self informs Python that the method belongs\n",
    "        # to this class.\n",
    "        self.add_attributes(doc)\n",
    "        \n",
    "        # After the 'add_attributes' method finishes, the __call__\n",
    "        # method returns the object.\n",
    "        return doc\n",
    "    \n",
    "    # Next, we define the 'add_attributes' method that will modify\n",
    "    # the incoming Doc object by calling a series of methods.\n",
    "    def add_attributes(self, doc):\n",
    "        \n",
    "        # spaCy Doc objects have an attribute named 'user_hooks',\n",
    "        # which allows customising the default attributes of a \n",
    "        # Doc object, such as 'vector'. We use the 'user_hooks'\n",
    "        # attribute to replace the attribute 'vector' with the \n",
    "        # Transformer output, which is retrieved using the \n",
    "        # 'doc_tensor' method defined below.\n",
    "        doc.user_hooks['vector'] = self.doc_tensor\n",
    "        \n",
    "        # We then perform the same for both Spans and Tokens that\n",
    "        # are contained within the Doc object.\n",
    "        doc.user_span_hooks['vector'] = self.span_tensor\n",
    "        doc.user_token_hooks['vector'] = self.token_tensor\n",
    "        \n",
    "        # We also replace the 'similarity' method, because the \n",
    "        # default 'similarity' method looks at the default 'vector'\n",
    "        # attribute, which is empty! We must first replace the\n",
    "        # vectors using the 'user_hooks' attribute.\n",
    "        doc.user_hooks['similarity'] = self.get_similarity\n",
    "        doc.user_span_hooks['similarity'] = self.get_similarity\n",
    "        doc.user_token_hooks['similarity'] = self.get_similarity\n",
    "    \n",
    "    # Define a method that takes a Doc object as input and returns \n",
    "    # Transformer output for the entire Doc.\n",
    "    def doc_tensor(self, doc):\n",
    "        \n",
    "        # Return Transformer output for the entire Doc. As noted\n",
    "        # above, this is the last item under the attribute 'tensor'.\n",
    "        # Average the output along axis 0 to handle batched outputs.\n",
    "        return doc._.trf_data.tensors[-1].mean(axis=0)\n",
    "    \n",
    "    # Define a method that takes a Span as input and returns the Transformer \n",
    "    # output.\n",
    "    def span_tensor(self, span):\n",
    "        \n",
    "        # Get alignment information for Span. This is achieved by using\n",
    "        # the 'doc' attribute of Span that refers to the Doc that contains\n",
    "        # this Span. We then use the 'start' and 'end' attributes of a Span\n",
    "        # to retrieve the alignment information. Finally, we flatten the\n",
    "        # resulting array to use it for indexing.\n",
    "        tensor_ix = span.doc._.trf_data.align[span.start: span.end].data.flatten()\n",
    "        \n",
    "        # Fetch Transformer output shape from the final dimension of the output.\n",
    "        # We do this here to maintain compatibility with different Transformers,\n",
    "        # which may output tensors of different shape.\n",
    "        out_dim = span.doc._.trf_data.tensors[0].shape[-1]\n",
    "        \n",
    "        # Get Token tensors under tensors[0]. Reshape batched outputs so that\n",
    "        # each \"row\" in the matrix corresponds to a single token. This is needed\n",
    "        # for matching alignment information under 'tensor_ix' to the Transformer\n",
    "        # output.\n",
    "        tensor = span.doc._.trf_data.tensors[0].reshape(-1, out_dim)[tensor_ix]\n",
    "        \n",
    "        # Average vectors along axis 0 (\"columns\"). This yields a 768-dimensional\n",
    "        # vector for each spaCy Span.\n",
    "        return tensor.mean(axis=0)\n",
    "    \n",
    "    # Define a function that takes a Token as input and returns the Transformer\n",
    "    # output.\n",
    "    def token_tensor(self, token):\n",
    "        \n",
    "        # Get alignment information for Token; flatten array for indexing.\n",
    "        # Again, we use the 'doc' attribute of a Token to get the parent Doc,\n",
    "        # which contains the Transformer output.\n",
    "        tensor_ix = token.doc._.trf_data.align[token.i].data.flatten()\n",
    "        \n",
    "        # Fetch Transformer output shape from the final dimension of the output.\n",
    "        # We do this here to maintain compatibility with different Transformers,\n",
    "        # which may output tensors of different shape.\n",
    "        out_dim = token.doc._.trf_data.tensors[0].shape[-1]\n",
    "        \n",
    "        # Get Token tensors under tensors[0]. Reshape batched outputs so that\n",
    "        # each \"row\" in the matrix corresponds to a single token. This is needed\n",
    "        # for matching alignment information under 'tensor_ix' to the Transformer\n",
    "        # output.\n",
    "        tensor = token.doc._.trf_data.tensors[0].reshape(-1, out_dim)[tensor_ix]\n",
    "\n",
    "        # Average vectors along axis 0 (columns). This yields a 768-dimensional\n",
    "        # vector for each spaCy Token.\n",
    "        return tensor.mean(axis=0)\n",
    "    \n",
    "    # Define a function for calculating cosine similarity between vectors\n",
    "    def get_similarity(self, doc1, doc2):\n",
    "        \n",
    "        # Calculate and return cosine similarity\n",
    "        return np.dot(doc1.vector, doc2.vector) / (doc1.vector_norm * doc2.vector_norm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2b984142",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('transformer',\n",
       "  <spacy_transformers.pipeline_component.Transformer at 0x180e2c640>),\n",
       " ('tagger', <spacy.pipeline.tagger.Tagger at 0x180e524c0>),\n",
       " ('parser', <spacy.pipeline.dep_parser.DependencyParser at 0x180e50d60>),\n",
       " ('attribute_ruler',\n",
       "  <spacy.pipeline.attributeruler.AttributeRuler at 0x177b58b00>),\n",
       " ('lemmatizer', <spacy.lang.en.lemmatizer.EnglishLemmatizer at 0x180e8a540>),\n",
       " ('ner', <spacy.pipeline.ner.EntityRecognizer at 0x180e293c0>),\n",
       " ('tensor2attr', <__main__.Tensor2Attr at 0x18435dd00>)]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "\n",
    "# Add the component named 'tensor2attr', which we registered using the\n",
    "# @Language decorator and its 'factory' method to the pipeline.\n",
    "nlp_trf.add_pipe('tensor2attr')\n",
    "\n",
    "# Call the 'pipeline' attribute to examine the pipeline\n",
    "nlp_trf.pipeline\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "47321f9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "#This block is just a convenient way for you to get the data\n",
    "football_data = [['Argentina','United Arab Emirates',0,\n",
    "'Lionel Messi played the full 90 minutes and got on the scoresheet as Argentina beat the United Arab Emirates 5-0 in their final World Cup warmup match. The Argentina captain scored their fourth goal just before the break as the pre-tournament favourites stretched their unbeaten run to 36 games. Messi also set up Manchester City’s Julián Álvarez to open the scoring in the 17th minute, and has now scored 10 goals in his past four international matches. Ángel Di María also showed he is approaching peak form with two fine first-half goals in Abu Dhabi, superbly volleying home Marcos Acuña’s cross at the far post in the 25th minute. The Juventus winger, who has recovered from a thigh injury in time for Qatar, dribbled through the hosts’ defence 11 minutes later to score his second.'],\n",
    "['France','Australia',0,\n",
    "'Giroud ties record as France pummels Australia. Not tonight! That\\'s what France shouted in Qatar as the game came to a close. The French national team saw Argentina vs Saudi Arabia and didn\\'t want to face the same consequences. There are no small rivals, every team should always know this, a saying as old as the sport, yet teams never seem to learn it. Well, the French did so for 83 minutes. Australia was better in the first 7 minutes, and they went up in the game. Australia also saw the Argentina game. They also believed they could win this. For a bit, they did do the miracle. But this is too much France. This is too much of a team. Mbappe and Dembele started to get in the game, and from the right and left, the blue wave came, and Australia tried to hold on as much as possible.'],\n",
    "['Iran', 'England', 1,\n",
    "'First up, it was England with a point to prove, and oh how they proved it. After being denied a clear penalty early on, England finally got their goal 35 minutes in. It was Liverpool’s number one transfer target Jude Bellingham that gave the Three Lions the lead with a fantastic header, reminiscent of his idol Steven Gerrard’s in the 2005 Champions League final. Southgate’s men soon made it two then three just before halftime. Bakayo Saka’s outstanding finish after Harry Maguire knocking it back to him doubled their lead and Raheem Sterling added the third after wonderful work by Harry Kane. After the break, the game continued to go down the same path. Arsenal’s Saka added another for himself after tricking two Iranian defenders to then place it past the keeper with ease. Harry Maguire then got caught sleeping and Iran got a shock goal through Mehdi Taremi, which did not go down well with Jordan Pickford. Substitutes Marcus Rashford and Jack Grealish added yet more goals for England, making it 6-1. However, Iran weren’t done either, Taremi scoring his second, this time from the spot. England’s empathic 6-2 win against the 20th ranked in the world sets a marker down for the rest of the teams. They play USA on Friday next.'],\n",
    "['Switzerland','Brazil',1,\n",
    "'I\\'m tired after that. ​​​​​​​It took a long, long time for Brazil to get into their groove and become, well, Brazil. They did it in the end, thanks to Casemiro, and by the final stages of the game the confidence was there for all to see. They weren\\'t particularly special by any means, but they worked hard and never stopped attacking. In the end, 1-0 is probably a fair result. Switzerland lacked ambition, a difficult trait to have against the Seleção, I admit, but they defence kept up well for the whole game, minus probably three lapses of concentration: Vini\\'s chance and offside attempt plus Casemiro\\'s strike. Brazil did not dominate Switzerland; but Brazil did win. And in the end, it was that moment of brilliance that decided the game and Brazil are top of the group and through to the next round. Along with France, they are the only team to have 2 wins from 2.'],\n",
    "['Portugal','Uruguay',0,\n",
    "'Portugal wanted it more than Uruguay. We don’t want Brazil. Portugal’s first thought tonight when coming into the match. Portgual controlled the game for 70 minutes of the match. They just wanted it more, as they proposed from the beginning. Not always in a correct way, not always with a plan, but knowing they wanted to win this one. Uruguay, where were you? The Charruas gave 25 minutes of great Football. Pallestri was amazing from the right. Coming and coming, but it was not enough. One can’t expect to beat a team like Portugal by speculating. Alonso played it for the tie and the what-if moment, but why? They clearly have the tools to win. Portugal is a team of great players that have no idea what they are doing. Bruno and Bernardo were amazing tonight, individually, but Portugal has a lot to work on as a team. They are just too good that their lack of coaching goes unnoticed. They, for now, avoid Brazil, but they need to work on being a band of brothers. In the end, Uruguay lost due to lack of action.'],\n",
    "['USA','Iran', 0,\n",
    "'Huge win for USA. Defensively, the US stayed tight and in midfield, Yunus Musah, Tyler Adams and Weston McKennie impressed, getting through a huge amount of work. It was a solid performance throughout. They put their bodies on the line in what was a proper team display. Christian Pulisic scored arguably the biggest goal of his career, however, ​​​​it remains to be seen if he will be back for Saturday\\'s clash against the Netherlands. The match against the Netherlands will be a huge test for Gregg Berhalter\\'s young side, who will be confident of getting a result and progressing to the quarter-finals. The US have finished second in Group B, behind group winners England, while Iran have been knocked out.'],\n",
    "['Qatar', 'Ecuador', 0,\n",
    "'Ecuador had a disallowed goal in the opening minutes, but eventually won 2–0 with two goals from Enner Valencia. Qatar became the first host nation to lose their opening match at a World Cup. Many Qatar natives were seen leaving the game before the end, with ESPN reporting that two-thirds of the attendance had left'],\n",
    "['USA', 'Wales', 2,\n",
    "' Timothy Weah, of the United States, scored a first-half goal against Wales; however, the match finished as a draw after a penalty kick was won and scored by Gareth Bale.'],\n",
    "['Wales', 'Iran', 1,\n",
    "'Iran defeated Wales 2–0 following a red card to Welsh goalkeeper Wayne Hennessey after he committed a foul outside of his penalty area. Substitute Rouzbeh Cheshmi scored the first goal eight minutes into stoppage time, followed by Ramin Rezaeian scoring three minutes later'],\n",
    "['Senegal', 'Netherlands', 1,\n",
    "'The other starting match in group A was won by the Netherlands 2–0 over Senegal. Cody Gakpo scored the opening goal in the 84th minute and Davy Klaassen added a second in stoppage time.'],\n",
    "['Senegal', 'Qatar', 0,\n",
    "'Senegal faced Qatar in the third match of the group; Boulaye Dia capitalised on a slip by Boualem Khoukhi to put Senegal 1–0 ahead. Famara Diédhiou scored a second with a header, before Mohammed Muntari scored Qatar\\'s first-ever goal at a World Cup to reduce the deficit back to one. Senegal eventually won the match 3–1 after an 84th-minute goal by Bamba Dieng. With this result, Qatar became the first team to be eliminated from the tournament, as well as becoming the first host nation to ever be knocked out of the tournament after two games.'],\n",
    "['Qatar', 'Netherlands', 1,\n",
    "'The Netherlands won 2–0 against Qatar following goals by Gakpo and Frenkie de Jong to win the group, while Qatar attained the distinction of being the first home nation to lose all three group matches.'],\n",
    "['Ecuador', 'Senegal', 1,\n",
    "'Clement Turpin blows the whistle and Ecuador\\'s World Cup is over. They join Qatar as the teams dumped out of Group A. Ecuador had frustrated Senegal for much of the first-half, knowing their opponents needed to win to progress, but the Africans were awarded a penalty late on after Piero Reyna fouled Ismaila Sarr. The Watford winger confidently tucked his spot-kick away to put Senegal into the driving seat at the break. The South Americans struggled offensively all game but dug out an equaliser through Moisés Caicedo. A draw would have been enough to send them through but their hope lasted just 150 seconds as Kalidou Koulibaly restored Senegal’s lead. Ecuador could not muster another big chance and it ended 1-2 after six nerve-racking minutes of stoppage-time.'],\n",
    "['Japan', 'Spain', 0,\n",
    "'Having in the first half looked like they were going to stroll into the last 16 as group winners, Spain were completely blown away by Japan after the break. You\\'ll struggle to find a better definition of that old football cliché \\'a game of two halves\\'. The Spaniards are through as Group E runners-up, but even flirted with going out altogether. For the three minutes that Costa Rica were ahead against Germany, La Roja were heading for elimination. As for Japan, they may have been non-existent in the first half, but they were marvellous in the second. As Luis Enrique says, having beaten Spain and Germany, the Samurai Blue are deserved group winners. The Japanese will now take on Croatia in the last 16, while Spain will face Morocco.'],\n",
    "['Brazil', 'South Korea', 0,\n",
    "'Brazil were simply irresistible in the first half. They went in at the break 4-0 up and it could easily have been seven or eight. Yes, South Korea caused their own problems by pushing so far up the pitch and leaving so few players back but Brazil still had to know how to exploit it and exploit it they did. There was only going to be one winner after Vinícius\\' opening goal, quickly followed by a Neymar penalty. All in favour of Brazil. Goals three and four were things of beauty; fast, crisp passing moves finished off by Richardson and Lucas Paquetà. On that form, there is no stopping Brazil, who paid the best tribute to Pelé, watching in his hospital bed in São Paolo. '],\n",
    "['Spain', 'Morocco',1,\n",
    "'Morocco’s Bono and Hakimi make history for Morocco after defeating Spain on penalties, booking their spot in their first Quarter-Finals. The North African team became the first African side to reach the World Cup quarter-finals since 2010, and the first African team to win a penalty shootout at the World Cup.'],\n",
    "['Morocco', 'Portugal',0,\n",
    "'Morocco proved to the world that they deserve to be considered among the best at the World Cup. They have made it to the semifinals, the first African team to ever make it to this stage. They first topped their group, beating Canada and Belgium and coming to a scoreless draw with Croatia. They went on to beat Spain on a penalty shootout in the Round of 16. And now, they’ve defeated Portugal in a 1-0 victory that most people were not expecting. Now though, as they get ready to face France in the semifinals, they should not be underestimated.'],\n",
    "['Argentina', 'Croatia', 0,\n",
    "'That was a terrific performance from Argentina, who are in tears on the pitch. Croatia battled well but did not have enough firepower up front to compete with the Argentinian talent on show tonight. Julián Álvarez was immense throughout, constantly making dangerous movements to give his teammates - Messi in particular - more time and space on and off the ball. The first goal came from fantastic movement and quick thinking from the Manchester City man, the same with the second, where he didn\\'t give up and rightly claimed his goal. The third goal, although finished by Álvarez, was a work of art from Lionel Messi, who made Gvardiol - many people\\'s choice for defender of the tournament - look like a complete novice. Messi twisted and turned and squirmed his way around, under, over and through Gvardiol all at the same time, dematerialising his physical form and appearing on the other side in a feat of physics that scientists from this century are surely not familiar with. Argentina look scarily good; their evolution into the final stage is complete and either France or Morocco are going to have to have the performance to mark a generation if they want to beat this side.'],\n",
    "['Germany', 'Costa Rica', 0,\n",
    "'I didn\\'t have a headache before that, now I have twelve at once. There was a period when I fell off my seat, when I couldn\\'t do anything other than stare at my hands and beg them to type, when all I could do was write AAAHHHHHHH.​​​Germany is out even though they won the match. They played a frantic game from start to finish, both in the positive and negative sense, letting Costa Rica into the next round and out of it, putting themselves within touching distance and then as far away as possible.​​​​​​​Costa Rica looked dead, buried and washed out to sea in the first 40 minutes, before they jumped up and made the European side that there were two teams on the pitch and not eleven red scarecrows.'],\n",
    "['France', 'Argentina', 1,\n",
    "'The final was played on 18 December between Argentina and France. Both teams had won the event twice previously.[242] Early goals from Lionel Messi and Ángel Di María gave Argentina, leading 2–0, a head start against the French.[242][243] Despite multiple substitutions in the first half, France did not record a shot until after the 70th minute, but were energised by additional substitutions in the 71st. A few minutes later, France were awarded a penalty as Randal Kolo Muani was brought down in the penalty area by Nicolas Otamendi. Mbappé scored the penalty, and added a second goal less than two minutes later to equalise the scores.[243] With the score tied at two goals apiece, the match went to extra time. Messi scored his second goal in the 108th minute, once again giving Argentina the lead. However, Mbappé was awarded a second penalty in the 115th minute after his shot hit the arm of Gonzalo Montiel. Mbappé scored his third goal, becoming the second player ever to complete a hat-trick in the final of a World Cup after Geoff Hurst for England in 1966.[243] With the score tied at 3–3, the match was determined via a penalty shootout. Argentina won the final after scoring all of their penalties, winning 4–2.[243] This marked their third World Cup win and their first since 1986. It also marked the first time that a South American team won the World Cup in 20 years and as Copa América champions. ']\n",
    "]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8233ff6",
   "metadata": {},
   "outputs": [],
   "source": [
    "wn = nlp_trf('winner')\n",
    "\n",
    "for datapoint in football_data:\n",
    "    #find the contextualized representation of each country and compare it to the embedding of winner and/or loser, \n",
    "    #pick the one closest"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "nlpupf",
   "language": "python",
   "name": "nlpupf"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

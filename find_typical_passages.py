import os, json
import pdb
from cltk.stem.latin.j_v import JVReplacer
from cltk.tokenize.word import WordTokenizer
from cltk.stem.lemma import LemmaReplacer


with open('./data/virgil__aeneid__lat.json') as data_file:
	data = json.load(data_file)

lines = []

jv_replacer = JVReplacer()
word_tokenizer = WordTokenizer('latin')
lemmatizer = LemmaReplacer('latin')

for book_key in data['text'].keys():
	for line_key in data['text'][book_key]:
		# line from the json file
		text = data['text'][book_key][line_key]
		# j/v
		text = jv_replacer.replace(text.lower())
		# add it to the list
		lines.append({
			'book': book_key,
			'line': line_key,
			'text': text, 
		})

full_text = ' '.join([x['text'] for x in lines])
full_text = jv_replacer.replace(full_text.lower())

# tokenize 
full_text_word_tokens = word_tokenizer.tokenize(full_text.lower())
full_text_word_tokens = [token for token in full_text_word_tokens if token not in ['.', ',', ':', ';']]

unique_word_tokens = set(full_text_word_tokens)

pdb.set_trace()



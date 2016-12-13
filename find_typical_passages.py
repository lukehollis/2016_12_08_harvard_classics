import os, json
import pdb
from collections import Counter
from cltk.stem.latin.j_v import JVReplacer
from cltk.stop.latin.stops import STOPS_LIST
from cltk.tokenize.word import WordTokenizer
from cltk.stem.lemma import LemmaReplacer




def count_lemmata(text):
	"""
	count the unique lemmata in input string of Latin 
	"""

	# tokenize 
	word_tokenizer = WordTokenizer('latin')
	word_tokens = word_tokenizer.tokenize(text.lower())
	word_tokens = [token for token in word_tokens if token not in ['.', ',', ':', ';', '?'] and token not in STOPS_LIST]

	# lemmatize
	lemmatizer = LemmaReplacer('latin')
	lemmata = lemmatizer.lemmatize(word_tokens)

	# count unique lemmata
	lemmata_counts = Counter(lemmata)

	return lemmata_counts


def main():
	
	lines = []
	full_text_lemmata_counts = {}
	line_counts = {}

	# Open our json file with the full text of the aeneid
	with open('./data/virgil__aeneid__lat.json') as data_file:
		data = json.load(data_file)

	# create a jv replacer to be used in the next step
	jv_replacer = JVReplacer()

	# put every line of text of the aeneid into a list
	for book_key in data['text'].keys():
		for line_key in data['text'][book_key]:
			# line from the json file
			text = data['text'][book_key][line_key]
			# j/v
			text = jv_replacer.replace(text.lower())
			# add it to the list
			lines.append({
				'book': str(int(book_key) + 1),
				'line': str(int(line_key) + 1),
				'text': text, 
			})
	
	# Sort the lines by book and line number
	lines = sorted(lines, key = lambda x: (int(x['book']), int(x['line'])))

	# Caluclate counts of all unique lemmata in the work
	print('Calculating counts of all lemmata in work')
	full_text = ' '.join([x['text'] for x in lines])
	full_text_lemmata_counts = count_lemmata(full_text)
	total_lemmata_count = sum(full_text_lemmata_counts.values())
	print(' -- finished lemmatazing and counting work with', total_lemmata_count, 'lemmata found')

	# Calculate counts of lemmata for a given passage and determine
	# it's similarity to the text as a whole
	# -- for the moment use 10 line increments
	print('Calculating counts for segments')
	i = 0
	segments = []
	segment_length = 10
	for i in range(0, len(lines), segment_length): 
		segment_lines = lines[i:(i + segment_length)]
		segment_text = ' '.join([x['text'] for x in segment_lines])
		segment_text_lemmata_counts = count_lemmata(segment_text)	
		similarities = []
		similarities_meta = []

		for lemma, count in segment_text_lemmata_counts.items():
			if full_text_lemmata_counts[lemma] > 1:
				similarity_value = count * (full_text_lemmata_counts[lemma] / total_lemmata_count)
				similarities_meta.append([
					lemma,
					count,
					full_text_lemmata_counts[lemma],
					])
				similarities.append(similarity_value)

		starting_line = segment_lines[0]
		ending_line = segment_lines[-1]
		segments.append({
			'start': starting_line['book'] + '.' + starting_line['line'],
			'end': ending_line['book'] + '.' + ending_line['line'],
			'similarity_index': sum(similarities),
			'text': segment_text,
			'meta': similarities_meta,
		})
		print(' -- calculated similarity for', starting_line['book'] + '.' + starting_line['line'], '-', ending_line['book'] + '.' + ending_line['line'], 'at', sum(similarities))

	# Sort results by similarity index
	segments = sorted(segments, key = lambda x: x['similarity_index'], reverse=True)
	pdb.set_trace()


if __name__ == '__main__':
	main()

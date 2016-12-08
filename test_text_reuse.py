from cltk.text_reuse.levenshtein import Levenshtein
from cltk.text_reuse.text_reuse import TextReuse
from cltk.text_reuse.comparison import long_substring
from cltk.text_reuse.comparison import minhash


demo_verg = """
tuque o, cui prima frementem
fudit equum magno tellus percussa tridenti,
Neptune; et cultor nemorum, cui pinguia Ceae
ter centum niuei tondent dumeta iuuenci;
ipse nemus linquens patrium saltusque Lycaei
Pan, ouium custos, tua si tibi Maenala curae,
adsis, o Tegeaee, fauens, oleaeque Minerua
inuentrix, uncique puer monstrator aratri,
et teneram ab radice ferens, Siluane, cupressum:
dique deaeque omnes, studium quibus arua tueri,
munera vestra cano. et vos o agrestum praesentia
quique nouas alitis non ullo semine fruges
quique satis largum caelo demittitis imbrem.
"""

demo_prop = """
corniger Arcadii vacuam pastoris in aulam
dux aries saturas ipse reduxit oves;
dique deaeque omnes, quibus est tutela per agros,
praebebant vestri verba benigna foci:
'et leporem, quicumque venis, venaberis, hospes,
et si forte meo tramite quaeris avem:
et me Pana tibi comitem de rupe vocato,
sive petes calamo praemia, sive cane.'
at nunc desertis cessant sacraria lucis:
aurum omnes victa iam pietate colunt.
auro pulsa fides, auro venalia iura,
aurum lex sequitur, mox sine lege pudor.
"""

def test_distance_ratio():
	"""Test returning simple Levenshtein distance calculation ratio between two strings"""
	print("Testing distance ratio between two passages")
	print(" -- passage 1: dique deaeque omnes, studium quibus arua tueri,")
	print(" -- passage 2: dique deaeque omnes, quibus est tutela per agros,")


	l = Levenshtein()
	ratio = l.ratio("dique deaeque omnes, studium quibus arua tueri,", "dique deaeque omnes, quibus est tutela per agros,")

	print(" -- -- Levenshtein distance ratio:", ratio)

def test_distance_sentences():
	"""Test comparing two passages tokenized at the sentence level"""
	print("Testing distance ratio between two long passages by sentence")

	t = TextReuse()
	comparisons = t.compare_sentences(demo_verg, demo_prop, 'latin')

	print(" -- -- Comparisons:", comparisons)

def test_distance_sliding_window():
	"""Test comparing two passages with the sliding window strategy"""
	print("Testing distance ratio between two long passages by a sliding window strategy")

	t = TextReuse()
	comparisons = t.compare_sliding_window(demo_verg, demo_prop)

	print(" -- -- Comparisons:", comparisons)


if __name__ == '__main__':

	# distance ratio
	test_distance_ratio()

	# distance ratio by sentences
	test_distance_sentences()

	# distance sliding window
	test_distance_sliding_window()

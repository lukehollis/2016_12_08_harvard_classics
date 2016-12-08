from cltk.stem.latin.syllabifier import Syllabifier

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

word = 'sidere'

def test_syllabify():
	print("Syllabify word", word)

	syllabifier = Syllabifier()
	syllables = syllabifier.syllabify(word)

	print(" -- syllables:", syllables)







if __name__ == '__main__':
	test_syllabify()

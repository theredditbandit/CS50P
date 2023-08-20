from twttr import shorten

def test_consonants():
    tlist = ["twttr","wrds","wtht"]
    for i in tlist:
        assert shorten(i) == i

def test_words():
    tlist = ["twitter","words","with","vowels"]
    tlist2 = ["twttr","wrds","wth","vwls"]
    for i in range(len(tlist)):
        assert shorten(tlist[i]) == tlist2[i]

def test_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_alphanums():
    assert shorten("abcd1234") == "bcd1234"
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("A sentence.") == " sntnc."
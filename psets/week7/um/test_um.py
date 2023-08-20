from um import count

def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_words_with_um():
    assert count("yummy") == 0
    assert count("um,yum,um..") == 2

def test_case():
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM") == 1
    assert count("um,Um,UMM,uM,MU") == 3

def test_space():
    assert count("       um       ") == 1
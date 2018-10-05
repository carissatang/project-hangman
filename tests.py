from hangman import *

def test_get_secret_word():
    words = {get_secret_word() for _ in range(100)}
    assert len(words) >= 5, "Should contain a list of at least 5 words."
    
    # do the following:
    assert what secret word returns is a string, "Should return a string"


def test_word_is_solved():
    assert word_is_solved("hello", "eh") == False, "Should not be solved guesses: 'eh' for word: 'hello'."
    assert word_is_solved("world", "dorlw") == True, "Should be solved"

    
def test_display_letters():
    assert display_letters("hello", "") == "_ _ _ _ _", "Should reveal no letters"
    assert display_letters("hello", "h") == "h _ _ _ _", "Should reveal only first letter"
    assert display_letters("hello", "e") == "_ e _ _ _", "Should reveal only second letter"
    assert display_letters("hello", "l") == "_ _ l l _", "Should reveal two ls"
    assert display_letters("hello", "o") == "_ _ _ _ o", "Should reveal only last letter"
    assert display_letters("hello", "he") == "h e _ _ _", "Should reveal only first and second letter"
    assert display_letters("hello", "hello") == "h e l l o", "Should reveal all letters"
    
# Test display_platform(wrong_guesses)
# display_platform("a") -> display with head



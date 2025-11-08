# backwards_translator.py

bl_info = {
    "name": "Backwards Translator",
    "author": "Shadow-Fire-Rebecca (ORCID: 0009-0006-3358-6484)",
    "version": (1, 0),
}

def reverse_word(word):
    """Reverse a single word, preserving case and punctuation."""
    # Separate punctuation from the word
    punctuation = ""
    clean_word = word
    
    # Check if word ends with punctuation
    if word and word[-1] in ".,!?;:":
        punctuation = word[-1]
        clean_word = word[:-1]
    
    # Reverse the clean word
    reversed_word = clean_word[::-1]
    
    # Restore punctuation at the *end* of reversed word
    return reversed_word + punctuation

def backwards_sentence(sentence):
    """
    Convert a full sentence to backwards speech.
    Example: "I love grey aliens!" → "I evol yerg sneila!"
    """
    words = sentence.split()
    reversed_words = []
    
    for word in words:
        # Reverse each word individually
        rev = reverse_word(word)
        reversed_words.append(rev)
    
    # Join words back with spaces
    return " ".join(reversed_words)

def teach_backwards(phrase):
    """Show original + backwards + pronunciation guide"""
    backwards = backwards_sentence(phrase)
    print(f"Original:  {phrase}")
    print(f"Backwards: {backwards}")
    print(f"Pronounce: {backwards.replace('!', '').replace('?', '')} (like alien speak!)")
    print("-" * 50)

# === Interactive Learning Mode ===
def learn_backwards_mode():
    print("🌌 WELCOME TO BACKWARDS LANGUAGE SCHOOL 🌌")
    print("Type a sentence and I'll teach you to say it backwards!")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You say: ").strip()
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Keep practicing, future backwards master! 👽")
            break
        if user_input:
            teach_backwards(user_input)
        else:
            print("Say something!")

# === Example Dictionary of Fun Phrases ===
BACKWARDS_DICTIONARY = {
    "Hello, world!": "olleH, dlrow!",
    "I love grey aliens!": "I evol yerg sneila!",
    "Python is awesome.": "nohtyP si emosewa.",
    "Racecar is a palindrome.": "racecaR si a emordnilap.",
    "Backwards is fun!": "sdrawkcaB si nuf!"
}

# === Demo ===
if __name__ == "__main__":
    print("BACKWARDS TRANSLATION DICTIONARY")
    print("=" * 50)
    
    # Show dictionary examples
    for eng, back in BACKWARDS_DICTIONARY.items():
        teach_backwards(eng)
    
    print("\nReady to practice live?")
    learn_backwards_mode()
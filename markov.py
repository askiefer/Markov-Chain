from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # opens the entire file 

    content = open(file_path).read() 
    return content


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    
    # splits the text into a list of strings 
    words = text_string.split()


    chains = {}

    # iterates through the text and saves unique pairs of words into a dict; keeps track of the word that comes next 
    for i in range(len(words)-2):
        if (words[i], words[i+1]) in chains:
            chains[(words[i], words[i+1])].append(words[i + 2])
        else:
            chains[(words[i], words[i+1])] = [words[i + 2]]

    # for i in range(len(words)-2):
    #     word_tuple = (words[i], words[i+1])
    #     following_word = words[i+2]
    #     value = chains.get(word_tuple, [])
    #     value.append(following_word)
    #     chains[word_tuple] = value
    #     print chains
    #     print

    # finds the two last words in the file to prompt the random generator to stop 
    last_words = (words[-2], words[-1])

    return chains, last_words


def make_text(chains, last_words):
    """Takes dictionary of markov chains; returns random text."""

    # Chooses a key to start at randomly and saves it to a working tuple 
    working_tuple = choice(chains.keys())

    # Creates our list of strings that we add the selected words to
    final_text = list(working_tuple)

    while working_tuple != last_words:

        word = choice(chains[working_tuple])
        final_text.append(word)
        working_tuple = (working_tuple[1], word)

    # concatenates the words into the final text 
    return (" ").join(final_text)


input_path = "Lose_yourself.txt"

#Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains, last_words = make_chains(input_text)

# Produce random text
random_text = make_text(chains, last_words)

print random_text

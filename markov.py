from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

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
    words = text_string.split()


    chains = {}

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


    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # Chooses a key to start at randomly 
    starting_tuple = choice(chains.keys())  

    # Creates our list of strings that we eventually join together 
    final_text = [starting_tuple[0], starting_tuple[1]]
    
    # Chooses a word randomly from the list 
    word = choice(chains[starting_tuple])

    # Creates a tuple with the second word of the random key and its random value
    working_tuple = (starting_tuple[1], word)

    while working_tuple != ("the", "earth."):

        word = choice(chains[working_tuple])
        final_text.append(word)
        working_tuple = (working_tuple[1], word)
        print working_tuple

    return (" ").join(final_text)



        #text = ""


    # your code goes here

    # return text


input_path = "gettysburg.txt"

#Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)


# Produce random text
random_text = make_text(chains)

print random_text

import helper
import gold

def parse_content(content):
    # function accepts the text contents of a file and returns a
    # dict mapping a word to its frequency

    freq_dict = {}
    word_lst = content.split()
    for word in word_lst:
        if freq_dict.get(word) is None:
            freq_dict[word] = 1
        else:
            freq_dict[word] = freq_dict.get(word) + 1

    return freq_dict

def make_tree(words):
    # function takes a dictionary mapping words to their frequency an returns
    # a trie represantation dictionary

    trie_dict = {}

    for word in words.keys():
        curr_node = trie_dict
        for character in word:
            if character not in curr_node:
                curr_node[character] = {}
            curr_node = curr_node[character]
        curr_node["$" + word] = words.get(word)

    return trie_dict

def predict(tree, numbers):
    return {}


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = gold.predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break

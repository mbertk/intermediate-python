def find_anagrams(letters, words):
    """Find a collection of anagrams of given letters from a given word bank.

    :param letters: The letters from which to form anagrams.
    :param words: A set of lowercase, alphabetic English words in a word bank.
    :return: A set of anagrams of the given letters found in the word bank.
    """
    #### ADD YOUR CODE BELOW ####
    # build up canonical rep
    dict = {}
    for word in words:
        # get canonical rep
        lst = word.split()
        word.sort()
        canonical = "".join(lst)
        # check if rep is in dict
        if dict.get(canonical) is None:
            dict[canonical] = {word,}
        else:
            dict[canonical] = dict.get(canonical).add(word)

    query = "".join(list(letters).sort())

    return dict.get(query)


    #### ADD YOUR CODE ABOVE ####


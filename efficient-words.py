"""Check whether a word is 'efficient' - if each letter can be drawn by a pencil without lifting."""
EFFICIENT_LETTERS = set('BCDGIJLMNOPSUVWZ')

def is_efficient(letters):
    diff =  set(letters).difference(EFFICIENT_LETTERS);
    if (len(diff) == 0):
        return True
    else:
        return False

"""Swap the keys and values in a mapping."""

def swap_keys_and_values(d):
    d2 = {y: x for x, y in d.items()}

    return d2
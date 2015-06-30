#!/usr/bin/python

# http://fallout.wikia.com/wiki/Terminal

test_data = [
    'having-3',
    'during-4',
    'shrine-3',
    'caring',
    'sirens',
    'friend',
    'living',
    'sprung',
    'facing',
    'period',
    'spring',
    'strong',
    'firmly',
    'firing',
]

def parse_args(arguments):
    guesses = []
    words = []
    for word in arguments:
        arg = word.split('-')
        if len(arg) > 1:
         guesses.append(arg)
        else:
            words.extend(arg)
    return guesses, words


def run(guesses, words):
    assert guesses, 'Guess at least once!'
    assert words, 'No words!'
    length = len(words[0])
    # for each word compare each letter to the letters/position of a guessed word
    # count the correct positions and letters
    # must be equal to be valid
    results = {}
    for word in words:
        results[word] = True
        for guess in guesses:
            correct_in_guess = int(guess[1])
            match_count = 0
            matches = []
            for position in range(0, length):
                if word[position].lower == guess[0][position].lower:
                    matches.append(word[position])
                    match_count += 1
                else:
                    matches.append('_')
            if match_count == correct_in_guess:
                print '{} vs. {} {}/{} \t{}'.format(guess[0], word, match_count, correct_in_guess, '.'.join(matches))
            else:
                results[word] = False

    for word, valid in results.iteritems():
        if valid:
            print word


if __name__ == '__main__':
    guesses, words = parse_args(test_data)
    run(guesses, words)

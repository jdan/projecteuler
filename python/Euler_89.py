# Euler 89 solution
# by Jordan Scales (http://jordanscales.com)
# 17 May 2013

def minimal_roman(n):
    alphabet = { 'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    # Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
    # I can only be placed before V and X.
    # X can only be placed before L and C.
    # C can only be placed before D and M.
    alphabet['IV'] = 4
    alphabet['IX'] = 9
    alphabet['XL'] = 40
    alphabet['XC'] = 90
    alphabet['CD'] = 400
    alphabet['CM'] = 900

    def greedy(num):
        keys = alphabet.keys()
        best_key = 'XL' # dummy best_key (length 2) and best_val
        best_val = 0

        for k in keys:
            # check that our key is better than the previous best
            if alphabet[k] <= num and alphabet[k] >= best_val:
                # check that our key isn't longer!
                if alphabet[k] == alphabet[best_key] and len(k) > len(best_key):
                    continue
                best_val = alphabet[k]
                best_key = k

        # return the best key
        return best_key

    string = ''
    # keep adding best_key's while we chop away at n
    while n > 0:
        best_match = greedy(n)
        string += best_match
        n -= alphabet[best_match]

    return string

def eval_roman(r):
    n = 0
    alphabet = { 'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

    for i, char in enumerate(r):
        # if the current symbol is LESS than the next, subtract it
        if i < len(r) - 1 and alphabet[r[i+1]] > alphabet[char]:
            n -= alphabet[char]
        else:
            n += alphabet[char]

    return n

if __name__ == '__main__':
    saved_chars = 0

    f = file('roman.txt')
    for item in f.readlines():
        item = item[:-1] # get rid of the \n at the end
        
        # compute the old length, and new length
        old_length = len(item)
        new_length = len(minimal_roman(eval_roman(item)))

        print item + ' (' + str(eval_roman(item)) + ')' + ' -> ' + minimal_roman(eval_roman(item)) + ' (' + str(old_length - new_length) + ')'

        # add them to the total
        saved_chars += old_length - new_length

    f.close()

    print 'Total: %s' % saved_chars

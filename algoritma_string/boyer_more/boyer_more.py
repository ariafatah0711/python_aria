class last_onccurence(object):
    def __init__(self, pattern, alphabet):
         self.occurrences = dict()
         for letter in alphabet:
            # print(letter, self.occurrences)
            self.occurrences[letter] = pattern.rfind(letter)
    def __call__(self, letter):
        return self.occurrences[letter]

def boyer_more(text, pattern):
    
    alphabet = set(text)
    last = last_onccurence(pattern, alphabet)
    t = len(text)
    p = len(pattern)
    i = p - 1
    j = p - 1
    
    while i < t:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + p - min(j, 1 + l)
            j = p - 1
    return -1
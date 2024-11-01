'''
logika algoritma pencokan stringnya udah paham tapi implementasi di codinganya masih lumayan binggung


membuat data set gitu untuk melihat apakah text itu terdapat pada pettern jika tidak ada return -1
jika ada maka dia akan dicocokan di index berapa patternya
misal text: hewan sapi memiliki 4 kaki sedangkan hewan ayam memiliki 2 kaki
      patt: kaki
    maka a = 1
         b = -1
         c = -1
         ....
         k = 2 (index terbesar)
         i = 3
'''
class last_onccurence(object):
    '''membuat data set untuk mencocokan apakah set(alphabet uniqe) ada pada pattern
    dan akan dibuatt dict semuanya namun ketika ditemukan kesamaan maka akan dilakukan'''
    def __init__(self, pattern, alphabet):
         self.occurrences = dict()
         for letter in alphabet:
            # mencari posisi akhir
            print(letter, self.occurrences)
            self.occurrences[letter] = pattern.rfind(letter)
    def __call__(self, letter):
        '''jika tidak cocok akan menghasilkan -1'''
        return self.occurrences[letter]

def boyer_more(text, pattern):
    
    alphabet = set(text)
    last = last_onccurence(pattern, alphabet)
    t = len(text)
    p = len(pattern)
    i = p - 1 # text index
    j = p - 1 # pattern index
    
    while i < t:
        if text[i] == pattern[j]:
        # jika text[i] ()
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
            
def show_match(text, pattern):
    print(text)
    position = boyer_more(text, pattern)
    if position != -1:
        print(f'{"." * position}{pattern}')
        print(f'Match at position {position}')
    else:
        print(f'Pattern "{pattern}" not found in the text.')

text = "hewan sapi memiliki 4 kaki sedangkan hewan ayam memiliki 2 kaki"
pattern = "kaki"

alphabet = set(text)
last = last_onccurence(pattern, alphabet)
print(last(text[0]))

show_match(text, pattern)

##############################
# alphabet = set(text)
# last = last_onccurence(pattern, alphabet)
print(last(text[0]))
print(last(text[1]))
print(last(text[22])) # k = 2
print(last(text[23])) # a = 1
print(last(text[24])) # k = 1

# template
# text = 'abacaabadcabacabaabb'
# pattern = 'abacab'
# show_match(text, pattern)
# print("")

# text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.'
# pattern = 'dolor'
# show_match(text, pattern)
# show_match(text, pattern + 'e')

# https://gist.github.com/dbrgn/1154006
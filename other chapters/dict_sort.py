import operator

def main(filename):
    frequency = word_frequency(read_words(filename))
    for c in frequency:
        print c[0] ,c[1]

def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    a=sorted(frequency.iteritems(), key=operator.itemgetter(1))[::-1]
    return a   
def read_words(filename):
    return open(filename).read().split()


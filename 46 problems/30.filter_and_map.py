#Q30
# prints the indexes of the words which are greater than the specified length
filter(lambda x: map(lambda x: len(x), words)[x] > 3, range(0, len(words)) )
#prints the respective words, from words list from the index list provided using map function
map(lambda x: words[x], filter(lambda x: map(lambda x: len(x), words)[x] > 3, range(0, len(words)) ) )

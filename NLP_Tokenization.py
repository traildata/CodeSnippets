from nltk.tokenize import word_tokenize,sent_tokenize

para = "Hi Mr. Sam how are you doing today ? I hope you like the oranges!"

print(word_tokenize(para))

print(sent_tokenize(para))


for i in sent_tokenize(para):
    print(i)



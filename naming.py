
while True:

    sentence = input('file name?: ')

    words = sentence.split()
    words_with_hyphen = []

    i = 0
    while i < len(words)-1:
        words[i] += '-'
        words_with_hyphen.append(words[i])
        i += 1

    sentence_with_hyphen = ''
    for i in words_with_hyphen:
        sentence_with_hyphen += i 

    sentence_with_hyphen += words[-1] 

    print(sentence_with_hyphen)

    response = input('Quit y/n?: ')

    if response == 'y':
        break


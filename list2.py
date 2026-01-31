def match_word(word):
    ctr = 0
    lst = []
    for word in word:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print(lst)
    return ctr
print("The number of words whose first and last letter are matching:")
ctr = match_word(['aba' , 'xyz', '12221'])
print(ctr)
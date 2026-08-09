def process(l,word):
    word=word.strip()
    if word in l:
        l.remove(word)
    return l1

l1=['sinchana', 'mokshith', 'harshan;']
l1=process(l1, 'mokshith')
print(l1)
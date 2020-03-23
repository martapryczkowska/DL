def fibonacci(word):
    if word == 1:
        return 1
    elif word == 0:
        return 0
    else:
        return fibonacci(word-1)+fibonacci(word-2)


res = fibonacci(10)
print(res)

def fib2(word):
    word1 = 0
    word2 = 1
    for i in range(word):
        word1 = word1 + word2

    return word1

print(fib2(5))



def findMissing(tab):
    tab = sorted(tab)
    for i in range(tab[1], len(tab)):
        word = tab[i-1] + 1
        if tab[i] != word:
            return word

tablica = [0, 2, 1, 4, 3, 8, 6, 5]
print(findMissing(tablica))



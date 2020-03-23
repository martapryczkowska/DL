a = ("a", "b", "c", "d", "e", "f", "g", "h")

x = slice(2)

print(a[x])

h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

list = [letter for letter in "human" if letter > "b"]
print(list)

#dekoratory wykonują coś przed, jako paramtertr przyjmują funkcje
def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")
result = divide(10, 2)
print(result)
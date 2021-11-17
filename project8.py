word = [(n) for n in input("Enter words: ").split()]
print(word)
l = 0
for i in (word):
    if len(i) > l:
        l = len(i)
        a = i
print(f"Name:{a} and No. of alpha.:{l}")

def count_vowel(string):
    counter = 0
    for char in string.lower():
        if char in "aeiou":
            counter += 1
    print(counter)

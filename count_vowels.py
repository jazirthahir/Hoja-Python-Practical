def count_vowels(text):
    count_of_vowels = 0
    
    for letter in text :
        if letter.lower() in "aeiou":
            count_of_vowels = +1
    return count_of_vowels

text = input("enter your tex: ")
countof_vowel = count_vowels(text)
print(countof_vowel)
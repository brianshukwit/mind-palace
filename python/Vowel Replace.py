# Vowel Replace
def translate(phrase):
    translation = ""
    for vowel in phrase:
        if vowel.lower() in "aeiou":
            if vowel.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"

        else:
            translation = translation + vowel
    return translation


print(translate(input("Enter a phrase: ")))
# Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.

words = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie', 'boy': 'matey', 'madam': 'proud beauty',
         'professor': 'foul blaggart', 'restaurant': 'galley', 'your': 'yer', 'excuse': 'arr', 'students': 'swabbies',
         'are': 'be', 'lawyer': 'foul blaggart', 'the': "th'", 'restroom': 'head', 'my': 'me', 'hello': 'avast',
         'is': 'be', 'man': 'matey'}

sentence = input("Type a string to translate to pirate language: ")
translate = ""

for word in sentence.split():
    if word in words:
        translate += words[word] + " "
    else:
        translate += word + " "
print(translate)

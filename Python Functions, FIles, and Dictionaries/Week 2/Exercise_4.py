# Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in
# alphabetical order which occur in the string together with the number of times each letter occurs. Case should be
# ignored.

string = input("Enter a string: ")
string = string.lower()
string = sorted(string)
d = {}

for c in string:
    if c not in d:
        d[c] = 0
    d[c] += 1

keys = d.keys()
for char in keys:
    print(char, d[char])

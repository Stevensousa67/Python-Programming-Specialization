# In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and
# up. Upper level Psychology classes are 400 and up. Create two lists, upper and lower. Assign each course in classes to
# the correct list, upper or lower. HINT: remember, you can convert some strings to different types!

classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103",
           "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper = []
lower = []

for word in classes:
    if 'MATH' in word:
        if int(word[5]) >= 3:
            upper.append(word)
        else:
            lower.append(word)

    elif 'ENG' in word:
        if int(word[4]) >= 2:
            upper.append(word)
        else:
            lower.append(word)

    elif 'PSYCH' in word:
        if int(word[6]) >= 4:
            upper.append(word)
        else:
            lower.append(word)

print(upper)
print(lower)

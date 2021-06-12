# Import the keyword module and test to see whether each of the words in list test are keywords. Save the respective
# answers in a list, keyword_test.

import keyword

test = ["else", "integer", "except", "elif"]
keyword_test = []

for word in test:
    keyword_test.append(keyword.iskeyword(word))

print(keyword_test)

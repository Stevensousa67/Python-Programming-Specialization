# Below, we have provided a nested list called big_list. Use nested iteration to create a dictionary, word_counts, that
# contains all the words in big_list as keys, and the number of times they occur as values.

big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]

word_counts = {}

for layer1 in big_list:
    if type(layer1) is list:
        for layer2 in layer1:
            if type(layer2) is list:
                for layer3 in layer2:
                    if layer3 not in word_counts:
                        word_counts[layer3] = 1
                    else:
                        word_counts[layer3] += 1
            else:
                if layer2 not in word_counts:
                    word_counts[layer2] = 1
                else:
                    word_counts[layer2] += 1
    else:
        if layer1 not in word_counts:
            word_counts[layer1] = 1
        else:
            word_counts[layer1] += 1

print(word_counts)

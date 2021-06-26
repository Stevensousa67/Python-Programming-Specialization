def strip_punctuation(s):
    new_s = ""
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for char in s:
        if char in punctuation_chars:
            continue
        else:
            new_s = new_s + char
    return new_s


def get_neg(s):
    global positive_words
    s = strip_punctuation(s)
    s = s.lower()
    counter = 0
    for word in s.split():
        if word in negative_words:
            counter += 1
    return counter


def get_pos(s):
    global positive_words
    s = strip_punctuation(s)
    s = s.lower()
    counter = 0
    for word in s.split():
        if word in positive_words:
            counter += 1
    return counter


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

outfile = open('resulting_data.csv', 'w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

with open('project_twitter_data.csv') as file:
    lines = file.readlines()
    for row in lines[1:]:
        num = row.split()[-1].split(',')
        positive_score = 0
        negative_score = 0
        for word in row.split():
            if word in positive_words:
                positive_score += 1
            if word in negative_words:
                negative_score += 1
        net_score = positive_score - negative_score
        row_file = '{}, {}, {}, {}, {}'.format(num[1], num[2], positive_score, negative_score, net_score)
        outfile.write(row_file)
        outfile.write('\n')
outfile.close()

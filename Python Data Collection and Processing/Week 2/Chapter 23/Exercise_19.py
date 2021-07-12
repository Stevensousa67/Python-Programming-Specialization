# Challenge: Write code to assign to the variable class_sched all the values of the key important classes.
# Do this using list comprehension.

tester = {'info': [
    {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science",
     'important classes': ['SI 106', 'ENGLISH 125', 'SI 110', 'AMCULT 202']},
    {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science',
     "important classes": ['SI 106', 'SI 410', 'PSYCH 111']},
    {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology',
     'important classes': ['WOMENSTD 220', 'SOC 101', 'ENS 384']},
    {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science',
     "important classes": ['SOC 101', 'AMCULT 334', 'EECS 281']},
    {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History',
     'important classes': ['ENGLISH 125', 'HIST 259', 'ENGLISH 130']},
    {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior',
     'important classes': ['PIANO 101', 'STUDIO 300', 'THEORY 229', 'MUSC 356']}]}

sublist = [d['important classes'] for d in tester['info']]
class_sched = []
[class_sched.append(word) for word in sublist for word in word]
print(class_sched)

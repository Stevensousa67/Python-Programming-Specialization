# Iterate through the list so that if the character ‘m’ is in the string, then it should be added to a new list called
# m_list. Hint: Because this isn’t just a list of lists, think about what type of object you want your data to be stored
# in. Conditionals may help you.

d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']

m_list = []

for item in d:
    if type(item) is not list:
        if 'm' in item:
            m_list.append(item)
    else:
        for item2 in item:
            if type(item2) is not list:
                if 'm' in item2:
                    m_list.append(item2)
            else:
                for item3 in item2:
                    if 'm' in item3:
                        m_list.append(item3)

print(m_list)

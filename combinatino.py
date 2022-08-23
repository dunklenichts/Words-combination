import csv

with open("combination.csv", encoding="utf8") as f:
    reader = csv.reader(f, delimiter=',')
    groups2 = list(reader)
    list_adj = []
    # print(len(groups2))

    # taking all adjectives
    for elem in range(1, len(groups2)):              # stroke
        for elem2 in range(0, 2):                    # column
            try:
                if groups2[elem][elem2] != '':
                    list_adj.append(groups2[elem][elem2])
            except:
                continue
    for elem in range(1, len(groups2)):
        for elem2 in range(3, 4):
            try:
                if groups2[elem][elem2] != '':
                    list_adj.append(groups2[elem][elem2])
            except:
                continue
    for elem in range(1, len(groups2)):
        for elem2 in range(5, 11):
            try:
                if groups2[elem][elem2] != '':
                    list_adj.append(groups2[elem][elem2])
            except:
                continue
    for elem in range(1, len(groups2)):
        for elem2 in range(12, len(groups2)):
            try:
                if groups2[elem][elem2] != '':
                    list_adj.append(groups2[elem][elem2])
            except:
                continue

    # creating lists of features and bases
    base1_list = []
    features = []
    # base
    for elem in range(1, len(groups2)):
        for elem2 in range(4, 5):
            try:
                if groups2[elem][elem2] != '':
                    base1_list.append(groups2[elem][elem2])
            except:
                continue
    for elem in range(1, len(groups2)):
        for elem2 in range(11, 12):
            try:
                if groups2[elem][elem2] != '':
                    base1_list.append(groups2[elem][elem2])
            except:
                continue
    # features
    for elem in range(1, len(groups2)):
        for elem2 in range(2, 3):
            try:
                if groups2[elem][elem2] != '':
                    features.append(groups2[elem][elem2])
            except:
                continue

# combination start
with open("combination.txt", "w+", encoding="utf8") as f:
    all_words = []
    # combination of base + adjective
    for elem in range(len(base1_list)):
        for elem2 in range(len(list_adj)):
            try:
                all_words = base1_list[elem] + ' ' + list_adj[elem2]
                f.write("".join(all_words) + '\n')
            except:
                continue

    # combination of base + feature
    for elem in range(len(base1_list)):
        for elem2 in range(len(features)):
            try:
                all_words = base1_list[elem] + ' ' + features[elem2]
                f.write("".join(all_words) + '\n')
            except:
                continue

    # combination of base + feature + adjective
    for elem in range(len(base1_list)):
        for elem2 in range(len(features)):
            for elem3 in range(len(list_adj)):
                try:
                    all_words = base1_list[elem] + ' ' + features[elem2] + ' ' + list_adj[elem3]
                    f.write("".join(all_words) + '\n')
                except:
                    continue
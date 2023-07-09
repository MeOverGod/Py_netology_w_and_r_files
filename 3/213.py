import os

with open('213.txt', 'w', encoding='utf-8') as file_213:

    with open('1.txt', 'rt', encoding='utf-8') as file_1:
        text_1  = file_1.readlines()
        count_1 = len(text_1)
        name_1 = str(file_1).split("'")[1]

    with open('2.txt', 'rt', encoding='utf-8') as file_2:
        text_2  = file_2.readlines()
        count_2 = len(text_2)
        name_2 = str(file_2).split("'")[1]

    with open('3.txt', 'rt', encoding='utf-8') as file_3:
        text_3  = file_3.readlines()
        count_3 = len(text_3)
        name_3 = str(file_3).split("'")[1]

    def def_1():
        file_213.write(str(name_1) + '\n')
        file_213.write(str(count_1) + '\n')

        for line in text_1:
            file_213.write(line)

    def def_2():
        file_213.write(str(name_2) + '\n')
        file_213.write(str(count_2) + '\n')

        for line in text_2:
            file_213.write(line)
        
    def def_3():
        file_213.write(str(name_3) + '\n')
        file_213.write(str(count_3) + '\n')

        for line in text_3:
            file_213.write(line)
        
    counts = []
    counts.append(count_1)
    counts.append(count_2)
    counts.append(count_3)
    counts = sorted(counts)    
    n = 0
    while n != 4:
        if count_1 == counts[n]:
            def_1()
        if count_2 == counts[n]:
            def_2()
        if count_3 == counts[n]:
            def_3()
        n += 1
        if n == 3:
            break
        file_213.write('\n')
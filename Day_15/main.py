with open("file1.txt") as f1:
    list_1 = [int(txt.strip()) for txt in f1.readlines()]
    # print(list_1)

with open("file2.txt") as f2:
    list_2 = [int(txt.strip()) for txt in f2.readlines()]
    # print(list_2)

new_list  = [item for item in list_1 if item in list_2]
print(new_list)
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

russian = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
my_file = []
with open("hw_5_4.txt", "r") as file_obj:
    for item in file_obj:
        item = item.split(" ", 1)
        my_file.append(russian[item[0]] + " " + item[1])
    print(my_file)
with open("hw_new.txt", "w") as file_obj_2:
    file_obj_2.writelines(my_file)


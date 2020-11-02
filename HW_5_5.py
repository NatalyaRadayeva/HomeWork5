# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def my_func():
    try:
        with open('file_6.txt', 'w+') as file_obj:
            my_line = input('Введите цифры через пробел \n')
            file_obj.writelines(my_line)
            my_numb = my_line.split()

            print(sum(map(int, my_numb)))

    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно введен номер. Ошибка ввода-вывода')
my_func()
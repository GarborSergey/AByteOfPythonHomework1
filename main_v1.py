import os  # Модуль для взаимодействия с операционной системой
import platform  # Модуль для получения информации о платформе
import time

version = '0.0.4'

if platform.platform().startswith('Windows'):  # Проверяет какая ОС на компьютере
    # формирует путь директории
    way_book_directory = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'Address books')
else:
    way_book_directory = os.path.join(os.getenv('HOME'), 'Address books')


# Печатает файл не найден
def file_not_found():
    print('\nАдресная книга с таким именем не найдена!\nМожет быть вы где-то ошиблись?')


# класс ЧЕЛОВЕК name, age, number
class Human:
    """Информация о человеке"""

    def __init__(self, name: str, age: str, number: str):
        self.name = name
        self.age = age
        self.number = number



# Проверка существования Адресной книги name_address_book.txt
def existence_book(name_address_book):
    """Проверяет существует-ли такая книга"""
    if os.path.exists(way_book_directory + os.sep + name_address_book + '.txt'):
        return True
    else:
        return False


# Создает адресную книгу
def create_book(name: str):
    """Создает каталог с адресными книгами, если такового нет, и пустую адресную книгу.
       Если данные о человеке уже есть в адресной книги не дублирует информацию"""

    if os.path.exists(way_book_directory):  # Проверяет есть ли уже такой каталог на компьютере
        None
    else:
        os.mkdir(way_book_directory)  # Создает каталог если нет
        print('Создан новый каталог с адресными книгами -->', way_book_directory)

    address_book = way_book_directory + os.sep + name + '.txt'  # Путь и имя создаваемой книги

    if existence_book(name):  # Проверяет есть ли уже такая книга в каталоге
        print('Адресная книга с таким именем уже есть, попробуйте другое')
    else:
        address_book = open(address_book, 'w+')  # Создаёт книгу
        # Напишем первую строчку в файле
        address_book.write('Адресная книга : ' + name + ' создана - ' + time.strftime('%d.%m.%Y') + '\n')
        address_book.close()
        print('Создана новая адресная книга с именем: {0} \nВ каталоге --> {1}'.format(name, way_book_directory))


# Удаляет адресную книгу
def delete_book(name_address_book):
    """Удаляет адресную книгу"""
    if existence_book(name_address_book):
        say = input('Are you sure? "Y" - yes or "N" - no --->')
        if say == 'Y':
            os.remove(way_book_directory + os.sep + name_address_book + '.txt')
            print('Адресная книга с именем: {0} была удалена'.format(name_address_book))
        elif say == 'N':
            print('Delete canceled')
        else:
            print("I don't understand what you input")
    else:
        file_not_found()


# Удаляет все данные из книги
def cleanup_book(name_address_book):
    """Удаляет все контакты из адресной книги"""
    if existence_book(name_address_book):
        file = open(way_book_directory + os.sep + name_address_book + '.txt', 'r+')
        lines = file.readlines()
        file.close()
        file = open(way_book_directory + os.sep + name_address_book + '.txt', 'w+')
        file.write(lines[0])
        file.close()
        print('\nВсе данные из адресной книги {0} были удалены'.format(name_address_book))
    else:
        file_not_found()


# Преобразовывает все данные из файла в список для дальнейшей работы с ними
# Обязательная функция перед работой с адресной книгой
def open_book(name_address_book: str):
    address_book_resources = []
    if existence_book(name_address_book):
        file = open(way_book_directory + os.sep + name_address_book + '.txt', 'r+')
        lines = file.readlines()
        file.close()
        for line in lines:
            strl = line.split(',')
            address_book_resources.append(strl)
            for lists in address_book_resources:
                i = 0
                for strings in lists:
                    up_str = strings.replace('\n', '')  # Удалил переход строки, чтобы в дальнейшем он не мешал
                    lists[i] = up_str
                    i += 1
        return address_book_resources
    else:
        file_not_found()
        return None


# Записывает новую информацию в книгу, стирая старую(старую мы вытаскивали и преобразовывали)
# Обязательная функция после работы с книгой, если были изменения
def write_book(name_address_book: str, upgrade_information: list):
    if existence_book(name_address_book):
        file = open(way_book_directory + os.sep + name_address_book + '.txt', 'w+')
        for info_lines in upgrade_information:
            info_lines_str = ",".join(info_lines)  # Преобразовал массив из массива, в строчку
            file.write(info_lines_str + '\n')  # Записал эту строчку в файл
        file.close()
    else:
        file_not_found()


# проверяет совпадения всех данных человека с людьми мз книги
def repeat_all(list_book_human: list, human: list):
    repeat = 0
    for person in list_book_human[1:]:
        if person[0] == human[0] and person[1] == human[1]:
            repeat += 1

    return repeat


# Возвращает из данных книги людей с одинаковым именем
def repeat_name(list_book_human: list, human_name: str):
    repeat_list = []
    for person in list_book_human:
        if person[0] == human_name:
            repeat_list.append(person)
        else:
            None
    return repeat_list


# Вывести параметры человека по имени
def find_human_by_name(name_address_book: str, human_name: str):
    list_book_human = open_book(name_address_book)
    repeat_list = repeat_name(list_book_human, human_name)
    if len(repeat_list) > 0:
        print('Найден(о) {0} человек(а) с именем {1}, в адресной книге {2} \nИМЯ____ВОЗРАСТ___НОМЕР:'.format(
            len(repeat_list), human_name, name_address_book))
        for repeat in repeat_list:
            print(*repeat)
    else:
        print('Человек с именем "{0}" не найден в адресной книге {1}'.format(human_name, name_address_book))


# Добавляет человека в адресную книгу
def add_human(name_address_book: str, human: Human):
    if existence_book(name_address_book):
        information = open_book(name_address_book)
        list_human = [human.name, human.age, human.number]
        # Если человек с такими данными уже есть в книге, ничего не сделает
        if repeat_all(information, list_human) == 0:
            information.append(list_human)
            write_book(name_address_book, information)
        else:
            None
    else:
        file_not_found()


# Удаляет человека из адресной книги по имени
# если таких имен несколько удаляет все это БАГА
def delete_human_of_name(name_address_book: str, human_name):
    if existence_book(name_address_book):
        list_book_human = open_book(name_address_book)
        delete = 0
        for person in list_book_human:
            if person[0] == human_name:
                list_book_human.remove(person)
                delete += 1
        if delete == 0:
            print('Human not found in address book')

        write_book(name_address_book, list_book_human)
    else:
        file_not_found()


# Выводит всю книгу на экран
def print_book(name_address_book: str):
    print_lists = open_book(name_address_book)
    for information in print_lists:
        print(*information)


# Если пользователь отменил
def canceled_script(word):
    if word == 'cancel':
        return False
    else:
        return True


def change_information(name_address_book: str, human_name):
    book_list = open_book(name_address_book)
    repeat_list = repeat_name(book_list, human_name)
    index = 0
    for repeat in repeat_list:
        index += 1
        print(index, '.', *repeat)
    if index >= 1:
        print('Information about which of these people you want to change?')
        index_change = int(input('input his number --->'))
        index_change -= 1
        print('Do you want to change age?')
        change_age = input('writ to "y" - to do it or any other key - dont do it ---> ')
        print('Do you want to change number?')
        change_number = input('writ to "y" - to do it or any other key - dont do it ---> ')
        if change_age == 'y':
            new_age = input('Input new information about age --->')
            repeat_list[index_change][1] = new_age
        if change_number == 'y':
            new_number = input('Input new number --->')
            repeat_list[index_change][2] = new_number
        delete_human_of_name(name_address_book, human_name)  # Тут использовал из-за баги
        for info in repeat_list:
            human = Human(info[0], info[1], info[2])
            add_human(name_address_book, human)
    if index == 0:
        print('This name dont found in address book "{0}"'.format(name_address_book))


# Предупреждение перед командой
def warning_script():
    print('Are you sure to do this? After you cant find this information')
    answer = input('writ to "y" - to do it or any other key - dont do it ---> ')
    if answer == 'y':
        return True
    else:
        return False


run = True

while run:
    command = input('\nInput command ---> ')
    if command == 'exit':
        run = False
    elif command == 'create book':
        name = input('Input name of the book ---> ')
        if canceled_script(name):
            create_book(name)
    elif command == 'delete book':
        name = input('Input name of the book to delete ---> ')
        if warning_script():
            delete_book(name)
    elif command == 'read book':
        name = input('Input name of the book to read ---> ')
        if canceled_script(name):
            print_book(name)
    elif command == 'cls':
        os.system('cls')
    elif command == 'add person':
        name_book = input('Input name of the book to add person ---> ')
        print('___Input info about the person___')
        human_name = input("Person's name ---> ")
        human_age = input("Person's age ---> ")
        human_number = input("Person's number ---> ")
        human = Human(human_name, human_age, human_number)
        add_human(name_book, human)
    elif command == 'find a person':
        name_book = input('Input name of the book to find person ---> ')
        name = input('Input name of the person to find ---> ')
        find_human_by_name(name_book, name)
    elif command == 'delete person':
        name_book = input('Input name of the book to delete person ---> ')
        name = input('Input name of the person to delete ---> ')
        delete_human_of_name(name_book, name)
        print('{0} удален(а) из адресной книги {1}'.format(name, name_book))
    elif command == 'clean book':
        name = input('Input name of the book to clean ---> ')
        if warning_script():
            cleanup_book(name)
    elif command == 'help':
        file = open('help.txt', 'r+')
        lines = file.readlines()
        file.close()
        for line in lines:
            print(line, end='')
    elif command == 'change info':
        name_book = input('Input name of the book to change person information  ---> ')
        if existence_book(name_book):
            name_human = input('Input the name of the person whose information you want to change ---> ')
            change_information(name_book, name_human)
    elif command == 'start':
        file = open('start.txt', 'r+')
        lines = file.readlines()
        file.close()
        for line in lines:
            print(line, end='')
    elif command == 'version':
        print('version is - {0}'.format(version))
    else:
        print('"{0}" is not a program command enter "help" to to view all commands'.format(command))

import os  # Модуль для взаимодействия с операционной системой
import platform  # Модуль для получения информации о платформе
import time

address_book_list = []  # Список всех адресных книг

if platform.platform().startswith('Windows'):  # Проверяет какая ОС на компьютере
    # формирует путь директории
    way_book_directory = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'Address books')
else:
    way_book_directory = os.path.join(os.getenv('HOME'), 'Address books')


def file_not_found():
    print('\nАдресная книга с таким именем не найдена!\nМожет быть вы где-то ошиблись?')


class Human:
    """Информация о человеке"""
    numbers_of_human = 0

    def __init__(self, name: str, age: str, number: str):
        self.name = name
        self.age = age
        self.number = number
        Human.numbers_of_human += 1

    def __del__(self):
        Human.numbers_of_human -= 1


def existence_book(name_address_book):
    """Проверяет существует-ли такая книга"""
    if os.path.exists(way_book_directory + os.sep + name_address_book + '.txt'):
        return True
    else:
        return False


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

    address_book_list.append(name)


def add_human(name_address_book: str, human: Human):
    """Добавить человека в адресную книгу"""

    if existence_book(name_address_book):
        repeat = False
        file = open(way_book_directory + os.sep + name_address_book + '.txt', 'r+')
        lines = file.readlines()  # Получил список строк из файла
        file.close()
        for line in lines[1:]:  # Бегу по элементам списка т.е по строкам
            line_list_str = line.split(',')  # Делю строку по запятым получаю список параметров
            # Сравниваю данные из книги с вводимыми данными
            # удалил переход на следующую строку т.к. иначе условие не выполнялось если данные одинаковые
            if line_list_str[0] == human.name and line_list_str[1] == human.age and line_list_str[2].replace('\n', '') == human.number:
                repeat = True

        if repeat:
            print('Хмм, странно, человек с таким именем и данными уже есть в адресной книги {0}'.format(
                name_address_book))
        else:
            file = open(way_book_directory + os.sep + name_address_book + '.txt', 'a+')
            file.write(human.name + ',' + human.age + ',' + human.number + '\n')
            file.close()
            print('{0} записан(а) в адресную книгу "{1}"'.format(human.name, name_address_book))
    else:
        file_not_found()


def read_book(name_address_book):
    """Напечатать всю адресную книгу"""
    if existence_book(name_address_book):
        file = open(way_book_directory + os.sep + name_address_book + '.txt', 'r+')
        while True:
            line = file.readline()
            if len(line) == 0:
                break
            print(line, end='')
        file.close()
    else:
        file_not_found()


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


def delete_book(name_address_book):
    """Удаляет адресную книгу"""
    if existence_book(name_address_book):
        os.remove(way_book_directory + os.sep + name_address_book + '.txt')
        print('Адресная книга с именем: {0} была удалена'.format(name_address_book))
    else:
        file_not_found()


def information_human_of_name(human_name: str, name_address_book: str):
    """Выводит информацию о всех людях с указанным именем в у казанной адресной книги,
       так же выводит число совпадений и информацию о каждом совпадении"""
    repeat = 0
    age = []
    number = []
    if existence_book(name_address_book):
        file = open(way_book_directory + os.sep + name_address_book + '.txt', 'r+')
        lines = file.readlines()  # Получил список строк из файла
        file.close()
        for line in lines[1:]:  # Бегу по элементам списка т.е по строкам
            line_list_str = line.split(',')  # Делю строку по запятым получаю список параметров
            if line_list_str[0] == human_name:
                repeat += 1
                age.append(line_list_str[1])
                number.append(line_list_str[2])

        if repeat > 0:
            print('Найден(о) {0} человек(а), с именем {1} в адресной книги {2}'.format(repeat, human_name,
                                                                                       name_address_book))
            print('Вот информация о них')
            for i in range(repeat):
                print('{0} совпадение: возраст {1}, номер {2}'.format(str(i+1), age[i], number[i]))
        else:
            print('В адресной книги {0}, нету информации о человеке с именем {1}'.format(name_address_book, human_name))





def test():
    h1 = Human('fff', '1221322', '123')
    h2 = Human('fdf', '1223112', '1233')
    h3 = Human('fds', '1221132', '12312')
    add_human('test1', h1)
    add_human('test1', h2)
    add_human('test1', h3)

create_book('test1')
test()





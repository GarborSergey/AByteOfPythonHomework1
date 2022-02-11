import os  # Модуль для взаимодействия с операционной системой
import platform  # Модуль для получения информации о платформе
import time

address_book_list = []  # Список всех адресных книг на компьютере
how_many_people = 0  # Количество людей во всех адресных книгах


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
    numbers_of_human = 0

    def __init__(self, name: str, age: str, number: str):
        self.name = name
        self.age = age
        self.number = number
        Human.numbers_of_human += 1

    def __del__(self):
        Human.numbers_of_human -= 1


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
        address_book_list.append(name)

    address_book_list.append(name)


# Удаляет адресную книгу
def delete_book(name_address_book):
    """Удаляет адресную книгу"""
    if existence_book(name_address_book):
        os.remove(way_book_directory + os.sep + name_address_book + '.txt')
        print('Адресная книга с именем: {0} была удалена'.format(name_address_book))
        address_book_list.remove(name_address_book)
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
# Обязательная функция после работы с книгой
def write_book(name_address_book: str, upgrade_information: list):
    if existence_book(name_address_book):
        file = open(way_book_directory + os.sep + name_address_book + '.txt', 'w+')
        for info_lines in upgrade_information:
            info_lines_str = ",".join(info_lines)  # Преобразовал массив из массива, в строчку
            file.write(info_lines_str + '\n')  # Записал эту строчку в файл
        file.close()
    else:
        file_not_found()


def add_human(name_address_book: str, human: Human):
    if existence_book(name_address_book):
        information = open_book(name_address_book)
        list_human = [human.name, ] # Остановился вот здесь нужно добавить чела в книгу!!!

    else:
        file_not_found()

m = open_book('test1')
write_book('test1', m)
print(m)







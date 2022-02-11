import os

way_book_directory = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'Address books')
name_address_book = 'test1'
file = open(way_book_directory + os.sep + name_address_book + '.txt', 'r+')
lines = file.readlines()
file.close()
print(lines)
about_human = []
for line in lines[1:]:
    print(line)

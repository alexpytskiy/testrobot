import os
import shutil
import time

path = "C:\\Users\\a.pytskiy\\Downloads"


#ищем последний файл в папке загрузок
filename = max([os.path.join(path, f) for f in os.listdir(path)], key=os.path.getmtime)
print(filename)

#переименовываем файл
rename_file = os.rename(filename, os.path.join(path, "123.pptx"))
new_filename = max([os.path.join(path, f) for f in os.listdir(path)], key=os.path.getmtime)
print(new_filename)

#перемещаем новый файл в нужную папку
new_path = "L:\\ОТДЕЛЫ\\ОТДЕЛ ФИЛИАЛОВ и ПРЕДСТАВИТЕЛЬСТВ\\Маркетинговый союз\\Отчёты\\!Python projects\\выгрузки\\" + "123.pptx"
shutil.move(new_filename, new_path)

print(new_path)




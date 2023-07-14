import openpyxl as xl
from datetime import datetime as dt



#указываем путь до файла с датами
filename = "L:\\ОТДЕЛЫ\ОТДЕЛ ФИЛИАЛОВ и ПРЕДСТАВИТЕЛЬСТВ\\Маркетинговый союз\\Отчёты\\!Python projects\\test venv\\files\\dates.xlsx"

#загружаем файл. указываем, что из него нужно брать только значения (без формул)
wb = xl.load_workbook(filename, data_only=True)

#активируем первый открывшийся лист (Лист1)
ws = wb.active

#достаем ячейку A2 в переменную
cell = ws.cell(row=2, column=1).value

#меняем формат даты на нужный
cell_2 = dt.strftime(cell, '%Y-%m-%d')


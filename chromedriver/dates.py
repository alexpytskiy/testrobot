import openpyxl as xl
from datetime import datetime as dt
import win32com.client
import time



#указываем путь до файла с датами
filename = "L:\\ОТДЕЛЫ\ОТДЕЛ ФИЛИАЛОВ и ПРЕДСТАВИТЕЛЬСТВ\\Маркетинговый союз\\Отчёты\\!Python projects\\test venv\\files\\dates.xlsx"

xlapp = win32com.client.DispatchEx("Excel.Application")
wb = xlapp.Workbooks.Open(filename)
wb.RefreshAll()
time.sleep(5)
wb.Save()
xlapp.Quit()



#загружаем и открываем файл. указываем, что из него нужно брать только значения (без формул)
#wb = xl.load_workbook(filename, data_only=True)
wb = xl.open(filename, data_only=True)

#активируем первый открывшийся лист (Лист1)
ws = wb.active
wb.save(filename)
wb.close()

#достаем ячейку A2 в переменную
cell = ws.cell(row=2, column=1).value

#меняем формат даты на нужный
cell_2 = dt.strftime(cell, '%Y-%m-%d')


print(cell_2)


# python packages
"""
NumPy
pyQt
pyTestpy -
Pendulum
Requests
Tkinter
py32
Pandas
Python Imaging Library
MoviePy

"""
import xlrd

loc = ("C:\\Users\\Lenovo\\Desktop\\Book1.xlsx")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)
print(sheet.cell_value(0, 0))

# Editing Excel Workbooks

import openpyxl, os

wb = openpyxl.Workbook() # creates a new Workbook object
wb.get_sheet_names()

sheet = wb.get_sheet_by_name('Sheet')

sheet

sheet['A1'].value
# will be none at this time

sheet['A1'] = 42
sheet['A2'] = 'Hello'

wb.save('new_example.xlsx')


>> workbook = openpyxl.load_workbook('example.xlsx')
>>> type(workbook)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> workbook.get_sheet_by_name('Sheet1')
<Worksheet "Sheet1">
>>> sheets = workbook.get_sheet_names
>>> sheets
<bound method Workbook.get_sheet_names of <openpyxl.workbook.workbook.Workbook object at 0x0000017AF58480F0>>
>>> print(sheets)
<bound method Workbook.get_sheet_names of <openpyxl.workbook.workbook.Workbook object at 0x0000017AF58480F0>>
>>> workbook.get_sheet_names()
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheets = workbook.get_sheet_names()
>>> sheets
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet = workbook.get_sheet_by_name('Sheet1')
>>> sheet['A1']
sheet['A1'].value
str(sheet['A1'].value)

sheet.cell(row=1, column=2)
# that's another way of accessing the same value
# allows you to iterate through as though it's a 2D array

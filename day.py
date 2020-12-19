from openpyxl import load_workbook

wb = load_workbook('./lxml/schedule.xlsx')
sheet = wb.active
var = sheet['A1'].value
c = sheet['B2']
c.row
c.column
c.coordinate

# ПОНЕДЕЛЬНИК
massive_monday = ['Понедельник']
lesson = 0
for monday in range(8):
    lesson += 1
    monday = sheet.cell(row=lesson, column=2).value
    if monday == 'Понедельник':
        continue
    if monday is None:  # избавились от пустых значений в таблице
        continue
    massive_monday.append(f'{lesson - 1} пара: ' + monday)
monday = '\n'.join(massive_monday)  # делать все через массив

# ВТОРНИК
massive_tuesday = ['Вторник']
lesson = 0
for tuesday in range(8):
    lesson += 1
    tuesday = sheet.cell(row=lesson, column=3).value
    if tuesday == 'Вторник':
        continue
    if tuesday is None:  # избавились от пустых значений в таблице
        continue
    massive_tuesday.append(f'{lesson - 1} пара: ' + tuesday)
tuesday = '\n'.join(massive_tuesday)  # делать все через массив

# СРЕДА
massive_wednesday = ['Среда']
lesson = 0
for wednesday in range(8):
    lesson += 1
    wednesday = sheet.cell(row=lesson, column=4).value
    if wednesday == 'Среда':
        continue
    if wednesday is None:  # избавились от пустых значений в таблице
        continue
    massive_wednesday.append(f'{lesson - 1} пара: ' + wednesday)
wednesday = '\n'.join(massive_wednesday)  # делать все через массив

# ЧЕТВЕРГ
massive_thursday = ['Четверг']
lesson = 0
for thursday in range(8):
    lesson += 1
    thursday = sheet.cell(row=lesson, column=5).value
    if thursday == 'Четверг':
        continue
    if thursday is None:  # избавились от пустых значений в таблице
        continue
    massive_thursday.append(f'{lesson - 1} пара: ' + thursday)
thursday = '\n'.join(massive_thursday)  # делать все через массив

# ПЯТНИЦА
massive_friday = ['Пятница']
lesson = 0
for friday in range(8):
    lesson += 1
    friday = sheet.cell(row=lesson, column=6).value
    if friday == 'Пятница':
        continue
    if friday is None:  # избавились от пустых значений в таблице
        continue
    massive_friday.append(f'{lesson - 1} пара: ' + friday)
friday = '\n'.join(massive_friday)  # делать все через массив

# СУББОТА
massive_saturday = ['Пятница']
lesson = 0
for saturday in range(8):
    lesson += 1
    saturday = sheet.cell(row=lesson, column=7).value
    if saturday == 'Пятница':
        continue
    if saturday is None:  # избавились от пустых значений в таблице
        continue
    massive_saturday.append(f'{lesson - 1} пара: ' + saturday)
saturday = '\n'.join(massive_saturday)  # делать все через массив

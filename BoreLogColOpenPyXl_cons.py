import openpyxl
import os

filepath = 'BoreLogCol.xlsx'
if not os.path.exists(filepath): 
	workbook = openpyxl.Workbook()
	sheet = workbook.active
	sheet.append(['N объекта', 'N скважины', 'Дата', 'Абс.отм.', 'Глуб.скв.', 'Кровля ИГЭ', 'Описание ИГЭ', 'Вид обр.', 
					'Глуб.обр.', 'Подошва ИГЭ'])
	workbook.save(filepath)
else:
	workbook = openpyxl.load_workbook(filepath)
	sheet = workbook.active
	sheet.append(['N объекта', 'N скважины', 'Дата', 'Абс.отм.', 'Глуб.скв.', 'Кровля ИГЭ', 'Описание ИГЭ', 'Вид обр.', 
					'Глуб.обр.', 'Подошва ИГЭ'])
	workbook.save(filepath)

print('Электронный журнал')
obj_nm = input('N объекта: ')
bore_nm = input('N скважины: ')
bore_date = input('Дата: ')
bore_abs = input('Абс.отм.: ')
bore_depth = input('Глуб.скв.: ')
layer_roof = input('Кровля ИГЭ: ')
layer_descr = input('Описание ИГЭ: ')
sample_type = input('Вид образца: ')
sample_depth = input('Глуб.образца: ')
sheet.append([obj_nm, bore_nm, bore_date, bore_abs, bore_depth, layer_roof, layer_descr, sample_type, sample_depth])
sample_plus = input('Ещё образец? д/н: ')
while sample_plus != 'н':
	sample_type = input('Вид образца: ')
	sample_depth = input('Глуб.образца: ')
	sheet.append(['','','','','','','',sample_type, sample_depth])
	sample_plus = input('Ещё образец? д/н ')
layer_base = input('Подошва ИГЭ: ')
sheet.append(['','','','','','','','','',layer_base])
while bore_depth != layer_base:
	layer_roof = input('Кровля ИГЭ: ')
	layer_descr = input('Описание ИГЭ: ')
	sample_type = input('Вид образца: ')
	sample_depth = input('Глуб.образца: ')
	sheet.append([obj_nm, bore_nm, bore_date, bore_abs, bore_depth, layer_roof, layer_descr, sample_type, sample_depth])
	sample_plus = input('Ещё образец? д/н: ')
	while sample_plus != 'н':
		sample_type = input('Вид образца: ')
		sample_depth = input('Глуб.образца: ')
		sheet.append(['','','','','','','',sample_type, sample_depth])
		sample_plus = input('Ещё образец? д/н ')
	layer_base = input('Подошва ИГЭ: ')
	sheet.append(['','','','','','','','','',layer_base])
workbook.save(filepath)
f = open('BoreLog.xls', 'a')
bore_nm = input('Электронный журнал скважины No: ')
f.write('Электронный журнал скважины No '+bore_nm+'\n')
bore_date = input('Дата: ')
f.write('Дата: '+bore_date+'\n')
bore_abs = input('Абс.отм., м: ')
f.write('Абс.отм., м: '+bore_abs+'\n')
bore_depth = input('Глуб.скв., м: ')
f.write('Глуб.скв., м: '+bore_depth+'\n')
layer_roof = input('Кровля ИГЭ, м: ')
f.write('Кровля ИГЭ, м: '+layer_roof+'\n')
layer_descr = input('Описание ИГЭ: ')
f.write('Описание ИГЭ: '+layer_descr+'\n')
sample_type = input('Вид образца: ')
f.write('Вид образца: '+sample_type+' \n')
sample_depth = input('Глуб.образца, м: ')
f.write('Глуб.образца, м: '+sample_depth+' \n')
sample_plus = input('Ещё образец? д/н ')
while sample_plus == 'д':
	sample_type = input('Вид образца: ')
	f.write('Вид образца: '+sample_type+' \n')
	sample_depth = input('Глуб.образца, м: ')
	f.write('Глуб.образца, м: '+sample_depth+' \n')
	sample_plus = input('Ещё образец? д/н ')
layer_depth = input('Подошва ИГЭ, м: ')
f.write('Подошва ИГЭ, м: '+layer_depth+' \n')
while bore_depth != layer_depth:
	layer_roof = input('Кровля ИГЭ, м: ')
	f.write('Кровля ИГЭ, м: '+layer_roof+' \n')
	layer_descr = input('Описание ИГЭ: ')
	f.write('Описание ИГЭ: '+layer_descr+' \n')
	sample_type = input('Вид образца: ')
	f.write('Вид образца: '+sample_type+' \n')
	sample_depth = input('Глуб.образца, м: ')
	f.write('Глуб.образца, м: '+sample_depth+' \n')
	sample_plus = input('Ещё образец? д/н ')
	while sample_plus == 'д':
		sample_type = input('Вид образца: ')
		f.write('Вид образца: '+sample_type+' \n')
		sample_depth = input('Глуб.образца, м: ')
		f.write('Глуб.образца, м: '+sample_depth+' \n')
		sample_plus = input('Ещё образец? д/н ')
	layer_depth = input('Подошва ИГЭ, м: ')
	f.write('Подошва ИГЭ, м: '+layer_depth+'\n')
f.write('\n')
f.close()
def xlupload():
	if True:
	
		file="dataset.xlsx"
		print(file,'---------------------------------------------------------------------')
		import xlrd
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		dataset.objects.all().delete()
		for r in range(1, sheet.nrows):
			f0 = sheet.cell(r, 0).value
			f1 = sheet.cell(r, 1).value
			f2 = sheet.cell(r, 2).value
			f3 = sheet.cell(r, 3).value
			f4 = sheet.cell(r, 4).value
			f5 = sheet.cell(r, 5).value
			f6 = sheet.cell(r, 6).value
			f7 = sheet.cell(r, 7).value
			f8 = sheet.cell(r, 8).value
			f9 = sheet.cell(r, 9).value
			f10 = sheet.cell(r, 10).value
			f11 = sheet.cell(r, 11).value
			f12 = sheet.cell(r, 12).value
			f13 = sheet.cell(r, 13).value
			f14 = sheet.cell(r, 14).value
			f15 = sheet.cell(r, 15).value
			f16 = sheet.cell(r, 16).value
			res = sheet.cell(r, 17).value
			print(res)
xlupload()

			

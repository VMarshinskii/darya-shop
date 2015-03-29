import xlrd
rb = xlrd.open_workbook('sf.xls', formatting_info=True)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    print(row[1] + " " + row[2] + " " + str(row[7]).replace(".0", "") + " " + row[3])

print(range(sheet.nrows))
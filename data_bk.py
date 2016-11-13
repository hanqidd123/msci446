import openpyxl
import nltk

wb = openpyxl.load_workbook('clean_data.xlsx')
sheet = wb.get_sheet_by_name("data")
dataStr = wb.get_sheet_by_name("matrix")
discipline_list = []

for x in range(1,4481):
    discipline_list.append(sheet.cell(row=2, column=x).value)

discipline_list = list(set(discipline_list))
discipline_list.sort()

print(discipline_list)

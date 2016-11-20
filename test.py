import openpyxl
import xlwt
import nltk
source = openpyxl.load_workbook('rawData-1.xlsx')
sheet = source.get_sheet_by_name("ps")
for x in range(2, 4):
    sentence = sheet["C" + str(x)].value.replace('\n', ' ')
    print(sentence)
    tokens = nltk.word_tokenize(sentence)
    print(tokens)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
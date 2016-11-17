import openpyxl
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

wb = openpyxl.load_workbook('clean_data.xlsx')
sheet = wb.get_sheet_by_name("Sheet1")
dataStr = wb.get_sheet_by_name("data")
matrix = wb.get_sheet_by_name("matrix")
regex_token = RegexpTokenizer(r'\w+')

for x in range(1, 4481):
    print(x)
    sentence = sheet["D" + str(x)].value
    print(sentence)
    countvectorizer = CountVectorizer(stop_words='english')
    tokens = regex_token.tokenize(sentence)
    y = countvectorizer.fit_transform(tokens)

    print(y)

#finding unique words

#wb.save('clean_ data.xlsx')







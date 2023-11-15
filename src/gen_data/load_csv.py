import csv

name_list = []
with open("./src/gen_data/static/names.csv","r") as fr:
    name_reader = csv.reader(fr,dialect='excel')
    
    for row in name_reader:
        if row != []:
            name_list.append(row[0])

surname_list = []
with open("./src/gen_data/static/surnames.csv","r") as fr:
    name_reader = csv.reader(fr,dialect='excel')
    
    for row in name_reader:
        if row != []:
            surname_list.append(row[0])


word_list = []
with open("./src/gen_data/static/word.csv","r") as fr:
    name_reader = csv.reader(fr,dialect='excel')
    
    for row in name_reader:
        word_list.append(row[0])
import csv
import json
import bz2
import os


# directory = "data/edges"
# print (directory)
# txt_file = 'processed/cleanedWD.txt'
# my_output_file = open(txt_file, "w")
# import chardet

# for filename in os.listdir(directory):
#     if filename.endswith('csv'):
#         file_path = os.path.join(directory, filename)
#         # with open(file_path, 'rb') as rawdata:
#         #     result = chardet.detect(rawdata.read(200000))
#         # if(result['encoding'] != 'ascii'):
#         #     print(filename)
#         #     print(result)
    
#         my_input_file = open(file_path, "r", encoding='utf-8')
#         # with open(csv_file, "r") as my_input_file:
#         [my_output_file.write("\t".join([row[0], row[3], row[2]])+'\n') for row in csv.reader(my_input_file, delimiter=',')]
#         my_input_file.close()

# my_output_file.close()

directory = 'data/subgraph'

# # input_file=open('data/small_try_file.json', 'r')
# # json_decode=json.load(input_file)
entity_names_file = 'data/names_file.txt'
entity_output_file = open(entity_names_file, 'w')
for filename in os.listdir(directory):
    if(filename.endswith('bz2')):
        file_path = os.path.join(directory, filename)
        with bz2.open(file_path, "rt") as bzinput:
            # json_decode=json.load(bzinput)
            for i, line in enumerate(bzinput):
            # for item in json_decode:
                item = json.loads(line)
                key = item.get('key')
                label = item.get('labels').get('en')
                aliases = item.get('aliases')
                if label:
                    entity_output_file.write(key+'\t'+'name'+'\t'+label+'\n')
                    [entity_output_file.write(key+'\t'+'alias'+'\t'+alias+'\n') for alias in aliases]


entity_output_file.close()


# for item in json_decode:
#     label = item.get('labels').get('en')
#     print(label)
#     aliases = item.get('aliases')
#     print(aliases)
#     if label:
#         entity_output_file.write(label+'\n')
#         [entity_output_file.write(alias+'\n') for alias in aliases]

# entity_output_file.close()
import os

color_green = '\x1b[5;30;42m'
color_red = '\x1b[1;30;41m'
color_end = '\x1b[0m'

# stop words modified from https://countwordsfree.com/stopwords
stopwords_filename = "stopwords.txt"
stopwords_filepath = os.path.join(os.path.dirname(__file__), stopwords_filename)
# print(stopwords_filepath)
with open(stopwords_filepath, 'r') as fd:
    lines = fd.readlines()
    stopwords_list = set([line.strip() for line in lines])
    print("load stop words...\t" + color_green + " Done " + color_end)
# print(stopwords_list)
# print(len(stopwords_list))

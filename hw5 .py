
# coding: utf-8

# In[5]:


# -*- coding:utf-8 -*-

import re
import csv
import json
import pickle


def main(filename):
    file = open(filename, "r+")
    wordcount = {}
    for word in file.read().split():
        word = re.sub(r'\W', "", word).lower()
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    with open('./word_counter.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        for key, value in wordcount.items():
            writer.writerow([key, value])
    
    with open('./word_counter.json', 'w') as json_file:
        json.dump(wordcount, json_file)

    with open('word_counter.pickle', 'wb') as handle:
        pickle.dump(wordcount, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    with open('word_counter.pickle', 'rb') as handle:
        b = pickle.load(handle)
        
    print(wordcount == b)
    
    file.close()


if __name__ == '__main__':
    filename = 'i_have_a_dream(1).txt'  # for filename inputting
    main(filename)

    


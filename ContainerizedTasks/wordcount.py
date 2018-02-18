#!/usr/bin/python                                                            
from pprint import pprint
import sys                                                
import os                                              
import urllib.request
import html2text
import time
import re
import uuid
from sh import tail
from azure.storage.table import TableService, Entity

urllib.request.urlretrieve (sys.argv[1], "foo.txt")                                  
                                                                             
file=open("foo.txt","r+")                                                     
html = open("foo.txt").read()                                                 
text = html2text.html2text(html)

# Set defaults
minLength = 0
numWords = 10

minLength = int(os.environ['MinLength'])
storageName = os.environ['AzureStorageName']
storageKey = os.environ['AzureStorageKey']

wordcount={}                                                                  
for word in text.split():

    word = re.sub('[^A-Za-z0-9]+', '', word)

    if len(word) == 0 or len(word) < minLength:
      continue

    if word not in wordcount:   
        wordcount[word] = 1             
    else:                                            
        wordcount[word] += 1
sortedList = sorted(wordcount.items(), key=lambda item: item[1], reverse=True)
                                                                              
numWords = int(os.environ['NumWords'])                                        
topWords = sortedList[:numWords]                                                
pprint(topWords)                                                                
file.close();


table_service = TableService(storageName, storageKey)
table_service.create_table('tasktable')

partitionKey = uuid.uuid4().hex

for result in topWords:
    task = Entity()
    task.PartitionKey = partitionKey
    task.RowKey = uuid.uuid4().hex
    task.url = sys.argv[1]
    task.word = result[0]
    task.count = result[1]
    table_service.insert_entity('tasktable', task)
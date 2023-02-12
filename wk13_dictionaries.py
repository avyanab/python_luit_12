#!/usr/bin/env python3.7

import os

#Create an empty list
my_list = []

#Create an empty dictionary
my_dict = {}

#List items and their attributes in current working directory
my_dir = os.getcwd()
file_list = os.listdir(my_dir)

for file in file_list:
    file_path = os.path.join(my_dir, file)
    file_attr = os.stat(file_path)

    #Add items into dictionaries and print the dictionaries in a list   
    my_dict = {
        'path': file_path,
        'file_name': file,
        'size': file_attr.st_size
    }
    my_list.append(my_dict)

print(*my_list, sep="\n")
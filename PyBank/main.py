# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 16:32:06 2023

@author: hriebow
"""

import csv
import os
from itertools import cycle

filename = os.path.join("Resources","budget_data.csv")

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    csv_header = next(csv_file)
    
    total_months = 0
    total_value = 0
    value_list = []
    change_list = []
    month = []
    
    for row in csv_reader:
        
        total_value += int(row[1])
        value_list.append(int(row[1]))
        month.append(row[0])
        
        
    
    total_months = len(value_list)

    value = cycle(value_list)
    
    num1 = next(value)
    num2 = next(value)
    length1 = int(len(value_list)-1)
    length2 = int(len(value_list)/2)
    diff = num2-num1
    change_list.append(diff)
   
    for i in range(length2):
        
        num1 = next(value)
        diff = num1 - num2
        change_list.append(diff)
        
        num2 = next(value)
        diff = num2 - num1
        change_list.append(diff)
    
    change_list.pop(-1)
    change_list.pop(-1)

    averageChangeValue = round(sum(change_list)/((length1)),2)
    
    max_change = max(change_list)
    min_change = min(change_list)
    
    max_indx = change_list.index(max_change)
    min_indx = change_list.index(min_change)
    
    max_date = month[max_indx+1]
    min_date = month[min_indx+1]
    
    
    print(f"Financial Analysis\n\n-----------------------------\n\nTotal Months: {total_months}\n\nTotal: {total_value}\n\nAverage Change: ${averageChangeValue}\n\nGreatest Increase in Profits: {max_date} (${max_change})\n\nGreatest Decrease in Profits: {min_date} (${min_change})")
    with open("Analysis\Analysis.txt",'w') as analysis_file:
        analysis_file.write(f"Financial Analysis\n\n-----------------------------\n\nTotal Months: {total_months}\n\nTotal: {total_value}\n\nAverage Change: ${averageChangeValue}\n\nGreatest Increase in Profits: {max_date} (${max_change})\n\nGreatest Decrease in Profits: {min_date} (${min_change})")

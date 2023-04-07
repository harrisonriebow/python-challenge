# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 22:43:22 2023

@author: hriebow
"""

import csv
import os

filename = os.path.join("Resources","election_data.csv")

with open(filename) as csv_file:
    
    csv_reader = csv.reader(csv_file)
    
    csv_header = next(csv_file)
    
    total_votes_list = []
    candidate_list = []
    
    for row in csv_reader:
        
        total_votes_list.append(row[0])
        candidate_list.append(row[2])
        
    total_votes = len(total_votes_list)
    total_charles = candidate_list.count("Charles Casper Stockham")
    total_diana = candidate_list.count("Diana DeGette")
    total_ray = candidate_list.count("Raymon Anthony Doane")
    
    percent_charles = round((total_charles/total_votes)*100,3)
    percent_diana = round((total_diana/total_votes)*100,3)
    percent_ray = round((total_ray/total_votes)*100,3)
    
    percent_dict = {"Charles Casper Stockham":percent_charles,"Diana DeGette":percent_diana,"Raymon Anthony Doane":percent_ray}
    
    winner_percent = max(percent_dict.values())
    
    name_list = list(percent_dict.keys())
    percent_list = list(percent_dict.values())
 
    for i in percent_list:
        if i == winner_percent:
            winner = name_list[percent_list.index(i)]
            
    print(f"Election Results\n"
          f"-----------------------------"
          f"\nTotal Votes: {total_votes}"
          f"\n-----------------------------"
          f"\nCharles Casper Stockham: {percent_charles}% ({total_charles})"
          f"\nDiana DeGette: {percent_diana}% ({total_diana})"
          f"\nRaymon Anthony Doane: {percent_ray}% ({total_ray})"
          f"\n-----------------------------"
          f"\nWinner: {winner}"
          f"\n-----------------------------")
       
    with open("Analysis\Analysis.txt",'w') as analysis_file:
        analysis_file.write(f"Election Results\n"
          f"-----------------------------"
          f"\nTotal Votes: {total_votes}"
          f"\n-----------------------------"
          f"\nCharles Casper Stockham: {percent_charles}% ({total_charles})"
          f"\nDiana DeGette: {percent_diana}% ({total_diana})"
          f"\nRaymon Anthony Doane: {percent_ray}% ({total_ray})"
          f"\n-----------------------------"
          f"\nWinner: {winner}"
          f"\n-----------------------------")
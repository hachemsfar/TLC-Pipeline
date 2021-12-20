#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:14:00 2021

@author: sfar
"""
import sqlite3
import pandas as pd

def load(list_files):
    # connecting to the database
    connection = sqlite3.connect("NYC_Taxi.db")
      
    # cursor
    crsr = connection.cursor()
      
    # print statement will execute if there
    # are no errors
    print("Connected to the database")
    
    for i in list_files:
        print(i)
        if(i.split("/raw")[0]=="Yellow Taxi Trip Records"):
            df = pd.read_csv(i)
            df.columns = [c.lower() for c in df.columns] 
            df.to_sql("Yellow Taxi", crsr)
            
        if(i.split("/raw")[0]=="Green Taxi Trip Records"):
            df = pd.read_csv(i)
            df.columns = [c.lower() for c in df.columns] 
            df.to_sql("Green Taxi", crsr)

        if(i.split("/raw")[0]=="For-Hire Vehicle Trip Records"):
            df = pd.read_csv(i)
            df.columns = [c.lower() for c in df.columns] 
            df.to_sql("FH Vehicle Taxi", crsr)
            
        if(i.split("/raw")[0]=="High Volume For-Hire Vehicle Trip Records"):
            df = pd.read_csv(i)
            df.columns = [c.lower() for c in df.columns] 
            df.to_sql("HV For-Hire Vehicle Taxi", crsr)

        
    # close the connection
    connection.close()
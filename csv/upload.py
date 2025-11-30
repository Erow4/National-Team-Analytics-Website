# Insert data from a csv file into a SQL db -- Note this is not used in the actual page, just to red data into SQL db

# NOTE: if you use this program you do need to hardcode the name of the table in the SQL command
# While not ideal, it was merely used as a stepping stone rather than used in the actual website
#------------

import os
import csv
import sys
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)


# Configure CS50 Library to use SQLite database
db = SQL(f"sqlite:///general.db")


def get_columns():

    # list to store the names of columns
    list_of_column_names = []

    # Read lines into memory from file
    filename = sys.argv[1]

    with open(filename) as f:
        file_reader = csv.reader(f, delimiter = ',')
        # loop to iterate through the rows of csv

        for row in file_reader:
            # add the first row & break after first iteration
            list_of_column_names.append(row)
            break
        columns = list_of_column_names[0]
        return columns


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python upload.py FILENAME")

    #get columns
    columns = get_columns()
    if len(columns) != 5:
        sys.exit("Usage: csv must have 5 columns")

     # Read lines into memory from file
    filename = sys.argv[1]

    with open(filename) as f:
        file_reader = csv.reader(f, delimiter = ',')
        # loop to iterate through the rows of csv
        next(file_reader, None)  # skip the headers
        for row in file_reader:
           # for column in columns:

                event = row[0]
                athlete = row[1]
                distance = row[2]
                time = row[3]
                classification = row[4]

###### Input table name each time ###############################
                index = db.execute("INSERT INTO may22 (event, athlete, distance, time, classification) VALUES (?, ?, ?, ?, ?)", event, athlete, distance, time, classification)



# Final Project/ $ python upload.py dec_2021.csv

# CREATE TABLE may22 (
#     event TEXT NOT NULL,
#     athlete TEXT NOT NULL,
#     distance TEXT NOT NULL,
#     time TIME NOT NULL,
#     classification TEXT
# );


if __name__ == "__main__":
    main()
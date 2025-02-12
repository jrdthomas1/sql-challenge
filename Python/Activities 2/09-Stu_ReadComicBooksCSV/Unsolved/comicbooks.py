# Modules
import os
import csv

# Prompt user for title lookup
title = input("what title are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "comic_books.csv")

# Set variable to check if we found the comic book

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(cvsreader)
    csv_header = next(csv.reader)

    # Loop through looking for the comic book
    for row in cvsreader:
                if row[0] == title:
                        print(f"{title} was published by {row[8]} in {row[9]}).")
                # Set variable to confirm we have found the comic book
                        found = true
    # If the comic book is never found, alert the user
if found == False:
                print("sorry, we dont have the title you're looking for!")
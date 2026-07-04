import csv
import os

filename = input("Alright, what CSV file are we looking for (include .csv)? ")

if os.path.exists(filename):
    print("File existing")
    
else:
    print("File does not exist. Give me a second, creating file.")
    with open(filename, mode= "w", newline= "") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "age", "gender"])
        
name = input("What's your name, darling😊? ")
age = input("How old are you? ")
gender = input("What gender do you identify as😏? ")

with open(filename, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, age, gender])
    
print("Yay💃! Information succesfully written to the CSV file.")


        
    

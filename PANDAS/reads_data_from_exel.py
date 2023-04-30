import os,sys
import pandas as pd

# Read the Excel file
df = pd.read_excel('friend.xlsx')

# Create an empty dictionary to store the data
students_dict = {}

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Get the rollno, name, and marks of the student
    rollno = row['roll no']
    name = row['name']
    marks1 = row['maths']
    marks2 = row['physics']
    marks3 = row['chemistry']
    
    # Calculate the total marks
    total = marks1 + marks2 + marks3
    
    # Create a dictionary for the student and add it to the main dictionary
    student_dict = {'name': name, 'maths': marks1, 'physics': marks2, 'chemistry': marks3, 'total': total}
    students_dict[rollno] = student_dict

# Print the dictionary data on the monitor
print(students_dict)
d = pd.DataFrame(students_dict)
print(d)

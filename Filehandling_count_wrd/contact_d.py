import pandas as pd,os

# Read the Excel file into a pandas dataframe
df = pd.read_excel(r'C:\Users\vaibh\Downloads\sports.xlsx')

# Create an empty dictionary to store the data
data = {}

# Iterate over the rows in the dataframe
for index, row in df.iterrows():
    # Extract the data from the row
    name = row['name']
    number = row['number']
    
    
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{name}\nFN:{name}\nTEL;TYPE=WORK,VOICE:{number}\nEND:VCARD"
    filename = f"{name.replace(' ', '_')}.vcf"
    with open(filename, "w") as f:
        f.write(vcard)
    data ={'name': name, 'number': number }
   

    # Add the student's data to the dictionary
    # data[index] = student_data
    print(data)
# Display the dictionary data on the monitor

# Open file in default application
    os.startfile(filename)


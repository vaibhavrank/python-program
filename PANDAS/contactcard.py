import os

# Accept contact details from user
name = input("Enter full name: ")
job_title = input("Enter job title: ")
company = input("Enter company name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")
website = input("Enter website (if any): ")
home_address = input("Enter home address: ")
work_address = input("Enter work address (if any): ")

# Create vcard string
vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{name}\nFN:{name}\nORG:{company}\nTITLE:{job_title}\nTEL;TYPE=WORK,VOICE:{phone}\nEMAIL;TYPE=PREF,INTERNET:{email}\nADR;TYPE=HOME:;;{home_address}\nADR;TYPE=WORK:;;{work_address}\nURL:{website}\nEND:VCARD"

# Save vcard to file
filename = f"{name.replace(' ', '_')}.vcf"
with open(filename, "w") as f:
    f.write(vcard)

# Open file in default application
os.startfile(filename)

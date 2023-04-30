# Import the necessary libraries
import vobject

# Prompt the user for their contact details
name = input("Enter your full name: ")
job_title = input("Enter your job title: ")
company_name = input("Enter your company name: ")
phone_number = input("Enter your phone number: ")
email_address = input("Enter your email address: ")
website = input("Enter your website (if any): ")
home_address = input("Enter your home address: ")
work_address = input("Enter your work address (if any): ")

# Create a new vCard object
card = vobject.vCard()

# Set the contact details for the vCard
card.add('n')
card.n.value = vobject.vcard.Name(family=name.split()[-1], given=name.split()[0])
card.add('fn')
card.fn.value = name
card.add('title')
card.title.value = job_title
card.add('org')
card.org.value = [company_name]
card.add('tel')
card.tel.type_param = 'WORK'
card.tel.value = phone_number
card.add('email')
card.email.type_param = 'INTERNET'
card.email.value = email_address
card.add('url')
card.url.value = website
card.add('adr')
card.adr.type_param = 'HOME'
card.adr.value = vobject.vcard.Address(street=home_address)
if work_address:
    card.add('adr')
    card.adr.type_param = 'WORK'
    card.adr.value = vobject.vcard.Address(street=work_address)

# Save the vCard to a file
with open(f"{name.replace(' ', '_')}.vcf", "w") as f:
    f.write(card.serialize())

print("vCard file created successfully!")

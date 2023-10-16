# Contact Information: Store name, phone number, email, and address for each contact.
# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers.
# Search Contact: Implement a search function to find contacts by name or phone number.
# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction.\
# for name in sorted(contacts.keys()):

# I have choosen a dictionary within a dictionary as a Data Structure to create a Contact List
# Where name should act as key to the contact (dictionary)
def add_contact(contacts, name):
    contact = {}     #create contact dictionary 
    contact["name"] = name
    contact["phone_number"] = input("Enter the contact's phone number: ")
    contact["email_address"] = input("Enter the contact's email address: ")
    contact["address"] = input("Enter the contact's address: ")

    #Adds to Contacts Dictionary
    contacts[name] = contact
    print("Contact Added Succesfully \n")  

def delete_contact(contacts, name):

    if name in contacts:
        del contacts[name]
    else:
      print("Contact not found.")
    
    print("Contact Deleted Succesfully \n")

def update_contact(contacts, name):
 
    if name in contacts:
        contact = contacts[name]

        print("What information do you want to update?")
        print("1. Phone number")
        print("2. Email address")
        print("3. Address")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            contact["phone_number"] = input("Enter the new phone number: ")
        elif choice == 2:
            contact["email_address"] = input("Enter the new email address: ")
        elif choice == 3:
            contact["address"] = input("Enter the new address: ")
        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")

    print("Contact Updated Succesfully \n")


def display_contacts(contacts,query):

    print("Contact's Details: \n")
    
    for name,contact in contacts.items():
        if name == query or contact['phone_number'] == query:
            print(f"{name}:")
            print(f"\tPhone number: {contact['phone_number']}")
            print(f"\tEmail address: {contact['email_address']}")
            print(f"\tAddress: {contact['address']}")
            break
        else: 
            print("Wrong Input")

    #For Printing Whole List
    # print("Contact list:")
    # for name, contact in contacts.items():
    #     print(f"{name}:")
    #     print(f"\tPhone number: {contact['phone_number']}")
    #     print(f"\tEmail address: {contact['email_address']}")
    #     print(f"\tAddress: {contact['address']}")

def main():
  """The main function of the program."""

#Creats an empty dictionary
contacts = {}

while True:
        print("\n\n What do you want to do?")
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Update contact")
        print("4. Display contact list")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name of the new contact: ")
            add_contact(contacts, name)
        elif choice == 2:
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)
        elif choice == 3:
            name = input("Enter the name of the contact to update: ")
            update_contact(contacts, name)
        elif choice == 4:
            query = input("Enter Name or phone Number to search: ")
            display_contacts(contacts,query)
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
  main()

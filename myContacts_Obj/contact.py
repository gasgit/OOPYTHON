#!/usr/bin/python
"""
     script declaring classes
"""

class ContactList(list):
    """
        create contact list
    """
    def search(self, name):
        """
            search method and list of found contacts by name
        """
        found_contacts = []
        for contact in self:
            if name in contact.name:
                found_contacts.append(contact)
        return found_contacts



class Contact(object):
    """
        create new contact class, name, email, telephone number, list contacts for storage
    """
    my_contacts = ContactList()

    def __init__(self, name, email, tel):
        self.name = name
        self.email = email
        self.tel = tel

        Contact.my_contacts.append(self)

    def __str__(self):
        return  self.name + " "  + self.email + " " +  str(self.tel)


class Personal(Contact):
    """
        create new class Personal, inherit from Contact, add new method private_message
    """
    def __init__(self, name, email, tel, address):
        super(Personal, self).__init__(name, email, tel)
        self.address = address

    def message(self, private_message):
        """
            print message and contact name
        """
        print "This is a private '{}' from '{}' ".format(private_message, self.name)

    def __str__(self):
        return super(Personal, self).__str__() + ", " + self.address

class Professional(Contact):
    """
        create new class Personal, inherit from Contact, add new method professional_message
    """
    def __init__(self, name, email, tel, fax):
        super(Professional, self).__init__(name, email, tel)
        self.fax = fax


    def message(self, professional_message):
        """
            print message and contact name
        """
        print "This is a professional '{}' from '{}' ".format(professional_message, self.name)

    def __str__(self):
        return super(Professional, self).__str__() + ", " + str(self.fax)

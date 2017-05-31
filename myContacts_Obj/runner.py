#!/usr/bin/python


from contact import Contact, Personal, Professional


def main():
    """
        create contacts, carry out various operations
    """

    _a = Contact("glen", "glen@mail.ie", 0102030405)
    _b = Contact("gordon", "gordon@mail.ie", 9008070605)
    _c = Personal("jane", "jane@mail.com", 12345, "21 The Bells")
    _d = Professional("doe", "doe@mail.de", 555555, 7777)
    _e = Contact("doedy", "dn@mail.ie", 6767676)

    print _a.name, _b.name, _c.name, _d.name

    _c.message("hi")
    _d.message("hello")

    print _c
    print _d


    for i in Contact.my_contacts:
        print i


    #list_results = [[c.name, c.email, c.tel] for c in Contact.my_contacts.search('doe')]
    list_results = [c.__str__() for c in Contact.my_contacts.search('doe')]

    """
        print details for contacts found, searched by name
    """
    print list_results




if __name__ == '__main__':
    main()

from model.contact import Contact

def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Jan", middlename="Adam", lastname="Kowalski", nickname="", title="", company="",
                                address="", home="", mobile="", email="",bday="", bmonth="", byear=""))


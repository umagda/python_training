from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test", lastname="test"))
    app.contact.modify_first_contact(Contact(firstname="Jan", middlename="Adam", lastname="Kowalski", nickname="", title="", company="",
                                address="", home="", mobile="", email="",bday="", bmonth="", byear=""))


from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test", lastname="test"))
    app.contact.delete_first_contact()

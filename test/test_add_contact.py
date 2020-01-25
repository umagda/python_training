# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(name="Anna", middlename="Maria", lastname="Kowalska", nickname="Ania K.", title="Ms.", company="IBM",
                                address="ul. Ogrodowa 3\n41-549 Warszawa", home="123-456-789", mobile="788-000-987", email="anna.kowalska@gmail.com",
                                bday="13", bmonth="September", byear="1983"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(wusername="admin", password="secret")
    app.contact.add_new(Contact(name="", middlename="", lastname="", nickname="", title="", company="",
                                address="", home="", mobile="", email="",
                                bday="", bmonth="", byear=""))
    app.session.logout()
    

# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


def test_add_new_contact(app):
    app.contact.add_new(Contact(firstname="Anna", middlename="Maria", lastname="Kowalska", nickname="Ania K.", title="Ms.", company="IBM",
                                address="ul. Ogrodowa 3\n41-549 Warszawa", home="123-456-789", mobile="788-000-987", email="anna.kowalska@gmail.com",
                                bday="13", bmonth="September", byear="1983"))

def test_add_empty_contact(app):
    app.contact.add_new(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                address="", home="", mobile="", email="",
                                bday="", bmonth="", byear=""))


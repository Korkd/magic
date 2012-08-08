# -*- coding: UTF-8 -*-
import cgi
from card import Card
from mako.template import Template
from mako import exceptions
import pymongo

print "Content-Type: text/html;charset=utf-8"
print

form = cgi.FieldStorage()

connection = pymongo.Connection('localhost', 27017)
db = connection.magic
cards = db.cards

qs = form.getvalue("card")

if "--" in qs:
    c = cards.find_one({"_id": qs.split("--")[0]})
    ca = Card(c)
    ca.assignPair(Card(cards.find_one({"_id": qs.split("--")[1]})))
else:
    c = cards.find_one({"_id": qs})
    ca = Card(c)

try:
    template = Template(filename='templates\card.html')
    print template.render_unicode(card=ca).encode('utf-8', 'replace')
except:
    print exceptions.text_error_template().render()
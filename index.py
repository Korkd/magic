# -*- coding: UTF-8 -*-
import sys
sys.path.append('./modules')
from card import Card
from mako.template import Template
from mako import exceptions
import pymongo

# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: text/html;charset=utf-8"
print

connection = pymongo.Connection('localhost', 27017)
db = connection.magic
cards = db.cards

name = "Tok-Tok, Volcano Born"

allCards = cards.find()

cardList = []
foundCards = []

for c in allCards:
    if c["_id"] not in foundCards:
        card = Card(c)
        if c["pair"] is not None:
            otherCard = cards.find_one({"_id": c["pair"]})
            card.assignPair(Card(otherCard))
            foundCards.append(otherCard["_id"])

        cardList.append(card)


try:
    template = Template(filename='modules\\templates\main.html')
    print template.render_unicode(cards=cardList).encode('utf-8', 'replace')
except:
    print exceptions.text_error_template().render()
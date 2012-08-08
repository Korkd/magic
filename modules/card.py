# -*- coding: UTF-8 -*-
class Card:
    def __init__(self, card):
        self.name = card['_id']
        self.mana = self.Mana(card['mana'])
        self.color = card['color']
        self.cmc = card['cmc']
        self.set = card['set'][0]['name']
        self.type = card['type']
        self.subtype = card['subtype']
        self.abilities = self.Abilities(card['abilities'])
        self.power = card['power']
        self.toughness = card['toughness']
        self.artist = card['set'][0]['artist']
        self.flavor = card['set'][0]['flavor']
        self.loyalty = card['loyalty']
        self.rarity = card['set'][0]['rarity']
        self.legality = None
        self.tags = None
        self.back = None
        self.pair = None
        self.test = None
    
    def Abilities(self, card):
        ability = []
        if card is not None:
            for ab in card:
                for a in ab.encode('utf-8', 'replace').split('£'):
                    temp = a.replace('#_#_', '<i>')
                    temp = temp.replace('_#_#', '</i>')
                    temp = temp.replace('#_', '<i>')
                    temp = temp.replace('_#', '</i>')
                    ability.append(temp.decode('utf-8', 'ignore'))
        else:
            ability.append("")

        return ability

    def Mana(self, card):
        manaNum = {"W": 0, "U": 1, "B": 2, "R": 3, "G": 4}
        mana = []
        if card is not None:
            if card.has_key("X"):
                mana.append("X")
                del card["X"]
            elif card.has_key("CL"):
                mana.append(card["CL"])
                del card["CL"]
            else:
                phyrexian = []
                hybrid = []
                basic = []
                for k in card.keys():
                    if len(k) == 2:
                        if k[0] == "P":
                            phyrexian.append(manaNum[k[1]])
                        else:
                            hybrid.append(manaNum[k[0]])
                    else:
                        nums.append(manaNum[k])




        return mana

    def position(self, source, num):
        offset = source - 2

        if num - offset < 0:
            n += 5;

        return n % 5

    def assignPair(self, card):
        self.pair = card
        card.pair = self
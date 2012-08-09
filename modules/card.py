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

    def Mana(self, cardMana):
        manaNum = {"W": 0, "U": 1, "B": 2, "R": 3, "G": 4}
        manaOrder = "WUBRG"
        mana = []
        if cardMana is not None:
            if cardMana.has_key("X"):
                for x in range(cardMana["X"]):
                    mana.append("X")
                del cardMana["X"]

            if cardMana.has_key("CL"):
                mana.append(cardMana["CL"])
                del cardMana["CL"]

            types = {"phyrexian": [],
                      "hybrid": [],
                      "hybridpair": [],
                      "basic": []
                      }

            for k in cardMana.keys():
                if len(k) == 2:
                    if k[0] == "P":
                        types["phyrexian"].append(manaNum[k[1]])
                    else:
                        if not k[0].isdigit():
                            types["hybrid"].append(manaNum[k[0]])
                            types["hybridpair"].append(k[1])
                        else:
                            for x in range(cardMana[k]):
                                mana.append(k)
                else:
                    types["basic"].append(manaNum[k])

            for k,color in types.iteritems():
                if k != "hybridpair":
                    if len(color) == 5: # 5 color match
                        types[k] = ["W","U","B","R","G"]
                    elif len(color) == 4: # 4 color match
                        total = 0
                        for m in color:
                            total += m
                        total = 10 - total

                        types[k] = []
                        for x in range(4):
                            total += 1
                            types[k].append(manaOrder[total % 5])

                    elif len(color) == 3: # 3 color match
                        pair = [0, 1, 2, 3, 4]
                        for c in color:
                            pair.remove(c)

                        enemyColor = None
                        allyColor = None
                        if (pair[0] + 2) % 5 == pair[1]:
                            enemyColor = (pair[0]) + 1 % 5
                        elif (pair[1] + 2) % 5 == pair[0]:
                            enemyColor = (pair[1] + 1) % 5
                        elif (pair[0] + 1) % 5 == pair[1]:
                            allyColor = (pair[1] + 1) % 5
                        else:
                            allyColor = (pair[0] + 1) % 5

                        types[k] = []
                        if enemyColor is not None:
                            types[k].append(manaOrder[enemyColor])
                            types[k].append(manaOrder[(enemyColor + 2) % 5])
                            types[k].append(manaOrder[(enemyColor + 3) % 5])
                        elif allyColor is not None:
                            types[k].append(manaOrder[allyColor])
                            types[k].append(manaOrder[(allyColor + 1) % 5])
                            types[k].append(manaOrder[(allyColor + 2) % 5])

                    elif len(color) == 2: # 2 color match
                        types[k] = []
                        if (color[0] + 1) % 5 == color[1] or (color[0] + 2) % 5 == color[1]:
                            types[k].append(manaOrder[color[0]])
                            types[k].append(manaOrder[color[1]])
                        else:
                            types[k].append(manaOrder[color[1]])
                            types[k].append(manaOrder[color[0]])

                    elif len(color) == 1: # 1 color match
                        types[k] = manaOrder[color[0]]

            ii = 0
            for m in types["hybrid"]:
                for x in range(cardMana[m+types["hybridpair"][ii]]):
                    mana.append(m+types["hybridpair"][ii])
                ii += 1

            for m in types["phyrexian"]:
                for x in range(cardMana["P"+m]):
                    mana.append("P"+m)

            for m in types["basic"]:
                for x in range(cardMana[m]):
                    mana.append(m)

        return mana

    def assignPair(self, card):
        self.pair = card
        card.pair = self
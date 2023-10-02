# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class UpdateStrategy:
    def normal(item: Item):
        item.sell_in -= 1
        if (item.sell_in >= 0):
            item.quality = max(0, item.quality-1)
        else:
            item.quality = max(0, item.quality-2)

    def AgedBrie(item: Item):
        item.sell_in -= 1
        if (item.sell_in >= 0):
            item.quality = min(50, item.quality+1)
        else:
            item.quality = min(50, item.quality+2)

    def Sulfuras(item: Item):
        pass

    def BackstagePasses(item: Item):
        item.sell_in -= 1
        if (item.sell_in >= 10):
            item.quality = min(50, item.quality+1)
        elif (item.sell_in >= 5):
            item.quality = min(50, item.quality+2)
        elif (item.sell_in >= 0):
            item.quality = min(50, item.quality+3)
        else:
            item.quality = 0

    def Conjured(item: Item):
        item.sell_in -= 1
        if (item.sell_in >= 0):
            item.quality = max(0, item.quality-1)
        else:
            item.quality = max(0, item.quality-2)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:

            if (item.name == "Aged Brie"):
                UpdateStrategy.AgedBrie(item)
            elif (item.name == "Sulfuras, Hand of Ragnaros"):
                UpdateStrategy.Sulfuras(item)
            elif (item.name == "Backstage passes to a TAFKAL80ETC concert"):
                UpdateStrategy.BackstagePasses(item)
            elif (item.name == "Conjured Mana Cake"):
                UpdateStrategy.Conjured(item)
            else:
                UpdateStrategy.normal(item)

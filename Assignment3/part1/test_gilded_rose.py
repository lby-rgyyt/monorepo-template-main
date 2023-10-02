# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert",
                 sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert",
                 sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert",
                 sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEquals(19, items[0].quality)
        self.assertEquals(1, items[1].quality)
        self.assertEquals(6, items[2].quality)
        self.assertEquals(80, items[3].quality)
        self.assertEquals(80, items[4].quality)
        self.assertEquals(21, items[5].quality)
        self.assertEquals(50, items[6].quality)
        self.assertEquals(50, items[7].quality)
        self.assertEquals(5, items[8].quality)

        gilded_rose.update_quality()
        self.assertEquals(18, items[0].quality)
        self.assertEquals(2, items[1].quality)
        self.assertEquals(5, items[2].quality)
        self.assertEquals(80, items[3].quality)
        self.assertEquals(80, items[4].quality)
        self.assertEquals(22, items[5].quality)
        self.assertEquals(50, items[6].quality)
        self.assertEquals(50, items[7].quality)
        self.assertEquals(4, items[8].quality)

        gilded_rose.update_quality()
        self.assertEquals(17, items[0].quality)
        self.assertEquals(4, items[1].quality)
        self.assertEquals(4, items[2].quality)
        self.assertEquals(80, items[3].quality)
        self.assertEquals(80, items[4].quality)
        self.assertEquals(23, items[5].quality)
        self.assertEquals(50, items[6].quality)
        self.assertEquals(50, items[7].quality)
        self.assertEquals(3, items[8].quality)

        gilded_rose.update_quality()
        self.assertEquals(16, items[0].quality)
        self.assertEquals(6, items[1].quality)
        self.assertEquals(3, items[2].quality)
        self.assertEquals(80, items[3].quality)
        self.assertEquals(80, items[4].quality)
        self.assertEquals(24, items[5].quality)
        self.assertEquals(50, items[6].quality)
        self.assertEquals(50, items[7].quality)
        self.assertEquals(1, items[8].quality)


if __name__ == '__main__':
    unittest.main()

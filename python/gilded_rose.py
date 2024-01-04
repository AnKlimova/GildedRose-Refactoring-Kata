# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _reduce_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def _increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def _update_aged_brie(self, item):
        self._increase_quality(item)
        if item.sell_in < 0:
            self._increase_quality(item)

    def _update_backstage_passes(self, item):
        self._increase_quality(item)
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)
        if item.sell_in <= 0:
            item.quality = 0

    def _update_simple_item(self, item):
        self._reduce_quality(item)
        if item.sell_in <= 0:
            self._reduce_quality(item)

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_passes(item)
            elif item.name == "Aged Brie":
                self._update_aged_brie(item)
            else:
                self._update_simple_item(item)
            item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags, replace_escape_chars

main_url = 'https://www.jacadi.fr'


class OuisncfItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


def mainTitle_clear(values):
    valuer = replace_escape_chars(values, which_ones=('\t', '\r', '\n'), replace_by=u' ')
    return valuer

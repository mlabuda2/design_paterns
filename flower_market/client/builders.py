from flower_market.price_list.german_price_builder import GermanPriceBuilder
from flower_market.price_list.polish_price_builder import PolishPriceBuilder

builder_dispatcher = {
    'PL': PolishPriceBuilder,
    'GR': GermanPriceBuilder
}
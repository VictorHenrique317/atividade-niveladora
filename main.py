# -*- coding: utf-8 -*-
from stock import Stock
from product import Product
from cart import Cart
from chatbot import Chatbot

test_carrot = Product("carrot", 1.80)

test_stock = Stock()
# test_stock.load() # carrega do arquivo
test_stock.add(test_carrot, 4)

test_cart = Cart(test_stock)

test_chatbot = Chatbot(test_stock)
test_chatbot.run()
# test_stock.persist() # salva no arquivo


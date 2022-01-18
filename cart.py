# -*- coding: utf-8 -*-
from stock import Stock
from product import Product
class Cart:
    def __init__(self, stock:Stock):
        self.__products = dict() # {"name": quantity}
        self.__stock = stock
    
    def add(self, product_name:str, quantity:int) -> bool:
        cart_quantity = self.__products.get(product_name, 0)
        cart_quantity += quantity
        
        if self.__stock.isAvailable(product_name, cart_quantity) is False: 
            # n disponivel no estoque
            return False
        
        self.__products[product_name] = cart_quantity
        return True
    
    def remove(self, product_name:str, quantity:int)-> bool:
        cart_quantity = self.__products.get(product_name, None)
        if cart_quantity is None:
            print(f"Não tem {product_name} no carrinho")
            return False
        cart_quantity -= quantity
        
        if cart_quantity < 0 : # removendo mais doq tem
            print(f"Impossível remover {quantity}, porque existem apenas {cart_quantity+quantity} disponíveis")
            return False
        elif cart_quantity == 0: # removeu todos os produtos
            del self.__products[product_name]
            return True
        elif cart_quantity > 0: # remoção menor que numero existente
            self.__products[product_name] = cart_quantity
            return True
        return False
    
    def getProducts(self):
        return self.__products
    
    def __calculateTotal(self):
        total = 0
        for product_name, quantity in self.__products.items():
            total += self.__stock.getPriceFor(product_name) *  quantity
        return float(f"{total:.2f}")
    
    def closeCart(self):
        for product_name, quantity in self.__products.items():
            self.__stock.remove(product_name, quantity)
        total_value = self.__calculateTotal()
        self.resetCart()
        return total_value
    
    def resetCart(self):
        self.__products = dict()
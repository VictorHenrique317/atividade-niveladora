# -*- coding: utf-8 -*-.
from product import Product
import json
class Stock:
    def __init__(self):
        self.__products:dict = dict() # {"name": [Product, quantity]}
    
    def add(self, product:Product, quantity:int) -> None:
        product_name = product.getName()
        product_quantity = self.__products.setdefault(product_name, \
                                                   [product, 0])
            
        product_quantity[1] += quantity
        self.__products[product_name] = product_quantity
            
    def addMultiple(self, products:list) -> None:
        for product, quantity in products:
            self.add(product, quantity)
            
    def remove(self, product_name:str, quantity:int)-> bool:
        if product_name not in self.__products: # produto n existe no estoque
            print(f"{product_name} não existe no estoque")
            return False
        
        product_quantity = self.__products[product_name] # [Product, quantity]
        final_quantity = product_quantity[1] - quantity
        
        if final_quantity < 0 : # removendo mais doq tem
            print(f"Impossível remover {quantity} {product_name}, porque existem apenas {product_quantity[1]} disponíveis")
            return False
        elif final_quantity == 0: # removeu todos os produtos
            del self.__products[product_name]
            return True
        elif final_quantity > 0: # remoção menor que numero existente
            self.__products[product_name] = [product_quantity[0], \
                                             final_quantity]
            return True
        return False
            
    def removeMultiple(self, products:list) -> bool:
        remove_results = []
        for product_name, quantity in products:
            result = self.remove(product_name, quantity)
            remove_results.append(result)
        return all(remove_results)
    
    
    def getProducts(self) -> dict : # usado apenas nos testes
        return self.__products
    
    def isAvailable(self, product_name, asked_quantity) -> bool:
        if product_name not in self.__products: # produto n existe no estoque
            print(f"Não temos {product_name}")
            return False
    
        product, available_quantity = self.__products[product_name]
        if asked_quantity > available_quantity:
            print(f"Temos apenas {available_quantity} disponíveis")
            return False
    
        return True
    
    def hasProduct(self, product_name:str) -> bool:
        return product_name in self.__products 
    
    def __parse(self)-> str:
        parsed_products = dict() # {quantity: ["name", price], ...}
        for product, quantity in self.__products.values():
            parsed_products[quantity] = product.parse()
        return json.dumps(parsed_products)
        
    def persist(self) -> None:
        with open("stock.json", "w") as file:
            file.write(self.__parse())
            
    def load(self) -> None:
        with open("stock.json", "r") as file:
            parsed_stock = json.load(file)
            for quantity, parsed_product in parsed_stock.items():
                quantity = int(quantity)
                product = Product.deparse(parsed_product)
                self.__products[product.getName()] = [product, quantity]
            
    def getPriceFor(self, product_name:str):
        if product_name in self.__products:
            return self.__products[product_name][0].getPrice()
            
    
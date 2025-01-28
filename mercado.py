import agentpy as ap
from utils import PRODUCTOS

class Mercado(ap.Agent):

    def setup(self):
        self.money = 100
        self.ventas = 0
        self.precios = {p: 1 for p in PRODUCTOS}
        self.items = {p: 10 for p in PRODUCTOS}
        self.threshold = 5

    def vender(self, item, cantidad):
        self.items[item] -= cantidad
        self.money += self.precios[item] * cantidad
        self.ventas += 1
        return self.precios[item] * cantidad

    def get_precio(self, item):
        return self.precios[item]
    
    def item_disp(self, item, cantidad):
        return self.items[item] >= cantidad
    
    def update_precios(self):
        for k,v in self.items.items():
            if v < 5:
                self.precios[k] += 1
            elif v > 15:
                self.precios[k] -= 1

    def buy_items(self):
        for item, cantidad in self.items.items():
            if cantidad < self.threshold:
                # imitate the provider agent
                self.items[item] += 10

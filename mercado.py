import agentpy as ap
from utils import PRODUCTOS

class Mercado(ap.Agent):

    def setup(self):
        self.money = 100
        self.ventas = 0
        self.precios = {p: 1 for p in PRODUCTOS}
        self.items = {p: 10 for p in PRODUCTOS}
        self.items_copy = self.items.copy()
        self.threshold = 5
        self.inflacion = 1.1
        self.deflacion = 0.9

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
        demanda = {k: self.items_copy[k] - self.items[k] for k in self.items.keys()}
        for k,v in demanda.items():
            if v > self.items[k]*0.8:
                self.precios[k] *= self.inflacion
            elif v < self.items[k]*0.2:
                self.precios[k] *= self.deflacion
        
        self.items_copy = self.items.copy()

    def buy_items(self):
        for item, cantidad in self.items.items():
            if cantidad < self.threshold:
                # imitate the provider agent
                self.items[item] += 10

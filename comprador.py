import agentpy as ap
from utils import PRODUCTOS
from mercado import Mercado


class Comprador(ap.Agent):

    def setup(self):
        self.money = 10
        self.items = {p: 0 for p in PRODUCTOS}
        self.mercados_disponibles = []
        self.threshold = self.p.c_threshold
        self.comer = self.p.c_comer
        self.satisfaction = 0

    def comprar(self):
        cantidad = 1
        for ing in self.decidir_comprar():
            for mercado in self.mercados_disponibles:
                if mercado.item_disp(ing, cantidad):
                    precio = mercado.get_precio(ing)
                    if precio*cantidad <= self.money:
                        precio = mercado.vender(ing, cantidad)
                        self.items[ing] += cantidad
                        self.money -= precio
                        break

    def seleccionar_mercados(self, distancia):
        self.mercados_disponibles = [
        vecino for vecino in self.model.espacio.neighbors(self, distance=distancia)
        if isinstance(vecino, Mercado) 
        ]

    def decidir_comprar(self):
        comprar = []
        for k,v in self.items.items():
            if v <= self.threshold:
                comprar.append(k)
        
        return comprar
    
    def generar_dinero(self):
        self.money += 2
        return self.money
    
    def consume(self):
        for k,v in self.items.items():
            if v > 0:
                self.items[k] -= self.comer
                self.satisfaction += 1
            else:
                self.satisfaction -= 1

    def get_0_items(self):
        return sum([v for v in self.items.values()]) == 0
                    

    
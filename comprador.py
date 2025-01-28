import agentpy as ap
from utils import PRODUCTOS


class Comprador(ap.Agent):

    def setup(self):
        self.money = 10
        self.items = {p: 0 for p in PRODUCTOS}
        self.mercados_disponibles = []
        self.threshold = 1

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

    def seleccionar_mercados(self, mercados):
        self.mercados_disponibles = self.model.random.sample(mercados, 2)

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
                self.items[k] -= 1
                break

    def get_0_items(self):
        return sum([v for v in self.items.values()]) == 0
                    

    
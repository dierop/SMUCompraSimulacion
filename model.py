import agentpy as ap
from comprador import Comprador
from mercado import Mercado
from utils import PRODUCTOS, gini, get_0_agents
class SimulacionModel(ap.Model):

    def setup(self):
        self.random.seed(42)
        self.compradores = ap.AgentList(self, self.p.compradores, Comprador)
        self.mercados = ap.AgentList(self, self.p.mercados, Mercado)
        for comprador in self.compradores:
            comprador.seleccionar_mercados(self.mercados)

    def step(self):
        self.compradores.shuffle()
        for comprador in self.compradores:
            comprador.consume()
            comprador.comprar()
            comprador.generar_dinero()

        for mercado in self.mercados:
            mercado.update_precios()
            mercado.buy_items()


    def update(self):
        self.record('comprador_no_compra', get_0_agents(self.compradores))
        self.record('mercado_gini', gini(self.mercados.money))
    
    def end(self):
        self.record('mercado_money', self.mercados.money)
        self.record('comprador_money', self.compradores.money)
        self.record('ventas', self.mercados.ventas)

        for p in PRODUCTOS:
            
            precios_producto = [mercado.precios[p] for mercado in self.mercados if p in mercado.precios]
            items_producto = [comprador.items[p] for comprador in self.compradores if p in comprador.items]

            # Guardar la lista de precios directamente
            self.record(f'price_{p}', precios_producto)
            self.record(f'items_{p}', items_producto)





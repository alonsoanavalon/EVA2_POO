class Precio():
    def __init__(self, idprecio, preciolista, ganancia):
        self.idprecio = idprecio
        self.preciolista = preciolista
        self.ganancia = (ganancia / 100) + 1
        self.precio = self.ganancia * self.preciolista

    """def mostrarPrecio(self):
        txt = "El precio es {:.0f}".format(self.precio)
        return txt
"""






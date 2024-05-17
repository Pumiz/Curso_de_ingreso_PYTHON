class Boligrafo:
    def __init__(self, grosor, color) -> None:
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor
        self.color = color
        self.cantidad_tinta = 80

    def escribir(self, texto: str) -> str:
        longitud_texto = len(texto)
        trazo_grueso = (len(texto) * 2)
        if longitud_texto <= self.cantidad_tinta and self.grosor_punta == "Fino":
            self.cantidad_tinta - longitud_texto
            cadena = f"Su texto en color {self.color} es: {texto}"

        elif trazo_grueso <= self.cantidad_tinta:
            self.cantidad_tinta - trazo_grueso
            cadena = f"Su texto en color {self.color} es: {texto}"

        else:
            cadena = "No alcanza la tinta"

        return cadena
    
    def recargar(self, cantidad: int) -> str:
        self.cantidad_tinta += cantidad
        if self.cantidad_tinta > self.capacidad_tinta_maxima:
            sobro = self.cantidad_tinta - self.capacidad_tinta_maxima
            sobro = f"Se recargó la lapicera y sobró {sobro} cantidad de tinta"
            self.cantidad_tinta = 100
        else:
            sobro = "Lapicera recargada"

        return sobro



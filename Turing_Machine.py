import itertools

class Cinta:
    def __init__(self, entrada, blanco):
        self.celdas = [blanco for _ in range(50000)]
        self.posicion_actual = 0
        self.salida = ''
        self.celdas = [x for x, y in itertools.zip_longest(entrada, self.celdas, fillvalue='B')]

    def fin_de_cinta(self):
        return self.posicion_actual < 0 or self.posicion_actual >= len(self.celdas)

    def leer(self):
        if self.fin_de_cinta():
            return -1
        else:
            return self.celdas[self.posicion_actual]

    def escribir(self, simbolo):
        self.celdas[self.posicion_actual] = simbolo

    def mover(self, direccion):
        if self.fin_de_cinta():
            raise Exception('Fin de la máquina')
        if direccion == 'R':
            self.posicion_actual += 1
        elif direccion == 'L':
            self.posicion_actual -= 1

    def extraer_salida(self):
        valores = []
        pos = 0
        while pos < len(self.celdas):
            if self.celdas[pos] != 'B':
                valores.append(self.celdas[pos])
            pos += 1
        self.salida = "".join(valores)

    def obtener_resultado(self):
        return self.salida

    def __str__(self):
        return str(self.celdas)

class MaquinaTuring:
    def __init__(self, entrada, transiciones, estado_inicial, estado_final, blanco):
        self.transiciones = transiciones
        self.estado_final = estado_final
        self.estado_actual = estado_inicial
        self.blanco = blanco
        self.cinta = Cinta(entrada, self.blanco)

    def calcular_fibonacci(self, mostrar_proceso=False):
        while self.estado_actual != self.estado_final:
            simbolo = self.cinta.leer()
            if simbolo is None:
                return None 
            try:
                destino, nuevo_simbolo, direccion = self.transiciones[(self.estado_actual, simbolo)]
                self.estado_actual = destino
                self.cinta.escribir(nuevo_simbolo)
                self.cinta.mover(direccion)

                if mostrar_proceso:
                    self.mostrar_estado()

                if self.estado_actual == self.estado_final:
                    self.cinta.salida += simbolo
            except:
                print(f"Error en transición: ({self.estado_actual}, {simbolo})")
                
        self.cinta.extraer_salida()
        return self.cinta.obtener_resultado()

    def mostrar_estado(self):
        estado_str = f"🌐 Estado: {self.estado_actual} | 📍 Posición: {self.cinta.posicion_actual}"
        cinta_str = f"📜 Cinta: " + "".join(self.cinta.celdas[:self.cinta.posicion_actual]) + \
                    f"[{self.cinta.celdas[self.cinta.posicion_actual]}]" + \
                    "".join(self.cinta.celdas[self.cinta.posicion_actual+1:self.cinta.posicion_actual+10])
        print(estado_str)
        print(cinta_str)
        print("-" * 50)

def generar_cinta(num):
    return '1' * num

def construir_maquina(entrada):
    transiciones = {}
    estado_inicial = None
    estado_final = None

    with open('config/turing_rules.txt', 'r') as file:
        for line in file:
            if line.strip() == "":
                continue
            line = line.strip().split(':')
            tupla = eval(line[0])
            tupla2 = eval(line[1])
            transiciones[(tupla[0], tupla[1])] = (tupla2[0][0], tupla2[0][1], tupla2[0][2])

    with open('config/turing_setup.txt', 'r') as file:
        lista = [line.strip() for line in file]
        blanco = lista[2].strip("'")
        estado_inicial = lista[4].strip("'")
        estado_final = lista[5].strip("'")

    return MaquinaTuring(entrada, transiciones, estado_inicial, estado_final, blanco)

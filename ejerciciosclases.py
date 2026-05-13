class Vehiculo:
    def __init__(self, marca, modelo):
        # Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0        # Inicia en 0 (entero)
        self.encendido = False    # Inicia en False (booleano)

    def encender(self):
        # Si NO está encendido, lo encendemos
        if not self.encendido:
            self.encendido = True
            print("El vehículo se ha encendido.")
        else:
            # Si ya está encendido, avisamos
            print("El vehículo ya está en marcha.")

    def acelerar(self, km):
        # Solo podemos acelerar si el vehículo está encendido
        if self.encendido:
            self.velocidad += km
            print(f"Acelerando... Velocidad actual: {self.velocidad} km/h")
        else:
            print("No se puede acelerar: el vehículo está apagado.")

    def frenar(self, km):
        # Usamos max() para asegurar que la velocidad nunca baje de 0
        # Resta km a la velocidad, pero si el resultado es negativo, queda en 0.
        self.velocidad = max(0, self.velocidad - km)
        print(f"Frenando... Velocidad actual: {self.velocidad} km/h")

    def apagar(self):
        # Solo se apaga si la velocidad es 0
        if self.velocidad == 0:
            self.encendido = False
            print("El vehículo se ha apagado.")
        else:
            print("¡Cuidado! Debe frenar antes de apagar el vehículo.")

    def estado(self):
        # Imprime un resumen del estado actual
        print(f"--- Estado del Vehículo ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad: {self.velocidad} km/h")
        print(f"Encendido: {self.encendido}")
        print(f"---------------------------")

# --- BLOQUE DE PRUEBAS 

if __name__ == "__main__":
    # 1. INSTANCIAR: Creamos un objeto (un coche real) basado en el plano
    print("Creando el vehículo...")
    mi_carro = Vehiculo("Toyota", "Corolla")

    # 2. PROBAR EL ESTADO INICIAL
    mi_carro.estado()

    print("\n--- Intentando acelerar sin encender ---")
    # 3. INTENTO FALLIDO: Tratar de acelerar sin encender (Debe dar error)
    mi_carro.acelerar(50)

    print("\n--- Encendiendo el coche ---")
    # 4. ENCENDER: Cambia el estado a True
    mi_carro.encender()

    print("\n--- Acelerando ---")
    # 5. ACELERAR: Ahora suma velocidad
    mi_carro.acelerar(50)
    mi_carro.acelerar(20) # Velocidad debería ser 70

    print("\n--- Frenando ---")
    # 6. FRENAR: Resta velocidad
    mi_carro.frenar(10) # Velocidad debería ser 60

    print("\n--- Intentando apagar en marcha ---")
    # 7. INTENTO FALLIDO: Apagar con velocidad > 0 (Debe dar error)
    mi_carro.apagar()

    print("\n--- Deteniendo el coche por completo ---")
    # 8. FRENAR HASTA 0: Frenamos más de la velocidad actual para probar el max(0, ...)
    mi_carro.frenar(100) 

    print("\n--- Apagando el coche ---")
    # 9. APAGAR: Ahora la velocidad es 0, así que se debe apagar
    mi_carro.apagar()

    print("\n--- Estado Final ---")
    # 10. VER ESTADO FINAL
    mi_carro.estado()
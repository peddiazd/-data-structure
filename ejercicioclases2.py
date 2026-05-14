class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        # El saldo inicia en 0.0 por defecto
        self.saldo = 0.0

    def depositar(self, monto):
        # Validación: El monto debe ser positivo
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso: ${monto:,.2f}")
        else:
            print("Error: El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        # Validación 1: El monto debe ser positivo
        if monto > 0:
            # Validación 2: Debe haber saldo suficiente
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Retiro exitoso: ${monto:,.2f}")
            else:
                print("Error: Saldo insuficiente para realizar el retiro.")
        else:
            print("Error: El monto a retirar debe ser positivo.")

    def ver_saldo(self):
        # Usamos :,.2f para formato de moneda (separador de miles y 2 decimales)
        # Ejemplo de salida: Saldo: $500,000.00
        print(f"Titular: {self.titular} | Saldo: ${self.saldo:,.2f}")
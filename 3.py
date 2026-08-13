class Conta:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite = 500.00  # Limite de crédito negativo

    def adicionar_saldo(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido para depósito.")

    def transferir(self, valor, conta_destino):
        print(f"ANTES DA TENTATIVA DE TRANSFERÊNCIA ---")
        print(f"Saldo de {self.titular}: R$ {self.saldo:.2f}")
        print(f"Saldo de {conta_destino.titular}: R$ {conta_destino.saldo:.2f}")
        
    
        if valor <= 0:
            print("Erro: O valor da transferência deve ser positivo.")
        elif (self.saldo - valor) < -self.limite:
            print(f"Transferência de R$ {valor:.2f} bloqueada!")
            print(f"Motivo: Limite negativo de R$ {self.limite:.2f} seria excedido.")
        else:
    
            self.saldo -= valor
            conta_destino.adicionar_saldo(valor)
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso!")

        print(f" DEPOIS DA TENTATIVA DE TRANSFERÊNCIA ---")
        print(f"Saldo de {self.titular}: R$ {self.saldo:.2f}")
        print(f"Saldo de {conta_destino.titular}: R$ {conta_destino.saldo:.2f}")
        print("-" * 43)




conta_joao = Conta("João", 100.00)
conta_maria = Conta("Maria", 50.00)

conta_joao.transferir(400.00, conta_maria)

conta_joao.transferir(300.00, conta_maria)
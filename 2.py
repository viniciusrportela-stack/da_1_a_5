class Carro:

    def __init__(
        self, modelo: str, combustivel: int = 0, quilometragem: int = 0
    ):
        self.modelo = modelo
        self.combustivel = combustivel
        self.quilometragem = quilometragem

    def abastecer(self, quantidade: int):
        if quantidade <= 0:
            print("A quantidade a abastecer deve ser maior que zero.")
            return

        self.combustivel += quantidade

        if self.combustivel > 100:
            self.combustivel = 100
            print(f"Tanque cheio!, o nivel foi ajustado para 100 litros.")
        else:
            print(
                f"Abastecidos!, {quantidade} litros. Nivel atual: {self.combustivel} litros."
            )

    def acelerar(self):
        if self.combustivel > 0:
            self.combustivel -= 1
            self.quilometragem += 15
            print(f"vrum!, o {self.modelo} acelerou e andou 15 km.")
        else:
            print(
                f"Falha ao acelerar!, o {self.modelo} esta sem combustivel."
            )

    def painel(self):
        print("-" * 30)
        print(f"Painel: {self.modelo}")
        print(f"Nivel de combustivel: {self.combustivel}/ 100 L")
        print(f"Odômetro (Quilometragem): {self.quilometragem} KM.")
        print("-" * 30)


def main():
    meu_carro = Carro("Honda Civic")
    meu_carro.painel()
    meu_carro.acelerar()

    print("Indo ao posto")
    meu_carro.abastecer(40)
    meu_carro.painel()

    print("Pegando a estrada!")
    meu_carro.acelerar()
    meu_carro.acelerar()
    meu_carro.painel()

    print("Enchendo o tanque")
    meu_carro.abastecer(80)
    meu_carro.painel()


if __name__ == "__main__":
    main()
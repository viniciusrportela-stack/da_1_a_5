class Animal: 
    def __init__(self, nome: str, barulho: str, idade: int = 0):
        self.nome = nome 
        self.barulho = barulho 
        self.idade = idade 

    def fazer_barulho(self):
        print(f"O {self.nome} fez {self.barulho}")

    def aniversario(self): 
        self.idade += 1 
        print(f"O {self.nome} fez {self.idade} anos!!")

def main(): 
    pato = Animal("Pato-do-mato", "Quá! quá!")
    pombo = Animal("Pombo Jacobino", "PRUUU! PRUUU!")
    raposa = Animal("Raposa Fennec", "YAP YAP!!")

    pato.fazer_barulho()
    pombo.fazer_barulho()
    raposa.fazer_barulho()

    print("Comemoração de aniversário")

    pato.aniversario()
    pato.aniversario()

    pombo.aniversario()
    pombo.aniversario()

    raposa.aniversario()
    raposa.aniversario()

if __name__ == "__main__":
    main()
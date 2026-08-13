GABARITOS = [
    ['A', 'B', 'C', 'D', 'E'],  # Prova 1: Português
    ['A', 'A', 'B', 'C', 'D'],  # Prova 2: Matemática
    ['E', 'D', 'C', 'B', 'A']   # Prova 3: História
]


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        # Transformado de self.nota para um histórico em formato de lista
        self.historico_notas = []

    def fazer_prova(self, respostas, gabarito):
        """
        Compara as respostas do aluno com o gabarito fornecido,
        calcula a nota (0 a 10) e adiciona ao histórico de notas.
        """
        acertos = sum(1 for resp, resp_correta in zip(respostas, gabarito) if resp.upper() == resp_correta.upper())
        nota = (acertos / len(gabarito)) * 10
        nota = round(nota, 2)
        
        # Adiciona a nota ao histórico em vez de sobrescrever
        self.historico_notas.append(nota)
        print(f"Prova realizada por {self.nome}. Nota obtida: {nota}")

    def calcular_media(self):
        """
        Percorre o histórico de notas e retorna a média aritmética.
        """
        if not self.historico_notas:
            return 0.0
        return sum(self.historico_notas) / len(self.historico_notas)

    def ver_boletim(self):
        """
        Exibe o nome do aluno, todas as notas, a média final e a situação.
        """
        media = self.calcular_media()
        situacao = "Aprovado" if media >= 6.0 else "Reprovado"

        print("\n" + "=" * 35)
        print("          BOLETIM ESCOLAR          ")
        print("=" * 35)
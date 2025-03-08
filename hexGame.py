import numpy as np

class JogoHex:
    def __init__(self, tamanho=11):
        self.tamanho = tamanho
        self.tabuleiro = np.full((tamanho, tamanho), '.', dtype=str)
        self.jogador_atual = 'X'

    def exibir_tabuleiro(self):
        print("\n=====================================")
        print("X vence conectando esquerda e direita")
        print("O vence conectando topo e base")
        print("=====================================\n")
        print("   " + "   ".join(f"{i}" for i in range(self.tamanho)))
        for linha in range(self.tamanho):
            espacamento = " " * (2 * linha)
            linha_tabuleiro = "   ".join(self.tabuleiro[linha])
            print(f"{espacamento}{linha:2} {linha_tabuleiro}  {linha}")
        print()

    def movimento_valido(self, linha, coluna):
        return 0 <= linha < self.tamanho and 0 <= coluna < self.tamanho and self.tabuleiro[linha, coluna] == '.'

    def fazer_movimento(self, linha, coluna):
        if self.movimento_valido(linha, coluna):
            self.tabuleiro[linha, coluna] = self.jogador_atual
            if self.verificar_vitoria(self.jogador_atual):
                print("\n=====================================")
                print(f"🎉 Jogador {self.jogador_atual} venceu! 🎉")
                print("=====================================")
                self.exibir_tabuleiro()
                return True
            self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
            return True
        return False

    def verificar_vitoria(self, jogador):
        visitados = set()
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]

        def bfs(linha, coluna):
            if (linha, coluna) in visitados:
                return False
            if jogador == 'X' and coluna == self.tamanho - 1:
                return True
            if jogador == 'O' and linha == self.tamanho - 1:
                return True
            visitados.add((linha, coluna))
            for deslocamento_linha, deslocamento_coluna in direcoes:
                nova_linha, nova_coluna = linha + deslocamento_linha, coluna + deslocamento_coluna
                if 0 <= nova_linha < self.tamanho and 0 <= nova_coluna < self.tamanho and self.tabuleiro[nova_linha, nova_coluna] == jogador:
                    if bfs(nova_linha, nova_coluna):
                        return True
            return False

        posicoes_iniciais = [(i, 0) for i in range(self.tamanho) if self.tabuleiro[i, 0] == 'X'] if jogador == 'X' else [(0, i) for i in range(self.tamanho) if self.tabuleiro[0, i] == 'O']
        return any(bfs(linha, coluna) for linha, coluna in posicoes_iniciais)

    def calcular_utilidade(self, jogador):
        utilidade = 0
        for linha in range(self.tamanho):
            for coluna in range(self.tamanho):
                if self.tabuleiro[linha, coluna] == jogador:
                    utilidade += self.forca_conectada(linha, coluna, jogador)
        return utilidade

    def forca_conectada(self, linha, coluna, jogador):
        return sum(1 for deslocamento_linha, deslocamento_coluna in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)] if 0 <= linha + deslocamento_linha < self.tamanho and 0 <= coluna + deslocamento_coluna < self.tamanho and self.tabuleiro[linha + deslocamento_linha, coluna + deslocamento_coluna] == jogador) + 1

    def gerar_sucessores(self):
        sucessores = []
        for linha in range(self.tamanho):
            for coluna in range(self.tamanho):
                if self.tabuleiro[linha, coluna] == '.':
                    novo_tabuleiro = self.tabuleiro.copy()
                    novo_tabuleiro[linha, coluna] = self.jogador_atual
                    sucessores.append(novo_tabuleiro)
        return sucessores

    def jogar(self):
        self.exibir_tabuleiro()
        while True:
            print(f"Jogador {self.jogador_atual}, sua vez!")
            print(f"Avaliando o tabuleiro para o Jogador {self.jogador_atual}: {self.calcular_utilidade(self.jogador_atual)} pontos")

            # Gerar sucessores e calcular a utilidade antes de cada jogada 
            sucessores = self.gerar_sucessores()
            print(f"Total de sucessores possíveis: {len(sucessores)}")

            try:
                linha, coluna = map(int, input("Digite uma linha e uma coluna (ex: 3 4): ").split())
                if self.fazer_movimento(linha, coluna):
                    if self.verificar_vitoria(self.jogador_atual):
                        break
                    self.exibir_tabuleiro()
                else:
                    print("\n❌ Movimento inválido, tente novamente.\n")
            except ValueError:
                print("\n⚠️ Entrada inválida! Use números separados por espaço.\n")

if __name__ == "__main__":
    jogo = JogoHex()
    jogo.jogar()
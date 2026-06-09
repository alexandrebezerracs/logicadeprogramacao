def imprimir_tabuleiro(tabuleiro):
    print("\n")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    # Combinações possíveis para vencer (linhas, colunas e diagonais)
    condicoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    for condicao in condicoes_vitoria:
        if tabuleiro[condicao[0]] == tabuleiro[condicao[1]] == tabuleiro[condicao[2]] == jogador:
            return True
    return False

def jogar():
    # Cria o tabuleiro vazio (lista com 9 espaços)
    tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    jogador_atual = "X"
    jogadas = 0

    print("Bem-vindo ao Jogo da Velha em Python!")
    print("As posições do tabuleiro vão de 1 a 9 (da esquerda para a direita, de cima para baixo).")

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}.")
        
        # Recebe a escolha do jogador e ajusta para o índice da lista (0 a 8)
        try:
            escolha = int(input("Escolha uma posição (1-9): ")) - 1
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        # Verifica se a jogada é válida
        if escolha < 0 or escolha > 8:
            print("Posição inválida! Escolha um número entre 1 e 9.")
            continue
        elif tabuleiro[escolha] != " ":
            print("Esse espaço já está ocupado! Tente outro.")
            continue

        # Registra a jogada
        tabuleiro[escolha] = jogador_atual
        jogadas += 1

        # Verifica se o jogador atual venceu
        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"🎉 Parabéns! O jogador {jogador_atual} venceu!")
            break

        # Verifica se deu velha (empate)
        if jogadas == 9:
            imprimir_tabuleiro(tabuleiro)
            print("Deu Velha! O jogo empatou.")
            break

        # Alterna o jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Inicia o jogo
if __name__ == "__main__":
    jogar()

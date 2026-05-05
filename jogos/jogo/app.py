import pygame
import random
import sys
import os

# Inicialização
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 400
CHAO_Y = ALTURA - 30
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("T-Rex Runner - Visual Complexo")

# Cores e Fontes
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (150, 150, 150)
VERDE_CACTO = (20, 120, 20) # Um verde mais escuro e detalhado
fonte_pontuacao = pygame.font.SysFont("Arial", 24, bold=True)
fonte_gameover = pygame.font.SysFont("Arial", 40, bold=True)

# Nome do arquivo que guardará o recorde
ARQUIVO_RECORDE = "recorde.txt"

def carregar_recorde():
    if os.path.exists(ARQUIVO_RECORDE):
        with open(ARQUIVO_RECORDE, "r") as arquivo:
            try:
                return int(arquivo.read())
            except ValueError:
                return 0
    return 0

def salvar_recorde(recorde):
    with open(ARQUIVO_RECORDE, "w") as arquivo:
        arquivo.write(str(recorde))

class Dino:
    def __init__(self):
        # A hitbox total permanece 40x40 para consistência de jogo
        self.largura = 40
        self.altura = 40
        self.x = 50
        self.y = CHAO_Y - self.altura
        self.velocidade_y = 0
        self.pulo = False
        # Novo contador para a animação de corrida
        self.animacao_count = 0 
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def pular(self):
        if not self.pulo:
            self.velocidade_y = -14
            self.pulo = True

    def atualizar(self):
        self.velocidade_y += 0.8
        self.y += self.velocidade_y

        if self.y >= CHAO_Y - self.altura:
            self.y = CHAO_Y - self.altura
            self.velocidade_y = 0
            self.pulo = False
        
        # Animação de corrida (só conta se não estiver pulando)
        if not self.pulo:
            self.animacao_count += 1
            if self.animacao_count >= 10: # Reseta a cada 10 frames
                self.animacao_count = 0

        self.rect.topleft = (self.x, self.y)

    def desenhar(self, superficie):
        # --- DESENHO COMPLEXO DO DINO (Geométrico) ---
        x, y = self.x, self.y
        # Cor Principal (Preto)
        
        # Cabeça/Focinho (Parte de cima)
        pygame.draw.rect(superficie, PRETO, (x + 18, y, 20, 15)) 
        pygame.draw.rect(superficie, PRETO, (x + 23, y + 2, 13, 10)) # Detalhe do focinho

        # Olho (Ponto branco)
        pygame.draw.rect(superficie, BRANCO, (x + 23, y + 3, 3, 3)) 

        # Pescoço
        pygame.draw.rect(superficie, PRETO, (x + 10, y + 5, 10, 15)) 

        # Corpo/Tail
        pygame.draw.rect(superficie, PRETO, (x, y + 15, 25, 20)) 
        
        # Pernas (Animação Alternada)
        largura_perna = 6
        altura_perna = 10
        pos_perna_y = y + 32
        
        # Alterna qual perna está levantada baseado no contador de animação
        if self.pulo:
            # Em pulo, ambas as pernas ficam retas
            pygame.draw.rect(superficie, PRETO, (x + 5, pos_perna_y, largura_perna, altura_perna))
            pygame.draw.rect(superficie, PRETO, (x + 15, pos_perna_y, largura_perna, altura_perna))
        else:
            # Em corrida, pernas alternam
            if self.animacao_count < 5:
                # Frame 1: Perna 1 reta, Perna 2 levantada
                pygame.draw.rect(superficie, PRETO, (x + 5, pos_perna_y, largura_perna, altura_perna))
                pygame.draw.rect(superficie, PRETO, (x + 15, pos_perna_y - 2, largura_perna, altura_perna - 2))
            else:
                # Frame 2: Perna 1 levantada, Perna 2 reta
                pygame.draw.rect(superficie, PRETO, (x + 5, pos_perna_y - 2, largura_perna, altura_perna - 2))
                pygame.draw.rect(superficie, PRETO, (x + 15, pos_perna_y, largura_perna, altura_perna))

class Obstaculo:
    def __init__(self, x_inicial):
        self.tipo = random.choice(['simples', 'duplo', 'braços'])
        # Ajusta a largura da hitbox baseada no tipo de cacto
        if self.tipo == 'simples':
            self.largura = 20
        elif self.tipo == 'duplo':
            self.largura = 45
        elif self.tipo == 'braços':
            self.largura = 50
        
        # A altura é fixa para consistência
        self.altura = 50 
        self.x = x_inicial
        self.y = CHAO_Y - self.altura
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def mover(self, velocidade):
        self.x -= velocidade
        self.rect.x = self.x

    def desenhar(self, superficie):
        x, y = self.x, self.y
        largura_tronco = 18
        largura_braço = 8

        # --- DESENHO COMPLEXO DO CACTO (Geométrico) ---

        if self.tipo == 'simples':
            # Tronco Único e Arredondado
            # Desenha tronco reto
            pygame.draw.rect(superficie, VERDE_CACTO, (x + (self.largura // 2 - largura_tronco // 2), y + 5, largura_tronco, self.altura - 5))
            # Topo arredondado
            pygame.draw.circle(superficie, VERDE_CACTO, (x + self.largura // 2, y + 8), largura_tronco // 2)

        elif self.tipo == 'duplo':
            # Dois Cactos Simples lado a lado
            # Cacto 1 (Pequeno)
            y1 = y + 10
            alt1 = self.altura - 10
            pygame.draw.rect(superficie, VERDE_CACTO, (x, y1 + 5, largura_tronco - 2, alt1 - 5))
            pygame.draw.circle(superficie, VERDE_CACTO, (x + (largura_tronco - 2) // 2, y1 + 8), (largura_tronco - 2) // 2)
            # Cacto 2 (Grande, no centro da hitbox total)
            pygame.draw.rect(superficie, VERDE_CACTO, (x + 25, y + 5, largura_tronco, self.altura - 5))
            pygame.draw.circle(superficie, VERDE_CACTO, (x + 25 + largura_tronco // 2, y + 8), largura_tronco // 2)

        elif self.tipo == 'braços':
            # Cacto Saguaro Complexo (Tronco + Braços)
            centro_x = x + (self.largura // 2)
            # Tronco Principal
            pygame.draw.rect(superficie, VERDE_CACTO, (centro_x - largura_tronco // 2, y + 5, largura_tronco, self.altura - 5))
            pygame.draw.circle(superficie, VERDE_CACTO, (centro_x, y + 8), largura_tronco // 2)
            
            # Braço Esquerdo (Cima + Curva)
            y_base_braço = y + 25
            alt_braço_cima = 15
            # Parte de cima
            pygame.draw.rect(superficie, VERDE_CACTO, (centro_x - largura_tronco // 2 - largura_braço, y_base_braço - alt_braço_cima, largura_braço, alt_braço_cima))
            pygame.draw.circle(superficie, VERDE_CACTO, (centro_x - largura_tronco // 2 - largura_braço + largura_braço // 2, y_base_braço - alt_braço_cima), largura_braço // 2)
            # Conexão horizontal (curva)
            pygame.draw.rect(superficie, VERDE_CACTO, (centro_x - largura_tronco // 2 - largura_braço + 2, y_base_braço - 2, largura_braço - 2, 6))

            # Braço Direito (Mais baixo)
            y_base_braço2 = y + 35
            alt_braço_cima2 = 12
            # Parte de cima
            pygame.draw.rect(superficie, VERDE_CACTO, (centro_x + largura_tronco // 2, y_base_braço2 - alt_braço_cima2, largura_braço, alt_braço_cima2))
            pygame.draw.circle(superficie, VERDE_CACTO, (centro_x + largura_tronco // 2 + largura_braço // 2, y_base_braço2 - alt_braço_cima2), largura_braço // 2)
            # Conexão horizontal (curva)
            pygame.draw.rect(superficie, VERDE_CACTO, (centro_x + largura_tronco // 2 - 2, y_base_braço2 - 2, largura_braço - 2, 6))

def desenhar_texto(texto, fonte, cor, x, y, centralizado=False):
    superficie = fonte.render(texto, True, cor)
    rect_texto = superficie.get_rect()
    if centralizado:
        rect_texto.center = (x, y)
    else:
        rect_texto.topleft = (x, y)
    tela.blit(superficie, rect_texto)

def jogar(recorde_atual):
    clock = pygame.time.Clock()
    dino = Dino()
    obstaculos = [Obstaculo(LARGURA)]
    velocidade_jogo = 7
    pontuacao = 0
    game_over = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                if pontuacao > recorde_atual:
                    salvar_recorde(pontuacao)
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if game_over:
                        if pontuacao > recorde_atual:
                            salvar_recorde(pontuacao)
                            return pontuacao
                        return recorde_atual
                    else:
                        dino.pular()

        if not game_over:
            dino.atualizar()

            for obs in obstaculos[:]:
                obs.mover(velocidade_jogo)

                if dino.rect.colliderect(obs.rect):
                    game_over = True

                if obs.x < -obs.largura:
                    obstaculos.remove(obs)
                    pontuacao += 1
                    
                    if pontuacao > 0 and pontuacao % 5 == 0:
                        velocidade_jogo += 0.5
            
            if pontuacao > recorde_atual:
                recorde_atual = pontuacao

            if len(obstaculos) == 0 or obstaculos[-1].x < LARGURA - random.randint(250, 500):
                obstaculos.append(Obstaculo(LARGURA + random.randint(0, 150)))

        tela.fill(BRANCO)
        pygame.draw.line(tela, CINZA, (0, CHAO_Y), (LARGURA, CHAO_Y), 3)

        dino.desenhar(tela)
        for obs in obstaculos:
            obs.desenhar(tela)

        texto_pontos = f"HI: {recorde_atual:05d}   Pontuação: {pontuacao:05d}"
        desenhar_texto(texto_pontos, fonte_pontuacao, PRETO, 20, 20)

        if game_over:
            desenhar_texto("GAME OVER", fonte_gameover, PRETO, LARGURA // 2, ALTURA // 2 - 20, centralizado=True)
            desenhar_texto("Pressione ESPAÇO para reiniciar", fonte_pontuacao, PRETO, LARGURA // 2, ALTURA // 2 + 30, centralizado=True)

        pygame.display.flip()
        clock.tick(60)

recorde_salvo = carregar_recorde()
while True:
    recorde_salvo = jogar(recorde_salvo)
import pygame
import random

# Inicialização
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("T-Rex Runner Simples")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)

# Variáveis do Jogo
clock = pygame.time.Clock()
gravidade = 0.8

class Dino:
    def __init__(self):
        self.largura = 40
        self.altura = 40
        self.x = 50
        self.y = ALTURA - self.altura - 10
        self.velocidade_y = 0
        self.pulo = False

    def pular(self):
        if not self.pulo:
            self.velocidade_y = -15
            self.pulo = True

    def aplicar_gravidade(self):
        self.velocidade_y += gravidade
        self.y += self.velocidade_y
        if self.y >= ALTURA - self.altura - 10:
            self.y = ALTURA - self.altura - 10
            self.pulo = False

    def desenhar(self):
        pygame.draw.rect(tela, PRETO, (self.x, self.y, self.largura, self.altura))

class Obstaculo:
    def __init__(self):
        self.largura = 20
        self.altura = 40 + random.randint(0, 30)
        self.x = LARGURA
        self.y = ALTURA - self.altura - 10

    def mover(self, velocidade):
        self.x -= velocidade

    def desenhar(self):
        pygame.draw.rect(tela, VERDE, (self.x, self.y, self.largura, self.altura))

def jogar():
    dino = Dino()
    obstaculos = [Obstaculo()]
    velocidade_jogo = 7
    pontuacao = 0
    rodando = True

    while rodando:
        tela.fill(BRANCO)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    dino.pular()

        # Lógica do Dino
        dino.aplicar_gravidade()
        dino.desenhar()

        # Lógica dos Obstáculos
        for obs in obstaculos[:]:
            obs.mover(velocidade_jogo)
            obs.desenhar()

            # Colisão
            dino_rect = pygame.Rect(dino.x, dino.y, dino.largura, dino.altura)
            obs_rect = pygame.Rect(obs.x, obs.y, obs.largura, obs.altura)
            if dino_rect.colliderect(obs_rect):
                print(f"Fim de Jogo! Pontuação: {pontuacao}")
                rodando = False

            # Remover obstáculo e adicionar novo
            if obs.x < -obs.largura:
                obstaculos.remove(obs)
                obstaculos.append(Obstaculo())
                pontuacao += 1
                if pontuacao % 5 == 0: # Aumenta a velocidade
                    velocidade_jogo += 0.5

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

jogar()
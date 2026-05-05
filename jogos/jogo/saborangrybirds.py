import pygame
import math

# Inicialização
pygame.init()

# Configurações da Tela
LARGURA, ALTURA = 1000, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Angry Birds - Física Avançada Nativa")
CLOCK = pygame.time.Clock()
FPS = 60

# Cores
CEU = (135, 206, 235)
CHAO = (34, 139, 34)
MADEIRA_CLARA = (205, 133, 63)
MADEIRA_ESCURA = (139, 69, 19)
PÁSSARO_COR = (220, 20, 60)
PORCO_COR = (50, 205, 50)
ESTILINGUE_COR = (48, 22, 8)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA_RASTRO = (200, 200, 200)

fonte = pygame.font.SysFont("Arial", 24, bold=True)

def colisao_circulo_retangulo(cx, cy, raio, rect):
    px = max(rect.left, min(cx, rect.right))
    py = max(rect.top, min(cy, rect.bottom))
    dist_x = cx - px
    dist_y = cy - py
    return (dist_x**2 + dist_y**2) < (raio**2)

class Passaro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.raio = 12
        self.voando = False
        self.parado = False
        self.rastro = []
        self.contador_rastro = 0

    def lancar(self, dx, dy):
        potencia = 0.2
        self.vx = dx * potencia
        self.vy = dy * potencia
        self.voando = True

    def atualizar(self):
        if self.voando and not self.parado:
            self.vy += 0.5 # Gravidade
            self.x += self.vx
            self.y += self.vy

            # Rastro
            self.contador_rastro += 1
            if self.contador_rastro >= 3:
                self.rastro.append((int(self.x), int(self.y)))
                self.contador_rastro = 0

            # Limite do chão
            if self.y >= ALTURA - 50 - self.raio:
                self.y = ALTURA - 50 - self.raio
                self.vy *= -0.5
                self.vx *= 0.7
                if abs(self.vx) < 0.5 and abs(self.vy) < 0.5:
                    self.parado = True

            # Saiu da tela
            if self.x > LARGURA or self.x < 0:
                self.parado = True

    def desenhar(self, tela):
        for ponto in self.rastro:
            pygame.draw.circle(tela, CINZA_RASTRO, ponto, 3)
        pygame.draw.circle(tela, PÁSSARO_COR, (int(self.x), int(self.y)), self.raio)
        pygame.draw.circle(tela, PRETO, (int(self.x), int(self.y)), self.raio, 2)

class EntidadeFisica:
    def __init__(self, x, y, w, h, tipo):
        self.rect = pygame.Rect(x, y, w, h)
        self.tipo = tipo # 'bloco' ou 'porco'
        self.vy = 0

    def atualizar(self, todas_entidades):
        self.vy += 0.5 # Gravidade para blocos e porcos
        self.rect.y += int(self.vy)

        # Colisão com o chão
        chao_y = ALTURA - 50
        if self.rect.bottom >= chao_y:
            self.rect.bottom = chao_y
            self.vy = 0

        # Colisão com outras entidades (ficar um em cima do outro)
        for outra in todas_entidades:
            if outra != self and self.rect.colliderect(outra.rect):
                # Se eu estou caindo e bati na parte de cima de outro objeto
                if self.vy > 0 and self.rect.bottom - int(self.vy) <= outra.rect.top + 5:
                    self.rect.bottom = outra.rect.top
                    self.vy = 0

    def desenhar(self, tela):
        if self.tipo == 'bloco':
            pygame.draw.rect(tela, MADEIRA_CLARA, self.rect)
            pygame.draw.rect(tela, MADEIRA_ESCURA, self.rect, 2)
        elif self.tipo == 'porco':
            # O porco usa um Rect para física, mas desenhamos um círculo no centro dele
            cx, cy = self.rect.center
            raio = self.rect.width // 2
            pygame.draw.circle(tela, PORCO_COR, (cx, cy), raio)
            pygame.draw.circle(tela, PRETO, (cx, cy), raio, 2)
            pygame.draw.circle(tela, PRETO, (cx - 5, cy - 3), 3)
            pygame.draw.circle(tela, PRETO, (cx + 5, cy - 3), 3)

class Jogo:
    def __init__(self):
        self.ancora_x = 200
        self.ancora_y = ALTURA - 150
        self.passaro = Passaro(self.ancora_x, self.ancora_y)
        self.arrastando = False
        self.mouse_x = self.ancora_x
        self.mouse_y = self.ancora_y
        self.montar_fase()

    def montar_fase(self):
        self.passaro = Passaro(self.ancora_x, self.ancora_y)
        self.entidades = []
        
        # Blocos [x, y, largura, altura]
        self.entidades.append(EntidadeFisica(650, ALTURA - 150, 20, 100, 'bloco'))
        self.entidades.append(EntidadeFisica(750, ALTURA - 150, 20, 100, 'bloco'))
        self.entidades.append(EntidadeFisica(630, ALTURA - 170, 160, 20, 'bloco'))
        
        self.entidades.append(EntidadeFisica(680, ALTURA - 270, 20, 100, 'bloco'))
        self.entidades.append(EntidadeFisica(720, ALTURA - 270, 20, 100, 'bloco'))
        self.entidades.append(EntidadeFisica(660, ALTURA - 290, 100, 20, 'bloco'))

        # Porcos (Tratados como retângulos de 30x30 para a física de suporte)
        self.entidades.append(EntidadeFisica(695, ALTURA - 80, 30, 30, 'porco'))
        self.entidades.append(EntidadeFisica(695, ALTURA - 200, 30, 30, 'porco'))

    def atualizar(self):
        self.passaro.atualizar()

        # Atualiza gravidade dos blocos e porcos
        for entidade in self.entidades:
            entidade.atualizar(self.entidades)

        # Checa colisão do Pássaro com as Entidades
        if self.passaro.voando and not self.passaro.parado:
            velocidade_impacto = math.hypot(self.passaro.vx, self.passaro.vy)

            for entidade in self.entidades[:]:
                if colisao_circulo_retangulo(self.passaro.x, self.passaro.y, self.passaro.raio, entidade.rect):
                    if entidade.tipo == 'bloco':
                        if velocidade_impacto > 4.0:
                            self.entidades.remove(entidade) # Quebra
                            self.passaro.vx *= 0.8
                            self.passaro.vy *= 0.8
                        else:
                            self.passaro.vx *= -0.5 # Quica
                            self.passaro.vy *= -0.5
                            self.passaro.x += self.passaro.vx 
                            self.passaro.y += self.passaro.vy
                    elif entidade.tipo == 'porco':
                        self.entidades.remove(entidade) # Porco morre ao ser tocado

    def desenhar_trajetoria(self, tela):
        # Simula o caminho do pássaro no futuro
        dx = self.ancora_x - self.mouse_x
        dy = self.ancora_y - self.mouse_y
        
        sim_x, sim_y = self.ancora_x, self.ancora_y
        sim_vx, sim_vy = dx * 0.2, dy * 0.2
        
        for _ in range(15): # Desenha 15 pontos
            for _ in range(4): # Avança 4 frames por ponto para espaçar mais
                sim_vy += 0.5
                sim_x += sim_vx
                sim_y += sim_vy
            
            # Para de desenhar a mira se bater no chão
            if sim_y >= ALTURA - 50:
                break
            
            pygame.draw.circle(tela, BRANCO, (int(sim_x), int(sim_y)), 4)

    def desenhar(self):
        TELA.fill(CEU)
        pygame.draw.rect(TELA, CHAO, (0, ALTURA - 50, LARGURA, 50))

        texto = fonte.render("Arraste e solte! Pressione [R] para reiniciar.", True, PRETO)
        TELA.blit(texto, (20, 20))

        pygame.draw.rect(TELA, ESTILINGUE_COR, (self.ancora_x - 5, self.ancora_y, 10, 100))

        if self.arrastando:
            self.desenhar_trajetoria(TELA)
            pygame.draw.line(TELA, PRETO, (self.ancora_x, self.ancora_y), (self.mouse_x, self.mouse_y), 4)
            pygame.draw.circle(TELA, PÁSSARO_COR, (int(self.mouse_x), int(self.mouse_y)), 12)
            pygame.draw.circle(TELA, PRETO, (int(self.mouse_x), int(self.mouse_y)), 12, 2)
        else:
            self.passaro.desenhar(TELA)

        for entidade in self.entidades:
            entidade.desenhar(TELA)

        pygame.display.flip()

def main():
    jogo = Jogo()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1 and not jogo.passaro.voando:
                    dist = math.hypot(evento.pos[0] - jogo.ancora_x, evento.pos[1] - jogo.ancora_y)
                    if dist < 50:
                        jogo.arrastando = True

            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1 and jogo.arrastando:
                    jogo.arrastando = False
                    dx = jogo.ancora_x - jogo.mouse_x
                    dy = jogo.ancora_y - jogo.mouse_y
                    jogo.passaro.lancar(dx, dy)

            elif evento.type == pygame.MOUSEMOTION:
                if jogo.arrastando:
                    mx, my = evento.pos
                    dx = mx - jogo.ancora_x
                    dy = my - jogo.ancora_y
                    angulo = math.atan2(dy, dx)
                    dist = math.hypot(dx, dy)
                    if dist > 100:
                        mx = jogo.ancora_x + math.cos(angulo) * 100
                        my = jogo.ancora_y + math.sin(angulo) * 100
                    jogo.mouse_x, jogo.mouse_y = mx, my

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    jogo.montar_fase()

        jogo.atualizar()
        jogo.desenhar()
        CLOCK.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
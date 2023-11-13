import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블럭 깨기 게임")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 패들 설정
paddle_width, paddle_height = 400, 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - 20

# 공 설정
ball_radius = 10
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 5, 5

# 블럭 설정
block_width, block_height = 50, 20
block_rows = 5
block_cols = width // block_width
blocks = []

for row in range(block_rows):
    for col in range(block_cols):
        block_x = col * block_width
        block_y = row * block_height + 50
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 패들 이동
    keys = pygame.key.get_pressed()
    paddle_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 7
    paddle_x = max(0, min(width - paddle_width, paddle_x))

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌
    if ball_x <= 0 or ball_x >= width:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과 충돌
    if paddle_x < ball_x < paddle_x + paddle_width and paddle_y < ball_y < paddle_y + paddle_height:
        ball_speed_y = -ball_speed_y

    # 블럭과 충돌
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, white, block)

    pygame.display.flip()
    clock.tick(60)

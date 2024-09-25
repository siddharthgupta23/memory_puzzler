# import pygame
# import random
# import time
# import requests
# from PIL import Image,ImageFont
# from io import BytesIO


# pygame.init()

# font = ImageFont.truetype("arial.ttf", size=36)
# SCREEN_WIDTH=600
# SCREEN_HEIGHT=600
# CARD_SIZE=125
# GRID_SIZE=4
# YELLOW=(255,255,255)

# fLIP_DISPLAY=0.8

# BUTTON_WIDTH=250

# ORANGE=(255,255,255)

# BUTTON_HEIGHT=180

# TIMER_LIMIT=15

# image_urls=[
#     './assets/card11.png',
#     './assets/card22.png',
#     './assets/card33.png',
#     './assets/card44.png',
#     './assets/card55.png',
    
# ]

# screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# pygame.display.set_caption("Memory puzzler game")
# response=requests.get(
#     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHhQBZjKlHB5Pgkpk4V2DF15a3yDQDQ9K2ZA&s"
# )
# image=Image.open(BytesIO(response.content))
# image=image.convert("RGB")

# with BytesIO() as img_bytes:
#     image.save(img_bytes,"PNG")
#     img_bytes.seek(0)
#     card_back=pygame.image.load(img_bytes)
    
#     card_images=[]
#     for url in image_urls:
#         response=requests.get(url)
#         image=Image.open(BytesIO(response._content))
#         image=Image.convert("RGB")
#         with BytesIO as img_bytes:
#             image.save(img_bytes,"PNG")
#             img_bytes.seek(0)
#             card_images.append(pygame.image.load(img_bytes))
            
            
#     card_images *=2
#     random.shuffle(card_images)
    
#     card_state=[False] * (GRID_SIZE*GRID_SIZE)
#     def rect(c,d):
#         e,f = c
#         rx, ry, rw, rh = d
#         return rx < e < rx + rw and ry < f < ry + rh
#     def d_r_button():
#         restart_button_rect = (SCREEN_WIDTH - BUTTON_WIDTH -
#                            20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
#         pygame.draw.rect(screen, ORANGE, restart_button_rect)
    
#         restart_text = font.render("Restart Game", True, (0, 0, 0))
#         text_rect = restart_text.get_rect(center=(
#         restart_button_rect[0] + BUTTON_WIDTH / 2, restart_button_rect[1] + BUTTON_HEIGHT / 2))
#         screen.blit(restart_text, text_rect)
#     def d_timer():
#             elapsed_time = max(0, int(time.time() - t_s_t))
#             remaining_time = max(0, TIMER_LIMIT - elapsed_time)
#             timer_text = font.render(f"Time: {remaining_time}s", True, YELLOW)
#             screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))
#     def display_message(message):
#         message_text = font.render(message, True, YELLOW)
#         text_rect = message_text.get_rect(
#         center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
#         screen.blit(message_text, text_rect)
#     running=True
#     while running:
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 running=False
#             elif event.type==pygame.MOUSEBUTTONDOWN:
#                 x,y=pygame.mouse.get.pos()
#                 AB=(
                    
#                 SCREEN_WIDTH-BUTTON_WIDTH-20,20,BUTTON_WIDTH,BUTTON_HEIGHT
            
#                 )
#                 if rect((x,y),AB):
#                     random.shuffle(card_images)
#                     card_state=[False] * (GRID_SIZE **2)
#                     Flipped_cards=[]
#                     matched_pairs=[]
                    
#                     moves=0
#                     t_s_t = time.time()
#                 else:
#                     m = x // CARD_SIZE
#                     n = y // CARD_SIZE
#                     index = m * GRID_SIZE + n
#                     if not card_state[index] and len(Flipped_cards) < 2:
#                         card_state[index] = True
#                         Flipped_cards.append(index)
#                         moves += 1
#         screen.fill(ORANGE)
#         for i in range(GRID_SIZE):
#             for j in range(GRID_SIZE):
#                 index=i* GRID_SIZE+j
#                 pygame.draw.rect(screen, ORANGE, (j * CARD_SIZE,
#                                              i * CARD_SIZE, CARD_SIZE, CARD_SIZE)
#                 )
                
#                 if card_state[index] or index in Flipped_cards:
#                     card = card_images[index]
#                 else:
#                     card = card_back
#                 card = pygame.transform.scale(card, (CARD_SIZE - 8, CARD_SIZE - 8))
#                 screen.blit(card, (j * CARD_SIZE + 4, i * CARD_SIZE + 4))
#             moves_text = font.render(f"Moves: {moves}", True, ORANGE)
#     screen.blit(moves_text, (10, 10))
#     d_r_button()

    
#     d_timer()

#     if len(Flipped_cards) == 2:
#         time.sleep(fLIP_DISPLAY)
#         if card_images[Flipped_cards[0]] == card_images[Flipped_cards[1]]:
#             matched_pairs += 1
#             Flipped_cards = []
#         else:
#             card_state[Flipped_cards[0]] = False
#             card_state[Flipped_cards[1]] = False
#             Flipped_cards = []

#     if matched_pairs == GRID_SIZE ** 2 // 2:
#         display_message("Congratulations! You found all the pairs!")
#         pygame.display.flip()
#         time.sleep(2)
#         running = False

   
#     elapsed_time = time.time() - t_s_t
#     if elapsed_time >= TIMER_LIMIT:
#         display_message("Time's up! You lost the game.")
#         pygame.display.flip()
#         time.sleep(2)  
#         running = False
#     elapsed_time = time.time() - t_s_t
#     if elapsed_time >= TIMER_LIMIT:
#         display_message("Time's up! You lost the game.")
#         pygame.display.flip()
#         time.sleep(2)  
#         running = False

#     pygame.display.flip()

# pygame.quit()
    
    
# import pygame
# import random
# import time
# from PIL import Image, ImageFont

# # Initialize Pygame
# pygame.init()

# # Load the font
# font = pygame.font.Font("arial.ttf", 36)
# SCREEN_WIDTH = 600
# SCREEN_HEIGHT = 600
# CARD_SIZE = 125
# GRID_SIZE = 4
# YELLOW = (255, 255, 255)
# fLIP_DISPLAY = 0.8
# BUTTON_WIDTH = 250
# ORANGE = (255, 165, 0)  # Changed to a distinct orange color
# BUTTON_HEIGHT = 180
# TIMER_LIMIT = 15

# # Paths to local card images
# image_urls = [
#     './assets/card11.png',
#     './assets/card22.png',
#     './assets/card33.png',
#     './assets/card44.png',
#     './assets/card55.png',
#     './assets/card66.png',
    
#     './assets/color-balloons-clipart-md.png',
#     './assets/card77.png'
    
# ]

# # Create the game window
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Memory Puzzler Game")

# # Load local images directly
# card_images = []
# for filename in image_urls:
#     card_image = pygame.image.load(filename)
#     card_images.append(card_image)

# # Duplicate the images for matching pairs
# card_images *= 2
# random.shuffle(card_images)

# # Card state and game variables
# card_state = [False] * (GRID_SIZE * GRID_SIZE)
# Flipped_cards = []
# matched_pairs = []
# moves = 0
# t_s_t = time.time()

# # Function to check if a point is within a rectangle
# def rect(c, d):
#     e, f = c
#     rx, ry, rw, rh = d
#     return rx < e < rx + rw and ry < f < ry + rh

# # Draw the restart button
# def d_r_button():
#     restart_button_rect = (SCREEN_WIDTH - BUTTON_WIDTH - 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
#     pygame.draw.rect(screen, ORANGE, restart_button_rect)
#     restart_text = font.render("Restart Game", True, (0, 0, 0))
#     text_rect = restart_text.get_rect(center=(restart_button_rect[0] + BUTTON_WIDTH / 2, restart_button_rect[1] + BUTTON_HEIGHT / 2))
#     screen.blit(restart_text, text_rect)

# # Draw the timer
# def d_timer():
#     elapsed_time = max(0, int(time.time() - t_s_t))
#     remaining_time = max(0, TIMER_LIMIT - elapsed_time)
#     timer_text = font.render(f"Time: {remaining_time}s", True, YELLOW)
#     screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))

# # Display a message in the center
# def display_message(message):
#     message_text = font.render(message, True, YELLOW)
#     text_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
#     screen.blit(message_text, text_rect)

# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()
#             AB = (SCREEN_WIDTH - BUTTON_WIDTH - 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
#             if rect((x, y), AB):
#                 random.shuffle(card_images)
#                 card_state = [False] * (GRID_SIZE ** 2)
#                 Flipped_cards = []
#                 matched_pairs = []
#                 moves = 0
#                 t_s_t = time.time()
#             else:
#                 m = x // CARD_SIZE
#                 n = y // CARD_SIZE
#                 index = m * GRID_SIZE + n
#                 if not card_state[index] and len(Flipped_cards) < 2:
#                     card_state[index] = True
#                     Flipped_cards.append(index)
#                     moves += 1

#     screen.fill(ORANGE)
#     for i in range(GRID_SIZE):
#         for j in range(GRID_SIZE):
#             index = i * GRID_SIZE + j
#             pygame.draw.rect(screen, ORANGE, (j * CARD_SIZE, i * CARD_SIZE, CARD_SIZE, CARD_SIZE))

#             if card_state[index] or index in Flipped_cards:
#                 card = card_images[index]
#             else:
#                 card = pygame.Surface((CARD_SIZE - 8, CARD_SIZE - 8))
#                 card.fill((255, 255, 255))  # Placeholder for card back

#             card = pygame.transform.scale(card, (CARD_SIZE - 8, CARD_SIZE - 8))
#             screen.blit(card, (j * CARD_SIZE + 4, i * CARD_SIZE + 4))

#     moves_text = font.render(f"Moves: {moves}", True, (0, 0, 0))
#     screen.blit(moves_text, (10, 10))
#     d_r_button()
#     d_timer()

#     if len(Flipped_cards) == 2:
#         time.sleep(fLIP_DISPLAY)
#         if card_images[Flipped_cards[0]] == card_images[Flipped_cards[1]]:
#             matched_pairs.append(Flipped_cards[0])
#             matched_pairs.append(Flipped_cards[1])
#             Flipped_cards = []
#         else:
#             card_state[Flipped_cards[0]] = False
#             card_state[Flipped_cards[1]] = False
#             Flipped_cards = []

#     if len(matched_pairs) == GRID_SIZE ** 2:
#         display_message("Congratulations! You found all the pairs!")
#         pygame.display.flip()
#         time.sleep(2)
#         running = False

#     elapsed_time = time.time() - t_s_t
#     if elapsed_time >= TIMER_LIMIT:
#         display_message("Time's up! You lost the game.")
#         pygame.display.flip()
#         time.sleep(2)
#         running = False

#     pygame.display.flip()

# pygame.quit()
# import pygame
# import random
# import time

# # Initialize Pygame
# pygame.init()

# # Load the font
# font_large = pygame.font.Font("arial.ttf", 36)
# font_small = pygame.font.Font("arial.ttf", 24)
# SCREEN_WIDTH = 700
# SCREEN_HEIGHT = 600
# CARD_SIZE = 125
# GRID_SIZE = 4
# YELLOW = (255, 255, 255)
# fLIP_DISPLAY = 0.8
# BUTTON_WIDTH = 90
# ORANGE = (255, 165, 0)
# BUTTON_HEIGHT = 130
# TIMER_LIMIT = 78

# # Paths to local card images
# image_urls = [
#     './assets/card11.png',
#     './assets/card22.png',
#     './assets/card33.png',
#     './assets/card44.png',
#     './assets/card55.png',
#     './assets/card66.png',
#     './assets/color-balloons-clipart-md.png',
#     './assets/card77.png'
# ]

# # Create the game window
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Memory Puzzler Game")


# card_images = []
# for filename in image_urls:
#     card_image = pygame.image.load(filename)
#     card_images.append(card_image)

# # Duplicate the images for matching pairs
# card_images *= 2
# random.shuffle(card_images)

# # Card state and game variables
# card_state = [False] * (GRID_SIZE * GRID_SIZE)
# Flipped_cards = []
# matched_pairs = []
# moves = 0
# t_s_t = time.time()

# # Function to check if a point is within a rectangle
# def rect(c, d):
#     e, f = c
#     rx, ry, rw, rh = d
#     return rx < e < rx + rw and ry < f < ry + rh

# # Draw the restart button
# def d_r_button():
#     restart_button_rect = (SCREEN_WIDTH - BUTTON_WIDTH - 80, 80, BUTTON_WIDTH, BUTTON_HEIGHT)
#     pygame.draw.rect(screen, YELLOW, restart_button_rect)
#     restart_text = font_small.render("Restart Game", True, (0, 0, 0))
#     text_rect = restart_text.get_rect(center=(restart_button_rect[0] + BUTTON_WIDTH / 2, restart_button_rect[1] + BUTTON_HEIGHT / 2))
#     screen.blit(restart_text, text_rect)

# # Draw the timer
# def d_timer():
#     elapsed_time = max(0, int(time.time() - t_s_t))
#     remaining_time = max(0, TIMER_LIMIT - elapsed_time)
#     timer_text = font_small.render(f"Time: {remaining_time}s", True, (0, 0, 0))
#     screen.blit(timer_text, (10, 10))

# # Display a message in the center
# def display_message(message):
#     message_text = font_large.render(message, True, YELLOW)
#     text_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
#     screen.blit(message_text, text_rect)

# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()
#             AB = (SCREEN_WIDTH - BUTTON_WIDTH - 80, 80, BUTTON_WIDTH, BUTTON_HEIGHT)
#             if rect((x, y), AB):
#                 random.shuffle(card_images)
#                 card_state = [False] * (GRID_SIZE ** 2)
#                 Flipped_cards = []
#                 matched_pairs = []
#                 moves = 0
#                 t_s_t = time.time()
#             else:
#                 m = x // CARD_SIZE
#                 n = y // CARD_SIZE
#                 index = m * GRID_SIZE + n
#                 if index < len(card_state) and not card_state[index] and len(Flipped_cards) < 2:
#                     card_state[index] = True
#                     Flipped_cards.append(index)
#                     moves += 1

#     screen.fill(ORANGE)
#     for i in range(GRID_SIZE):
#         for j in range(GRID_SIZE):
#             index = i * GRID_SIZE + j
#             pygame.draw.rect(screen, ORANGE, (j * CARD_SIZE, i * CARD_SIZE, CARD_SIZE, CARD_SIZE))

#             if card_state[index] or index in Flipped_cards:
#                 card = card_images[index]
#             else:
#                 card = pygame.Surface((CARD_SIZE - 8, CARD_SIZE - 8))
#                 card.fill((255, 255, 255))  # Placeholder for card back

#             card = pygame.transform.scale(card, (CARD_SIZE - 8, CARD_SIZE - 8))
#             screen.blit(card, (j * CARD_SIZE + 4, i * CARD_SIZE + 4))

#     moves_text = font_small.render(f"Moves: {moves}", True, (0, 0, 0))
#     screen.blit(moves_text, (10, 40))  # Adjusted position
#     d_r_button()
#     d_timer()

#     if len(Flipped_cards) == 2:
#         time.sleep(fLIP_DISPLAY)
#         if card_images[Flipped_cards[0]] == card_images[Flipped_cards[1]]:
#             matched_pairs.append(Flipped_cards[0])
#             matched_pairs.append(Flipped_cards[1])
#             Flipped_cards = []
#         else:
#             card_state[Flipped_cards[0]] = False
#             card_state[Flipped_cards[1]] = False
#             Flipped_cards = []

#     if len(matched_pairs) == GRID_SIZE ** 2:
#         display_message("Congratulations! You found all the pairs!")
#         pygame.display.flip()
#         time.sleep(2)
#         running = False

#     elapsed_time = time.time() - t_s_t
#     if elapsed_time >= TIMER_LIMIT:
#         display_message("Time's up! You lost the game.")
#         pygame.display.flip()
#         time.sleep(2)
#         running = False

#     pygame.display.flip()

# pygame.quit()
import pygame
import random
import time


pygame.init()

font_large = pygame.font.Font("arial.ttf", 36)
font_small = pygame.font.Font("arial.ttf", 24)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CARD_SIZE = 125
GRID_SIZE = 4
YELLOW = (255, 255, 255)
WHITE = (255, 255, 255)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK = (0, 0, 0)
fLIP_DISPLAY = 0.8
BUTTON_WIDTH = 150  
BUTTON_HEIGHT = 50
ORANGE = (255, 165, 0)
TIMER_LIMIT = 78


image_urls = [
    './assets/card11.png',
    './assets/card22.png',
    './assets/card33.png',
    './assets/card44.png',
    './assets/card55.png',
    './assets/card66.png',
    './assets/color-balloons-clipart-md.png',
    './assets/card77.png'
]


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Puzzler Game")

card_images = []
for filename in image_urls:
    card_image = pygame.image.load(filename)
    card_images.append(card_image)


card_images *= 2
random.shuffle(card_images)


card_state = [False] * (GRID_SIZE * GRID_SIZE)
Flipped_cards = []
matched_pairs = []
moves = 0
t_s_t = time.time()

def rect(c, d):
    e, f = c
    rx, ry, rw, rh = d
    return rx < e < rx + rw and ry < f < ry + rh


def d_r_button():
    restart_button_rect = (SCREEN_WIDTH - BUTTON_WIDTH - 10, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, ORANGE, restart_button_rect)
    restart_text = font_small.render("Restart", True, BLACK)
    text_rect = restart_text.get_rect(center=(restart_button_rect[0] + BUTTON_WIDTH / 2, restart_button_rect[1] + BUTTON_HEIGHT / 2))
    screen.blit(restart_text, text_rect)


def d_timer():
    elapsed_time = max(0, int(time.time() - t_s_t))
    remaining_time = max(0, TIMER_LIMIT - elapsed_time)
    timer_text = font_small.render(f"Time: {remaining_time}s", True, BLACK)
    screen.blit(timer_text, (10, 10))


def display_message(message, color):
    message_text = font_large.render(message, True, color)
    text_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(message_text, text_rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            AB = (SCREEN_WIDTH - BUTTON_WIDTH - 10, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
            if rect((x, y), AB):
                random.shuffle(card_images)
                card_state = [False] * (GRID_SIZE ** 2)
                Flipped_cards = []
                matched_pairs = []
                moves = 0
                t_s_t = time.time()
            else:
                m = x // CARD_SIZE
                n = y // CARD_SIZE
                index = m * GRID_SIZE + n
                if index < len(card_state) and not card_state[index] and len(Flipped_cards) < 2:
                    card_state[index] = True
                    Flipped_cards.append(index)
                    moves += 1

    screen.fill(ORANGE)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            index = i * GRID_SIZE + j
            pygame.draw.rect(screen, ORANGE, (j * CARD_SIZE, i * CARD_SIZE, CARD_SIZE, CARD_SIZE))

            if card_state[index] or index in Flipped_cards:
                card = card_images[index]
            else:
                card = pygame.Surface((CARD_SIZE - 8, CARD_SIZE - 8))
                card.fill(WHITE)  

            card = pygame.transform.scale(card, (CARD_SIZE - 8, CARD_SIZE - 8))
            screen.blit(card, (j * CARD_SIZE + 4, i * CARD_SIZE + 4))

    moves_text = font_small.render(f"Moves: {moves}", True, BLACK)
    screen.blit(moves_text, (10, 40))  
    d_r_button()
    d_timer()

    if len(Flipped_cards) == 2:
        time.sleep(fLIP_DISPLAY)
        if card_images[Flipped_cards[0]] == card_images[Flipped_cards[1]]:
            matched_pairs.append(Flipped_cards[0])
            matched_pairs.append(Flipped_cards[1])
            Flipped_cards = []
        else:
            card_state[Flipped_cards[0]] = False
            card_state[Flipped_cards[1]] = False
            Flipped_cards = []

    if len(matched_pairs) == GRID_SIZE ** 2:
        display_message("Congratulations! You won!", GREEN) 
        pygame.display.flip()
        time.sleep(2)
        running = False

    elapsed_time = time.time() - t_s_t
    if elapsed_time >= TIMER_LIMIT:
        display_message("Time's up! You lost!", RED)  
        pygame.display.flip()
        time.sleep(2)
        running = False

    pygame.display.flip()

pygame.quit()


#understand m not that bright, 'm learning don't harsh on me
#first I'll Initialise and load the requriements
import pygame
import random

pygame.init()

#Now melon will set up screen 480p is optimal I guess
screen_width = 854
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("aa bhai gaali kha le")

#now melon will add two colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font ki baari
font = pygame.font.Font(None, 36)
#Define Gaalis format in a table, wil use this to make random combination
subjects = ["abe Randi ke", "Teri ", "oo", "Saale", "Chal", "ae", "Bhadwa", " ", ]
verbs = [" ", "Ma Ki", "Baap ka", "Bhai ka", "Boor ka", "Lund lega" "Bhosda" ]
objects = [" ", "Chut", "Gaand","Bhosda","Taang", "Lund", "Choda", "saala", "saala Randibaaz" "Madhar chod", "randibaaz", "Khodunga"]

#lets tabulate the same
kindness_messages = [
    subjects,
    verbs,
    objects
]
#GEND for our GenDu Genration
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5
ball_speed_y = 5

#Patta

paddle_width = 10
paddle_height = 100
paddle_speed = 5
w1_score = 0

#Draw GeNd andd Patta
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (50, paddle1_y, paddle_width, paddle_height))  # Paddle for w1
    pygame.draw.rect(screen, WHITE, (screen_width - 50 - paddle_width, paddle2_y, paddle_width, paddle_height))  # Paddle for w2
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)  # Ball
    render_score()
    render_kindness_message()

#SCORE
    def render_score():
    score_text = font.render(f"Score: {w1_score}", True, WHITE)
    screen.blit(score_text, (screen_width // 2 - 50, 20))
#Kindness Messages
    def render_kindness_message():
    if kindness_message:
        kindness_text = " ".join(kindness_message)
        message_text = font.render(kindness_text, True, WHITE)
        screen.blit(message_text, (screen_width // 2 - message_text.get_width() // 2, 50))
        
# Generate kindness message
def generate_kindness_message():
    return " ".join(random.choice(kindness_messages[i]) for i in range(3))

# Computer-driven opponent(DOST) logic
def move_computer_paddle():
    global paddle1_y
    if ball_y < paddle1_y + paddle_height // 2:
        paddle1_y -= paddle_speed
    elif ball_y > paddle1_y + paddle_height // 2:
        paddle1_y += paddle_speed

# Main game loop
running = True
paddle1_y = screen_height // 2 - paddle_height // 2
paddle2_y = screen_height // 2 - paddle_height // 2
kindness_message = ""  # Variable to store the kindness message
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_s] and paddle2_y < screen_height - paddle_height:
        paddle2_y += paddle_speed

    # Move w1 paddle (computer-driven)
    move_computer_paddle()

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with paddles
    if ball_x - ball_radius <= 50 + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x *= -1
        w1_score += 1
        kindness_message = generate_kindness_message()  # Display kindness message for w1
    elif ball_x + ball_radius >= screen_width - 50 - paddle_width and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x *= -1
        kindness_message = generate_kindness_message()  # Display kindness message for w2

    # Ball collision with top and bottom walls
    if ball_y - ball_radius <= 1 or ball_y + ball_radius >= screen_height:
        ball_speed_y *= -1

    # Ball out of bounds
    if ball_x - ball_radius <= 1 or ball_x + ball_radius >= screen_width:
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x *= random.choice([-1, 1])
        ball_speed_y *= random.choice([-1, 1])

    # Draw objects
    draw_objects()
    pygame.display.flip()

    # Adjust frame rate
    pygame.time.Clock().tick(60)

pygame.quit()

import pygame

# Initializing general varaibles
x = 0
y = 0
global box
box = 650 / 9
global grid
grid = [[[[0] * 3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
x0 = None
y0 = None


# Initializing
pygame.init()

# # Creating Screen
screen = pygame.display.set_mode((650, 800))

pygame.display.set_caption("ULTIMATE TIC-TAC-TOE")
img = pygame.image.load('ultimate.png')
pygame.display.set_icon(img)
x_img = pygame.image.load('x.png')
o_img = pygame.image.load('o.png')
font2 = pygame.font.SysFont("comicsans", 40)

def get_cord(pos):
    x = pos[0] // box
    y = pos[1] // box
    return (int(x), int(y))

def draw_box(x, y):
    if x == None and y == None:
        return
    for i in range(2):
        pygame.draw.line(screen, (223, 0, 0), (x * box * 3, (y + i) * box * 3), (x * box * 3 + box * 3, (y + i) * box * 3), 4)
        pygame.draw.line(screen, (223, 0, 0), ((x + i) * box * 3, y * box * 3), ((x + i) * box * 3, y * box * 3 + box * 3), 4)

def draw_ultimate():
    for i in range (3):
        for j in range (3):
            if grid[i][j] == 2:
                Rect = pygame.Rect(3 * i * box, j * 3 * box, 3 * box, 3 * box)
                pygame.draw.rect(screen, (250, 0, 0), Rect)
                # pygame.display.flip()
                continue
            if grid[i][j] == 1:
                Rect = pygame.Rect(3 * i * box, j * 3 * box, 3 * box, 3 * box)
                pygame.draw.rect(screen, (0, 0, 0), Rect)
                # pygame.display.flip()
                continue
            for p in range (3):
                for q in range (3):
                    # Fill gird with signs specified
                    if grid[i][j][p][q] == 2:
                        screen.blit(x_img, ((3 * i + p) * box + box/15, (3 * j + q) * box + box/15))
                    if grid[i][j][p][q] == 1:
                        screen.blit(o_img, ((3 * i + p) * box + box/15, (3 * j + q) * box + box/15))
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, (223, 223, 0), (box * i, 0), (box * i, 9 * box), 5)
            pygame.draw.line(screen, (223, 223, 0), (0, box * i), (9 * box, box * i), 5)
        else:
            pygame.draw.line(screen, (223, 223, 0), (0, box * i), (9 * box, box * i), 3)
            pygame.draw.line(screen, (223, 223, 0), (box * i, 0), (box * i, 9 * box), 3)

def update_game(val, val_in):
    x = val[0]
    y = val[1]
    x0 = x // 3
    y0 = y // 3
    x = x % 3
    y = y % 3
    if val_in:
        grid[x0][y0][x][y] = val_in % 2 + 1

def check(matrix):
    c = 0
    if (matrix[0][0] == 1 or matrix[0][0] == 2) and matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2]:
        c = 1
    elif (matrix[0][0] == 1 or matrix[0][0] == 2) and matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]:
        c = 1
    elif (matrix[0][0] == 1 or matrix[0][0] == 2) and matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0]:
        c = 1
    elif (matrix[0][1] == 1 or matrix[0][1] == 2) and matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1]:
        c = 1
    elif (matrix[1][0] == 1 or matrix[1][0] == 2) and matrix[1][0] == matrix[1][1] and matrix[1][0] == matrix[1][2]:
        c = 1
    elif (matrix[0][2] == 1 or matrix[0][2] == 2) and matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2]:
        c = 1
    elif (matrix[2][0] == 1 or matrix[2][0] == 2) and matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2]:
        c = 1
    elif (matrix[0][2] == 1 or matrix[0][2] == 2) and matrix[0][2] == matrix[1][1] and matrix[0][2] == matrix[2][0]:
        c = 1
    if c == 1:
        return True
    return False

# # Support variables for the Game loop
run = True
val = None
val_in = 0
end = 0
# # Main Game loop
while run:
    # White Background 
    screen.fill((255, 255, 255))

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and end == 0:
            pos = pygame.mouse.get_pos()
            (x, y) = get_cord(pos)

            if x >= 9 or y >= 9 or grid[x // 3][y // 3] == 1 or grid[x // 3][y // 3] == 2 or grid[x // 3][y // 3][x % 3][y % 3] != 0:
                continue

            # elif x0 == None and y0 == None and grid[x // 3][y // 3][x % 3][y % 3] == 0:
            elif x0 == None and y0 == None:
                val = [x, y]
                val_in += 1
                update_game(val, val_in)
                if check(grid[x // 3][y // 3]):
                    grid[x // 3][y // 3] = val_in % 2 + 1
                if grid[x % 3][y % 3] == 1 or grid[x % 3][y % 3] == 2:
                    x0 = None
                    y0 = None
                else:
                    x0 = x % 3
                    y0 = y % 3
                
            # elif  x < 3 * x0 + 3 and x >= 3 * x0 and y < 3 * y0 + 3 and y >= 3 * y0 and grid[x // 3][y // 3][x % 3][y % 3] == 0:
            elif  x < 3 * x0 + 3 and x >= 3 * x0 and y < 3 * y0 + 3 and y >= 3 * y0:
                val = [x, y]
                val_in += 1
                update_game(val, val_in)
                if check(grid[x0][y0]):
                    grid[x0][y0] = val_in % 2 + 1
                if grid[x % 3][y % 3] == 1 or grid[x % 3][y % 3] == 2:
                    x0 = None
                    y0 = None
                else:
                    x0 = x % 3
                    y0 = y % 3
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
    draw_ultimate()
    if check(grid):
        end = 1
        if val_in % 2 == 0:
            text1 = font2.render("Congratulations Player 1 won", 1, (0, 0, 0))
            screen.blit(text1, (20, 680))
        else:
            text1 = font2.render("Congratulations Player 2 won", 1, (0, 0, 0))
            screen.blit(text1, (20, 680))
        
        text0 = font2.render("Game Over !", 1, (0, 0, 0))
        screen.blit(text0, (20, 720)) 
        text3 = font2.render("Press 'Q' to quit the game", 1, (0, 0, 0))
        screen.blit(text3, (20, 760))

    else:
        draw_box(x0, y0)
        if val_in % 2 != 0:
            text2 = font2.render("Player 2 turn", 1, (0, 0, 0))
            screen.blit(text2, (20, 680))
            screen.blit(o_img, (200, 660))
            text3 = font2.render("Press 'Q' to quit the game", 1, (0, 0, 0))
            screen.blit(text3, (20, 750))
        else:
            text2 = font2.render("Player 1 turn", 1, (0, 0, 0))
            screen.blit(text2, (20, 680))
            screen.blit(x_img, (200, 660))
            text3 = font2.render("Press 'Q' to quit the game", 1, (0, 0, 0))
            screen.blit(text3, (20, 750))
    pygame.display.update()
pygame.quit()
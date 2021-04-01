# FOLLOWING CODE IS A GUI BASED n x n SUDOKU SOLVER ALONG WITH BACKTRACKING ALGORITHM VISUALISATION

import pygame
import math

# Input the size of the sudoku
while True:
    global n2
    n2 = int(input('Enter the Size of the sudoku: '))
    if  n2 == int(math.sqrt(n2)) * int(math.sqrt(n2)) and n2 != 0:
        print('Valid Input', n2)
        break
    elif n2 == 0:
        print('Forcefully terminated')
        break

# Initializing general varaibles
x = 0
y = 0
global box
box = 600 / n2
n = int(math.sqrt(n2))
global grid
if n2 == 4:
    grid = [
        [4, 0, 0, 3],
        [0, 2, 1, 0],
        [0, 3, 4, 0],
        [1, 0, 0, 0]
    ]
elif n2 == 9:
    grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
else:
    grid = [[0] * n2 for _ in range(n2)]

        


# Initializing
pygame.init()

# # Creating Screen
screen = pygame.display.set_mode((600, 800))

pygame.display.set_caption("SUDOKU SOLVER")
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)
font1 = pygame.font.SysFont("comicsans", int((40 / 66.66) * box))
font2 = pygame.font.SysFont("comicsans", 20)

def get_cord(pos):
    x = pos[0] // box
    y = pos[1] // box
    return (int(x), int(y))

def draw_box(x, y):
    for i in range(2):
        pygame.draw.line(screen, (223, 0, 0), (x * box, (y + i) * box), (x * box + box, (y + i) * box), 5)
        pygame.draw.line(screen, (223, 0, 0), ( (x + i)* box, y * box), ((x + i) * box, y * box + box), 5)

def draw_sudoku(x, y, err):
    for i in range (n2):
        for j in range (n2):
            if grid[i][j]!= 0:
                # Fill blue color in already numbered grid
                if err == True and i == x and j == y:
                    pygame.draw.rect(screen, (255, 0, 0), (i * box, j * box, box + 1, box + 1))
                else:
                    pygame.draw.rect(screen, (0, 150, 150), (i * box, j * box, box + 1, box + 1))
  
                # Fill gird with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * box + (box / 2.5), j * box + (box / 3)))
    for i in range(n2 + 1):
        if i % n == 0:
            pygame.draw.line(screen, (0, 0, 0), (box * i, 0), (box * i, n2 * box), 5)
            pygame.draw.line(screen, (0, 0, 0), (0, box * i), (n2 * box, box * i), 5)
        else:
            pygame.draw.line(screen, (0, 0, 0), (0, box * i), (n2 * box, box * i), 3)
            pygame.draw.line(screen, (0, 0, 0), (box * i, 0), (box * i, n2 * box), 3)

def check_sudoku(x, y):
    val = grid[x][y]
    for i in range(n2):
        if i == y or val == 0:
            continue
        if grid[x][i] == val:
            return False
    for i in range(n2):
        if i == x or val == 0:
            continue
        if grid[i][y] == val:
            return False
    i = x // n
    j = y // n
    for k in range(i * n, i * n + n):
        for l in range (j * n, j * n + n):
            if (k == x and l == y) or val == 0:
                continue
            if grid[k][l] == val:
                return False
    return True

def sudoku_solve(x, y):
    if x == n2 - 1 and y == n2:
        return True
    if y == n2:
        y = 0
        x += 1
    if grid[x][y] != 0:
        return sudoku_solve(x, y + 1)
        if delay == 1:
            pygame.event.pump()
    for i in range(1, n2 + 1):
        grid[x][y] = i
        if check_sudoku(x, y) == True:
            if delay == 1:
                screen.fill((255, 255, 255))
                draw_sudoku(x, y, True)
                pygame.display.update()
                pygame.time.delay(20)
            if sudoku_solve(x, y + 1) == True:
                return True
            if delay == 1:
                screen.fill((255, 255, 255))
                draw_sudoku(x, y, True)
                pygame.display.update()
                pygame.time.delay(50) 
        grid[x][y] = 0
    return False

# Support variables for the Game loop
run = True
box_select = 0
val = 0
global delay
delay = 0

# Main Game loop
while run:
    # White Background 
    screen.fill((255, 255, 255))

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            (x, y) = get_cord(pos)
            if x < n2 and y < n2 and x >= 0 and y >= 0:
                box_select = 1
            else:
                box_select = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            if event.key == pygame.K_LEFT:
                x -= 1
                box_select = 1
                if x < 0:
                    x = 0
            if event.key == pygame.K_RIGHT:
                x += 1
                box_select = 1
                if x >= n2:
                    x = n2 - 1
            if event.key == pygame.K_UP:
                y -= 1
                box_select = 1
                if y < 0:
                    y = 0
            if event.key == pygame.K_DOWN:
                y += 1
                box_select = 1
                if y >= n2:
                    y = n2 - 1
            if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                grid[x][y] = 0   
            if event.key == pygame.K_1:
                grid[x][y] = 1
            if event.key == pygame.K_2:
                grid[x][y] = 2    
            if event.key == pygame.K_3:
                grid[x][y] = 3
            if event.key == pygame.K_4:
                grid[x][y] = 4
            if event.key == pygame.K_5:
                grid[x][y] = 5
            if event.key == pygame.K_6:
                grid[x][y] = 6 
            if event.key == pygame.K_7:
                grid[x][y] = 7
            if event.key == pygame.K_8:
                grid[x][y] = 8
            if event.key == pygame.K_9:
                grid[x][y] = 9
            if event.key == pygame.K_RETURN:
                sudoku = grid
                if sudoku_solve(0, 0) == False:
                    text5 = font2.render("NO SOLUTION EXISTS FOR THE ENTERED SUDOKU", 1, (0, 0, 0))
                    screen.blit(text5, (20, 750))
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                delay = 1
                if sudoku_solve(0, 0) == False:
                    text5 = font2.render("NO SOLUTION EXISTS FOR THE ENTERED SUDOKU", 1, (0, 0, 0))
                    screen.blit(text5, (20, 750))
            if event.key == pygame.K_p:
                box_select = 0
                val = 0
                delay = 0
                grid = [[0] * n2 for _ in range(n2)]
            if event.key == pygame.K_a:
                box_select = 0
                val = 0
                delay = 0
                if n2 == 4:
                    grid = [
                        [4, 0, 0, 3],
                        [0, 2, 1, 0],
                        [0, 3, 4, 0],
                        [1, 0, 0, 0]
                    ]
                elif n2 == 9:
                    grid =[
                        [7, 8, 0, 4, 0, 0, 1, 2, 0],
                        [6, 0, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 0, 6, 0, 1, 0, 7, 8],
                        [0, 0, 7, 0, 4, 0, 2, 6, 0],
                        [0, 0, 1, 0, 5, 0, 9, 3, 0],
                        [9, 0, 4, 0, 6, 0, 0, 0, 5],
                        [0, 7, 0, 3, 0, 0, 0, 1, 2],
                        [1, 2, 0, 0, 0, 7, 4, 0, 0],
                        [0, 4, 9, 2, 0, 6, 0, 0, 7]
                    ]

    if check_sudoku(x, y) == True:
        err = False
    else:
        err = True
    draw_sudoku(x, y, err)
    if box_select == 1:
        draw_box(x, y)

    # Instructions
    text1 = font2.render("PRESS A TO RESET TO DEFAULT or P TO EMPTY THE SUDOKU", 1, (0, 0, 0))
    text2 = font2.render("ENTER AND DELETE VALUES AND CUSTOMIZE YOUR SUDOKU", 1, (0, 0, 0))
    text3 = font2.render("PRESS ENTER TO DIRECTLY DISPLAY THE ANSWER", 1, (0, 0, 0))
    text4 = font2.render("PRESS SHIFT TO VIEW THE BACKTRACKING ALGORITHM APPLIED", 1, (0, 0, 0))
    screen.blit(text1, (20, 630))        
    screen.blit(text2, (20, 660))
    screen.blit(text3, (20, 690))        
    screen.blit(text4, (20, 720))

    pygame.display.update()
pygame.quit()
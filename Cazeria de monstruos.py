#pgzero
import random

TITLE = "Cazeria de monstruos"
FPS = 60
time_elapsed = 15
spawn_interval = 9

cell = Actor('default')
sand = Actor('sand')
brick = Actor('brick')
lbrick = Actor('leftbrick')
rbrick = Actor('rightbrick')
rwall = Actor('rightwall')
lwall = Actor('leftwall')
downwall = Actor('wall')
bdlc = Actor('bdownlcorner')
bdrc = Actor('bdownrcorner')
src = Actor('smallrcorner')
slc = Actor('smalllcorner')
blc = Actor('biglcorner')
brc = Actor('bigrcorner')
wall = Actor('downwall')
dirt = Actor('dirt')
shadowsand = Actor('shadowsand')
shadowsand2 = Actor('shadowsand2')
sand2 = Actor('sand2')
singledoor = Actor('singledoor')
leftdoor = Actor('leftdoor')
rightdoor = Actor('rightdoor')
prisonwall = Actor('prisonwall')
flagwall = Actor('flagwall')
fountain1 = Actor('fountain1')
fountain2 = Actor('fountain2')
spikes = Actor('spikes')
roofrcorner = Actor('roofrcorner')

button1 = Actor('bonus', (150, 210))
button2 = Actor('bonus', (400, 210))
button3 = Actor('bonus', (650, 210))

desierto = Actor('desierto')

cross = Actor('cross', (775, 25))

info1 = Actor('info', (150, 275))
info2 = Actor('info', (400, 275))
info3 = Actor('info', (650, 275))

titulo1 = Actor('info2', (400, 100))
titulo1_1 = Actor('info2', (400, 50))
titulo1_2 = Actor('info2', (400, 50))
titulo2 = Actor('info3', (400, 100))
titulo3 = Actor('info4', (400, 150))
titulo4 = Actor('info4', (400, 225))
titulo5 = Actor('info4', (400, 300))
titulo6 = Actor('info4', (400, 375))

part1 = Actor('part1', (505,35))
part2 = Actor('part2' , (368,111))
part3 = Actor('part3',(210,40))
part8 = Actor('part8' , (735,194))
part9 = Actor('part9',(729,230))

character = Actor('character1')

size_w = 50
size_h = 26

WIDTH  = cell.width * size_w
HEIGHT = cell.height * size_h
TITLE = "Cazeria de enemigos"
FPS = 30
modo = 'menu'
win = 0

my_map = [
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 18, 1, 18, 1, 18, 12, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 0],
          [0, 18, 1, 18, 1, 18, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 0],
          [0, 1, 18, 1, 18, 1, 18, 5, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 6, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 0],
          [0, 18, 1, 18, 1, 18, 1, 5, 0, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 0],
          [0, 1, 18, 1, 18, 1, 18, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 15, 0, 15, 11, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 1, 18, 1, 18, 1, 12, 14, 14, 14, 14, 14, 13, 0],
          [0, 18, 1, 18, 1, 18, 1, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 10, 0, 0, 15, 0, 15, 0, 6, 2, 23, 22, 23, 19, 23, 22, 23, 2, 4, 18, 1, 18, 1, 18, 5, 0, 0, 0, 0, 0, 6, 0],
          [0, 1, 18, 1, 18, 1, 18, 3, 24, 24, 23, 22, 23, 19, 23, 22, 23, 24, 24, 5, 0, 15, 0, 15, 0, 15, 6, 26, 17, 26, 17, 16, 17, 16, 26, 16, 26, 1, 18, 1, 18, 1, 5, 0, 15, 0, 15, 0, 6, 0],
          [0, 18, 1, 18, 1, 18, 1, 17, 25, 25, 16, 17, 16, 17, 16, 17, 16, 25, 25, 5, 0, 0, 15, 0, 15, 0, 6, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 5, 0, 0, 15, 0, 0, 6, 0],
          [0, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 5, 0, 15, 0, 15, 0, 15, 6, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 5, 0, 15, 0, 15, 0, 6, 0],
          [0, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 5, 0, 0, 15, 0, 15, 0, 6, 18, 1, 18, 1, 12, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 27, 0, 0, 15, 0, 0, 6, 0],
          [0, 12, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 18, 1, 18, 1, 18, 5, 0, 0, 0, 0, 0, 0, 6, 1, 18, 1, 18, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 15, 0, 6, 0],
          [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 18, 1, 18, 1, 8, 7, 7, 7, 7, 7, 7, 9, 18, 1, 18, 1, 5, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 0, 6, 0],
          [0, 5, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 6, 18, 1, 18, 1, 18, 3, 22, 23, 20, 21, 23, 22, 4, 1, 18, 1, 18, 5, 0, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 15, 0, 6, 0],
          [0, 5, 0, 0, 0, 0, 0, 0, 11, 7, 7, 7, 7, 9, 1, 18, 1, 18, 1, 26, 16, 17, 16, 17, 16, 17, 26, 18, 1, 18, 1, 5, 0, 0, 0, 0, 0, 0, 0, 15, 0, 15, 0, 15, 0, 15, 0, 0, 6, 0],
          [0, 8, 7, 7, 10, 0, 0, 0, 6, 2, 23, 19, 23, 4, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 8, 7, 7, 7, 7, 7, 10, 0, 0, 15, 0, 15, 0, 15, 0, 15, 0, 6, 0],
          [0, 3, 24, 24, 5, 0, 15, 0, 6, 26, 16, 17, 16, 26, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 3, 23, 20, 21, 23, 2, 5, 0, 15, 0, 15, 0, 15, 0, 15, 0, 0, 6, 0],
          [0, 17, 25, 25, 8, 7, 7, 7, 9, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 26, 17, 16, 17, 16, 26, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0],
          [0, 18, 1, 18, 3, 23, 19, 23, 4, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 3, 23, 22, 23, 2, 20, 21, 2, 23, 22, 23, 4, 0],
          [0, 1, 18, 1, 26, 16, 17, 16, 26, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 26, 17, 26, 17, 16, 17, 16, 17, 16, 26, 16, 26, 0],
          [0, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 0],
          [0, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

char1 = Actor('character1',(WIDTH//2,HEIGHT//2+20))
char1.health = 1000
char1.attack = 50
char1_2 = Actor('character1_2', (150, 350))
char1_3 = Actor('character1_3', (150, 280))

char2 = Actor('character2',(WIDTH//2,HEIGHT//2+20))
char2.health = 500
char2.attack = 100
char2_2 = Actor('character2_2', (400, 350))
char2_3 = Actor('character2_3', (400, 280))

char3 = Actor('character3', (WIDTH//2,HEIGHT//2+20))
char3.health = 750
char3.attack = 75
char3_2 = Actor('character3_2', (650, 350))
char3_3 = Actor('character3_3', (650, 280))

personajes = [char1,char2,char3]
personaje_aleatorio = random.randint(0,2)
enemies = []

def duplicate_enemies(enemies):
    global time_elapsed
    time_elapsed += 1
 
    if time_elapsed >= spawn_interval * FPS:
        if len(enemies) < 20:
            x = random.randint(1, 48) * cell.width
            y = random.randint(1, 21) * cell.height
            new_enemy = Actor("enemy1", topleft=(x, y))
            new_enemy.health = random.randint(50, 100)
            new_enemy.attack = random.randint(10, 25)
            enemies.append(new_enemy)
 
        time_elapsed = 0

def mover_enemigos(enemies):
    for enemy in enemies:
        direction = random.choice(['up', 'down', 'left', 'right'])
        movement_amount = random.randint(1, 2)
        if direction == 'up':
            enemy.y -= movement_amount
        elif direction == 'down' :
            enemy.y += movement_amount
        elif direction == 'left':
            enemy.x -= movement_amount
        elif direction == 'right':
            enemy.x += movement_amount

for i in range(5):
    x = random.randint(1, 48) * cell.width
    y = random.randint(1, 21) * cell.height
    enemy1 = Actor("enemy1", topleft = (x, y))
    enemy1.health = random.randint(100, 150)
    enemy1.attack = random.randint(25, 50)
    enemies.append(enemy1)
         
def draw_map():
    for x in range(len(my_map)):
        for y in range(len(my_map[0])):
            if my_map[x][y] == 0:
                cell.left = cell.width * y
                cell.top = cell.height * x
                cell.draw()
            elif my_map[x][y] == 1:
                sand.left = sand.width * y
                sand.top = sand.height * x
                sand.draw()
            elif my_map[x][y] == 2:
                brick.left = brick.width * y
                brick.top = brick.height * x
                brick.draw()
            elif my_map[x][y] == 3:
                lbrick.left = lbrick.width * y
                lbrick.top = lbrick.height * x
                lbrick.draw()
            elif my_map[x][y] == 4:
                rbrick.left = rbrick.width * y
                rbrick.top = rbrick.height * x
                rbrick.draw()
            elif my_map[x][y] == 5:
                rwall.left = rwall.width * y
                rwall.top = rwall.height * x
                rwall.draw()
            elif my_map[x][y] == 6:
                lwall.left = lwall.width * y
                lwall.top = lwall.height * x
                lwall.draw()
            elif my_map[x][y] == 7:
                downwall.left = downwall.width * y
                downwall.top = downwall.height * x
                downwall.draw()
            elif my_map[x][y] == 8:
                bdlc.left = bdlc.width * y
                bdlc.top = bdlc.height * x
                bdlc.draw()
            elif my_map[x][y] == 9:
                bdrc.left = bdrc.width * y
                bdrc.top = bdrc.height * x
                bdrc.draw()
            elif my_map[x][y] == 10:
                src.left = src.width * y
                src.top = src.height * x
                src.draw()
            elif my_map[x][y] == 11:
                slc.left = slc.width * y
                slc.top = slc.height * x
                slc.draw()
            elif my_map[x][y] == 12:
                blc.left = blc.width * y
                blc.top = blc.height * x
                blc.draw()
            elif my_map[x][y] == 13:
                brc.left = brc.width * y
                brc.top = brc.height * x
                brc.draw()
            elif my_map[x][y] == 14:
                wall.left = wall.width * y
                wall.top = wall.height * x
                wall.draw()
            elif my_map[x][y] == 15:
                dirt.left = dirt.width * y
                dirt.top = dirt.height * x
                dirt.draw()
            elif my_map[x][y] == 16:
                shadowsand.left = shadowsand.width * y
                shadowsand.top = shadowsand.height * x
                shadowsand.draw()
            elif my_map[x][y] == 17:
                shadowsand2.left = shadowsand2.width * y
                shadowsand2.top = shadowsand2.height * x
                shadowsand2.draw()
            elif my_map[x][y] == 18:
                sand2.left = sand2.width * y
                sand2.top = sand2.height * x
                sand2.draw()
            elif my_map[x][y] == 19:
                singledoor.left = singledoor.width * y
                singledoor.top = singledoor.height * x
                singledoor.draw()
            elif my_map[x][y] == 20:
                leftdoor.left = leftdoor.width * y
                leftdoor.top = leftdoor.height * x
                leftdoor.draw()
            elif my_map[x][y] == 21:
                rightdoor.left = rightdoor.width * y
                rightdoor.top = rightdoor.height * x
                rightdoor.draw()
            elif my_map[x][y] == 22:
                prisonwall.left = prisonwall.width * y
                prisonwall.top = prisonwall.height * x
                prisonwall.draw()
            elif my_map[x][y] == 23:
                flagwall.left = flagwall.width * y
                flagwall.top = flagwall.height * x
                flagwall.draw()
            elif my_map[x][y] == 24:
                fountain1.left = fountain1.width * y
                fountain1.top = fountain1.height * x
                fountain1.draw()
            elif my_map[x][y] == 25:
                fountain2.left = fountain2.width * y
                fountain2.top = fountain2.height * x
                fountain2.draw()
            elif my_map[x][y] == 26:
                spikes.left = spikes.width * y
                spikes.top = spikes.height * x
                spikes.draw()
            elif my_map[x][y] == 27:
                roofrcorner.left = roofrcorner.width * y
                roofrcorner.top = roofrcorner.height * x
                roofrcorner.draw()
                
def draw():
    screen.fill("#2f3542")
    
    if modo == 'menu':
        desierto.draw()
        button1.draw()
        button2.draw()
        button3.draw()
        titulo1.draw()
        screen.draw.text("JUGAR", center=(400, 205), color = 'black', fontsize = 30)
        screen.draw.text("ESTADISTICAS", center=(150, 205), color = 'black', fontsize = 20)
        screen.draw.text("CONTROLES", center=(650, 205), color = 'black', fontsize = 25)
        screen.draw.text("CAZERIA DE MONSTRUOS", center=(400, 100), color = 'white', fontsize = 40)
        
    elif modo == 'game':
        draw_map()
        personajes[personaje_aleatorio].draw()
        screen.draw.text("DERROTA A TODOS LOS ENEMIGOS PARA GANAR", center=(400, 390), color = 'white', fontsize = 30)
        for i in range(len(enemies)):
            enemies[i].draw()
            
    elif modo == 'stats':
        desierto.draw()
        info1.draw()
        info2.draw()
        info3.draw()
        titulo2.draw()
        cross.draw()
        char1_2.draw()
        char2_2.draw()
        char3_2.draw()
        screen.draw.text("ESTADÍSTICAS DE LOS PERSONAJES", center=(400, 100), color = 'white', fontsize = 40)
        screen.draw.text("HECHICERO", center=(150, 185), color = 'white', fontsize = 25)
        screen.draw.text("Salud:", center=(100, 225), color = 'white', fontsize = 20)
        screen.draw.text(char1.health, center=(200, 225), color = 'white', fontsize = 20)
        screen.draw.text("Ataque:", center=(100, 275), color = 'white', fontsize = 20)
        screen.draw.text(char1.attack, center=(200, 275), color = 'white', fontsize = 20)
        screen.draw.text("CABALLERO", center=(400, 185), color = 'white', fontsize = 25)
        screen.draw.text("Salud:", center=(350, 225), color = 'white', fontsize = 20)
        screen.draw.text(char2.health, center=(450, 225), color = 'white', fontsize = 20)
        screen.draw.text("Ataque:", center=(350, 275), color = 'white', fontsize = 20)
        screen.draw.text(char2.attack, center=(450, 275), color = 'white', fontsize = 20)
        screen.draw.text("AVENTURERO", center=(650, 185), color = 'white', fontsize = 25)
        screen.draw.text("Salud:", center=(600, 225), color = 'white', fontsize = 20)
        screen.draw.text(char3.health, center=(700, 225), color = 'white', fontsize = 20)
        screen.draw.text("Ataque:", center=(600, 275), color = 'white', fontsize = 20)
        screen.draw.text(char3.attack, center=(700, 275), color = 'white', fontsize = 20)
        
    elif modo == 'controls':
        desierto.draw()
        cross.draw()
        titulo1_2.draw()
        titulo3.draw()
        titulo4.draw()
        titulo5.draw()
        titulo6.draw()
        screen.draw.text("CONTROLES DEL JUEGO", center=(400, 50), color = 'white', fontsize = 40)
        screen.draw.text("W = te mueves hacia arriba", center=(400, 150), color = 'white', fontsize = 30)
        screen.draw.text("S = te mueves hacia abajo", center=(400, 225), color = 'white', fontsize = 30)
        screen.draw.text("A = te mueves hacia la izquierda", center=(400, 300), color = 'white', fontsize = 27)
        screen.draw.text("D = te mueves hacia la derecha", center=(400, 375), color = 'white', fontsize = 27)
        
    elif mode == "end":
        desierto.draw()
        if win == 1:
            screen.draw.text("¡LO LOGRASTE!", center=(400, 200), color = 'black', fontsize = 40)
    
def on_key_down(key):
    old_x = personajes[personaje_aleatorio].x
    old_y = personajes[personaje_aleatorio].y
 
    if keyboard.d :
        personajes[personaje_aleatorio].x += cell.width
    elif keyboard.a:
        personajes[personaje_aleatorio].x -= cell.width
    elif keyboard.s:
        personajes[personaje_aleatorio].y += cell.height
    elif keyboard.w:
        personajes[personaje_aleatorio].y -= cell.height
 
    enemy_index = personajes[personaje_aleatorio].collidelist(enemies)
 
    if enemy_index != -1 :
        personajes[personaje_aleatorio].x = old_x
        personajes[personaje_aleatorio].y = old_y
 
        enemy1 = enemies[enemy_index]
        enemy1.health -= personajes[personaje_aleatorio].attack
        personajes[personaje_aleatorio].health -= enemy1.attack
 
        if enemy1.health <= 0:
            enemies.pop(enemy_index)
    
    if enemy_index != -1 or char1.colliderect(part3):
        char1.x = old_x
        char1.y = old_y
        
        enemy1 = enemies[enemy_index]
        enemy1.health -= char1.attack
        char1.health -= enemy1.attack
        
        if enemy1.health <= 0:
            enemies.pop(enemy_index)
            
def victory():
    global mode, win
    if enemies == []:
        mode = "end"
        win = 1

def update(dt):
    mover_enemigos(enemies)
    duplicate_enemies(enemies)

def on_mouse_down(button, pos):
    global modo
    if modo == 'menu':
        if button2.collidepoint(pos):
            modo = 'game'
        elif button1.collidepoint(pos):
            modo = 'stats'
        elif button3.collidepoint(pos):
            modo = 'controls'
    elif cross.collidepoint(pos):
        modo = 'menu'

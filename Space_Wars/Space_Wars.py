import pygame
import random
import math
_ANCHO = 1000
_ALTO = 700
_LIVESPLAYER = 3
enemigos = 7
_LEVEL = 0

###### IMAGES ########

backgroundImage = pygame.image.load("background.jpg")
shipImage = pygame.image.load("ship.png")
enemyImage = pygame.image.load("enemy.png")
loseImage = pygame.image.load("lose.png")
bala = pygame.image.load("bullet.png")

######## SHIP ########
ship = {
    "pos" : [_ANCHO // 2, _ALTO - 50],
    "tamaño" : list(shipImage.get_size()),
    "color" : [87,35,100],
    "vel" : 5,
    "cooldown" : 15,
    "firewait" : 0,
    "respawncooldown" : 180,
    "respawnwait" : 0,
    "lives" : _LIVESPLAYER,
    "image" : shipImage
    }

def shipDraw(window,ship):
    """Se encarga de dibujar la nave en la ventana"""
    x = ship["pos"][0] - ship["tamaño"][0] // 2
    y = ship["pos"][1] - ship["tamaño"][1] // 2
    window.blit(ship["image"], [x,y] + ship["tamaño"])
    
def shipMoveRight(ship):
    if ship["respawnwait"] == 0:
        ship["pos"][0] = min(ship["pos"][0] + ship["vel"], _ANCHO -ship["tamaño"][0]// 2)
                         
def shipMoveLeft(ship):
    if ship["respawnwait"] == 0:
        ship["pos"][0] = max(ship["pos"][0] - ship["vel"] ,ship["tamaño"][0]// 2)

def shipFire(ship):
    if ship["firewait"] <= 0 and ship["respawnwait"] == 0:
        bullet = {
            "pos" : [ship["pos"][0], ship["pos"][1] - ship["tamaño"][1] // 2],
            "vel" : -20,
            "color" : bala,
            "radio" : 2
            }
        bullets.append(bullet)
        ship["firewait"] = ship["cooldown"]

def shipUpdate(ship):
    ship["firewait"] -= 1
    if ship["respawnwait"] > 0:
        ship["pos"][0] = -100
        ship["respawnwait"] -= 1
        if ship["respawnwait"] == 0:
            ship["pos"][0] = _ANCHO // 2 

def shipDeath(ship):
    ship["lives"] -= 1
    ship["respawnwait"] = ship["respawncooldown"]
    
########## BULLETS #########
bullets = []
def bulletUpdate(bullet):
    bullet["pos"][1] += bullet["vel"]

def bulletDraw(window,bullet):
    window.blit(bala,(bullet["pos"]))
    
def bulletsDraw(window, bullets):
    for b in bullets:
        bulletDraw(window, b)

def bulletsUpdate(bullets):
    for b in bullets:
        if b["pos"][1] < 0:
            bullets.remove(b)
        if b["pos"][1] > _ALTO:
            bullets.remove(b)
        else:
            bulletUpdate(b)

######### ENEMIES #########
enemies = []
enemyBullets = []
def enemyCreate(pos, w, h):
    enemy = {
        "pos" : pos[:],
        "tamaño" : [w,h],
        "color" : (0,123,35),
        "vel" : random.choice([3, -3]),
        "dirchangeprob" : 2,
        "time" : random.randrange(5),
        "timeinc" : 0.05,
        "firerate" : 120,
        "firewait" : random.randrange(60),
        "image" : enemyImage
        }
    enemies.append(enemy)
    
def enemyDraw(window, enemy):
    x = enemy["pos"][0] - enemy["tamaño"][0] //2
    y = enemy["pos"][1] - enemy["tamaño"][1] //2
    window.blit(enemy["image"], [x,y] + enemy["tamaño"])

def enemiesDraw(window, enemies):
    for e in enemies:
        enemyDraw(window, e)

def enemiesCreate(enemigos):
    for i in range(enemigos):
        pos = [random.randint(20,_ANCHO - 20), random.randint(0, int(_ALTO * 2/3))]
        enemyCreate(pos, 20, 20)

def enemyIsHit(enemy, bullet):
    x1 = enemy["pos"][0] - enemy["tamaño"][0] // 2 + bullet["radio"]
    x2 = enemy["pos"][0] + enemy["tamaño"][0] // 2 + bullet["radio"]
    y1 = enemy["pos"][1] - enemy["tamaño"][1] // 2 + bullet["radio"]
    y2 = enemy["pos"][1] + enemy["tamaño"][1] // 2 + bullet["radio"]
    return x1 <= bullet["pos"][0] <= x2 and y1 <= bullet["pos"][1] <= y2

def checkEnemyCollisions(enemies, bullets):
    for e in enemies:
        for b in bullets:
            if enemyIsHit(e,b):
                enemies.remove(e)
                bullets.remove(b)
                
def enemyLeftBorderTouch(enemy):
    if enemy["pos"][0] < enemy["tamaño"][0] // 2:
        return True
    return False

def enemyRightBorderTouch(enemy):
    if enemy["pos"][0] > _ANCHO - enemy["tamaño"][0] // 2:
        return True
    return False

def enemyUpdate(enemy):
    if enemyRightBorderTouch(enemy) and enemy["vel"] > 0:
        enemy["vel"] *= -1
    if enemyLeftBorderTouch(enemy) and enemy["vel"] < 0:
        enemy["vel"] *= -1
    if random.randrange(100) < enemy["dirchangeprob"]:
        enemy["vel"] *= -1
    enemy["pos"][0] += enemy["vel"]
    minY = enemy["tamaño"][1] // 2
    newY = enemy["pos"][1] + math.sin(enemy["time"])
    enemy["pos"][1] = max(minY, newY)
    enemy["time"] += enemy["timeinc"]

    if enemy["firewait"] <= 0:
        enemyFire(enemy)
        enemy["firewait"] = enemy["firerate"]
    else:
        enemy["firewait"] -= 1
        
def enemiesUpdate(enemies):
    for e in enemies:
        enemyUpdate(e)

def enemyFire(enemy):
    balas = {
        "pos" : [enemy["pos"][0], enemy["pos"][1] + enemy["tamaño"][1] // 2],
        "vel" : 5,
        "radio" : 3,
        "color" : (0,255,0)
        }
    enemyBullets.append(balas)

######## COLLISIONS ######
def checkEnemyCollisions(enemies, bullets):
    for e in enemies:
        for b in bullets:
            if enemyIsHit(e,b):
                enemies.remove(e)
                bullets.remove(b)

def checkShipCollisions(ship, enemyBullets):
    for b in enemyBullets:
        if enemyIsHit(ship, b):
            enemyBullets.remove(b)
            shipDeath(ship)
            
########## MAIN ###########
def main():
    """
    Juego de Space_Wars.
    #Jeramy Mairena Reyes
    """
    global enemigos
    global enemies
    global _LEVEL
    pygame.init()
    window = pygame.display.set_mode((_ANCHO,_ALTO))
    loop = True
    enemiesCreate(enemigos)
    
    while loop:
        pygame.time.delay(16)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            shipMoveLeft(ship)
        if keys[pygame.K_RIGHT]:
            shipMoveRight(ship)
        if keys[pygame.K_SPACE]:
            shipFire(ship)
        window.blit(backgroundImage, (0,0))
        if enemies == []:
            _LEVEL += 1
            enemigos += 2
            enemiesCreate(enemigos)
            ship["lives"] = 3
        checkEnemyCollisions(enemies, bullets)
        bulletsDraw(window,bullets)
        bulletsUpdate(bullets)
        bulletsDraw(window, enemyBullets)
        bulletsUpdate(enemyBullets)
        if ship["lives"] > 0:
            checkShipCollisions(ship, enemyBullets)
            shipDraw(window, ship)
            shipUpdate(ship)
        else:
            window.blit(loseImage, (_ANCHO // 4, _ALTO // 4))
            if keys[pygame.K_RETURN]:
                enemigos = enemigos - (_LEVEL * 2)
                enemies = []
                enemiesCreate(enemigos)
                ship["lives"] = _LIVESPLAYER
                shipDraw(window, ship)
        enemiesDraw(window, enemies)
        enemiesUpdate(enemies)
        pygame.display.update()
    pygame.quit()

main()
    

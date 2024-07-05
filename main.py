import pygame
import sys
import random
import pygame.locals

# simple cells
class Food():
    def __init__(self) -> None:
        pass
    def getState(self) -> str:
        return "food"
class DeadCell():
    def __init__(self) -> None:
        pass
    def getState(self) -> str:
        return "dead"
# cells with AI
class Herbivore():
    def __init__(self) -> None:
        pass
    def getState(self) -> str:
        return "herbivore"
class Predator():
    def __init__(self) -> None:
        pass
    def getState(self) -> str:
        return "predator"

class Grid():
    SPAWN_RARITY = 40
    colors = {
            "dead": (20, 20, 20), 
            "food": (0, 204, 0), 
            "predator": (255, 0, 0), 
            "herbivore": (255, 255, 0)
        }
    pixelSize = 2
    newFoodCount = 10
    def __init__(self, x, y) -> None:
        self.table = []
        for i in range(x):
            collumn = []
            for j in range(y):
                collumn.append(DeadCell())
            self.table.append(collumn)
    # print out for testing
    def print(self) -> None:
        for i in range(len(self.table[0])):
            row = ""
            for j in range(len(self.table)):
                row += f" {self.table[j][i].getState()}"
            print(row)
    def setCell(self, x, y, value) -> None:
        self.table[x][y] = value
    def getCell(self, x, y) -> int:
        return self.table[x][y].getState()
    def generateMap(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if random.randint(0, self.SPAWN_RARITY) == 0:
                    self.table[i][j] = random.choice([Food(), Herbivore(), Predator()])
    def draw(self, screen) -> None:
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                pygame.draw.rect(screen, self.colors[self.table[i][j].getState()], pygame.Rect(i*self.pixelSize, j*self.pixelSize, self.pixelSize, self.pixelSize))
    def update(self) -> None:
        table = self.table
        
        # get new food! yei!
        done = 0
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j].getState() == "dead":
                    if random.randint(1, len(table[i])*len(table)/self.newFoodCount) == 1:
                        if done < self.newFoodCount:
                            self.table[i][j] = Food()
                            done += 1
# window class, couse ewerything in main was gibberish(idk how to write the word). Thx, Nojau!
class Window():
    def __init__(self, width, height, fps=60) -> None:
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        self.clock.tick(self.fps)
        self.screen.fill((0, 0, 0))
    def getScreen(self) -> pygame.surface:
        return self.screen

if __name__ == "__main__":
    window = Window(1000, 800, 10)
    grid = Grid(200, 200)
    grid.generateMap()
    while True:
        grid.update()
        grid.draw(window.screen)
        window.update()
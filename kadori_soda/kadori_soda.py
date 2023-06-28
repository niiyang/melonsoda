from collections import deque, namedtuple
from random import randint
import pyxel

Point = namedtuple("Point", ["w", "h"])  # kadoriの向き

UP = Point(-16, 16)
DOWN = Point(16, 16)
RIGHT = Point(-16, 16)
LEFT = Point(16, 16)

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.load("my_resource.pyxres")
        self.direction = RIGHT

        # Score
        self.score = 0
        # Starting Point
        self.player_x = 42
        self.player_y = 60
        self.player_vy = 0
        self.soda = [(i * 60, randint(0, 104), True) for i in range(4)]
        self.sushi = [(i * 30, randint(0, 104), True) for i in range(4)] 

        # 音楽再生
        pyxel.playm(0, loop=True)

        #実行
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.update_player()

        for i, v in enumerate(self.soda):
            self.soda[i] = self.update_soda(*v)

    def update_player(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.player_x = max(self.player_x - 2, 0)
            self.direction = LEFT

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
            self.direction = RIGHT

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_UP):
            self.player_y = max(self.player_y - 2, 0)
            self.direction = UP

        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
            self.player_y = min(self.player_y + 2, pyxel.height - 16)
            self.direction = DOWN


    def draw(self):
        # bg color
        pyxel.cls(12)

        # draw melonsoda
        for x, y, is_active in self.soda:
            if is_active:
                pyxel.blt(x, y, 0, 16, 0, 16, 16, 0)

        # draw sushi
        for a, b, is_active in self.sushi:
            if is_active:
                pyxel.blt(a, b, 0, 32, 0, 16, 16, 0)

        # draw kadori
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            16 if self.player_vy > 0 else 0,
            0,
            self.direction[0],
            self.direction[1],
            1,
        )

        # スコアを表示
        s = "Score {:>4}".format(self.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)

    def update_soda(self, x, y, is_active):
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            is_active = False
            self.score += 100
            self.player_vy = min(self.player_vy, -8)
            pyxel.play(1,18,loop=False)

        x -= 2

        if x < -40:
            x += 240
            y = randint(0, 104)
            is_active = True

        return (x, y, is_active)

    def update_sushi(self, a, b, is_active):
        if is_active and abs(a - self.player_a) < 8 and abs(b - self.player_) < 8:
            is_active = False
            self.score += 300
            self.player_vy = min(self.player_vy, -8)
            pyxel.play(1,18,loop=False)

        a -= 2

        if a < -40:
            a += 240
            b = randint(0, 104)
            is_active = True

        return (a, b, is_active)
    
App()

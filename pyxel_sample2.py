import pyxel


class TextApp:
    def __init__(self):
        pyxel.init(160, 120, title="All Colors")
        self.count = 0
        self.old_list = pyxel.colors.to_list()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        if pyxel.frame_count % 30 == 0:
            y = 3
            pyxel.cls(7)
            self.count += 1
            new_list = []
            for idx in range(16):
                new_list.append(self.old_list[(self.count + idx) % 16])
            pyxel_table = [hex(x) for x in new_list]
            for idx, color in enumerate(pyxel_table):
                pyxel.text(55, y, color, (idx + self.count) % 16)
                y += 7


TextApp()

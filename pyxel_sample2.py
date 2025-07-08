import pyxel


class TextApp:
    def __init__(self):
        pyxel.init(160, 120, title="All Colors")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(7)
        pyxel_table = [hex(x) for x in pyxel.colors.to_list()]
        y = 3
        for idx, color in enumerate(pyxel_table):
            pyxel.text(55, y, color, idx)
            y += 7


TextApp()

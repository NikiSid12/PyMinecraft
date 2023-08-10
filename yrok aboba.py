from mcpi.minecraft import Minecraft

mc = Minecraft.create()

class Building:
    def __init__(self, weight, height, length, pos):
        self.pos = pos
        self.length = length
        self.height = height
        self.weight = weight
def build(self)
    x, y, z = self.pos
    mc.setBlocks(x, y, z,
                 x + self.weight,
                 y + self.height,
                 z + self.length, 1)
    mc.setBlocks(x + 1, y + 1, z + 1,
                 x + self.weight - 1,
                 y + self.height - 1,
                 z + self.length - 1, 0)

pos = mc.player.getTilepos()
ghost_house = Building(10, 6, 8, pos)
ghost_house.build()
sleep(15)
ghost_house.clear()


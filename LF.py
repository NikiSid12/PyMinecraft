from mcpi.minecraft import Minecraft
from random import randint

mc = Minecraft.create()

class Parfenon():
   def __init__(self, x, y, z, height):
       self.x = x
       self.y = y
       self.z = z
       self.height = height

   def column(self):
       mc.setBlocks(self.x, self.y, self.z,
                    self.x, self.y + self.height, self.z, 155)

   def base(self):
       mc.setBlocks(self.x - 1, self.y, self.z - 1,
                    self.x + 1, self.y, self.z + 1, 155)
       mc.setBlock(self.x - 1, self.y + 1, self.z, 156, 0)
       mc.setBlock(self.x + 1, self.y + 1, self.z, 156, 1)
       mc.setBlock(self.x, self.y + 1, self.z - 1, 156, 2)
       mc.setBlock(self.x, self.y + 1, self.z + 1, 156, 3)

   def capital(self):
       mc.setBlocks(self.x - 1, self.y + self.height,     self.z - 1,
                    self.x + 1, self.y + self.height,     self.z + 1, 155)
       mc.setBlock(self.x - 1,  self.y + self.height - 1, self.z, 156, 4)
       mc.setBlock(self.x + 1,  self.y + self.height - 1, self.z, 156, 5)
       mc.setBlock(self.x,      self.y + self.height - 1, self.z - 1, 156, 6)
       mc.setBlock(self.x,      self.y + self.height - 1, self.z + 1, 156, 7)

   def build_column(self):
       self.base()
       self.column()
       self.capital()

   def build_all_column(self):
       start_x = self.x        # сохраняем начальную координату x
       for i in range(10):     # цикл на 10 повторений
           self.build_column() # строим колонну
           self.x += 7         # сдвигаемся для постройки следующей колонны
       self.x = start_x        # возвращаем начальную координату x

   def build_parfenon(self):
       self.build_all_column()
       self.z += 20            # сдвигаемся для постройки параллельного ряда
       self.build_all_column()
       self.z -= 20            # возвращаемся обратно
       # пол
       mc.setBlocks(self.x - 1, self.y-1, self.z - 1,
                    self.x + 65, self.y-1, self.z + 21, 155)
       # потолок
       mc.setBlocks(self.x - 1,  self.y + self.height+1, self.z - 1,
                    self.x + 65, self.y + self.height+1, self.z + 21, 155)


class Object:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def info(self):
            mc.postToChat(f"Object {self.name} is located in the coordinates"
                          f"{self.x}:{self.y}:{self.z}")

class Forest(Object):
    def tree(self):
        height_trunk = randint(3, 6)
        height_leaves = randint(1, 3)

        # ствол дурува
        mc.setBlocks(self.x, self.y - 1, self.z,self.x, self.y + height_trunk, self.z, 17)
        # 1-ый слой листвы
        mc.setBlocks(self.x - 3, self.y + height_trunk, self.z - 3,
                     self.x + 3, self.y + height_trunk + height_leaves, self.z + 3, 161)
        # 2-ой слой листвы
        mc.setBlocks(self.x - 2, self.y + height_trunk + height_leaves, self.z - 2,
                     self.x + 2, self.y + height_trunk + height_leaves * 2, self.z + 2, 161)


   def row_trees(self, count):
       for i in range(count):
           self.tree
           self.x += 7

class Flowers(Object)
    def plant_flowers(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + 70, self.y, self.x + 25, 37)


class Fontane(Object)
    def __init__(self, name, x, y, z, height):
        Object.__init__(self, name, x, y, z)
        self.height = height

    def one_fontane(self):
        mc.setBlocks(self.x, self.y, self.z,
                     self.x, self.y + self.height, self.z, 1)
        mc.setBlock(self.x, self.y + self.height + 1, self.z, 8)

    def pool(self):
        mc.setBlocks(self.x - 2, self.y - 2, self.z - 2,
                     self.x + 2, self.y, self.z + 2, 1)
        mc.setBlocks(self.x - 1, self.y, self.z - 1,
                     self.x + 1, self.y, self.z + 1, 0)

    def row_fontane(self, count):
        for i in range(count):
            self.pool()
            self.one_fontane()
            self.x += 10


x, y, z = mc.player.getTilePos()
x += 10


forest_1 = Forest("Magic forest", 100, 11, 11)
forest_1.info()

from mcpi.minecraft import Minecraft

mc = Minecraft.create()


class Location:
    def __int__(self, pos, name, info):
        self.pos = pos
        self.name = name
        self.info = info

    def teleporting(self):
        mc.player.setTilePos(self.pos)
        mc.postToChat(f"Welcome to {self.name}")
        mc.postToChat(f"Some info  {self.info}")

obj = Location([34, 123, 456], "Болото", "Сильно пахнущая вода")
obj.teleporting()
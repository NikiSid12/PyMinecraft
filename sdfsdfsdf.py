class Color:
    def __init__(self, color_rgb):
        self.rgb = color_rgb

    def show_color(self):
        print(self.rgb)


obj = Color(input())
obj.show_color()

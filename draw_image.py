# encode: utf-8
from PIL import Image, ImageDraw
import sys
from random import randint

class ImageMod:
    def __init__(self, mod=5, size=20):
        self.mod = mod
        self.size = size
        self.set_default_colors()
        self.image_size = 300

    def draw_image(self):
        image = Image.new('RGB', (self.image_size, self.image_size))
        draw = ImageDraw.Draw(image)
        count = 0

        for tile in xrange(0, image.size[0], self.size):
            count += 1
            for other_tile in xrange(0, image.size[1], self.size):
                self.draw_rectangle(draw, tile, other_tile, count)
                count += 1

        image.save('image_' + str(self.mod) + '_' + str(self.size) + '.png')

    def set_default_colors(self):
        available_colors = ['black', 'red', 'orange', 'yellow', 'black', '#2323F0', 'blue']
        self.colors = []
        for i in xrange(0, self.mod):
            self.colors.append(available_colors[ i % len(available_colors) ])

    def draw_rectangle(self, draw, x, y, count):
        if(count > self.image_size):
            count = (count ** self.mod) + randint(0, count)

        draw.rectangle(
            [x, y, x + self.size, y + self.size],
            self.colors[count % self.mod])


image = ImageMod(mod=int(sys.argv[1]), size=int(sys.argv[2]))
image.draw_image()

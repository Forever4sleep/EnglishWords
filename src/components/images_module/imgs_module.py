import os
import sys

sys.path.append("..")

from PIL import Image, ImageFont, ImageDraw
from ..words_module.wrds_module import WordsCouple


class ImageOfWordHandler:
    """Lets edit an image (is represented as the 'flag' file) with an english word and its russian translation"""

    template_image_path = os.path.dirname(os.path.abspath("../flag")) + "/flag"
    font_path = os.path.dirname(os.path.abspath("../flag")) + "/fonts/ARIALBD.TTF"

    def __init__(self, word: WordsCouple):
        self.word = word
        self.file_name = word.source + "_image"
        self.image = Image.open(ImageOfWordHandler.template_image_path)
        self.word_source_font = ImageFont.truetype(ImageOfWordHandler.font_path, 75)
        self.word_translation_font = ImageFont.truetype(ImageOfWordHandler.font_path, 25)

    def get_image(self):
        draw = ImageDraw.Draw(self.image)


        src_width = self.image.width / 2 - 78 # is gonna be changed
        src_height = self.image.height / 2 - 36 # is gonna be changed

        trns_width = src_width + 39
        trns_height = src_height + 85


        draw.text((src_width, src_height),
                  self.word.source, font=self.word_source_font)
        
        draw.text((trns_width, trns_height),
                  self.word.russian_translation, font=self.word_translation_font)

        self.image.show()
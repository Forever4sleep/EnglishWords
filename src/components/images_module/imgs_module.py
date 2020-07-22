import os
import sys

sys.path.append("...")
sys.path.append("..")


from PIL import Image, ImageFont, ImageDraw
from ..words_module.wrds_module import WordsCouple
from constants import ROOT_FOLDER


class ImageOfWord:
    """Lets edit an image (is represented as the 'flag' file) with an english word and its russian translation"""

    template_image_path = ROOT_FOLDER + "/flag"
    font_path = ROOT_FOLDER + "/fonts/ARIALBD.TTF"
    output_path = ROOT_FOLDER + "/output"

    def __init__(self, word: WordsCouple):
        self.word = word
        self.file_name = word.source + "-output.jpeg"
        self.image = Image.open(ImageOfWord.template_image_path)
        self.word_source_font = ImageFont.truetype(ImageOfWord.font_path, 75)
        self.word_translation_font = ImageFont.truetype(ImageOfWord.font_path, 25)

    def save_image(self):
        """Saves an image into the output folder"""

        draw = ImageDraw.Draw(self.image)
        
        src_width = self.image.width / 2 - 78
        src_height = self.image.height / 2 - 36

        trns_width = src_width + 39
        trns_height = src_height + 85


        draw.text((src_width, src_height),
                  self.word.source, font=self.word_source_font)
        
        draw.text((trns_width, trns_height),
                  self.word.russian_translation, font=self.word_translation_font)
        
        self.image.save(ImageOfWord.output_path + "/" + self.file_name, "JPEG")
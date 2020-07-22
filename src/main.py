from components.images_module.imgs_module import ImageOfWord
from components.words_module.wrds_module import WordsCouple
from constants import ROOT_FOLDER
import os


file_path = ROOT_FOLDER + "/components/words_moudle/words.txt"
content_file = open(file_path, "r")

counter = 0
eng, rus = "", ""

words = []
# Here's the logic of translating pieces 
# of a text into an object of WordsCouple class
for line in content_file.readlines():

    if line == "\n":
        continue
    
    if counter == 0:
        eng = line
        counter += 1
        continue

    elif counter == 1:
        rus = line
        counter = 0
    
    word = WordsCouple(eng, rus)
    words.append(word)


# We've got these variables for limits in the further loop 
# since there will be a lot of images (over 900) in the folder
start_from = 0 
end_on = 1

for word in words[start_from:end_on]:
    handler = ImageOfWord(word)
    handler.save_image()
from components.images_module.imgs_module import ImageOfWordHandler
from components.words_module.wrds_module import WordsCouple

        
word = WordsCouple("surplus", "избыток")
handler = ImageOfWordHandler(word) 
handler.get_image()
from wrds_module import WordParser

parser = WordParser("https://studynow.ru/dicta/allwords")
parser.write_words_into_file()
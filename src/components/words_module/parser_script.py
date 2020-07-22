from wrds_module import WordParser

parser = WordParser("https://studynow.ru/dicta/allwords", "tr")
parser.write_words_into_file()
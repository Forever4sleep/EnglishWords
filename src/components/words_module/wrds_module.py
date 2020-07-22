import requests

class WordsCouple:
    """A model of couple of words"""
    def __init__(self, word, russian_translation):
        self.source = word
        self.russian_translation = russian_translation


class WordParser:
    """Represents a class that contains functions for getting english words and its translated ones"""

    def __init__(self, site):
        self.site = site

        from bs4 import BeautifulSoup
        self.__content = BeautifulSoup(self.__get_site_content__(), "html.parser")

    def __get_site_content__(self) -> str:
        """Just gets the site's html"""
        return requests.get(self.site).content

    def write_words_into_file(self):
        """Allows to write one thousand of translated english words from the certain site
           into a file
        """

        counter = 0
        file = open("words.txt", "w+")

        for tr in self.__content.find_all("tr"):
            source_word, translated_word = "", ""

            for child in tr.children:
                if counter == 1:
                    source_word = child.string + "\n"
                    counter += 1

                elif counter == 2:
                    translated_word = child.string + "\n\n"
                    counter = 0

                else:
                    counter += 1
                    continue
            
            file.writelines(source_word + translated_word)
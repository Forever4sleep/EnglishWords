# EnglishWords

This is a project that allows you to put English words into images and get them a Russian translation

# Content Gaining

To gain a content from site, there's parser_script.py file, it's the main script that collects the child elements from inside of the tag you sent into constructor

# Words' transformation into images

After we got some content into file, the logic written in main.py will wrap the words into objects of the 'ImageOfWord' class
The gotten list of words will be iterated over and every time an object of 'WordsCouple' class is being iterated, image will be created and saved into the output folder

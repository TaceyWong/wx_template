# coding:utf-8
# https://amueller.github.io/word_cloud/index.html
from os import path
from PIL import Image
import numpy as np


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'text.txt')).read()

alice_coloring = np.array(Image.open(path.join(d, "mask.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="black", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)

wc.generate(text)
wc.to_file("result.png")

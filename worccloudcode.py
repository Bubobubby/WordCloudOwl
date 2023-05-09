#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
from os import path, getcwd
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS


text = open('eagleowlfeatures.txt','r').read()
stopwords = set(STOPWORDS)
stopwords.add("said")

# read the mask; image taken from https://pixabay.com/pl/sylwetka-kobieta-dziewczyna-wyci%C4%85%C4%87-313666/
mask = np.array(Image.open(path.join(getcwd(), "eagleowl.png")))
wc = WordCloud(background_color="white", max_words=2000, mask=mask,repeat=True,stopwords=stopwords, contour_width=1,random_state=42, contour_color='steelblue')


# generate word cloud
wc.generate(text)
# create coloring from image
image_colors = ImageColorGenerator(mask)
#image_colors.default_color = [0,0,0]
fig, axes = plt.subplots(1, 3)
#plot wordcloud
#plt.figure()
# plt.imshow(wc, interpolation="bilinear")
# plt.axis("off")
# plt.show()

# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
axes[0].imshow(wc, interpolation="bilinear")
axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
axes[2].imshow(mask, cmap=plt.cm.gray, interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()
plt.show()


#wc.to_file('Figure.png')

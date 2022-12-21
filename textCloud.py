import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

# Load in the dataframe
df = pd.read_csv("data.csv")
# Designers
text1 = df.iloc[16, :6].tolist()
# Developers
#text1 = df.loc[16, 'Developer 1':'Developer 3'].tolist()
text = ' '.join([str(elem) for elem in text1])
print(text)
# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

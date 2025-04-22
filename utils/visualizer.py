from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_visuals(words):
    wc = WordCloud(width=800, height=400).generate(" ".join(words))
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("visualization.png")
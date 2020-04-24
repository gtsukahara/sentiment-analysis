#VADER: https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f
  #https://github.com/vaderSentiment/vaderSentiment/blob/master/README.rst
#Multi-Language: https://pypi.org/project/vader-multi/
  #Due to Google Translate API integration this is rate limited (approx 300 requests per 15 min)

#Jupyter Notebook: https://mybinder.org/v2/gh/ipython/ipython-in-depth/master?filepath=binder/Index.ipynb

pip install vaderSentiment #english only
pip install vader-multi #multi-language

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

sentiment_analyzer_scores("text string goes here")
sentiment_analyzer_scores("more text here")

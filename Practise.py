import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
"""
df=pd.read_csv("https://docs.google.com/spreadsheets/d/1QAbmMpa6VQgNvOWl5ax2X3woo_xin0C7JjMS0z1txDc/export?format=csv&usp=sharing")
x=df["Feedback"]
for k in x: #k value in iteration i.e x whhich has all feedback value
    print(k)
mymodel=SentimentIntensityAnalyzer()
l=[]
for k in x:
    pred=mymodel.polarity_scores(k)   # prediction is stored into pred varaible
    if(pred['compound']>=0.05):
        l.append("Positive")
    elif(pred["compound"]<=-0.05):
        l.append("Negative")
    else:
        l.append("Neutral")
df['Sentiment']=l
print(df)
df.to_csv("results.csv",index=False)
df=pd.read_csv("results.csv")
posper=len(df[df['Sentiment']=="Positive"])/len(df)*100
negper=len(df[df['Sentiment']=="Negative"])/len(df)*100
neuper=len(df[df['Sentiment']=="Neutral"])/len(df)*100
fig=px.pie(names=["Positive","Negative","Neutral"],values=[posper,negper,neuper])
fig.show"""

df=pd.read_csv("results.csv")
fig=px.histogram(x=df["State"],color=df['Sentiment'])
fig.show()

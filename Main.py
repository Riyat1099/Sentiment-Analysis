import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
st.set_page_config(page_title="SENTIMENT ANALYSIS SYSTEM",page_icon="https://cdn-icons-png.flaticon.com/512/12662/12662953.png")
st.title("SENTIMENT ANALYSIS SYSTEM")
choice=st.sidebar.selectbox("MY MENU",("HOME", "ANALYSIS", "VISUALISATION"))
if(choice=="HOME"):
    st.image("https://miro.medium.com/v2/1*_JW1JaMpK_fVGld8pd1_JQ.gif")
elif(choice=="ANALYSIS"):
    url=st.text_input("Enter google sheet url")
    c=st.text_input("Enter Column to be analyzed")
    btn=st.button("Analyze")
    if btn:
        df=pd.read_csv(url)
        x=df[c]
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
        df.to_csv("results.csv",index=False)
        st.subheader("Analysis Successfull and results saved as results.csv")
elif(choice=="VISUALISATION"):
    df=pd.read_csv("results.csv")
    st.dataframe(df)
    choice2=st.selectbox("Choose Visualization",("NONE","PIE","HISTOGRAM"))
    if(choice2=="PIE"):
        posper=len(df[df['Sentiment']=="Positive"])/len(df)*100
        negper=len(df[df['Sentiment']=="Negative"])/len(df)*100
        neuper=len(df[df['Sentiment']=="Neutral"])/len(df)*100
        fig=px.pie(names=["Positive","Negative","Neutral"])
        st.plotly_chart(fig)
    elif(choice2=="HISTOGRAM"):
        h=st.text_input("enter columns name")
        if h:
            fig=px.histogram(x=df[h],color=df['Sentiment'])
            st.plotly_chart(fig)
        
        
        

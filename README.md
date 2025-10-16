# Research-project

# Overview the Project

The stock market is a fast-changing and complex environment. Many people invest their money in stocks, but making the right decisions is difficult. Stock prices change based on many factors such as news, social media, global events, and investor behavior. Predicting these price changes is challenging because the market is highly uncertain and affected by both data and human emotions. Predicting these changes is challenging due to the dynamic and non-linear nature of the market.

Many current systems for stock analysis have important limitations. First, most stock prediction models are “black boxes.” They use deep learning or other complex methods but do not explain how a prediction is made. This lack of transparency makes users distrust the system. Explainable AI (XAI) is a growing area that helps solve this by making models easier to understand.

Second, most trading bots only use price data and ignore important signals like social media or financial news. Third, detecting fraud in trading patterns is mostly done by humans or requires labeled data. This takes time and effort, and some scams go unnoticed. Lastly, portfolio recommendation tools often give the same suggestions to everyone without understanding a person’s risk level or financial behavior.

These problems can lead to bad investment decisions, lack of trust in AI systems, and financial losses. There is a strong need for smart systems that are not only accurate but also transparent, personalized, and able to detect problems early.

Our research project aims to address these issues by developing four AI-based components:
• A stock price predictor with explainable AI.
• A sentiment-based trading bot using NLP.
• A fraud detection system using unsupervised learning.
• A personalized portfolio recommendation system based on user risk.

Each part solves a real problem in today’s stock market tools and brings a new feature not commonly found in existing solutions. This will help investors make smarter, safer, and more personalized decisions using AI.


## Architectural Diagram

<img width="2119" height="1568" alt="image" src="https://github.com/user-attachments/assets/f5b7cb74-6721-4161-9d94-e6e5d64b598c" />

## Project Dependencies

## backend dependencies
fastapi==0.103.0
uvicorn==0.24.0
pandas==2.1.0
numpy==1.26.0
requests==2.31.0
tweepy==4.13.0
praw==7.8.0
nltk==3.9.1
spacy==3.8.0
torch==2.1.0
transformers==4.35.0
sentence-transformers==2.2.2
python-dotenv==1.0.1
schedule==1.2.0
apscheduler==3.10.0
plotly==5.16.0
matplotlib==3.8.0
seaborn==0.12.3

## frontend dependencies
"dependencies": {
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "react-router-dom": "^6.16.0",
  "axios": "^1.6.0",
  "recharts": "^2.7.2",
  "framer-motion": "^10.12.16",
  "react-tsparticles": "^2.11.1",
  "tailwindcss": "^3.4.0",
  "shadcn/ui": "latest",
  "redux": "^4.2.1",
  "react-redux": "^8.1.1"
}



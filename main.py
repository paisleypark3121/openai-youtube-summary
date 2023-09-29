import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from utilities import *

load_dotenv()

url="https://www.youtube.com/watch?v=seNGVqRwG8c"
language_code="it"

llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.7)

transcript=get_youtube_transcript(url,language_code)
#print(transcript)

info_about_me="Sono un programmatore italiano non molto esperto e quindi ho bisogno di indicazioni precise su cosa deve essere fatto"
summary=get_summary(llm=llm,info_about_me=info_about_me,transcript=transcript)

print(summary)
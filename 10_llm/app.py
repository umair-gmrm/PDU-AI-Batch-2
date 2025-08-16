import streamlit as st
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider



model = GroqModel(
    'openai/gpt-oss-20b', provider=GroqProvider(api_key=groq_api_key)
)


agent = Agent(model , 
              system_prompt="Your name is BlahBot. " \
              "You are chef.",
              )



user_input =  st.chat_input("Type your message here...")

   
if user_input:
    st.write(f"You said: {user_input}")
    response = agent.run_sync(user_input)
    bot_response = st.chat_message("assistant")
    bot_response.write(response.output)

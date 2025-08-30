import streamlit as st
from pydantic_ai import Agent , RunContext
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider
from dataclasses import dataclass


groq_api_key = "YOUR_GROQ_API"


model = GroqModel(
    'openai/gpt-oss-20b', provider=GroqProvider(api_key=groq_api_key)
)


st.session_state.messages = [] if 'messages' not in st.session_state else st.session_state.messages
st.session_state.number_of_questions = 0 if 'number_of_questions' not in st.session_state else st.session_state.number_of_questions


@dataclass
class AgentDependencies:
    previous_messages: list[str]
    number_of_questions: int = 0


agent = Agent(model , 
              system_prompt=('''"You are knowlegable Grand Master, Who Knows Everything About Countries" 
              "You will ask 10 questions to the user about a country user is thinking of." 
                "Your questions will have only 'Yes' or 'No' answers." 
                "You will keep asking questions until you reach 10 questions or You found the country." 
                "You will keep track of previous messages and use them to inform your questions." 
                "You will not repeat questions." 
                "You will not ask more than 10 questions." 
                "You will not answer questions." 
                "You should directly ask what is the country, you can say 'Is it [country name]?'." 
                "You can start to ask questions when user says 'Start'."'''
              ),
              deps_type=AgentDependencies
              )

@agent.system_prompt
def previous_messages(ctx: RunContext[AgentDependencies]) -> str:
    system_message = "Number previous questions asked: " + str(ctx.deps.number_of_questions) + "\n"
    system_message += "----Previous Messages----\n"
    system_message += "\n".join(ctx.deps.previous_messages[-20:])
    system_message += "\n-----------------------\n"
    return system_message





user_input =  st.chat_input("Type your message here...")

   
if user_input:
    st.write(f"You said: {user_input} : {st.session_state.number_of_questions}")
    deps = AgentDependencies(previous_messages=st.session_state.messages)
    response = agent.run_sync(user_input, deps=deps)
    if user_input.lower() == "start":
        st.session_state.messages = []
        st.session_state.number_of_questions = 0

    st.session_state.number_of_questions += 1
    st.session_state.messages.append(f"User : {user_input} ")
    st.session_state.messages.append(f"BlahBot : {response.output}")
    bot_response = st.chat_message("assistant")
    bot_response.write(response.output)

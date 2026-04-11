import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase= usecase
        self.graph= graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase=self.usecase
        graph= self.graph
        user_message=self.user_message

        with st.chat_message("user"):
            st.write(user_message)

        if usecase == "Basic Chatbot":
            for event in graph.stream({'messages':("user",user_message)}):
                    print(event.values())
                    for value in event.values():
                        print(value['messages'])
                        messages = value["messages"]
                        assistant_msg = messages[-1] if isinstance(messages, list) else messages
                        
                        if isinstance(assistant_msg, AIMessage):
                            with st.chat_message("assistant"):
                                st.write(assistant_msg.content)

        elif usecase == "Chatbot With Tool":
            for event in graph.stream({'messages':("user",user_message)}):
                    print(event.values())
                    for value in event.values():
                        print(value['messages'])
                        messages = value["messages"]
                        assistant_msg = messages[-1] if isinstance(messages, list) else messages
                        
                        if isinstance(assistant_msg, AIMessage) and assistant_msg.content:
                            with st.chat_message("assistant"):
                                st.write(assistant_msg.content)
                        elif isinstance(assistant_msg, ToolMessage):
                            with st.expander(f"⚙️ Search Tool Used: {assistant_msg.name}"):
                                try:
                                    data = json.loads(assistant_msg.content)
                                    st.json(data)
                                except Exception:
                                    st.write(assistant_msg.content)

        elif usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⏳"):
                result = graph.invoke({"messages": frequency})
            try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./AiNews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()


                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
            except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
            except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
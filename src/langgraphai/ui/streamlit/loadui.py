import streamlit as st
import os

from src.langgraphai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title="🤖 " + self.config.get_page_title(),
            layout="wide"
        )
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = ["Select..."] + self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            # Groq settings
            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)

                api_key = st.text_input("GROQ API Key", type="password")
                if api_key:
                    os.environ["GROQ_API_KEY"] = api_key   # optional but good practice
                    st.session_state["GROQ_API_KEY"] = api_key
                    self.user_controls["GROQ_API_KEY"] = api_key
                else:
                    st.warning("⚠️ Please enter your GROQ API key")

            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecases", usecase_options
            )

            # Validate use case
            if self.user_controls["selected_usecase"] == "Select...":
                st.info("👈 Please select a use case")
                st.stop()

            # TAVILY only for specific usecase
            if self.user_controls["selected_usecase"] == "Chatbot With Tool":
                tavily_key = st.text_input("TAVILY API Key", type="password")

                if tavily_key:
                    os.environ["TAVILY_API_KEY"] = tavily_key   # ✅ FIX
                    st.session_state["TAVILY_API_KEY"] = tavily_key
                    self.user_controls["TAVILY_API_KEY"] = tavily_key
                else:
                    st.warning("⚠️ Please enter your TAVILY API key")

        return self.user_controls
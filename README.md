# 🤖 Agentic Chatbot

An intelligent, graph-based conversational agent and news assistant built with **LangGraph**, **Streamlit**, **Groq**, and **Tavily Search**.

## 🌟 Features

This project utilizes a dynamically setup LangGraph workflow that currently supports three distinct use cases:

* **Basic Chatbot**: A lightning-fast, straightforward conversational AI powered by Groq's high-speed Llama models.
* **Chatbot with Tools**: A grounded, intelligent chatbot equipped with the Tavily Search API. It determines when it needs extra knowledge, queries the web, and formats the output (including URLs) for you.
* **AI News Aggregator**: Automatically aggregates the latest Artificial Intelligence news globally. You can choose a Daily, Weekly, or Monthly timeframe. It fetches trending topics, formats the summaries using an LLM, and directly saves them as a markdown report into your `./AiNews/` directory.

## 🛠️ Tech Stack

* **Frontend UI**: [Streamlit](https://streamlit.io/)
* **Agentic Framework**: [LangGraph](https://python.langchain.com/v0.1/docs/langgraph/) & [LangChain](https://www.langchain.com/)
* **LLM Provider**: [Groq API](https://console.groq.com)
* **Search Engine**: [Tavily REST API](https://tavily.com) 

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed. You will also need to generate free API keys for the integrations:
- **GROQ API Key**
- **Tavily API Key**

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DS123-ally/Agentic_Chatbot.git
   cd Agentic_Chatbot
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run app.py  # or the specific entry point of your app
   ```

*Note: You do not have to mess around with `.env` files if you don't want to! The Streamlit UI has built-in sidebars to securely enter your `GROQ_API_KEY` and `TAVILY_API_KEY` at runtime.*

## 📂 Project Structure

```text
📦 AgenticProject
 ┣ 📂 AiNews/                         # Generated markdown summaries get saved here
 ┣ 📂 src/langgraphai
 ┃ ┣ 📂 graph/
 ┃ ┃ ┗ 📜 graph_builder.py            # The core logic mapping the LangGraph nodes & edges
 ┃ ┣ 📂 nodes/
 ┃ ┃ ┣ 📜 ai_news_node.py             # Logic for fetching & summarizing news arrays
 ┃ ┃ ┣ 📜 basic_chatbot_node.py       # Standard LLM Chat logic
 ┃ ┃ ┗ 📜 chatbot_with_tool_node.py   # Agentic logic utilizing tool states
 ┃ ┣ 📂 tools/
 ┃ ┃ ┗ 📜 search_tool.py              # Wrapper for the Tavily web search integration
 ┃ ┣ 📂 state/
 ┃ ┃ ┗ 📜 state.py                    # Schema definitions for LangGraph's state dictionaries
 ┃ ┗ 📂 ui/
 ┃   ┗ 📂 streamlit/
 ┃     ┗ 📜 loadui.py                 # Streamlit UI layouts, keys management, and forms
 ┗ 📜 README.md
 ```
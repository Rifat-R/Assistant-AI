# Asana AI Assistant

This project is a conversational AI assistant that can answer questions about your projects and tasks in Asana. It uses a large language model (LLM) to understand natural language queries and provide relevant information from your Asana workspace.

## Features

*   **Conversational Interface:** Interact with your Asana data using natural language.
*   **Project and Task Insights:** Ask questions about your projects, tasks, deadlines, and completion status.
*   **Web-Based UI:** A simple and intuitive web interface built with Streamlit.
*   **Extensible Toolset:** The agent's capabilities can be extended by adding new functions to its toolset.

## Key Skills Demonstrated

*   **AI/LLM Integration:**
    *   Utilized the `llama-index` library to build a conversational AI agent.
    *   Integrated with OpenAI's `gpt-3.5-turbo-1106` model to power the agent's natural language understanding.
    *   Implemented function calling/tool usage to allow the LLM to interact with external data sources.
*   **API Integration:**
    *   Connected to the Asana API to fetch real-time project and task data.
    *   Handled API authentication and data retrieval in a structured and efficient manner.
*   **Web Application Development:**
    *   Developed a user-friendly web interface using Streamlit.
    *   Created a chat-like interface for interacting with the AI assistant.
*   **Data Handling:**
    *   Fetched and processed data from the Asana API.
    *   Stored and retrieved data using JSON files.
*   **Object-Oriented Programming (OOP):**
    *   Used Python classes to model Asana data (Projects, Tasks) in a structured and reusable way.
*   **Environment Management:**
    *   Employed `python-dotenv` for secure management of API keys and other environment variables.

## How It Works

1.  **Data Retrieval:** The `asana_data_generate.py` script fetches project and task data from your Asana workspace using the Asana API and stores it in a `data.json` file.
2.  **Function Tools:** The `asana_function.py` file defines a set of functions that act as "tools" for the AI agent. These tools allow the agent to access the data in `data.json` and perform specific actions, such as retrieving project names or listing completed tasks.
3.  **AI Agent:** The `model.py` file uses `llama-index` to create an `OpenAIAgent` that is equipped with the function tools. This agent can understand user queries and decide which tool to use to find the answer.
4.  **User Interface:** The `streamlit_app.py` file provides a web-based chat interface for users to interact with the AI agent.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up your environment variables:**
    *   Create a `.env` file in the root directory of the project.
    *   Add your Asana and OpenAI API keys to the `.env` file:
        ```
        ASANA_API_TOKEN="your-asana-api-token"
        OPENAI_API_KEY="your-openai-api-key"
        ASANA_WORKSPACE_GID="your-asana-workspace-gid"
        ```
4.  **Generate the Asana data:**
    ```bash
    python asana_data_generate.py
    ```

## Usage

To start the web application, run the following command:

```bash
streamlit run streamlit_app.py
```

This will open the application in your web browser. You can then start asking questions about your Asana projects and tasks.

# AI-Powered Smart Chatbot

## 1. Project Overview

The AI-Powered Smart Chatbot is a Python-based application that allows users to ask questions and receive AI-generated responses using a locally running Large Language Model (LLM).

The application uses Streamlit for the user interface, LangChain for model interaction, and Ollama to run the Llama 3.2 3B model locally.

## 2. Project Objectives

- Build an interactive chatbot interface.
- Integrate a local LLM using LangChain and Ollama.
- Support follow-up questions using conversation history.
- Provide a clear-conversation option.
- Test the chatbot with general and programming questions.

## 3. Technologies Used

- Python
- Streamlit
- LangChain Core
- LangChain Ollama
- Ollama
- Llama 3.2 3B
- Jupyter Notebook

## 4. Project Structure

```text
AI_Powered_Smart_Chatbot/
├── app.py
├── project.ipynb
├── requirements.txt
├── README.md
├── report.pptx
└── Final_Capstone_Project.zip
```

The ZIP file is generated after the other project files are finalized. Do not place the ZIP inside itself.

## 5. Prerequisites

- Python 3.12 recommended
- Visual Studio Code
- Ollama installed
- Llama 3.2 3B model downloaded

## 6. Installation

### Create a virtual environment

```powershell
py -3.12 -m venv .venv
```

### Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### Download the language model

```powershell
ollama pull llama3.2:3b
```

## 7. Run the Application

From the project folder, execute:

```powershell
python -m streamlit run app.py
```

Streamlit will provide a local web address where the chatbot can be opened in a browser.

## 8. Application Features

- Interactive chat interface
- AI-generated responses
- Local language-model execution
- Session-based conversation history
- Clear-conversation button
- Basic error handling when the model is unavailable

## 9. Notebook and Testing

The `project.ipynb` notebook documents the problem statement, objectives, model configuration, example interactions, testing plan, limitations, and conclusion.

Run the notebook cells in order using the project virtual environment. Record the actual outputs and testing results before submitting the project.

## 10. Limitations

- AI-generated answers may be incorrect.
- Response speed depends on the computer's hardware.
- The model must be downloaded before local use.
- Conversation history is not permanently stored.
- The current version does not include document-based RAG.

## 11. Future Improvements

- Add document-based question answering using RAG.
- Support additional language models.
- Improve response evaluation.
- Add optional conversation export.
- Improve logging and error handling.

## 12. Conclusion

This project demonstrates the integration of Python, Streamlit, LangChain, and Ollama to build an interactive chatbot powered by a locally running language model.

## 13. Author Details

- **Author:** Neha Bansal
- **Trainer:** Anant Verma
- **Institute:** E&ICT IIT Roorkee

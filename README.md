# RAG Chatbot with Streamlit

A Retrieval-Augmented Generation (RAG) chatbot built with LangChain and Streamlit. This application allows users to ask questions about documents and get AI-powered responses.

## Features

- 🤖 RAG-based question answering
- 📚 Document retrieval and context generation
- 💬 Interactive chat interface with Streamlit
- ⚡ Real-time streaming responses
- 📝 Chat history preservation

## Prerequisites

- Python 3.8+
- OpenAI API key
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Start chatting with the bot!

## Project Structure

```
rag-chatbot/
├── app.py              # Streamlit application
├── main.py            # CLI version of the chatbot
├── requirements.txt   # Project dependencies
├── .env              # Environment variables (not in repo)
├── src/              # Source code
│   ├── model/        # LLM models
│   ├── task/         # RAG tasks
│   └── ...
└── data/             # Document data
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- LangChain for the RAG framework
- Streamlit for the web interface
- OpenAI for the language model 
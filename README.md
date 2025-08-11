# RAG Chatbot with Streamlit

A Retrieval-Augmented Generation (RAG) chatbot built with LangChain and Streamlit. This application allows users to ask questions about documents and get AI-powered responses.

## Features

- 🤖 RAG-based question answering
- 📚 Document retrieval and context generation
- 💬 Interactive chat interface with Streamlit
- ⚡ Real-time streaming responses
- 📝 Chat history preservation
- 🔄 OpenAI integration

## Prerequisites

- Python 3.8+
- OpenAI API key
- PostgreSQL (for vector store)
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

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Set up PostgreSQL:
   - Install PostgreSQL if you haven't already
   - Create a database named `vector_db`
   - Update database credentials in your code

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Start chatting with the bot!

## Project Structure

```
.
├── app.py              # Streamlit application
├── main.py            # CLI application
├── requirements.txt   # Python dependencies
├── src/              # Source code
│   ├── document_store/
│   ├── task/
│   └── ...
├── config/           # Configuration files
└── data/            # Document data
```

## Development

- The application uses PostgreSQL as a vector store
- Documents are processed and stored in the vector database
- Questions are answered using RAG pipeline with OpenAI

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 
from dotenv import load_dotenv
import os
from src import MyChatBot
from langchain_core.messages import HumanMessage, SystemMessage
from src.document_store.loader import DocumentStoring
from src import test_document_pipeline
from src import retrieve, generate, State
from src.prompt_template.template import load_prompt
from src.langgraph_tracking import build_graph
import re

def initialize_rag_pipeline():
    try:
        # Load environment variables
        load_dotenv()
        print("✅ Environment variables loaded successfully")
        
        # Initialize LLM
        print("🔄 Initializing LLM...")
        llm = MyChatBot()
        print("✅ LLM initialized successfully")

        # Initialize vector store
        print("🔄 Initializing vector store...")
        vector_store = test_document_pipeline()
        print("✅ Vector store initialized successfully")
        
        return llm, vector_store
    except Exception as e:
        print(f"❌ Error during initialization: {str(e)}")
        return None, None

def process_question(question: str, graph):
    try:
        # Process the question through the RAG pipeline with streaming
        print("\n📝 Answer:")
        for message, metadata in graph.stream(
            {"question": question}, 
            stream_mode="messages"
        ):
            if hasattr(message, 'content'):
                print(message.content, end="", flush=True)
        print()  # Add newline at the end
        return True
    except Exception as e:
        print(f"❌ Error processing question: {str(e)}")
        return None

def main():
    # Initialize the RAG pipeline
    llm, vector_store = initialize_rag_pipeline()
    if llm is None or vector_store is None:
        print("❌ Failed to initialize RAG pipeline")
        return

    # Build the RAG graph
    try:
        print("🔄 Building RAG graph...")
        # Create functions that will be used in the graph
        def retrieve_node(state):
            return retrieve(state, vector_store=vector_store)
            
        def generate_node(state):
            return generate(state, llm=llm, load_prompt=load_prompt)
            
        graph = build_graph(
            State,
            retrieve_node,
            generate_node
        )
        print("✅ RAG graph built successfully!")
    except Exception as e:
        print(f"❌ Error building RAG graph: {str(e)}")
        return

    # Interactive Q&A loop
    print("\n🤖 RAG Pipeline is ready! Type 'exit' to quit.")
    while True:
        try:
            question = input("\n❓ Please enter your question: ").strip()
            
            if question.lower() == 'exit':
                print("👋 Goodbye!")
                break
                
            if not question:
                print("⚠️ Please enter a valid question")
                continue
                
            print(f"\n🔄 Processing your question: {question}")
            process_question(question, graph)
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()


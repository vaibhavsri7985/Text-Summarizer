import streamlit as st
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.schema.runnable import RunnableLambda

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Text Summarizer", page_icon="📰", layout="centered")
st.header("📰 AI-Powered Text Summarizer")

# Hugging Face model setup
try:
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation",
    )
    model = ChatHuggingFace(llm=llm)
except Exception as e:
    st.error(f"Failed to initialize model: {e}")
    st.stop()

# Schema for structured output
schema = [
    ResponseSchema(name="summary 1", description="summary 1 about the topic"),
    ResponseSchema(name="summary 2", description="summary 2 about the topic"),
    ResponseSchema(name="summary 3", description="summary 3 about the topic"),
]
parser = StructuredOutputParser.from_response_schemas(schema)

url = st.text_input("🔗 Enter a news article URL")
button = st.button("✨ Get Summary")

if button:
    if not url or not url.startswith("http"):
        st.warning("Please enter a valid URL (must start with http/https).")
        st.stop()

    with st.spinner("📥 Loading article..."):
        try:
            loader = UnstructuredURLLoader(urls=[url])
            docs = loader.load()
        except Exception as e:
            st.error(f"⚠️ Failed to load the page: {e}")
            st.stop()

    with st.spinner("Splitting text into chunks..."):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=20)
        chunks = text_splitter.split_documents(docs)

    # Prompts
    chunks_prompt = """
    You are given a chunk of text scraped from a website.

    Task:
    - Focus only on the NEWS ARTICLE content (headlines, article body, analysis).
    - Ignore navigation menus, login/logout info, calculators, tools, alerts, or any unrelated website UI.
    - Summarize only the important business/news details in 2–3 concise sentences.

    input_documents:
    {text}

    Summary:
    """
    map_prompt_template = PromptTemplate(
        input_variables=['text'], template=chunks_prompt
    )

    final_prompt = """
    You are given multiple summaries of text chunks from a news article.

    Instructions:
    - First, read all the chunk summaries.
    - Identify the 3 most important insights from the news article.
    - Write a final summary of exactly three sentences (no more, no less).
    - Focus only on the news content. Ignore menus, calculators, login/logout info, or other website sections.

    input_documents:
    {text}

    {format_instruction}

    
    """
    final_prompt_template = PromptTemplate(
        input_variables=['text'],
        template=final_prompt,
        partial_variables={"format_instruction": parser.get_format_instructions()},
    )

    # Summarization chain
    summary_chain = load_summarize_chain(
        llm=model,
        chain_type="map_reduce",
        map_prompt=map_prompt_template,
        combine_prompt=final_prompt_template,
        verbose=False,
    )

    main_chain = summary_chain | RunnableLambda(lambda x: x['output_text']) | parser

    with st.spinner("🤖 Generating summary..."):
        try:
            final_output = main_chain.invoke({"input_documents": chunks})
        except Exception as e:
            st.error(f"⚠️ Failed to generate summary: {e}")
            st.stop()

    st.subheader("✅ Final 3-Sentence Summary")
    for key, val in final_output.items():
        st.markdown(f"- {val}")

    st.success("✨ Done! Article summarized successfully.")

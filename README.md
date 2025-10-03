# 📰 AI-Powered Text Summarizer

# 📰 AI Text Summarizer  

An **AI-powered text summarizer** built with **LangChain**, **HuggingFace LLaMA-3.1-8B-Instruct**, and **Streamlit**.  
The app can scrape articles from the web, split them into context-aware chunks, and generate **exactly three concise summaries** using advanced LLMs.  

---

## 🚀 Features
- 🔗 Input any article URL.  
- 📥 Scrapes content directly from the webpage.  
- ✂️ Splits text into context-preserving chunks (`RecursiveCharacterTextSplitter`).  
- 🤖 Summarizes text with HuggingFace LLaMA-3.1-8B-Instruct.  
- 📝 Produces **three structured summaries** (each in one sentence).  
- 🌐 Easy-to-use **Streamlit UI**.  

---

## 📂 Project Workflow
1. **Load environment variables** from `.env` (HuggingFace token).  
2. **Initialize HuggingFace model** (`LLaMA-3.1-8B-Instruct`).  
3. **Scrape article** via `UnstructuredURLLoader`.  
4. **Split into chunks** using `RecursiveCharacterTextSplitter`.  
5. **Apply two-stage summarization**:
   - *Map step*: Summarizes individual chunks.  
   - *Reduce step*: Combines chunk summaries into final 3-sentence output.  
6. **Display results** in a neat Streamlit UI.  

---

## 📊 Example Output
```json
{
  "summary 1": "India secured a historic victory in the Asia Cup final against Pakistan.",
  "summary 2": "Star performers contributed significantly to India’s success under pressure.",
  "summary 3": "The win boosts India’s confidence ahead of upcoming tournaments."
}


# 📰 AI-Powered Text Summarizer

This project demonstrates a full pipeline for summarizing news articles or blog posts using **LangChain** and **HuggingFace models**, with both a Jupyter Notebook walkthrough and a Streamlit web app.

---

## 📓 Notebook (`Text_Summarizer.ipynb`)

**Features:**
- Demonstrates integration of LangChain with HuggingFace.
- Splits documents into overlapping chunks for better summarization.
- Implements a **map-reduce summarization chain**.
- Returns structured JSON containing **3 key summaries**.

**How It Works:**
1. Import required libraries: `langchain`, `dotenv`, `huggingface`, etc.
2. Define a prompt template to ensure exactly 3 summaries.
3. Load content from the target webpage.
4. Process the content with the map-reduce summarization chain.
5. Display the final structured summaries.

---

## 🌐 Streamlit App (`app.py`)

**Features:**
- Clean and user-friendly UI built with **Streamlit**.
- Shows progress indicators (`st.spinner`) while loading and summarizing.
- Validates input URLs.
- Uses the same summarization chain as the notebook.
- Displays the final **3-sentence summary** in bullet points.

**How It Works:**
1. **Input:** User enters a news/blog URL in a text box.
2. **Processing:** The app scrapes content, splits it into chunks, and summarizes each chunk.
3. **Output:** Final structured 3-sentence summary is displayed on the UI.

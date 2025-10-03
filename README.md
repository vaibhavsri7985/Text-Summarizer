# 📰 AI-Powered Text Summarizer
![Alt text](<img width="1618" height="782" alt="Screenshot 2025-10-03 164251" src="https://github.com/user-attachments/assets/9c86d6e3-3081-4dfd-b397-6b51819e307c" />
)


This project is a **Streamlit-based web application** that leverages **Hugging Face LLMs** (Llama 3) through LangChain to summarize news articles from URLs. It breaks down articles into chunks, generates summaries for each chunk, and then produces a concise 3-sentence final summary.

---

## Features

- Accepts **any news article URL** as input.
- Splits long articles into manageable chunks for processing.
- Summarizes each chunk using **LLM-powered summarization**.
- Combines chunk summaries into a **final 3-sentence summary**.
- Ignores unrelated content like menus, calculators, and login/logout info.
- Provides a **user-friendly Streamlit interface** for interaction.

---

## Streamlit UI

1. **Header:** Displays "📰 AI-Powered Text Summarizer".
2. **Input Field:** Enter the URL of a news article.
3. **Button:** "✨ Get Summary" triggers the summarization.
4. **Loading Indicators:** Shows progress for loading articles, splitting text, and generating summary.
5. **Output:** Displays the final 3-sentence summary in a bullet-point format.
6. **Error Handling:** Warns if the URL is invalid or if the model fails.


---

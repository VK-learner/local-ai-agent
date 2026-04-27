# 🍕 Local RAG Chatbot (LangChain + Ollama)

A fully **local Retrieval-Augmented Generation (RAG) system** that answers questions about restaurant reviews using semantic search.

This project runs entirely on your machine using **Ollama**, **LangChain**, and **ChromaDB** — no external APIs required.

---

## 🚀 Features

* 🔍 Semantic search using embeddings (`mxbai-embed-large`)
* 🧠 Local LLM inference via Ollama (`llama3`)
* 📦 Vector database powered by ChromaDB
* 💬 Interactive question-answering system
* ⚡ Fast and private (runs locally)

---

## 🏗️ Tech Stack

* Python
* LangChain
* Ollama
* ChromaDB
* Pandas

---

## 📂 Project Structure

```
.
├── main.py          # Handles user interaction and LLM responses
├── vector.py        # Embedding generation and vector DB setup
├── realistic_restaurant_reviews.csv
├── concepts.md      # Notes explaining core concepts
├── README.md
└── .gitignore
```

---

## ⚙️ Setup

### 1. Install dependencies

```
pip install langchain langchain-ollama langchain-chroma pandas
```

### 2. Install and run Ollama

Download from: https://ollama.com

Pull required models:

```
ollama pull llama3
ollama pull mxbai-embed-large
```

---

## ▶️ Run the Project

```
python main.py
```

---

## 🧠 How It Works

1. Converts restaurant reviews into embeddings
2. Stores them in ChromaDB
3. Retrieves relevant reviews based on your question
4. Sends context to the LLM (`llama3`)
5. Generates a final answer

---

## 📌 Example

**Input:**

```
Which pizza has the best cheese?
```

**Output:**

```
Based on the reviews, the Margherita pizza is praised for its rich and creamy cheese.
```

---

## 🔮 Future Improvements

* Add a UI (Streamlit or web app)
* Support multiple datasets
* Improve retrieval with hybrid search
* Add chat memory

---

## 📜 License

MIT License

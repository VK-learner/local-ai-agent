# 🧠 Concepts Behind This Project

This file explains the core ideas used in this project in a simple way.

---

## 🔍 What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique that improves LLM responses by giving them relevant context from a database.

Instead of relying only on training data, the model:

1. Retrieves useful information
2. Uses it to generate better answers

---

## 🧩 Key Components

### 1. Embedding Model (`mxbai-embed-large`)

* Converts text into numerical vectors
* Captures semantic meaning
* Example:

  ```
  "Great pizza" → [0.21, -0.45, 0.88, ...]
  ```

---

### 2. Vector Database (ChromaDB)

* Stores embeddings
* Performs similarity search
* Finds the most relevant documents

Think of it as:

> 📚 A smart library that finds meaning, not just keywords

---

### 3. LLM (Ollama - llama3)

* Reads retrieved context
* Generates human-like answers
* Works locally (no API needed)

---

## 🔄 Pipeline Flow

1. Load dataset (restaurant reviews)
2. Convert reviews into embeddings
3. Store embeddings in ChromaDB
4. User asks a question
5. Retrieve top relevant reviews
6. Send them to the LLM
7. Generate final answer

---

## ⚙️ Libraries Used

### LangChain

* Framework for building LLM pipelines
* Connects all components together

### langchain-ollama

* Allows using local models via Ollama

### langchain-chroma

* Connects LangChain with ChromaDB

---

## 💡 Core Idea

* Embedding Model → understands meaning
* Vector Database → stores and retrieves knowledge
* LLM → generates answers

Together, they form a powerful AI system.

---

## 🚀 Why This Matters

* No API costs
* Full data privacy
* Fast local inference
* Real-world AI architecture

---

## 📌 Summary

This project demonstrates how to build a **local AI assistant** using modern tools like embeddings, vector databases, and LLMs.

It is a practical example of how real-world AI systems are built.

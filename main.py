# pip install langchain langchain-ollama langchain-chroma
# py -m venv venv
#  ./venv/Scripts/activate
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver

model = OllamaLLM(model='llama3.2:3b')

template = """
You are an expert in answering questions about a pizza restaurant.

Use ONLY the provided reviews to answer the question.
If the answer is not in the reviews, say "I don't have enough information."

Reviews:
{reviews}

Question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("-------------------------------------------")
    question = input("Ask your question (q to quit): ")
    if question == 'q':
        break
    
    docs = retriver.invoke(question)
    reviews = "\n\n".join([doc.page_content for doc in docs])

    print("\n🤖 Answer:\n")

    # 🔥 STREAMING OUTPUT
    for chunk in chain.stream({
        "reviews": reviews,
        "question": question
    }):
        print(chunk, end="", flush=True)

    print("\n")  # newline after response
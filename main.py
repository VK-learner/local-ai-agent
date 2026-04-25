# pip install langchain langchain-ollama langchain-chroma
# py -m venv venv
#  ./venv/Scripts/activate
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriver

model = OllamaLLM(model='llama3.2:3b')

template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model # this takes our prompt and passes to our model through '|' pipe and returns to chain.

while True:
    print("-------------------------------------------")
    question = input("Ask your question (q to quit): ")
    if question == 'q':
        break
    
    reviews = retriver.invoke(question)
    result = chain.invoke({"reviews":reviews,"question":question})# it invokes to our llama3.2 llm 
    print(result)
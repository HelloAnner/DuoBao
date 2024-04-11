from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from kimi import Kimi

prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

model = Kimi()

chain = prompt | model.bind(stop=["\n"])

response = chain.invoke({"topic": "bears"})

print(response)

# 加一个输出解析器

chain = prompt | model | StrOutputParser()

print(chain.invoke({"topic": "bears"}))

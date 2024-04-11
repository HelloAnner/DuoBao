import operator

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from kimi import Kimi

prompt1 = ChatPromptTemplate.from_template("{person} 是一个人的名字，告诉我他可能是来一个城市?")

prompt2 = ChatPromptTemplate.from_template("{city} 是属于哪一个国家的，使用{language}回答我")

model = Kimi()

chain1 = prompt1 | model | StrOutputParser()

chain2 = (
        {"city": chain1, "language": operator.itemgetter("language")}
        | prompt2
        | model
        | StrOutputParser()
)

response = chain2.invoke({"person": "obama", "language": "chinese"})

print(response)

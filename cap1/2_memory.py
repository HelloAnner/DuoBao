# 记忆组件
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, MessagesPlaceholder, \
    HumanMessagePromptTemplate

from kimi import Kimi

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            """
        接下来的对话是人和AI之间的友好交流
        """
        ),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}")
    ]
)

llm = Kimi()

memory = ConversationBufferMemory(return_messgaes=True)

memory.save_context({"input": "hi"}, {"output": "whats up"})

memory.load_memory_variables({})

conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

print(conversation.predict(input="你好，我是Anner"))

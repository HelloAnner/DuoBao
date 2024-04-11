#  提示词模板
from langchain.chains.llm import LLMChain
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

from kimi import Kimi

template = (
    "你是一个将{input_language} 翻译为 {output_language} 的机器人"
)

system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])

chain = LLMChain(llm=Kimi(), prompt=chat_prompt)

ans = chain.run(
    input_language="中文",
    output_language="英文",
    text="你好，多宝"
)

print(ans)

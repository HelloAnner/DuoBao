import os

from langchain_core.messages import HumanMessage

from kimi import Kimi

key = os.getenv("KIMI_API_KEY")

chat = Kimi()

ans = chat.predict_messages([
    HumanMessage(
        content=(
            "将中文翻译为法语"
            "你好 Kimi"
        )
    )
])

print(ans)

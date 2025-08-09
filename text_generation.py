from openai import AsyncOpenAI
import os
import asyncio
from draw_view.models import GlobalPrompt
from asgiref.sync import sync_to_async

PROMPT_TEXT = """
Ты — креативный крипто-нарратор с юмором и энергией крипто-комьюнити.
Составь сообщение длиной 5–6 предложений, которое:
 • объявляет, что покупка совершена;
 • называет адрес покупателя https://tonviewer.com/{wallet_address} (в формате TON, например EQxxxx...xxxx), подчёркивая его значимость;
 • указывает сумму покупки {purchase_amount} TON;
 • сообщает, что выпала награда {reward};
 • обязательно упоминает, что награда редкая, с шансом {rarity_percent}%;
 • передаёт чувство удачи и эксклюзивности момента;
 • в последних предложениях мотивирует к будущим покупкам, намекая на ещё более ценные дропы;
 • использует 2–3 тематических эмодзи (🚀💎📈🔥⚡🎯📦 и т.п.);
 • стиль — бодрый, в духе «крипто-чатов» с элементами мемов.

Пример структуры:
 1. Взрывная новость о покупке.
 2. Указание адреса и суммы.
 3. Объявление награды и редкости.
 4. Крипто-шутка или аналогия.
5–6. Мотивация к будущим покупкам и усиление FOMO.
"""



async def text_generation(client: AsyncOpenAI, address: str, winning_name: str, amount: str, percent) -> str:
    print(address, winning_name, amount, percent)        
    PROMPT_TEXT = await GlobalPrompt.aget_prompt()
    completion = await client.chat.completions.create(
        messages=[{"role": "user", "content": PROMPT_TEXT.prompt_text.format(wallet_address=address, purchase_amount=amount, reward=winning_name, rarity_percent=percent)}],
        model="gpt-5-nano"
    )
    return completion.choices[0].message.content


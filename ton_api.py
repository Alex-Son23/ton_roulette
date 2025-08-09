import asyncio
import requests
from config import TELEGRAM_CHAT_ID
from loader import database
from roulette import run_roulette
from aiogram import Bot
from openai import AsyncOpenAI
from text_generation import text_generation
from ton.utils import Address
from asgiref.sync import sync_to_async


chat_id = TELEGRAM_CHAT_ID


async def api_ton(bot: Bot, ai_client: AsyncOpenAI):
    try:
        r = requests.get(
            'https://jetton-index.tonscan.org/public-dyor/swaps/EQD1wiY26d7fGSvSIyoKyuXIKNxdmxah3ta37mMmtOi2eHFk?limit=50'
        )
        r.raise_for_status()
        r_json = r.json()
        transactions = r_json.get('transactions', [])
        buy_trans = [tr for tr in transactions if tr['type'] == 'TT_BUY']

        for tr in buy_trans:
            id_trans = tr['hash']
            amountTON = int(tr['counterpartAmount']['value']) / (10 ** 9)
            address = tr['whoFriendly']
            address_bounceable = Address(address).to_string(is_user_friendly=True, is_bounceable=False)
            print(address_bounceable)
            if await database.check_transaction_exists(id_trans):
                continue

            prize_name, percent, gifts_link, amount = await run_roulette(amountTON)

            await database.add_log(address=address_bounceable, winning_name=prize_name, id_trans=id_trans, amount=amount)

            try:
                msg = await text_generation(client=ai_client, address=address_bounceable, winning_name=prize_name, amount=amountTON, percent=percent)
            except Exception as e:
                print(f"ОШИБКА ОШИБКА ОШИБКА {e}")
                msg = (
                    f"🏆 <b>Победа зафиксирована!</b>\n"
                    f"👤 <b>Адрес:</b> <a href='https://tonviewer.com/{address_bounceable}'><code>{address_bounceable}</code></a>\n"
                    f"💰 <b>Сумма:</b> {amountTON} TON\n"
                    f"🎁 <b>Награда:</b> {prize_name}\n"
                    f"📊 <b>Шанс:</b> {percent}%\n\n"
                    f"⚙️ Алгоритм не ожидал такого исхода, но блокчейн всё принял.\n"
                    f"🚀 Это дроп вне логики. Кто следующий?"
                )
            await bot.send_message(chat_id, msg)
            # await asyncio.sleep(3)

    except Exception as e:
        print(f"Ошибка в api_ton: {e}")

# import asyncio
# import requests
# from config import TELEGRAM_CHAT_ID
# from loader import database
# from roulette import run_roulette
# from aiogram import Bot
#
# chat_id = TELEGRAM_CHAT_ID
#
#
# async def api_ton(bot: Bot):
#     try:
#         r = requests.get(
#             'https://jetton-index.tonscan.org/public-dyor/swaps/EQD1wiY26d7fGSvSIyoKyuXIKNxdmxah3ta37mMmtOi2eHFk?limit=50')
#         r_json = r.json()
#         transactions = r_json['transactions']
#         buy_trans = []
#         for tr in transactions:
#             if tr['type'] == 'TT_BUY':
#                 buy_trans.append(tr)
#         for tr in buy_trans:
#             id_trans = tr['hash']
#             prize_name, percent, gifts_link = await run_roulette(amountTON)
#             log = await database.get_log()
#             for i in log:
#                 if id_trans == i.id_trans:
#                     continue
#
#             amountTON = int(tr['counterpartAmount']['value']) / (10 ** 9)
#             if amountTON in (1, 2, 5):
#                 address = tr['whoFriendly']
#                 await database.add_log(address=address, winning_name=prize_name, id_trans=id_trans)
#                 msg_1 = (
#                     f"🎉 <b>Розыгрыш запущен!</b>\n"
#                     f"Кошелёк <code>{address}</code> совершил покупку на {amountTON} TON и запустил розыгрыш..."
#
#                 )
#                 await bot.send_message(chat_id, msg_1)
#                 await asyncio.sleep(5)
#                 msg_2 = (
#                     f"💥 <b>Победа!</b>\n"
#                     f"Кошелёк <code>{address}</code> получил приз: <b>{prize_name}</b> (бонус: {percent}%)." + (f' — <a href="{gifts_link}">Все подарки</a>' if gifts_link else "")
#                 )
#                 await bot.send_message(chat_id, msg_2)
#     except Exception as e:
#         print(e)

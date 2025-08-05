import asyncio
import requests
from config import TELEGRAM_CHAT_ID
from loader import database
from roulette import run_roulette
from aiogram import Bot

chat_id = TELEGRAM_CHAT_ID


async def api_ton(bot: Bot):
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
            if amountTON not in (1, 2, 5):
                continue

            if await database.check_transaction_exists(id_trans):
                continue

            prize_name, percent = await run_roulette()

            await database.add_log(address=address, winning_name=prize_name, id_trans=id_trans)

            msg_1 = (
                f"🎉 <b>Розыгрыш запущен!</b>\n"
                f"Кошелёк <code>{address}</code> совершил покупку на {amountTON} TON и запустил розыгрыш..."
            )
            await bot.send_message(chat_id, msg_1)
            await asyncio.sleep(5)

            msg_2 = (
                f"💥 <b>Победа!</b>\n"
                f"Кошелёк <code>{address}</code> получил приз: <b>{prize_name}</b> (шанс: {percent}%)"
            )
            await bot.send_message(chat_id, msg_2)

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
#             prize_name, percent = await run_roulette()
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
#                     f"Кошелёк <code>{address}</code> получил приз: <b>{prize_name}</b> (шанс: {percent}%)"
#                 )
#                 await bot.send_message(chat_id, msg_2)
#     except Exception as e:
#         print(e)

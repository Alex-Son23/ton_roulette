import datetime
from typing import List

import pytz

from utils.database_api.models.log import Log


class DB_Log:
    async def add_log(self, address, winning_name,id_trans):
        new_log = Log()
        new_log.address = address
        new_log.winning_name = winning_name
        new_log.id_trans = id_trans
        new_log.date_register = datetime.datetime.now(tz=pytz.timezone('Europe/Kiev'))
        await new_log.create()

    async def get_log(self,) -> List[Log]:
        return await Log.query.gino.all()

    async def check_transaction_exists(self, id_trans: str) -> bool:
        result = await Log.query.where(Log.id_trans == id_trans).gino.first()
        return result is not None
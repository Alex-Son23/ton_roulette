from dataclasses import dataclass

from utils.database_api.commands.log import DB_Log
from utils.database_api.commands.draw import DB_Draw


@dataclass
class DB_Commands:

    @property
    def draw(self) -> DB_Draw:
        return DB_Draw()

    @property
    def log(self) -> DB_Log:
        return DB_Log()

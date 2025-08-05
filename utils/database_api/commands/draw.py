from utils.database_api.models.draw import Draw


class DB_Draw:
    async def get_draw(self, id) -> Draw:
        return await Draw.query.where(Draw.id == id).gino.first()

    async def get_all_draws(self):
        return await Draw.query.gino.all()

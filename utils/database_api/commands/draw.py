from utils.database_api.models.draw import Draw


class DB_Draw:
    async def get_draw(self, id) -> Draw:
        return await Draw.query.where(Draw.id == id).gino.first()

    async def get_all_draws(self):
        return await Draw.query.gino.all()

    async def get_draws_by_amount(self, amount: float):
        # Вернёт все призы, у которых amount попадает в [min_amount, max_amount]
        print("_______________________", amount, "_______________________", sep="\n")
        return await Draw.query.where((Draw.min_amount <= amount) & (Draw.max_amount >= amount)).gino.all()


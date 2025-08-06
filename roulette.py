from typing import Tuple
import random
from loader import database
import logging

logger = logging.getLogger(__name__)


async def run_roulette(purchase_amount: float) -> Tuple[str, str, str | None, str]:
    try:
        draws = await database.get_draws_by_amount(purchase_amount)
        print("_______________________", draws, "_______________________", not draws, sep="\n")
        
    except Exception as e:
        logger.error(f"Ошибка получения призов: {e}")
        return "Ошибка приза", "0", None, ""

    if not draws:
        logger.warning("Нет доступных призов в базе")
        return "Приз не определён", "0", None, "",

    weights = [d.win_percentage for d in draws]
    print(weights)

    if sum(weights) == 0:
        draw = random.choice(draws)
        return draw.winning_name, str(draw.dis_percentage), getattr(draw, 'gifts_link', None), f"{draw.min_amount} - {draw.max_amount}"

    try:
        chosen_draw = random.choices(draws, weights=weights, k=1)[0]
        return chosen_draw.winning_name, str(chosen_draw.dis_percentage), getattr(chosen_draw, 'gifts_link', None), f"{chosen_draw.min_amount} - {chosen_draw.max_amount}"
    except Exception as e:
        logger.error(f"Ошибка выбора приза по весам: {e}")
        draw = random.choice(draws)
        return draw.winning_name, str(draw.dis_percentage), getattr(draw, 'gifts_link', None), ""

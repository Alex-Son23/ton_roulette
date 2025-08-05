from typing import Tuple
import random
from loader import database
import logging

logger = logging.getLogger(__name__)


async def run_roulette() -> Tuple[str, str]:
    try:
        draws = await database.get_all_draws()
    except Exception as e:
        logger.error(f"Ошибка получения призов: {e}")
        return "Ошибка приза", "0"

    if not draws:
        logger.warning("Нет доступных призов в базе")
        return "Приз не определён", "0"

    weights = [d.win_percentage for d in draws]

    if sum(weights) == 0:
        draw = random.choice(draws)
        return draw.winning_name, str(draw.dis_percentage)

    try:
        chosen_draw = random.choices(draws, weights=weights, k=1)[0]
        return chosen_draw.winning_name, str(chosen_draw.dis_percentage)
    except Exception as e:
        logger.error(f"Ошибка выбора приза по весам: {e}")
        draw = random.choice(draws)
        return draw.winning_name, str(draw.dis_percentage)





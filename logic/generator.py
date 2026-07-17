from pathlib import Path
import random
from logic.loader import load_json



CHARACTER_PATH = Path("data/character/appearance.json")


def generate_character() -> dict[str, str]:
    return generate(CHARACTER_PATH)


def generate(path: Path) -> dict[str, str]:
    """
    JSONファイルから各カテゴリをランダム生成する。
    """

    data = load_json(path)

    result = {}

    for category, values in data.items():
        result[category] = random.choice(values)

    return result
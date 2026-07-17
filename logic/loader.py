"""
JSONの読み込みを担当するファイル
"""

import json
from pathlib import Path


def load_json(path: Path) -> dict:
    """
    JSONファイルを読み込む。

    Parameters
    ----------
    path : Path
        JSONファイルへのパス

    Returns
    -------
    dict
        読み込んだデータ
    """

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
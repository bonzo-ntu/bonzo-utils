
import pandas as pd
from pathlib import Path


def jsonl_decode(file):
    df = pd.read_json(file, lines=True)
    out = f"{file}___"
    with open(out, 'w', encoding='utf8') as f:
        df.to_json(f, orient='records', force_ascii=False, lines=True)
    Path(out).rename(file)

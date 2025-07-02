import os
from decimal import Decimal
from typing import List, Callable
from dotenv import load_dotenv
from calculator.calculation import Calculation

load_dotenv()
CSV_FILE = os.getenv("CSV_HISTORY_PATH", "default_history.csv")

import pandas as pd

def save_to_csv(history: List[Calculation], filename: str = CSV_FILE):
    df = pd.DataFrame([{
        "a": str(calc.a),
        "b": str(calc.b),
        "operation": calc.operation.__name__,
        "result": str(calc.perform())
    } for calc in history])
    df.to_csv(filename, index=False)

def load_from_csv(filename: str =CSV_FILE, operation_lookup: Callable[[str], Callable] = None) -> List[Calculation]:
    df = pd.read_csv(filename)
    history = []
    for _, row in df.iterrows():
        a, b = row['a'], row['b']
        operation = operation_lookup(row['operation'])
        if operation:
            history.append(Calculation(Decimal(a), Decimal(b), operation))
    return history

def clear_csv(filename: str = CSV_FILE):
    """Clear the CSV file."""
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"File {filename} does not exist.")
        
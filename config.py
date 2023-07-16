import yaml
from typing import Dict
import polars as pl

def get_secrets() -> Dict[str, int]:
    with open("secrets.yaml", "r") as stream:
        return yaml.safe_load(stream)  

USERNO_MAP = pl.DataFrame(get_secrets())

PAYMENT_DESCS = {
    "CAPITAL ONE AUTOPAY PYMT",
    "CAPITAL ONE ONLINE PYMT",
}

CATEGORIES = {
    "Entertainment",
    "Payment/Credit",
    "Lodging",
    "Other Travel",
    "Dining",
    "Health Care",
    "Gas/Automotive",
    "Fee/Interest Charge",
    "Other Services",
    "Merchandise",
}


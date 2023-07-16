import typer 
import logging
import polars as pl
from config import USERNO_MAP
from utils import find_filenames_by_ext

app = typer.Typer()

@app.command()
def display_payment_history(name: str) -> None:
    ph_df = pl.DataFrame()
    filenames = find_filenames_by_ext("data", ".csv")
    for filename in filenames:
        logging.info(f"Reading {filename}")
        if name == "all": 
            ph_df_by_file = pl.read_csv(filename)
        else: 
            cardno = USERNO_MAP.filter(pl.col("name") == name).select(pl.col("cardno")).row(0)[0]
            ph_df_by_file = pl.read_csv(filename).filter(pl.col("Card No.") == cardno)
        ph_df = pl.concat([ph_df, ph_df_by_file]).unique()
    print(ph_df)
    totals = ph_df.select(pl.col("Debit", "Credit").sum())
    print(totals)

if __name__ == "__main__":
    app()
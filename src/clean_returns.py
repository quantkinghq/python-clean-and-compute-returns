import os
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df = df.sort_values("date")
    df = df.drop_duplicates(subset=["date"], keep="last")
    df["price"] = df["price"].ffill()

    return df


def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["return"] = df["price"].pct_change()
    return df


def save_output(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def main():
    input_path = "data/raw/prices.csv"
    output_path = "data/processed/cleaned_prices_with_returns.csv"

    df = load_data(input_path)
    df = clean_data(df)
    df = compute_returns(df)
    save_output(df, output_path)

    print(df.head())
    print(f"Saved cleaned dataset to {output_path}")


if __name__ == "__main__":
    main()

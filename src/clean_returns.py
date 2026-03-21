import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Drop rows with invalid dates
    df = df.dropna(subset=["date"])

    # Sort
    df = df.sort_values("date")

    # Drop duplicate dates (keep last)
    df = df.drop_duplicates(subset=["date"], keep="last")

    # Fill missing prices
    df["price"] = df["price"].ffill()

    return df


def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["return"] = df["price"].pct_change()
    return df


def main():
    df = load_data("data/raw/prices.csv")
    df = clean_data(df)
    df = compute_returns(df)

    print(df.head())


if __name__ == "__main__":
    main()

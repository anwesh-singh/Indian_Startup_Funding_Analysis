import pandas as pd

def clean_data(input_file, output_file):
    # Load data
    df = pd.read_csv(input_file)

    # Convert all object columns to string (important fix)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()

    # Clean column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Handle missing or invalid AmountInUSD
    df['AmountInUSD'] = df['AmountInUSD'].replace("Undisclosed", None)

    # Remove commas and convert to numeric safely
    df['AmountInUSD'] = df['AmountInUSD'].astype(str).str.replace(",", "", regex=False)
    df['AmountInUSD'] = pd.to_numeric(df['AmountInUSD'], errors='coerce')

    # Fill missing CityLocation
    df['CityLocation'] = df['CityLocation'].replace("nan", "Unknown")
    df['CityLocation'] = df['CityLocation'].fillna("Unknown")

    # Drop rows where funding amount is missing
    df = df.dropna(subset=['AmountInUSD'])

    # Optional: reset index for clean output
    df = df.reset_index(drop=True)

    # Save cleaned file
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved at: {output_file}")

if __name__ == "__main__":
    clean_data("data/startup_funding.csv", "data/cleaned_funding_data.csv")

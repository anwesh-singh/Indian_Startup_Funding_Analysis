import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    return df

def yearly_funding(df):
    yearly = df.groupby('Year')['AmountInUSD'].sum().reset_index()
    plt.figure(figsize=(8,5))
    sns.lineplot(data=yearly, x='Year', y='AmountInUSD', marker='o')
    plt.title("Yearly Startup Funding in India")
    plt.xlabel("Year")
    plt.ylabel("Funding in USD")
    plt.tight_layout()
    plt.show()

def top_cities(df):
    top = df['CityLocation'].value_counts().head(10)
    plt.figure(figsize=(8,5))
    sns.barplot(x=top.values, y=top.index)
    plt.title("Top 10 Startup Cities")
    plt.xlabel("Number of Startups")
    plt.ylabel("City")
    plt.tight_layout()
    plt.show()

def top_sectors(df):
    top = df['IndustryVertical'].value_counts().head(10)
    plt.figure(figsize=(8,5))
    sns.barplot(x=top.values, y=top.index)
    plt.title("Top 10 Startup Sectors")
    plt.xlabel("Number of Startups")
    plt.ylabel("Sector")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_data("data/cleaned_funding_data.csv")
    
    # Analysis
    yearly_funding(df)
    top_cities(df)
    top_sectors(df)
    
    # Optional: Save top insights
    with open("reports/summary_report.txt", "w") as f:
        f.write("Indian Startup Funding Analysis - Summary\n")
        f.write(f"Total funding from {df['Year'].min()} to {df['Year'].max()}: ${df['AmountInUSD'].sum():,.2f}\n")
        f.write(f"Top 5 sectors:\n{df['IndustryVertical'].value_counts().head()}\n")
        f.write(f"Top 5 cities:\n{df['CityLocation'].value_counts().head()}\n")
    print("✅ Summary report saved at reports/summary_report.txt")

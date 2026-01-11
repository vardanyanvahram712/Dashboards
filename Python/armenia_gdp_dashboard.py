"""
Armenia GDP Dashboard

This script creates a comprehensive dashboard visualizing Armenia's GDP data
from the World Bank API. The dashboard includes:
- Line chart showing GDP trends over time
- Bar chart displaying annual GDP
- Area chart showing cumulative GDP
- Growth rate chart showing year-to-year changes
"""

import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors


def fetch_gdp_data():
    """
    Fetches GDP data for Armenia from World Bank API or loads from local CSV.
    
    Returns:
        DataFrame with Year and GDP columns
    """
    filename = "Data/arm_gdp.csv"
    
    if os.path.exists(filename):
        print("Loading data from local file...")
        return pd.read_csv(filename)
    
    print("Fetching data from World Bank API...")
    url = "https://api.worldbank.org/v2/country/AM/indicator/NY.GDP.MKTP.CD?format=json&per_page=500"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        if len(data) < 2 or not data[1]:
            print("No data available from API")
            return pd.DataFrame()
        
        records = data[1]
        years = []
        values = []
        
        for record in records:
            if record.get("value") is not None:
                years.append(int(record["date"]))
                values.append(float(record["value"]))
        
        # Create DataFrame and sort
        df = pd.DataFrame({"Year": years, "GDP": values})
        df = df.sort_values("Year").reset_index(drop=True)
        
        # Save to CSV for next time
        df.to_csv(filename, index=False)
        print(f"✓ Data saved to {filename}")
        
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()


def create_gdp_dashboard(df):
    """
    Creates a 2x2 dashboard with multiple GDP visualizations.
    
    Args:
        df: DataFrame with Year and GDP columns
    """
    # Calculate additional metrics
    df["Cumulative_GDP"] = df["GDP"].cumsum()
    df["Growth_Rate"] = df["GDP"].pct_change() * 100
    
    # Create 2x2 subplot layout
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.patch.set_facecolor('#f0f0f0')
    
    # 1. Line Chart - GDP over time
    axes[0, 0].plot(df["Year"], df["GDP"], marker="o", linewidth=2, color='#1f77b4')
    axes[0, 0].set_title("Line Chart — GDP Over Time", fontsize=12, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xlabel("Year")
    axes[0, 0].set_ylabel("GDP (USD)")
    for spine in axes[0, 0].spines.values():
        spine.set_visible(False)
    
    # Add interactive cursor
    cursor = mplcursors.cursor(axes[0, 0], hover=True)
    
    @cursor.connect("add")
    def on_hover(sel):
        x, y = sel.target
        sel.annotation.set_text(f"Year: {int(x)}\nGDP: ${y:,.0f}")
    
    # 2. Bar Chart - Annual GDP
    axes[0, 1].bar(df["Year"], df["GDP"], color='#2ca02c', alpha=0.7)
    axes[0, 1].set_title("Bar Chart — Annual GDP", fontsize=12, fontweight='bold')
    axes[0, 1].grid(axis="y", alpha=0.3)
    axes[0, 1].set_xlabel("Year")
    axes[0, 1].set_ylabel("GDP (USD)")
    for spine in axes[0, 1].spines.values():
        spine.set_visible(False)
    
    # 3. Area Chart - Cumulative GDP
    axes[1, 0].fill_between(df["Year"], df["Cumulative_GDP"], alpha=0.4, color='#ff7f0e')
    axes[1, 0].plot(df["Year"], df["Cumulative_GDP"], linewidth=2, color='#ff7f0e')
    axes[1, 0].set_title("Area Chart — Cumulative GDP", fontsize=12, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xlabel("Year")
    axes[1, 0].set_ylabel("Cumulative GDP (USD)")
    for spine in axes[1, 0].spines.values():
        spine.set_visible(False)
    
    # 4. Growth Rate Chart
    growth_df = df.dropna(subset=["Growth_Rate"]).reset_index(drop=True)
    colors = ['green' if x > 0 else 'red' for x in growth_df["Growth_Rate"]]
    axes[1, 1].bar(growth_df["Year"], growth_df["Growth_Rate"], color=colors, alpha=0.7)
    axes[1, 1].axhline(0, color="black", linewidth=0.8)
    axes[1, 1].set_title("Growth Rate (%) — Year-to-Year", fontsize=12, fontweight='bold')
    axes[1, 1].grid(axis="y", alpha=0.3)
    axes[1, 1].set_xlabel("Year")
    axes[1, 1].set_ylabel("Growth Rate (%)")
    for spine in axes[1, 1].spines.values():
        spine.set_visible(False)
    
    # Rotate x-axis labels for better readability
    for ax in axes.flatten():
        for label in ax.get_xticklabels():
            label.set_rotation(45)
    
    # Dashboard title
    plt.suptitle("Armenia GDP Dashboard", 
                 fontsize=22, color='black', fontweight='bold', y=0.98)
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def main():
    """Main function to fetch data and create dashboard."""
    df = fetch_gdp_data()
    
    if df.empty:
        print("✗ No data available to visualize")
        return
    
    print(f"✓ Loaded {len(df)} records")
    print("Generating dashboard...")
    
    create_gdp_dashboard(df)


if __name__ == "__main__":
    main()

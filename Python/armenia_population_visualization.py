"""
Armenia Population Visualization

This script fetches population data for Armenia from the World Bank API
and creates a bar chart visualization showing population trends over time.
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt


def fetch_armenia_population_data():
    """
    Fetches population data for Armenia from World Bank API.
    
    Returns:
        List of dictionaries containing population and year data
    """
    url = "https://api.worldbank.org/v2/country/ARM/indicator/SP.POP.TOTL?format=json&per_page=100"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if len(data) < 2 or not data[1]:
            return []
        
        population_records = data[1]
        cleaned_data = []
        
        for record in population_records:
            cleaned_record = {
                "population": record.get("value"),
                "year": record.get("date")
            }
            cleaned_data.append(cleaned_record)
        
        return cleaned_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def visualize_population_trends(data):
    """
    Creates a bar chart visualization of Armenia's population over time.
    
    Args:
        data: List of dictionaries with 'year' and 'population' keys
    """
    df = pd.DataFrame(data)
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df = df.sort_values('year')
    
    plt.figure(figsize=(12, 6))
    plt.bar(df['year'], df['population'], color='#2e7d32', alpha=0.8)
    plt.title("Population of Armenia Over Time", fontsize=16, fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    """Main function to fetch and visualize population data."""
    print("Fetching Armenia population data from World Bank API...")
    
    population_data = fetch_armenia_population_data()
    
    if not population_data:
        print("✗ Failed to fetch population data")
        return
    
    print(f"✓ Successfully fetched {len(population_data)} records")
    print("Generating visualization...")
    
    visualize_population_trends(population_data)


if __name__ == "__main__":
    main()

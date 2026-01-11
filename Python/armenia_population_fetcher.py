"""
Armenia Population Data Fetcher

This script fetches population data for Armenia from the World Bank API
and saves it in a structured format for further analysis.
"""

import requests
import json


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
            print("No data available from API")
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


def main():
    """Main function to fetch and display population data."""
    print("Fetching Armenia population data from World Bank API...")
    
    population_data = fetch_armenia_population_data()
    
    if population_data:
        print(f"\n✓ Successfully fetched {len(population_data)} records")
        print("\nSample data:")
        for record in population_data[:5]:
            print(f"  Year: {record['year']}, Population: {record['population']}")
    else:
        print("✗ Failed to fetch population data")


if __name__ == "__main__":
    main()

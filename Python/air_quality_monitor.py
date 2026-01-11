"""
Air Quality Monitoring Stations

This script fetches air quality data from multiple monitoring stations
using the World Air Quality Index (WAQI) API and visualizes:
- Air Quality Index (AQI) per station
- PM2.5 levels per station
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt


def fetch_station_data(station_ids, api_token):
    """
    Fetches air quality data for multiple stations.
    
    Args:
        station_ids: List of station IDs
        api_token: WAQI API token
    
    Returns:
        List of dictionaries containing station information
    """
    all_stations_data = []
    
    for station_id in station_ids:
        try:
            url = f"https://api.waqi.info/feed/@{station_id}/?token={api_token}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            json_data = response.json()
            data = json_data.get("data", {})
            
            station_info = {
                "station_id": station_id,
                "name": data.get("city", {}).get("name", "Unknown"),
                "aqi": data.get("aqi"),
                "pm25": data.get("iaqi", {}).get("pm25", {}).get("v")
            }
            
            all_stations_data.append(station_info)
        
        except Exception as e:
            print(f"Failed to get data for station {station_id}: {e}")
    
    return all_stations_data


def visualize_air_quality(df):
    """
    Creates visualizations for air quality data.
    
    Args:
        df: DataFrame with station data
    """
    # Create shortened names for better display
    df['short_name'] = df['name'].apply(
        lambda x: x if len(x) <= 12 else x[:12] + '…'
    )
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # AQI Chart
    axes[0].bar(df['short_name'], df['aqi'], color='#3498db', alpha=0.8)
    axes[0].set_title("Air Quality Index (AQI) per Station", 
                      fontsize=14, fontweight='bold')
    axes[0].set_ylabel("AQI", fontsize=12)
    axes[0].grid(axis='y', alpha=0.3)
    for label in axes[0].get_xticklabels():
        label.set_rotation(45)
    
    # PM2.5 Chart
    axes[1].bar(df['short_name'], df['pm25'], color='#e67e22', alpha=0.8)
    axes[1].set_title("PM2.5 Levels per Station", 
                      fontsize=14, fontweight='bold')
    axes[1].set_ylabel("PM2.5 (µg/m³)", fontsize=12)
    axes[1].grid(axis='y', alpha=0.3)
    for label in axes[1].get_xticklabels():
        label.set_rotation(45)
    
    plt.tight_layout()
    plt.show()


def main():
    """Main function to fetch and visualize air quality data."""
    # Note: Replace with your own API token
    api_token = "c1d1b901dbda346250e15e057b4f8bd180d0187a"
    station_ids = ['A523555', 'A519781', 'A517234', 'A493552', 'A493621', 'A523558']
    
    print("Fetching air quality data from WAQI API...")
    
    stations_data = fetch_station_data(station_ids, api_token)
    
    if not stations_data:
        print("✗ No data retrieved")
        return
    
    print(f"✓ Successfully fetched data from {len(stations_data)} stations")
    
    # Create DataFrame
    df = pd.DataFrame(stations_data)
    df['aqi'] = pd.to_numeric(df['aqi'], errors='coerce')
    df['pm25'] = pd.to_numeric(df['pm25'], errors='coerce')
    
    print("\nGenerating visualizations...")
    visualize_air_quality(df)


if __name__ == "__main__":
    main()

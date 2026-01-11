# API Documentation

This document lists all external APIs used in this portfolio project.

## 🌐 APIs Used

### 1. **World Bank API**
**Used in:**
- `Python/armenia_gdp_dashboard.py`
- `Python/armenia_population_visualization.py`
- `Python/armenia_population_fetcher.py`

**Base URL:** `https://api.worldbank.org/v2/`

**Endpoints Used:**
- **GDP Data:** `/country/AM/indicator/NY.GDP.MKTP.CD?format=json&per_page=500`
- **Population Data:** `/country/ARM/indicator/SP.POP.TOTL?format=json&per_page=100`

**Description:**
The World Bank API provides access to economic and social development data. We use it to fetch:
- Armenia's GDP (Gross Domestic Product) data over time
- Armenia's population statistics

**Authentication:** None required (public API)

**Rate Limits:** 
- No official rate limits documented
- Recommended: Reasonable request frequency

**Documentation:** [World Bank API Documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)

---

### 2. **World Air Quality Index (WAQI) API**
**Used in:**
- `Python/air_quality_monitor.py`

**Base URL:** `https://api.waqi.info/`

**Endpoints Used:**
- **Station Data:** `/feed/@{station_id}/?token={api_token}`

**Description:**
The WAQI API provides real-time air quality data from monitoring stations worldwide. We use it to:
- Fetch air quality index (AQI) data
- Retrieve PM2.5 levels from multiple stations
- Monitor air quality across different locations

**Authentication:** 
- API token required
- Token stored in code (should be moved to environment variables in production)

**Rate Limits:**
- Free tier: Limited requests per day
- Check [WAQI API documentation](https://aqicn.org/api/) for current limits

**Documentation:** [WAQI API Documentation](https://aqicn.org/api/)

**Note:** 
⚠️ **Security Best Practice:** API tokens should be stored in environment variables or configuration files (not committed to Git). For this portfolio, the token is visible in the code for demonstration purposes.

---

## 🔐 API Key Management

### Current Implementation
API keys are currently stored directly in the code files. This is acceptable for portfolio/demonstration purposes but should be changed for production use.

### Recommended Approach for Production

1. **Environment Variables:**
   ```python
   import os
   api_token = os.getenv('WAQI_API_TOKEN')
   ```

2. **Configuration Files:**
   - Store keys in `.env` file (add to `.gitignore`)
   - Use `python-dotenv` to load variables

3. **Secret Management:**
   - Use cloud secret managers (AWS Secrets Manager, Azure Key Vault, etc.)
   - Never commit secrets to version control

---

## 📊 API Usage Summary

| API | Purpose | Authentication | Rate Limits |
|-----|---------|----------------|-------------|
| World Bank API | Economic & population data | None | None (reasonable use) |
| WAQI API | Air quality data | Token required | Limited (free tier) |

---

## 🚀 Getting Started with APIs

### World Bank API
No setup required - it's a public API:
```python
import requests
url = "https://api.worldbank.org/v2/country/AM/indicator/NY.GDP.MKTP.CD?format=json"
response = requests.get(url)
```

### WAQI API
1. Sign up at [aqicn.org](https://aqicn.org/api/)
2. Get your API token
3. Use in code:
```python
token = "your_token_here"
url = f"https://api.waqi.info/feed/@{station_id}/?token={token}"
```

---

## 📝 Notes

- All APIs used are publicly available or have free tiers
- Data fetched from APIs is cached locally when possible (see `arm_gdp.csv`)
- API responses are handled with proper error checking and timeouts
- For production use, implement proper error handling, retries, and rate limiting

---

**Last Updated:** 2025

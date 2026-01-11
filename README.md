# Data Analytics & Visualization Portfolio

A comprehensive collection of data analytics projects showcasing skills in Python, data visualization, database management, and business intelligence tools.

## 📊 Project Overview

This portfolio contains various projects demonstrating proficiency in:
- **Data Analysis & Processing**: Python (Pandas, NumPy)
- **Data Visualization**: Matplotlib, Looker Studio, Power BI, Excel
- **Database Management**: MySQL, MongoDB
- **API Integration**: World Bank API, Air Quality API
- **Financial Analysis**: Loan risk assessment, personal finance tracking

---

## 🐍 Python Projects

### 1. **Loan Reliability Scorer** (`loan_reliability_scorer.py`)
A comprehensive loan risk assessment tool that calculates reliability scores for loan applicants based on:
- Employment length (25% weight)
- Loan status (35% weight)
- Loan purpose (20% weight)
- Payment activity (20% weight)

**Features:**
- Data cleaning and preprocessing
- Multi-factor scoring algorithm
- CSV export functionality
- Error handling and data validation

**Technologies:** Pandas, DateTime

---

### 2. **Armenia GDP Dashboard** (`armenia_gdp_dashboard.py`)
Interactive dashboard visualizing Armenia's GDP data from the World Bank API.

**Visualizations:**
- Line chart showing GDP trends over time
- Bar chart displaying annual GDP values
- Area chart showing cumulative GDP
- Growth rate chart with year-to-year changes

**Features:**
- API integration with local caching
- Interactive hover tooltips
- Multiple chart types in a single dashboard
- Automatic data refresh capability

**Technologies:** Pandas, Matplotlib, Requests, mplcursors

---

### 3. **Armenia Population Visualization** (`armenia_population_visualization.py`)
Fetches and visualizes Armenia's population data from the World Bank API.

**Features:**
- Real-time API data fetching
- Bar chart visualization
- Data cleaning and formatting
- Error handling

**Technologies:** Pandas, Matplotlib, Requests

---

### 4. **Air Quality Monitor** (`air_quality_monitor.py`)
Monitors air quality from multiple stations using the World Air Quality Index (WAQI) API.

**Features:**
- Multi-station data aggregation
- AQI (Air Quality Index) visualization
- PM2.5 levels tracking
- Comparative analysis across stations

**Technologies:** Pandas, Matplotlib, Requests

---

### 5. **BMI Calculator** (`bmi_calculator.py`)
Health assessment tool that calculates Body Mass Index and categorizes results.

**Features:**
- BMI calculation with health categorization
- Input validation
- User-friendly interface
- Health category classification (Underweight, Normal, Overweight, Obese)

**Technologies:** Python Standard Library

---

### 6. **Personal Finance Calculator** (`personal_finance_calculator.py`)
Personal finance analysis tool for tracking income, expenses, and savings.

**Features:**
- Income and expense tracking
- Percentage calculations
- Savings status assessment
- Financial summary reports

**Technologies:** Python Standard Library

---

### 7. **Rectangle Area Calculator** (`rectangle_area_calculator.py`)
Simple geometric calculator with categorization.

**Features:**
- Area calculation
- Size categorization (Large, Normal, Small)
- Input validation

**Technologies:** Python Standard Library

---

## 📈 Data Visualization Projects

### Looker Studio Dashboards
📁 **Location:** `LookerStudio_Dashboards/`

**Project:** Healthy Eating Dashboard
- **Data Source:** Kaggle
- **Live Dashboard:** [View Interactive Dashboard](https://lookerstudio.google.com/reporting/39f0ddc8-6a79-4c9f-95da-b63885083b9c/page/lRadF)
- **Features:**
  - Interactive data exploration
  - Multiple visualization types
  - Real-time data updates
  - Nutritional analysis and food pattern tracking

📄 **See detailed documentation:** [LookerStudio_Dashboards/README.md](LookerStudio_Dashboards/README.md)

---

### Excel Dashboards
📁 **Location:** `Excel_Dashboards/`

**Project:** Flight Data 2024 Dashboard
- **Data Source:** Kaggle
- **Features:**
  - Flight data analysis
  - Interactive Excel dashboards
  - Pivot tables and charts
  - Performance metrics and route analysis

📄 **See detailed documentation:** [Excel_Dashboards/README.md](Excel_Dashboards/README.md)

---

### Power BI Dashboards
📁 **Location:** `PowerBI_Dashboards/`

#### 1. **Bank Loans Dashboard** (`Bank_Loans_Dashboard.pbix`)
- Loan portfolio analysis
- Risk assessment visualizations
- Performance metrics
- Payment trends and collection rates

#### 2. **Sales Summary Dashboard** (`Sales_Summary_Dashboard.pbix`)
- Sales performance tracking
- Revenue analysis
- Trend visualizations
- Product and customer insights

📄 **See detailed documentation:** [PowerBI_Dashboards/README.md](PowerBI_Dashboards/README.md)

---

## 🗄️ Database Projects
📁 **Location:** `Databases/`

### MySQL Projects
- **JOIN Operations** (`task JOIN`): Complex query practice with multiple table joins
- **ExplorePlaces Database** (`Tasks for ExplorePlaces Database`): Database exploration and analysis tasks
- **Advanced SQL**: Subqueries, CTEs, and complex queries

### MongoDB Projects
- **Filtering Practice** (`MongoDB Filtering Practice`): Document filtering and query optimization
- **Data Aggregation**: Advanced MongoDB operations and pipelines

📄 **See detailed documentation:** [Databases/README.md](Databases/README.md)

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas matplotlib requests mplcursors openpyxl
```

### Running Python Projects
```bash
# Example: Run the GDP Dashboard
cd Python
python armenia_gdp_dashboard.py

# Example: Run the Loan Reliability Scorer
python loan_reliability_scorer.py
```

### Data Files
All data files (Excel, CSV) are located in the `Data/` folder:
- `Data/loan_data.xlsx` - Required for loan reliability scorer
- `Data/arm_gdp.csv` - Auto-generated by GDP dashboard (or can be provided)
- `Data/loan_data_with_reliability.csv` - Output from loan reliability scorer
- `Data/healthy_eating.xlsx` - Data for Looker Studio dashboard

---

## 📁 Project Structure

```
Training_Projects/
├── Data/                          # All data files (Excel, CSV)
│   ├── loan_data.xlsx
│   ├── loan_data_with_reliability.csv
│   ├── loan_data_with_reliability.xlsx
│   ├── arm_gdp.csv
│   └── healthy_eating.xlsx
│
├── Python/                        # Python data analysis projects
│   ├── loan_reliability_scorer.py
│   ├── armenia_gdp_dashboard.py
│   ├── armenia_population_visualization.py
│   ├── air_quality_monitor.py
│   ├── bmi_calculator.py
│   ├── personal_finance_calculator.py
│   ├── rectangle_area_calculator.py
│   └── requirements.txt
│
├── PowerBI_Dashboards/            # Power BI interactive dashboards
│   ├── Bank_Loans_Dashboard.pbix
│   ├── Bank_Loans_Dashboard.pdf
│   ├── Sales_Summary_Dashboard.pbix
│   ├── Sales_Summary_Dashboard.pdf
│   └── README.md
│
├── LookerStudio_Dashboards/       # Looker Studio dashboards
│   ├── Healthy_Eating_Dashboard.pdf
│   └── README.md
│
├── Excel_Dashboards/              # Excel-based dashboards
│   ├── flight_data_2024_sample/
│   └── README.md
│
├── Databases/                     # SQL and NoSQL database projects
│   ├── MongoDB Filtering Practice/
│   ├── task JOIN/
│   ├── Tasks for ExplorePlaces Database/
│   └── README.md
│
└── README.md                      # Main project documentation
```

---

## 🛠️ Technologies Used

- **Programming Languages:** Python
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Looker Studio, Power BI, Excel
- **APIs:** World Bank API, WAQI API (see [APIs.md](APIs.md) for details)
- **Databases:** MySQL, MongoDB
- **File Formats:** CSV, Excel, JSON

---

## 📝 Key Skills Demonstrated

✅ **Data Analysis & Processing**
- Data cleaning and preprocessing
- Statistical analysis
- Data transformation

✅ **Data Visualization**
- Interactive dashboards
- Multiple chart types
- Real-time data visualization

✅ **API Integration**
- RESTful API consumption
- Data fetching and caching
- Error handling

✅ **Database Management**
- SQL queries and joins
- MongoDB operations
- Data modeling

✅ **Business Intelligence**
- Dashboard creation
- KPI tracking
- Financial analysis

---

## 🔗 Quick Links

- **Looker Studio Dashboard:** [Healthy Eating Dashboard](https://lookerstudio.google.com/reporting/39f0ddc8-6a79-4c9f-95da-b63885083b9c/page/lRadF)
- **Power BI Dashboards:** [PowerBI_Dashboards/README.md](PowerBI_Dashboards/README.md)
- **Database Projects:** [Databases/README.md](Databases/README.md)
- **Excel Dashboards:** [Excel_Dashboards/README.md](Excel_Dashboards/README.md)
- **Looker Studio:** [LookerStudio_Dashboards/README.md](LookerStudio_Dashboards/README.md)
- **API Documentation:** [APIs.md](APIs.md)

---

## 📧 Contact

For questions or collaboration opportunities, please reach out through GitHub.

---

## 📄 License

This portfolio is for demonstration purposes. All projects are created for learning and portfolio showcase.

---

**Last Updated:** 2025
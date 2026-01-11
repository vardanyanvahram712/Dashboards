"""
Loan Reliability Score Calculator

This script analyzes loan data and calculates a reliability score for each loan
based on employment length, loan status, purpose, and payment activity.
The score helps assess the creditworthiness and risk of loan applicants.
"""

import pandas as pd
from datetime import datetime


def clean_employment_length(emp_length):
    """
    Cleans employment length field:
    - <1 year -> 1 year
    - 10+ years -> 10 years
    - Handles missing values
    
    Args:
        emp_length: Employment length string (e.g., "<1 year", "10+ years")
    
    Returns:
        Cleaned employment length string or "Unknown"
    """
    if pd.isna(emp_length):
        return "Unknown"

    emp_length = str(emp_length)
    
    # Remove special symbols
    emp_length = emp_length.replace("<", "")
    emp_length = emp_length.replace(">", "")
    emp_length = emp_length.replace("+", "")
    emp_length = emp_length.replace("-", "")
    
    # Normalize spaces
    emp_length = emp_length.strip()
    
    return emp_length


def calculate_employment_score(emp_length):
    """
    Calculates employment length score (0.4 to 1.0).
    
    Args:
        emp_length: Cleaned employment length string
    
    Returns:
        Score between 0.4 and 1.0
    """
    if emp_length == "Unknown":
        return 0.4

    emp_length = emp_length.lower()

    if "10" in emp_length:
        return 1.0
    if "5" in emp_length:
        return 0.8
    if "1" in emp_length:
        return 0.6

    return 0.4


def calculate_loan_status_score(status):
    """
    Calculates loan status score based on payment history.
    
    Args:
        status: Loan status (e.g., "Fully Paid", "Current", "Charged Off")
    
    Returns:
        Score between 0.1 and 1.0
    """
    if status == "Fully Paid":
        return 1.0
    if status == "Current":
        return 0.8
    if status in ["Late", "In Grace Period"]:
        return 0.4
    return 0.1  # Charged Off / Default


def calculate_purpose_score(purpose):
    """
    Calculates loan purpose score based on risk assessment.
    
    Args:
        purpose: Loan purpose (e.g., "medical", "education", "home")
    
    Returns:
        Score between 0.4 and 0.9
    """
    if pd.isna(purpose):
        return 0.6

    purpose = purpose.lower()

    if "medical" in purpose or "debt" in purpose:
        return 0.4
    if "education" in purpose or "home" in purpose:
        return 0.9

    return 0.6


def calculate_payment_activity_score(last_payment_date):
    """
    Calculates payment activity score based on recency of last payment.
    
    Args:
        last_payment_date: Last payment date (datetime)
    
    Returns:
        Score between 0.3 and 1.0
    """
    if pd.isna(last_payment_date):
        return 0.3

    days_since_payment = (datetime.now() - last_payment_date).days

    if days_since_payment < 30:
        return 1.0
    if days_since_payment < 90:
        return 0.7

    return 0.4


def calculate_reliability_score(row):
    """
    Calculates overall reliability score for a loan record.
    
    Args:
        row: DataFrame row containing loan information
    
    Returns:
        Reliability score (0-100)
    """
    score = (
        calculate_employment_score(row["Emp_Length_Clean"]) * 0.25 +
        calculate_loan_status_score(row["Loan_Status"]) * 0.35 +
        calculate_purpose_score(row["Purpose"]) * 0.20 +
        calculate_payment_activity_score(row["Last_Payment_Date"]) * 0.20
    )
    return round(score * 100, 2)


def main():
    """Main function to process loan data and calculate reliability scores."""
    # Load Excel file
    df = pd.read_excel("Data/loan_data.xlsx")

    # Convert date columns
    df["Last_Payment_Date"] = pd.to_datetime(
        df["Last_Payment_Date"], errors="coerce"
    )

    # Clean employment length
    df["Emp_Length_Clean"] = df["Emp_Length"].apply(clean_employment_length)

    # Calculate reliability scores
    df["Reliability_Score (%)"] = df.apply(calculate_reliability_score, axis=1)

    # Save to CSV
    output_path = "Data/loan_data_with_reliability.csv"
    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )

    print("✓ Loan data processed successfully!")
    print(f"✓ Output saved to: {output_path}")
    print(f"✓ Total records processed: {len(df)}")


if __name__ == "__main__":
    main()

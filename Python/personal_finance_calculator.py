"""
Personal Finance Calculator

This script helps analyze personal finances by calculating:
- Total income and expenses
- Remaining balance
- Income and expense percentages
- Savings status based on remaining balance
"""


def calculate_financial_metrics(income, expenses):
    """
    Calculates financial metrics from income and expenses.
    
    Args:
        income: Monthly income
        expenses: Monthly expenses
    
    Returns:
        Dictionary containing financial metrics
    """
    total = income + expenses
    remaining = income - expenses
    income_percent = (income / total * 100) if total > 0 else 0
    expenses_percent = (expenses / total * 100) if total > 0 else 0
    
    return {
        'total': total,
        'remaining': remaining,
        'income_percent': income_percent,
        'expenses_percent': expenses_percent
    }


def assess_savings_status(remaining):
    """
    Assesses savings status based on remaining balance.
    
    Args:
        remaining: Remaining balance after expenses
    
    Returns:
        Savings status message
    """
    if remaining > 20:
        return "You are saving money."
    elif remaining < 20:
        return "You need to save more."
    else:
        return "You are breaking even."


def main():
    """Main function to get user input and calculate financial metrics."""
    print("Personal Finance Calculator")
    print("-" * 30)
    
    try:
        income = float(input("Enter monthly income: "))
        expenses = float(input("Enter monthly expenses: "))
        
        if income < 0 or expenses < 0:
            print("Error: Income and expenses must be non-negative numbers")
            return
        
        metrics = calculate_financial_metrics(income, expenses)
        savings_status = assess_savings_status(metrics['remaining'])
        
        print("\n" + "=" * 30)
        print("Financial Summary")
        print("=" * 30)
        print(f"Income: ${income:,.2f} ({metrics['income_percent']:.1f}%)")
        print(f"Expenses: ${expenses:,.2f} ({metrics['expenses_percent']:.1f}%)")
        print(f"Remaining: ${metrics['remaining']:,.2f}")
        print(f"\nStatus: {savings_status}")
    
    except ValueError:
        print("Error: Please enter valid numbers")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")


if __name__ == "__main__":
    main()

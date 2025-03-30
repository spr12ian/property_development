# Given purchase price
purchase_price = 350000

# SDLT bands for Second Home Buyer / Limited Company
bands = [(125000, 0.05), (125000, 0.07), (100000, 0.10)]  # (band amount, tax rate)

# Calculate SDLT
sdlt = sum(min(purchase_price, band) * rate for band, rate in bands)
print(sdlt)

# Given values
sale_price = 490000
profit = sale_price - purchase_price  # Capital gain
corporation_tax_rate = 0.25  # Assuming 25% rate
basic_income_tax_rate = 0.20  # Basic rate for individuals
dividend_basic_rate = 0.0875  # Dividend tax basic rate
dividend_allowance = 500  # Dividend tax-free allowance per person
num_people = 3  # Three individuals sharing profit
cgt_allowance = 3000  # CGT allowance for individuals

# Recalculate for Individuals/Partnership/LLP
individual_profit = profit / num_people
taxable_income = individual_profit - 12570  # Personal allowance deduction
individual_tax = max(0, taxable_income) * basic_income_tax_rate
total_individual_tax = individual_tax * num_people

# Recalculate for Limited Company
corp_tax = profit * corporation_tax_rate
post_corp_profit = profit - corp_tax
dividend_per_person = post_corp_profit / num_people

# Apply dividend tax after allowance
taxable_dividend = max(0, dividend_per_person - dividend_allowance)
dividend_tax_per_person = taxable_dividend * dividend_basic_rate
total_dividend_tax = dividend_tax_per_person * num_people

# Net profits
net_profit_individual = profit - total_individual_tax - sdlt
net_profit_llp = net_profit_individual  # LLP is taxed similarly
net_profit_ltd = profit - corp_tax - total_dividend_tax - sdlt

# Updated comparison table
comparison_results = {
    "Individual": {"SDLT": sdlt, "Total Tax": total_individual_tax, "Net Profit": net_profit_individual},
    "Partnership": {"SDLT": sdlt, "Total Tax": total_individual_tax, "Net Profit": net_profit_individual},
    "LLP": {"SDLT": sdlt, "Total Tax": total_individual_tax, "Net Profit": net_profit_llp},
    "Limited Company": {"SDLT": sdlt, "Total Tax": corp_tax + total_dividend_tax, "Net Profit": net_profit_ltd},
}

print(comparison_results)

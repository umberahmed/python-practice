def solve(meal_cost, tip_percent, tax_percent):     # function defined as solve and takes 3 parameters, meal cost, tip percent and tax percent
    """Calculates a meal cost, including tip and tax""" #
    tip = float(tip_percent) / 100  # tip variable created to calculate tip percent
    total_tip = meal_cost * tip     # total tip variable created to calculate meal with tip
    tax = float(tax_percent) / 100  # tax variable created to calculate tax percentage
    total_tax = meal_cost * tax     # total tax variable created to calculate meal with tax
    total_meal_cost = meal_cost + total_tip + total_tax # final cost of meal, including tip and tax
    return "The total meal cost is {} dollars.".format(int(total_meal_cost))

print solve(15.50, 15, 10)
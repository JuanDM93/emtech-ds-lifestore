"""
PROJECT 1
This is a data science use case solution using python basics
author: juan_dm93@hotmail.com
"""
# Imports
from utils.frontend import login
from utils.backend import *


#### TESTING
def test():
    cat = ['procesadores', 'audifonos']
    
    sales = global_sales()
    sold = least_sold(sales, cat)[:50]
    print(f'least_sold {get_categories(sold)}:')
    print(sold)
    
    searches = global_searches()
    searched = most_searched(cat)[:100]
    print(f'most_searched {get_categories(searched)}:')
    print(searched)
    
    stockes = global_stocks()
    stocked = lowest_stock(cat)
    print(f'lowest_stock {get_categories(stocked)}:')
    print(stocked)

    reviews = total_reviewes()
    reviewed = most_reviewed(cat)[:20]
    print(f'most_reviewed {get_categories(reviewed)}:')
    print(reviewed)
    
    refs = total_refunds()
    refunds = most_refund(cat)
    print(f'most_refund {get_categories(refunds)}:')
    print(refunds)

    revenues = total_revenue()
    revenue = least_revenue(cat)
    print(f'least_revenue {get_categories(revenue)}:')
    print(revenue)

    monthly = monthly_sales(most_sold(sales, cat), '01')
    print(f'monthly_sales {get_categories(monthly)}:')
    print(monthly)
####

# main program
def main():
    # GLOBALS
    CATEGORIES = get_categories()
    
    login()
    test()


if __name__ == "__main__":
    main()

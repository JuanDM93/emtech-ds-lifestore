"""
PROJECT 1
This is a basic python based data science solution
author: juan_dm93@hotmail.com
"""
# Imports
from utils.frontend import login
from utils.backend import *


#### TESTING
def test(c:str):
    cats = [c]

    searches = clean_list(global_searches())
    if len(searches) > 0:
        cats_searched = clean_list(filter_categories(searches, cats))

        if len(cats_searched) > 0:
            most_searched = custom_sort(cats_searched)[:10]
            print(f'most_searched {get_categories(most_searched)}:')
            print(most_searched)

    sales = clean_list(global_sales())
    if len(sales) > 0:
        cats_sold = clean_list(filter_categories(sales, cats))
        
        if len(cats_sold) > 0:
            least_sold = custom_sort(cats_sold, False)[:10]
            print(f'least_sold {get_categories(least_sold)}:')
            print(least_sold)

            monthly_sold = clean_list(filter_months(cats_sold, '01'))
            if len(monthly_sold) > 0:
                most_sold = custom_sort(monthly_sold)[:10]
                print(f'monthly_sales {get_categories(most_sold)}:')
                print(most_sold)
    
        reviews = clean_list(get_reviews(sales))
        if len(reviews) > 0:
            cats_reviewed = clean_list(filter_categories(reviews, cats))
        
            if len(cats_reviewed) > 0:
                most_reviewed = custom_sort(cats_reviewed)[:10]
                print(f'most_reviewed {get_categories(most_reviewed)}:')
                print(most_reviewed)

        stocks = get_stocks(sales)
        if len(stocks) > 0:
            cats_stocked = filter_categories(stocks, cats)
            if len(cats_stocked) > 0:
                lowest_stock = custom_sort(cats_stocked, False)
                print(f'lowest_stock {get_categories(lowest_stock)}:')
                print(lowest_stock)
    
        refunds = get_refunds(sales)
        if len(refunds) > 0:
            cats_refunds = filter_categories(refunds, cats)
            if len(cats_refunds) > 0:
                most_refund = custom_sort(cats_refunds)
                print(f'most_refund {get_categories(most_refund)}:')
                print(most_refund)

        revenues = get_revenue(sales)
        if len(revenues) > 0:
            cats_revenue = filter_categories(revenues, cats)
            if len(cats_revenue) > 0:
                least_revenue = custom_sort(cats_revenue, False)
                print(f'least_revenue {get_categories(least_revenue)}:')
                print(least_revenue)
####


def run(cats):
    for c in cats:
        print(f'"{c}" ->')
        test(c)


# main program
def main():
    CATEGORIES = get_categories()
    
    login()
    run(CATEGORIES)


if __name__ == "__main__":
    main()

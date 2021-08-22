"""
PROJECT 1
This is a data science use case solution using python basics
author: juan_dm93@hotmail.com
"""
# Datasets
from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products


# Login
def login():
    """
    user:       admin
    password:   pass
    """
    def ask():
        admin = input('Input admin user: ')
        secret = input('Password: ')
        return admin, secret
    
    admin, secret = ask()
    while 'admin' != admin or 'pass' != secret:
        print('Login failed... try again')
        admin, secret = ask()
    print('Login succesful!')


# Utils
def get_product(id:int) -> list:
    """
    returns: product object from dataset
    """
    return lifestore_products[id - 1]


def get_sale(id:int) -> list:
    """
    returns: sale object from dataset
    """
    return lifestore_sales[id - 1]


def get_categorie(product_id:int) -> str:
    """
    returns: categorie str from product_id
    """
    return lifestore_products[product_id - 1][3]
        

def get_categories(data:list=lifestore_products) -> list:
    """
    data: any list with product_id at [0]
    returns: categories list from input
    """
    categories = []
    for d in data:
        cat = get_categorie(d[0])
        if cat not in categories:
            categories.append(cat)
    return categories


def filter_by_categories(data:list, cats:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    cats: a custom categories list
    returns: list of products filtered by cats
    """
    result = []
    for d in data:
        p = get_product(d[0])
        if p[3] in cats:
            result.append(d)
    return result


# Sales
def global_sales() -> list:
    """
    returns: sales list by product
    """
    total_sales = [[p[0], []] for p in lifestore_products]
    for sale in lifestore_sales:
        total_sales[sale[1] - 1][1].append(sale[0])
    return total_sales


def most_sold(categories:list=['procesadores']) -> list:
    """
    returns: sorted most sold products list by category
    """
    result = global_sales()
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return filter_by_categories(result, categories)


def least_sold(categories:list=['procesadores']) -> list:
    """
    returns: sorted least sold products list by category
    """
    result = global_sales()
    result.sort(key=lambda p: len(p[-1]), reverse=False)
    return filter_by_categories(result, categories)


# Searches
def global_searches() -> list:
    """
    returns: search list by product
    """ 
    total_searches = [[p[0], []] for p in lifestore_products]
    for search in lifestore_searches:
        total_searches[search[1] - 1][1].append(search[0])
    return total_searches


def most_searched(categories:list=['procesadores']) -> list:
    """
    returns: sorted most searched products list
    """
    result = global_searches()
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return filter_by_categories(result, categories)


def least_searched(categories:list=['procesadores']) -> list:
    """
    returns: sorted least searched products list by category
    """
    result = global_searches()
    result.sort(key=lambda p: len(p[-1]), reverse=False)
    return filter_by_categories(result, categories)


# Stocks
def global_stocks() -> list:
    """
    returns: products in stock 
    """
    return [[p[0], p[-1]] for p in lifestore_products]


def lowest_stock(categories:list=['procesadores']) -> list:
    """
    low_limit: how low to warn
    returns: sorted low stock products list by category
    """
    result = global_stocks()
    result.sort(key=lambda p: p[1], reverse=False)
    return filter_by_categories(result, categories)


def most_stock(categories:list=['procesadores']) -> list:
    """
    low_limit: how low to warn
    returns: sorted low stock products list by category
    """
    result = global_stocks()
    result.sort(key=lambda p: p[1], reverse=True)
    return filter_by_categories(result, categories)


# Reviews
def total_reviewed() -> list:
    """
    returns: reviews per product list
    """
    result = []
    g_sales = global_sales()
    for i in range(len(g_sales)):
        result.append([g_sales[i][0], []])
        sales = g_sales[i][1]
        for s in sales:
            review = get_sale(s)[2]
            result[i][1].append(review)
    return result


def most_reviewed(categories:list=['procesadores']) -> list:
    """
    returns: product reviews list per categories
    """
    result = total_reviewed()
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return filter_by_categories(result, categories)


def least_reviewed(categories:list=['procesadores']) -> list:
    """
    returns: product reviews list per categories
    """
    result = total_reviewed()
    result.sort(key=lambda p: len(p[-1]), reverse=False)
    return filter_by_categories(result, categories)


# Refunds
def total_refunds(most:bool=True) -> list:
    """
    returns: refunds per product list
    """
    result = []
    g_sales = global_sales()
    for i in range(len(g_sales)):
        result.append([g_sales[i][0], []])
        sales = g_sales[i][1]
        for s in sales:
            refund = get_sale(s)[-1]
            if refund > 0:
                result[i][1].append(refund)
    return result


def most_refund(categories:list=['procesadores']) -> list:
    """
    returns: product refunds list per categories
    """
    result = total_refunds()
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return filter_by_categories(result, categories)


def least_refund(categories:list=['procesadores']) -> list:
    """
    returns: product refunds list per categories
    """
    result = total_refunds()
    result.sort(key=lambda p: len(p[-1]), reverse=False)
    return filter_by_categories(result, categories)


# Revenue
def total_revenue(most:bool=True) -> list:
    result = []
    for ps in global_sales():
        product = get_product(ps[0])
        ps_total = 0
        for s in ps[1]:
            refund = get_sale(s)[-1]
            if refund == 0:
                ps_total += product[2]
        result.append([ps[0], ps_total])
    return result


def most_revenue(categories:list=['procesadores']) -> list:
    """
    returns: product revenue list per categories
    """
    result = total_revenue()
    result.sort(key=lambda p: p[-1], reverse=True)
    return filter_by_categories(total_revenue(), categories)


def least_revenue(categories:list=['procesadores']) -> list:
    """
    returns: product revenue list per categories
    """
    result = total_revenue()
    result.sort(key=lambda p: p[-1], reverse=False)
    return filter_by_categories(total_revenue(False), categories)


#### TESTING
def test():
    cat = ['procesadores', 'audifonos']
    
    sold = most_sold(cat)
    print(f'most_sold {get_categories(sold)}:')
    print(sold)
    
    searched = most_searched(cat)
    print(f'most_searched {get_categories(searched)}:')
    print(searched)
    
    stocked = lowest_stock(cat)
    print(f'lowest_stock {get_categories(stocked)}:')
    print(stocked)

    reviewed = most_reviewed(cat)
    print(f'most_reviewed {get_categories(reviewed)}:')
    print(reviewed)
    
    refunds = most_refund(cat)
    print(f'most_refund {get_categories(refunds)}:')
    print(refunds)

    revenue = most_revenue(cat)
    print(f'most_revenue {get_categories(revenue)}:')
    print(revenue)
####                


def revenue():
    average_revenue = None
    average_sells = None
    
    best_months = None


# main program
def main():
    # GLOBALS
    CATEGORIES = get_categories()
    
    login()
    test()


if __name__ == "__main__":
    main()

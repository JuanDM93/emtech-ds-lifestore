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
    def ask(admin, secret):
        admin = input('Input admin user:')
        secret = input('Password:')
        return admin, secret
    
    admin, secret = '', ''
    while 'admin' != admin or 'pass' != secret:
        admin, secret = ask(admin, secret)
        print('Login failed... try again')
    print('Login succesful!')


# Utils
def get_product(id:int):
    """
    returns: product object from dataset
    """
    return lifestore_products[id - 1]


def get_sale(id:int):
    """
    returns: sale object from dataset
    """
    return lifestore_sales[id - 1]


def get_categories(data:list=lifestore_products):
    """
    data: any list with product_id at i:0
    returns: list with categories from list
    """
    categories = []
    for d in data:
        cat = get_product(d[0])[3]
        if cat not in categories:
            categories.append(cat)
    return categories


def filter_by_categories(data:list, cats:list=[]):
    """
    data: any list with products
    cats: a custom categories list
    """
    result = []
    for d in data:
        p = get_product(d[0])
        if p[3] in cats:
            result.append(d)
    return result


# Total Sales
def global_sales(most:bool=True):
    """
    most: True=Order by most, False:Order by less
    returns: sorted list by total sales
    """    
    total_sales = []
    for p in lifestore_products:
        my_p = p[:1]
        sales = 0
        for sale in lifestore_sales:
            if p[0] == sale[1]:
                sales += 1
        my_p.append(sales)
        total_sales.append(my_p)
    
    total_sales.sort(key=lambda p: p[-1], reverse=most)
    return total_sales


# Sales By Category
def most_sold(categories:list=['procesadores']):
    """
    categories = [
        'procesadores', 'tarjetas de video', 'tarjetas madre',
        'discos duros', 'memorias usb', 'pantallas', 'bocinas', 'audifonos'
        ]
    returns: sorted most sold products list by category
    """
    return filter_by_categories(global_sales(), categories)


# Total Searches
def global_searches(most:bool=True):
    """
    most: True=Order by most, False:Order by less
    returns: sorted list by total searches
    """    
    total_searches = []
    for p in lifestore_products:
        my_p = p[:1]
        searches = 0
        for search in lifestore_searches:
            if p[0] == search[1]:
                searches += 1
        my_p.append(searches)
        total_searches.append(my_p)
    
    total_searches.sort(key=lambda p: p[-1], reverse=most)
    return total_searches


# Searches By Category
def most_searched(categories:list=['procesadores']):
    """
    categories = [
        'procesadores', 'tarjetas de video', 'tarjetas madre',
        'discos duros', 'memorias usb', 'pantallas', 'bocinas', 'audifonos'
        ]
    returns: sorted most searched products list
    """
    return filter_by_categories(global_searches(), categories)


# Total Stocks
def global_stocks(most:bool=False):
    """
    most: True=Order by most, False:Order by less
    returns: products in stock 
    """
    lows = [[p[0], p[-1]] for p in lifestore_products]
    lows.sort(key=lambda p: p[1], reverse=most)
    return lows


# Stocks By Category
def lowest_stock(categories:list=['procesadores']):
    """
    low_limit: how low to warn
    returns: sorted low stock products list by category
    """
    return filter_by_categories(global_stocks(), categories)


#### TESTING
def test():
    print('most_sold:')
    print(most_sold())

    print('most_searched')
    print(most_searched())
    
    print('lowest_stock')
    print(lowest_stock())
####


# Reviews
def reviews():
    best_reviewed = None
    worst_reviewed = None


# Revenue
def revenue():
    total_revenue = None
    total_sells = None

    average_revenue = None
    average_sells = None
    
    best_months = None


# main program
def main():
    login()
    test()


if __name__ == "__main__":
    main()

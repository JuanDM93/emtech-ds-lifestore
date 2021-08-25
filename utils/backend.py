"""
Backend module
"""
# Datasets
from .lifestore_file import lifestore_searches, lifestore_sales, lifestore_products


# Single Getters
def get_product(id: int) -> list:
    """
    returns: product object from dataset
    """
    return lifestore_products[id - 1]


def get_sale(id: int) -> list:
    """
    returns: sale object from dataset
    """
    return lifestore_sales[id - 1]


def get_categorie(product_id: int) -> str:
    """
    returns: categorie str from product_id
    """
    return lifestore_products[product_id - 1][3]


# Global Getters
def global_sales() -> list:
    """
    returns: total sales list by product -> [p_id, [sales, ...]]
    """
    total_sales = [[p[0], []] for p in lifestore_products]
    for sale in lifestore_sales:
        total_sales[sale[1] - 1][1].append(sale[0])
    return total_sales


def global_searches() -> list:
    """
    returns: total search list by product -> [p_id, [searches, ...]]
    """
    total_searches = [[p[0], []] for p in lifestore_products]
    for search in lifestore_searches:
        total_searches[search[1] - 1][1].append(search[0])
    return total_searches


# Custom Getters
def get_categories(data: list = lifestore_products) -> list:
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


def get_products(data: list) -> list:
    """
    data: any list with product_id at [0]
    returns: custom full product list
    """
    return [get_product(d[0]) for d in data]


def get_sales(data: list) -> list:
    """
    data: any list with sales_id at [0]
    returns: custom full sales list
    """
    return [get_sale(d[0]) for d in data]


def get_stocks(data: list) -> list:
    """
    data: any list with product_id at [0]
    returns: stocks per product -> [p_id, stock]
    """
    stocks = []
    for d in data:
        p = get_product(d[0])
        stocks.append([p[0], p[-1]])
    return stocks


def get_reviews(data: list) -> list:
    """
    data: any list with product_id at [0] with sales_ids at [1]
    returns: reviews per product list -> [p_id, [review1, ...]]
    """
    result = []
    for d in data:
        reviews = []
        for s in d[1]:
            review = get_sale(s)[2]
            reviews.append(review)
        result.append([d[0], reviews])
    return result


def get_refunds(data: list) -> list:
    """
    data: any list with product_id at [0] with sales_ids at [1]
    returns: refunds per product list -> [p_id, refunds]
    """
    result = []
    for d in data:
        sum = 0
        for s in d[1]:
            sum += get_sale(s)[-1]
        result.append([d[0], sum])
    return result


def get_revenue(data: list) -> list:
    """
    data: any list with product_id at [0] with [sales_ids] at [1]
    returns: total revenue per product list -> [p_id, revenue]
    """
    revenue = []
    for d in data:
        product = get_product(d[0])
        total = 0
        for s in d[1]:
            refund = get_sale(s)[-1]
            if refund == 0:
                total += product[2]
        revenue.append([d[0], total])
    return revenue


# Filters
def clean_list(data: list, reverse: bool = True) -> list:
    """
    data: any list with id at [0] and to_clean_list at [-1]
    count: True -> remove [], False -> remove 0s
    returns: clean list
    """
    if reverse:
        return [d for d in data if len(d[1]) > 0]
    return [d for d in data if len(d[1]) == 0]


def custom_sort(data: list, reverse: bool = True) -> list:
    """
    data: any list with id at [0] and to_sort_list at [-1]
    reverse: ordering type, default -> most
    returns: sorted custom list
    """
    result = data[:]
    if type(result[0][-1]) is int:
        result.sort(key=lambda p: p[-1], reverse=reverse)
    else:
        result.sort(key=lambda p: len(p[-1]), reverse=reverse)
    return result


def filter_categories(data: list, cats: list) -> list:
    """
    data: any list with product_id at [0]
    cats: a custom categories list
    returns: list of products filtered by cats
    """
    return [d for d in data if get_categorie(d[0]) in cats]


def filter_months(data: list, months: list) -> list:
    """
    data: any list with product_id at [0] and sales_ids at [1]
    months: ['01', ..., '12']
    returns: list of product sales filtered by month
    """
    result = []
    for d in data:
        sales = []
        for s in d[1]:
            sale = get_sale(s)
            s_date = sale[3].split('/')[1]
            if s_date in months:
                sales.append(s)
        result.append([d[0], sales])
    return result

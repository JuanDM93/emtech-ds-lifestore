"""
Backend module
"""
# Datasets
from .lifestore_file import lifestore_searches, lifestore_sales, lifestore_products


# Global Getters
def global_sales() -> list:
    """
    returns: total sales list by product -> [p_id, [sales, ...]]
    """
    total_sales = [[p[0], []] for p in lifestore_products]
    for sale in lifestore_sales:
        total_sales[sale[1] - 1][1].append(sale[0])
    return total_sales


SALES = global_sales()


def global_searches() -> list:
    """
    returns: total search list by product -> [p_id, [searches, ...]]
    """
    total_searches = [[p[0], []] for p in lifestore_products]
    for search in lifestore_searches:
        total_searches[search[1] - 1][1].append(search[0])
    return total_searches


SEARCHES = global_searches()


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


def get_date(sale_id: str) -> list:
    """
    returns: date ['15','09','2020'] by sale_id 
    """
    return lifestore_sales[sale_id - 1][3].split('/')


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


CATEGORIES = get_categories()


def get_dates(data: list = lifestore_sales) -> list:
    """
    data: any list with sales_id at [0]
    returns: dates list from input
    """
    return [[d[0], get_date(d[0])] for d in data]


DATES = get_dates()


def get_monthly(data: list, month: str = 'SEP') -> list:
    """
    data: any list with sales_ids at [0]
    dates: 'JAN', ..., 'DEC'
    returns: list of product sales filtered by month
    """
    from .frontend import MONTHS
    result = []
    for p in data:
        sales = []
        for s in p[1]:
            date = int(get_date(s)[1])
            if MONTHS[date - 1] == month:
                sales.append(s)
        if len(sales) > 0:
            result.append([p[0], sales])
    return result


def get_yearly(data: list, year: str = '2020') -> list:
    """
    data: any list with sales_ids at [1]
    year: '2001', ..., '2030'
    returns: list of product sales filtered by year
    """
    result = []
    for p in data:
        sales = []
        for s in p[1]:
            date = get_date(s)
            if date[-1] == year:
                sales.append(s)
        if len(sales) > 0:
            result.append([p[0], sales])
    return result


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


def sum_reviews(reviews: list) -> list:
    """
    Averages review values at [1]
    """
    result = []
    for r in reviews:
        review = sum(r[1]) / len(r[1]) if len(r[1]) > 0 else 0
        result.append([r[0], review])
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
            total = total + product[2] if refund == 0 else total
        revenue.append([d[0], total])
    return revenue


def get_total_revenue(data: list) -> float:
    """
    data: any list with product_id at [0] and revenue at [1]
    returns: total revenue for data
    """
    revenue = get_revenue(data)
    total = 0
    for r in revenue:
        total += r[1]
    return float(total)


# Filters
def clean_list(data: list, reverse: bool = True) -> list:
    """
    data: any list with id at [0] and to_clean_list at [-1]
    count: True -> remove [], False -> remove 0s
    returns: clean list
    """
    if len(data) > 0:
        if type(data[0][1]) is list:
            return [d for d in data if len(d[1]) > 0]
        return [d for d in data if d[1] > 0]
    return data


def custom_sort(data: list, reverse: bool = True) -> list:
    """
    data: any list with id at [0] and to_sort_list at [-1]
    reverse: ordering type, default -> most
    returns: sorted custom list
    """
    if len(data) > 0:
        result = data[:]
        if type(result[0][-1]) is not list:
            result.sort(key=lambda p: p[-1], reverse=reverse)
        else:
            result.sort(key=lambda p: len(p[-1]), reverse=reverse)
        return result
    return data


def filter_categories(data: list, cat: str) -> list:
    """
    data: any list with product_id at [0]
    cat: a custom categorie
    returns: list of products filtered by cats
    """
    return [d for d in data if get_categorie(d[0]) == cat]

"""
Backend module
"""
from frontend.locals import MONTHS
from backend.globals import (
    get_date, get_product, get_sale,
)


def get_monthly(data: list, month: str = 'SEP') -> list:
    """
    data: any list with sales_ids at [0]
    dates: 'JAN', ..., 'DEC'
    returns: list of product sales filtered by month
    """
    result = []
    for product in data:
        sales = []
        for sale in product[1]:
            date = int(get_date(sale)[1])
            if MONTHS[date - 1] == month:
                sales.append(sale)
        if len(sales) > 0:
            result.append([product[0], sales])
    return result


def get_yearly(data: list, year: str = '2020') -> list:
    """
    data: any list with sales_ids at [1]
    year: '2001', ..., '2030'
    returns: list of product sales filtered by year
    """
    result = []
    for product in data:
        sales = []
        for sale in product[1]:
            date = get_date(sale)
            if date[-1] == year:
                sales.append(sale)
        if len(sales) > 0:
            result.append([product[0], sales])
    return result


def get_products(data: list) -> list:
    """
    data: any list with product_id at [0]
    returns: custom full product list
    """
    return [get_product(d[0]) for d in data]


def get_sales(data: list) -> list:
    """
    data: any list with sales_id at [0]
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
        product = get_product(d[0])
        stocks.append([product[0], product[-1]])
    return stocks


def get_reviews(data: list) -> list:
    """
    data: any list with product_id at [0] with sales_ids at [1]
    returns: reviews per product list -> [p_id, [review1, ...]]
    """
    result = []
    for d in data:
        reviews = []
        for sale in d[1]:
            review = get_sale(sale)[2]
            reviews.append(review)
        result.append([d[0], reviews])
    return result


def sum_reviews(reviews: list) -> list:
    """
    Averages review values at [1]
    """
    result = []
    for review in reviews:
        reviewed = sum(review[1]) / len(review[1]) if len(review[1]) > 0 else 0
        result.append([review[0], reviewed])
    return result


def get_refunds(data: list) -> list:
    """
    data: any list with product_id at [0] with sales_ids at [1]
    returns: refunds per product list -> [p_id, refunds]
    """
    result = []
    for d in data:
        sum = 0
        for sale in d[1]:
            sum += get_sale(sale)[-1]
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
        for sale in d[1]:
            refund = get_sale(sale)[-1]
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

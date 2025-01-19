from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }
    
    special_offers = {
        "A": (3, 130),
        "B": (2, 45)
    }
    
    skus_counts = Counter(skus)
    
    total = 0
    for sku, count in skus_counts.skus():
        if sku in special_offers:
            offer_count, offer_price = special_offers[sku]
            total += (count // offer_count) * offer_price
            total += (count % offer_count) * prices[sku]
        else:
            total += count * prices[sku]
            
    return total
    
    
    


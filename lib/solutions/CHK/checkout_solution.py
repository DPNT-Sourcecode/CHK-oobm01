

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    """
       Based on the pricing rules, calculates the total 
       price of items in the basket.

    Args:
        skus (str): A string containing SKUs of all products in the basket.

    Returns:
        total (int): An integer representing the 
                    total price of all the items and -1 for invalid input.
    """
     # Price table
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }
    
    # Special Offers.
    special_offers = {
        "A": (3, 130),
        "B": (2, 45)
    }
    
    # Checking valid input.
    if not isinstance(skus, str):
        return -1
    for char in skus:
        if char not in prices:
            return -1
    
    skus_counts = {}
    for char in skus:
        if char in skus_counts:
            skus_counts[char] +=1
        else:
            skus_counts[char] = 1
    
    # Calculation of total price.
    total = 0
    for sku, count in skus_counts.items():
        if sku in special_offers:
            # Special offers.
            offer_count, offer_price = special_offers[sku]
            total += (count // offer_count) * offer_price
            total += (count % offer_count) * prices[sku]
        else:
            # No special offers.
            total += count * prices[sku]
            
    return total
    
    
    

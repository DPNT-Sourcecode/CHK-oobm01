

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
        "D": 15,
        "E": 40
    }
    
    # Special Offers.
    special_offers = {
        "A": [(3, 130), (5, 200)],
        "B": [(2, 45)],
        "E": [(2, "B")] # 2E, you get one B free.
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
    free_b = 0
    for sku, count in skus_counts.items():
        if sku in special_offers:
            # Special offers.
            if sku == "E": # For E
                free_b += count // 2
                total += (count // 2) * prices["E"]
                remaining_e = count % 2
                total += remaining_e * prices["E"]
                
            else:
                for offer in sorted(special_offers[sku], key=lambda x: x[1], reverse=True):
                    offer_count, offer_price = offer
                    total += (count // offer_count) * offer_price
                    total += (count % offer_count) * prices[sku]
        else:
            # No special offers.
            total += count * prices[sku]
            
        if "B" in skus_counts:
            available_b = skus_counts["B"]
            skus_counts["B"] = max(0, available_b - free_b)
        
        total += skus_counts.get('B', 0) * prices["B"]
            
    return total
    
    
    


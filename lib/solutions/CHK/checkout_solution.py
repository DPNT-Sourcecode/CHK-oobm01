

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
    if not isinstance(skus, str):
        # Invalid input
        return -1
    if skus == "":
        # Empty basket
        return 0
     
    # Price table
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
        'Y': 10, 'Z': 50
    }
    
    # Special offers
    offers = {
        'A': [(5, 200), (3, 130)],  # Priority: larger bundles first
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)]      
    }
    
    # Free items.
    free_rules = {
        'E': ('B', 2), # 2E get one B free.
        'F': ('F', 3), # 3F get one F free.
        'N': ('M', 3), # 3N get one M free.
        'R': ('Q', 3), # 3R get one Q free.
        'U': ('U', 4)  # 3U get one U free.
    }
    
    # Check for invalid input
    if not skus.isalpha() or not all(char in prices for char in skus):
        return -1

    # Count occurrences of each SKU using a dictionary
    basket = {}
    for item in skus:
        basket[item] = basket.get(item, 0) + 1

    total = 0

    # Apply free rules.
    for rule_item, (free_item, threshold) in free_rules.items():
        if rule_item in basket:
            applicable_free = basket[rule_item] // threshold
            if free_item in basket:
                basket[free_item] = max(0, basket[free_item] - applicable_free)
            else:
                basket[free_item] = 0
        
    # Process each item
    for item, count in basket.items():
        if item in offers:
            # Apply special offers for the item
            for quantity, offer_price in sorted(offers[item], reverse=True):
                num_offers = count // quantity
                total += num_offers * offer_price
                count %= quantity  # Remaining items after applying the offer
        # Add remaining items at regular price
        total += count * prices[item]

    return total


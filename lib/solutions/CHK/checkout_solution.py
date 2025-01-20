

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
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10
    }
    
    # Special offers
    offers = {
        'A': [(5, 200), (3, 130)],  # Priority: larger bundles first
        'B': [(2, 45)],
        'E': [],  # No direct multi-buy discounts, "2E get one B free" handled separately
        'F': [],  # No direct multi-buy discounts, "2F get one F free" handled separately
    }
    
    # Check for invalid input
    if not all(char in prices for char in skus):
        return -1

    # Count occurrences of each SKU using a dictionary
    basket = {}
    for item in skus:
        if item in basket:
            basket[item] += 1
        else:
            basket[item] = 1

    total = 0

    # Apply "2E get one B free" offer
    if 'E' in basket:
        e_count = basket['E']
        free_b_count = e_count // 2  # One free B for every two E
        if 'B' in basket:
            # Deduct free B items if they already exist
            basket['B'] = max(0, basket['B'] - free_b_count)
        else:
            # Add free B items if no B is initially in the basket
            basket['B'] = 0  # Initialize B in basket if not present
    
    # Apply "2F get one F free" offer
    if 'F' in basket:
        f_count = basket['F']
        free_f_count = f_count // 3 # one free F for every three F
        total += (f_count - free_f_count) * prices['F']
        
        
    # Process each item
    for item, count in basket.items():
        if item == 'F':
            continue # already being handled.
        
        if item in offers:
            # Apply special offers for the item
            for quantity, offer_price in sorted(offers[item], reverse=True):
                num_offers = count // quantity
                total += num_offers * offer_price
                count %= quantity  # Remaining items after applying the offer
        # Add remaining items at regular price
        total += count * prices[item]

    return total

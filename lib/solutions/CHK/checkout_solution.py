

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
        'E': 40
    }
    
    # Special offers
    offers = {
        'A': [(5, 200), (3, 130)],  # Priority: larger bundles first
        'B': [(2, 45)],
        'E': [(2, 40)]  # "2E get one B free" handled separately
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
            basket['B'] = max(0, basket['B'] - free_b_count)  # Deduct free B from basket

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

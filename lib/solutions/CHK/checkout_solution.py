from collections import Counter

def checkout(items):
    # Define prices and special offers
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
        'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40,
        'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40,
        'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21
    }
    
    offers = {
        'A': [(3, 130), (5, 200)],  # 3A for 130, 5A for 200
        'B': [(2, 45)],             # 2B for 45
        'E': [(2, 40, 'B')],        # 2E get one B free
        'F': [(2, 10, 'F')],        # 2F get one F free
        'H': [(5, 45), (10, 80)],   # 5H for 45, 10H for 80
        'K': [(2, 120)],            # 2K for 120
        'N': [(3, 40, 'M')],        # 3N get one M free
        'P': [(5, 200)],            # 5P for 200
        'Q': [(3, 80)],             # 3Q for 80
        'R': [(3, 50, 'Q')],        # 3R get one Q free
        'S': [(3, 45)],             # buy any 3 of (S,T,X,Y,Z) for 45
        'T': [(3, 45)],             # buy any 3 of (S,T,X,Y,Z) for 45
        'X': [(3, 45)],             # buy any 3 of (S,T,X,Y,Z) for 45
        'Y': [(3, 45)],             # buy any 3 of (S,T,X,Y,Z) for 45
        'Z': [(3, 45)]              # buy any 3 of (S,T,X,Y,Z) for 45
    }
    
    # Check for invalid characters
    if not all(c.isupper() and c.isalpha() for c in items):
        return -1
    
    # Count the items
    item_counts = Counter(items)
    total_cost = 0
    
    # Process each item
    for item, count in item_counts.items():
        if item not in prices:
            return -1  # Invalid item
        
        item_price = prices[item]
        best_price = count * item_price  # Default to no offers applied
        
        # Check for special offers
        if item in offers:
            for offer in offers[item]:
                if len(offer) == 2:  # Simple offer (e.g., 3A for 130)
                    offer_count, offer_price = offer
                    num_groups = count // offer_count
                    remainder = count % offer_count
                    best_price = min(best_price, num_groups * offer_price + remainder * item_price)
                elif len(offer) == 3:  # Complex offer (e.g., 2E get one B free)
                    offer_count, offer_price, free_item = offer
                    num_groups = count // offer_count
                    remainder = count % offer_count
                    free_item_count = num_groups  # One free item for each group
                    total_free_item_count = item_counts.get(free_item, 0) + free_item_count
                    best_price = min(best_price, num_groups * offer_price + remainder * item_price)
        
        # Add the best price for the item to the total cost
        total_cost += best_price
    
    return total_cost

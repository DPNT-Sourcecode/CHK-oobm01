

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
     
    def checkout(skus: str) -> int:
    # Price and offers table
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40,
        'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60,
        'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10,
        'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20,
        'U': 40, 'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21,
    }

    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)],
        'E': [(2, 'B')],  # 2E gets 1B free
        'N': [(3, 'M')],  # 3N gets 1M free
        'R': [(3, 'Q')],  # 3R gets 1Q free
        'U': [(4, 120)],  # 3U gets 1 free, equivalent to 4 for 120
        'F': [(3, 20)],   # 2F gets 1 free, equivalent to 3 for 20
    }

    group_discount = {'S', 'T', 'X', 'Y', 'Z'}
    group_discount_price = 45

    # Check for invalid input
    if not isinstance(skus, str) or any(char not in prices for char in skus):
        return -1

    # Count occurrences of each item
    item_counts = {}
    for item in skus:
        item_counts[item] = item_counts.get(item, 0) + 1

    total = 0

    # Apply group discount for S, T, X, Y, Z
    group_items = [(item, item_counts[item]) for item in group_discount if item in item_counts]
    group_items.sort(key=lambda x: prices[x[0]], reverse=True)  # Favor expensive items first
    group_total_count = sum(count for _, count in group_items)

    groups_of_3 = group_total_count // 3
    total += groups_of_3 * group_discount_price

    # Subtract used items from group_items
    remaining_items = group_total_count % 3
    for item, count in group_items:
        used = min(count, groups_of_3 * 3)
        item_counts[item] -= used
        groups_of_3 -= used // 3
        if groups_of_3 == 0:
            break

    # Apply other special offers
    for item, count in item_counts.items():
        if count > 0 and item in offers:
            for offer in offers[item]:
                if isinstance(offer[1], int):  # Multi-buy discount
                    while count >= offer[0]:
                        total += offer[1]
                        count -= offer[0]
                elif isinstance(offer[1], str):  # Free item offer
                    free_item = offer[1]
                    while count >= offer[0]:
                        total += offer[0] * prices[item]
                        count -= offer[0]
                        if free_item in item_counts:
                            item_counts[free_item] = max(0, item_counts[free_item] - 1)

        # Add remaining items at full price
        total += count * prices[item]

    return total

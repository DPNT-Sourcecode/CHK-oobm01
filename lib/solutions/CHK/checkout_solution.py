def checkout(skus: str) -> int:
    # Price table
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

    # Initialize item counts dictionary
    item_counts = {}
    for item in skus:
        if item in prices:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1
        else:
            return -1  # Illegal SKU

    total = 0

    # Apply group discount for S, T, X, Y, Z
    group_items = {item: item_counts.get(item, 0) for item in group_discount}
    total_group_items = sum(group_items.values())

    # Apply group discount (group of 3 for 45)
    groups_of_3 = total_group_items // 3
    total += groups_of_3 * group_discount_price

    # Deduct used items for group discount
    used_count = groups_of_3 * 3
    for item in group_items:
        if used_count == 0:
            break
        used = min(group_items[item], used_count)
        item_counts[item] -= used
        used_count -= used

    # Apply other special offers
    for item, count in item_counts.items():
        if count > 0 and item in offers:
            for offer in offers[item]:
                if isinstance(offer[1], int):  # Multi-buy discount
                    while count >= offer[0]:
                        total += offer[1]
                        count -= offer[0]
                elif isinstance(offer[1], str):  # Free item offer (e.g. 2E gets 1B free)
                    free_item = offer[1]
                    while count >= offer[0]:
                        total += offer[0] * prices[item]
                        count -= offer[0]
                        if free_item in item_counts and item_counts[free_item] > 0:
                            item_counts[free_item] = max(0, item_counts[free_item] - 1)

        # Add remaining items at full price
        total += count * prices[item]

    return total

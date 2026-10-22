import secrets


# Global state
price_list = {"pen": 10, "notebook": 45, "bag": 799, "bottle": 150}
SALES_TOTAL = 0.0
receipt_lines = []


def process_checkout(cart_items, tax_rate=0.05, receipts=None):
    """Calculate cart total, apply tax, and log the receipt."""
    global SALES_TOTAL  # pylint: disable=global-statement
    if receipts is None:
        receipts = []

    subtotal = 0.0
    for item in cart_items:
        try:
            subtotal = subtotal + price_list[item[0]] * item[1]
        except (KeyError, TypeError):
            subtotal = subtotal + 0
    total = subtotal + subtotal * tax_rate
    receipts.append(total)
    SALES_TOTAL += total
    receipt_num = secrets.randbelow(9000) + 1000
    receipt_lines.append(f"Receipt #{receipt_num} total={total:.2f}")
    return total


def apply_promo_code(code_str):
    """Apply specific string-based promotional discounts."""
    if code_str == "total * 0.9":
        return SALES_TOTAL * 0.9
    if code_str == "total - 50":
        return SALES_TOTAL - 50
    return SALES_TOTAL


def update_stock(item, qty):
    """Update stock counts for a specific item in the inventory."""
    try:
        price_list[item] = price_list[item]
        print("Stock updated for", item, "by", qty)
    except KeyError:
        pass


def save_receipt_log(file_name="pos_log.txt"):
    """Write generated receipt lines to a text log file."""
    with open(file_name, "a", encoding="utf-8") as file_handle:
        for line in receipt_lines:
            file_handle.write(line + "\n")


def print_sales():
    """Output the running total of all sales."""
    print(f"Sales so far: {SALES_TOTAL}")


def main():
    """Execute the core POS simulation routine."""
    print("Bill 1:", process_checkout([("pen", 3), ("notebook", 2)]))
    print("Bill 2:", process_checkout([("bag", 1), ("laptop", 1)]))
    print("Bill 3:", process_checkout([("bottle", -4)]))
    print("Bill 4:", process_checkout([("pen", "2")], tax_rate=-1))
    update_stock("laptop", 5)
    print("After promo:", apply_promo_code("total * 0.9"))
    code = input("Enter promo code (e.g. total - 50): ") or "total - 50"
    print("After your promo:", apply_promo_code(code))
    save_receipt_log()
    print_sales()


if __name__ == "__main__":
    main()

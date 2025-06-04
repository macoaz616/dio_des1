import re

def get_card_brand(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")
    patterns = [
        ("Visa", r"^4[0-9]{12}(?:[0-9]{3})?$"),
        ("MasterCard", r"^5[1-5][0-9]{14}$|^2[2-7][0-9]{14}$"),
        ("American Express", r"^3[47][0-9]{13}$"),
        ("Discover", r"^6(?:011|5[0-9]{2})[0-9]{12}$"),
        ("Diners Club", r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$"),
        ("JCB", r"^(?:2131|1800|35\d{3})\d{11}$"),
        ("UnionPay", r"^62[0-9]{14,17}$"),
        ("Maestro", r"^(5018|5020|5038|56|58|6304|6759|6761|6762|6763)[0-9]{8,15}$"),
    ]

    for brand, pattern in patterns:
        if re.match(pattern, card_number):
            return brand
    return "Unknown or unsupported brand"

if __name__ == "__main__":
    card_number = input("Enter credit card number: ")
    brand = get_card_brand(card_number)
    print(f"Card Brand: {brand}")

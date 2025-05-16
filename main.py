def get_card_brand(card_number: str) -> str:
    """
    Returns the card brand ("Bandeira") based on the card number.
    """
    card_number = card_number.replace(" ", "")
    length = len(card_number)

    # Visa Electron specific IINs
    visa_electron_iins = ['4026', '417500', '4508', '4844', '4913', '4917']

    # American Express
    if length == 15 and (card_number.startswith('34') or card_number.startswith('37')):
        return "American Express"

    # Diners Club - Carte Blanche
    if length == 14 and any(card_number.startswith(str(i)) for i in range(300, 306)):
        return "Diners Club - Carte Blanche"

    # Diners Club - International
    if length == 14 and card_number.startswith('36'):
        return "Diners Club - International"

    # MasterCard
    if length == 16:
        first_two = int(card_number[:2])
        first_four = int(card_number[:4])
        first_six = int(card_number[:6])
        if (51 <= first_two <= 55) or (222100 <= first_six <= 272099):
            return "MasterCard"

    # Visa Electron
    if length == 16 and any(card_number.startswith(iin) for iin in visa_electron_iins):
        return "Visa Electron"

    # Visa
    if card_number.startswith('4') and length in [13, 16, 19]:
        return "Visa"

    return "Unknown"

# Example usage:
if __name__ == "__main__":
    test_numbers = [
        "3013 366228 2626",

    ]
    for number in test_numbers:
        print(f"{number}: {get_card_brand(number)}")
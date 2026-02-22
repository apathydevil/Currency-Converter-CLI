from api import get_exchange_rate, get_supported_currencies

def main():
    print("Welcome to my CLI currency converter!")
    currencies = get_supported_currencies()
    if not currencies:
        print("Error: Could not connect to the API. Check your internet.")
        return
    while True:
        choice = input("\nPress Enter to continue or type 'exit' to quit: ")
        if choice.lower() == "exit":
            print("Thank you for using my exchange rate converter! Goodbye!")
            break 

        print("Would you like to list supported currencies? (y/n)")
        if input().lower() == "y":
            for code, name in currencies.items():
                print(f"  {code}: {name}")

        from_c = input("\nFrom (acronym): ").upper()
        to_c = input("To (acronym): ").upper()

        if from_c not in currencies or to_c not in currencies:
            print("Error: One or both currencies are not supported.")
            continue

        amount_raw = input("Amount: ")
        try:
            amount = float(amount_raw)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        rate = get_exchange_rate(from_c, to_c, currencies)
        if rate is not None:
            result = amount * rate
            result = round(result, 2)
            print(f"\n{amount} {currencies[from_c]} is {result} {currencies[to_c]}")
            print(f"Current exchange rate: 1 {from_c} = {rate} {to_c}")
        else:
            print("Error: API failed to return a rate.")

if __name__ == "__main__":
    main()
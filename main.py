import requests


def get_data(endpoint):
    base_url = "https://api.ataix.kz/api"
    response = requests.get(f"{base_url}/{endpoint}")
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            return data["result"]  # Extracting the actual data
        else:
            print(f"Unexpected response format for {endpoint}")
            return None
    else:
        print(f"Error fetching {endpoint}: {response.status_code}")
        return None


def main():
    # 1. Fetching the list of currencies
    currencies = get_data("currencies")
    if currencies:
        print("\nList of currencies:")
        for currency in currencies:
            print(currency)
        print(f"Total number of currencies: {len(currencies)}")

    # 2. Fetching the list of trading pairs
    symbols = get_data("symbols")
    if symbols:
        print("\nList of trading pairs:")
        for symbol in symbols:
            print(symbol)
        print(f"Total number of trading pairs: {len(symbols)}")

        # 3. Fetching coin and token prices
        prices = get_data("prices")
    print("\nRaw prices data:", prices)

    if prices:
        print("\nCoin and token prices:")
        for item in prices:
            print("Entry:", item)

            if isinstance(item, dict) and "symbol" in item and "last" in item:
                print(f"{item['symbol']}: {item['last']}")
            else:
                print("Skipping invalid entry:", item)
    else:
        print("Unexpected data format in prices")


if __name__ == "__main__":
    main()

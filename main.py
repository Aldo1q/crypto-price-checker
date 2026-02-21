import requests

def get_price(symbol="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[symbol]["usd"]

if __name__ == "__main__":
    coin = input("Enter coin name (example: bitcoin, ethereum, dogecoin): ")
    price = get_price(coin)
    print(f"Current {coin} price: ${price}")

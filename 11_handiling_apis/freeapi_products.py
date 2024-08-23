import requests

def fetch_random_product_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/30"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        userdata = data["data"]
        brand = userdata["brand"]
        category = userdata["category"]
        discountPercentage = userdata["discountPercentage"]
        product_id = userdata["id"]
        return category, product_id, brand, discountPercentage
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        category, product_id, brand, discountPercentage = fetch_random_product_freeapi()
        print(f"Category: {category}\nProduct ID: {product_id}\nDiscount Percentage: {discountPercentage}\nBrand: {brand}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
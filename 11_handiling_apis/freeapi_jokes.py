import  requests

def fetch_random_jokes_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()


    if data["success"] and "data" in data:
       categories = data["data"]["categories"]
       return categories[1],categories[0],categories[0],categories[0]
    

    else:
       raise Exception("Failed to fetch userdata")


def main():
    try:
        category1 ,category2, _, _ = fetch_random_jokes_freeapi()
        print(f"category 1:{catagory1}\n category 2:{category2}")

    except Exception as e:
      print(str(e))

    if __name__  == "__main__":
      main()



    

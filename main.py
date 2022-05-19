from urllib.request import urlopen
import json


def calculatePrice(data):

    # item with list of items inside
    if 'items' in data:
        return data["count"] * calculatePrice(data["items"])

    # single item
    if 'price' in data:
        return data["count"] * data["price"]

    # list of items
    else:
        total = 0
        for item in data:
            total += calculatePrice(item)
        return total


def getJSON(url):

    # opening the url
    source = urlopen(url)

    # deserializing the JSON string into Python dictionary
    dataJSON = json.loads(source.read())

    return dataJSON


if __name__ == '__main__':

    url = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_3.json"

    data = getJSON(url)

    print(f"The result is: {calculatePrice(data)}")


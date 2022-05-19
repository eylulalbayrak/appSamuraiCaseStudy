from urllib.request import urlopen
import json


def calculatePrice(data):

    if 'items' not in data:
        return data['count'] * data['price']

    elif not isinstance(data['items'], list):
        return data['count'] * calculatePrice(data['items'])

    else:
        sum = 0

        for key in data['items']:
            sum += calculatePrice(key)

        return data['count'] * sum


def getJSON(url):
    source = urlopen(url)

    dataJSON = json.loads(source.read())

    return dataJSON


if __name__ == '__main__':

    url = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_2.json"

    data = getJSON(url)

    print(f"The result is: {calculatePrice(data)}")
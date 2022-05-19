from urllib.request import urlopen
import json


def getJSON(url):
    source = urlopen(url)

    dataJSON = json.loads(source.read())

    return dataJSON


if __name__ == '__main__':

    url = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_2.json"

    data = getJSON(url)
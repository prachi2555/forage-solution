import json
import datetime

# Convert from Format 1
def convertFromFormat1(jsonObject):

    locationParts = jsonObject["location"].split("/")

    result = {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": locationParts[0],
            "city": locationParts[1],
            "area": locationParts[2],
            "factory": locationParts[3],
            "section": locationParts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }

    return result


# Convert from Format 2
def convertFromFormat2(jsonObject):

    date = datetime.datetime.strptime(
        jsonObject["timestamp"],
        "%Y-%m-%dT%H:%M:%S.%fZ"
    )

    timestamp = round(
        (date - datetime.datetime(1970, 1, 1)).total_seconds() * 1000
    )

    result = {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": timestamp,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": jsonObject["data"]
    }

    return result


# Main function
def main(jsonObject):

    if jsonObject.get("device") is None:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)
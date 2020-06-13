import http.client, urllib.parse
import json


def location_params(location, api_key):
    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        'access_key': api_key,
        'query': location,
        'limit': 1,
        'output': 'json'
    })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()
    return data.decode('utf-8')


if __name__ == '__main__':
    location = input("Enter the location that you want to get location params:")
    api_key = input("Enter the api key that you get by creating account in apilayer.com [positionstack]:")
    print("Processing..........")
    loc_params = location_params(location, api_key)
    d = json.loads(loc_params)
    latitude = d['data'][0]['latitude']
    longitude = d['data'][0]['longitude']
    label =d['data'][0]['label']
    name =d['data'][0]['name']
    region =d['data'][0]['region']
    region_code =d['data'][0]['region_code']
    country =d['data'][0]['country']
    country_code=d['data'][0]['country_code']
    continent =d['data'][0]['continent']


    print("------------------------------------------------------------------------------------------")
    print("Location Params of the given location is:\n")
    print("Latitude:",latitude)
    print("longitude:", longitude)
    print("Label:", label)
    print("City Name:", name)
    print("Region:", region)
    print("Region_Code:", region_code)
    print("Country:", country)
    print("Country_Code:", country_code)
    print("Continent:", continent)
    print("------------------------------------------------------------------------------------------")



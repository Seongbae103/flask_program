import googlemaps as googlemaps

if __name__ == '__main__':
    key = 'AIzaSyAGmK7Y4ZBiQIBddE6PYXDwVjemiHioBLA'
    gmaps = googlemaps.Client(key=key)
    print(gmaps.geocode('대한민국 서울특별시 강남구 대치2동 514', language='ko'))
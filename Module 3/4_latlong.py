# by HAVERSINE formula
import math

if __name__ == '__main__':
    lat1 = float(input("Enter the latitude1: "))
    lon1 = float(input("Enter the longitude1:"))
    lat2 = float(input("Enter the latitude2: "))
    lon2 = float(input("Enter the longitude2:"))

    Radian = 6373.0
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)

    lat_dist = lat2 - lat1
    lon_dist = lon2 - lon1

    a = math.sin(lat_dist / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(lon_dist / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = Radian * c

    print("Distance between these given places is: %.2f " % distance)

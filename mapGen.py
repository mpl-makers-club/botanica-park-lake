import folium
import datetime

now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d")

with open('data.txt') as file:
    gpsData = str(file.read()).split('\n')
dateList = []
hourList = []
latitudeList = []
longitudeList = []
countList = []
for line in gpsData:
    if line != '':
        if 'latitude' not in str(line):
            line = line.split(',')
            print(line)
            date = str(line[0])
            hour = str(line[1])
            latitude = float(line[2])
            longitude = float(line[3])
            count = int(line[4])
            
            dateList.append(date)
            latitudeList.append(latitude)
            longitudeList.append(longitude)
            countList.append(count)

#m = folium.Map(location=[float(latitudeList[0]), float(longitudeList[0])],zoom_start=17)
#m = folium.Map(location=[float(latitudeList[len(latitudeList)-1]),float(longitudeList[len(longitudeList)-1])],zoom_start=17)
# GPS data location for Botanica Park Lake -37.679585,145.053497
m = folium.Map(location=[float(-37.679585), float(145.053497)],zoom_start=17)

                           
for i in range(len(latitudeList)):
    print("Dates")
    print(dateList[i])
    print(date_stamp)
    if date_stamp == dateList[i]:

        folium.Marker([float(latitudeList[i]),
                       float(longitudeList[i])],
                      popup='Litter collected on {}'.format(dateList[i]),
                      icon=folium.Icon(color='green')).add_to(m)
        print('Today - Marker {} added to map'.format(i+1))
    else:
        folium.Marker([float(latitudeList[i]),
                       float(longitudeList[i])],
                      popup='Litter collected on {}'.format(dateList[i]),
                      icon=folium.Icon(color='gray')).add_to(m)
        print('Old data - Marker {} added to map'.format(i+1))

m.save('dataLitterMap.html')
print("Map created")

        


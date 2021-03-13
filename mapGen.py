import folium
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

            latitudeList.append(latitude)
            longitudeList.append(longitude)
            countList.append(count)

m = folium.Map(location=[float(latitudeList[0]), float(longitudeList[0])])
                         
for i in range(len(latitudeList)):
               folium.Marker([float(latitudeList[i]),
                              float(longitudeList[i])],
                             popup='{} pieces of litter detected'.format(countList[i])).add_to(m)
               print('Marker {} added to map'.format(i+1))

m.save('dataLitterMap.html')

        


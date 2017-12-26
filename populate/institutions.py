#from populate import base
import json
from os import walk, path
from backend.models import Institution, City, Capacity, Institutions_Unit, Aqi

  

def read_json(dirname, file):
    return json.loads(open(dirname + '/' + file).read())

def fillCity(dirname, cityJson):
    cityJsonContent = read_json(dirname, cityJson)
    for items in cityJsonContent:
        cityName = items['city']
        for item in items['areas']:
            city = City()
            city.city_id = item['postal_code']
            city.city_name = cityName
            city.area_name = item['area_name']
            try:
                q1 = Aqi.objects.get(aqi_area=cityName)
                city.aqi_id = q1.aqi_id
            except:
                pass
            city.save()
    print('City table done!')


def fillInstitution(dirname):
    for root, dirs, files in walk(dirname):
        fileslist = files
    CapItems = set()
    cap = Capacity()
    c = 0

    for file in fileslist:
        jsonContent = read_json(dirname, file)
        for insContent in jsonContent:
            # print(insContent)
            ins = Institution()
            ins.ins_id = insContent['ins_id']
            ins.ins_type = insContent['ins_type']
            ins.ins_name = insContent['ins_name']
            ins.agent = insContent['agent']
            ins.phone = insContent['phone']
            ins.city = City.objects.get(city_id=insContent['ins_id'][:3])
            ins.address = insContent['address']
            ins.latitude = insContent['latitude']
            ins.longitude = insContent['longitude']
            CapItems.add(insContent['capacity'])
            ins.save()
    print('Institution table done!')

    for CapItem in CapItems:
        c = c + 1
        cap.cap_id = str(c) + '0'
        cap.cap_name = CapItem
        cap.save()
    print('Capacity table done!')

    for file in fileslist:
        jsonContent = read_json(dirname, file)
        for insContent in jsonContent:
            ins_unit = Institutions_Unit()
            ins_unit.Ins_id = Institution.objects.get(ins_id=insContent['ins_id'])
            ins_unit.Cap_id = Capacity.objects.get(cap_name=insContent['capacity'])
            ins_unit.num_bed = insContent['num_bed']
            ins_unit.save()
    print('Institutions_Unit table done!')


def populate():
    print('Populating..')
    fileslist = []
    dirname = '/Users/cytsai/FinalProject/SCWIP/csvToJson/'
    filterJsonDir = 'filterJson'
    cityJson = 'city.json'
    # allInit()
    fillCity(dirname, cityJson)
    fillInstitution(dirname + filterJsonDir)
    
if __name__ == '__main__':
    populate()

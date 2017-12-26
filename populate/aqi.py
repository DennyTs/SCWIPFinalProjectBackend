import json
from os import walk, path
from backend.models import Institution, City, Capacity, Institutions_Unit, Aqi


def allInit():
    Institution.objects.all().delete()
    City.objects.all().delete()
    Aqi.objects.all().delete()
    Capacity.objects.all().delete()
    Institutions_Unit.objects.all().delete()
    
def read_json(dirname, file):
    return json.loads(open(dirname + '/' + file).read())

def fillAqi(dirname, AQIJson):
    aqiJsonContent = read_json(dirname, AQIJson)
    # for items in aqiJsonContent:

def clasify(Area):
    if(Area == '北部'):
        return ['臺北市', '基隆市', '新北市', '桃園市']
    if(Area == '花東'):
        return ['花蓮縣', '臺東縣']
    if(Area == '高屏'):
        return ['高雄市', '屏東縣']
    if(Area == '雲嘉南'):
        return ['雲林縣', '嘉義縣', '臺南市']
    if(Area == '中部'):
        return ['臺中市', '彰化縣', '南投縣']
    if(Area == '竹苗'):
        return ['新竹縣', '苗栗縣']
    if(Area == '澎湖'):
        return ['澎湖縣']
    if(Area == '金門'):
        return ['金門縣']
    if(Area == '宜蘭'):
        return ['宜蘭縣']
    else:
        pass

def populate():
    allInit()
    a = 0 
    print('AQI populate')
    dirname = '/Users/cytsai/FinalProject/SCWIP/csvToJson/'
    aqiJson = 'AQI.json'
    aqiContent = read_json(dirname, aqiJson)
    for items in aqiContent:
        Area = clasify(items['Area'])
        if(Area != None):
            for item in Area:
                a = a + 1
                aqi = Aqi()
                aqi.aqi_id = str(a) 
                aqi.aqi_area = item
                aqi.aqi_index = items['AQI']
                aqi.save()
        else:
            pass
    print('AQI table done!')


if __name__ == '__main__':
    populate()


# class Aqi(models.Model):
#     aqi_id = models.IntegerField(primary_key=True)
#     aqi_area = models.CharField(max_length=10)
#     aqi_index = models.IntegerField()
#     aqi_pubdate = models.DateTimeField()
       
#     def __str__(self):
#         return str(self.aqi_area)

#     class Meta:
#         db_table = 'AQI'
#         # ordering = ('aqi_id')
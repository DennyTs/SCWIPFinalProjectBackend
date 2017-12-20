import json
from os import walk, path
from backend.models import Institution, City, Capacity, Institutions_Unit, Aqi


def allInit():
    Aqi.object.all().delete()

def read_json(dirname, file):
    return json.loads(open(dirname + '/' + file).read())

def fillAqi(dirname, AQIJson):
    aqiJsonContent = read_json(dirname, AQIjson)
    for items in aqiJsonContent:
        aqi = Aqi()
        try:
            if item['Area'] = "澎湖"：
                aqi.aqi_area = item['澎湖']
            else item['Area'] = "金門"：
                aqi.aqi_area = item['金門']
                
            


# class Aqi(models.Model):
#     aqi_id = models.IntegerField(primary_key=True)
#     aqi_area = models.CharField(max_length=10)
#     aqi_index = models.IntegerField()
#     aqi_pubdate = models.DateTimeField()
from django.shortcuts import render

from trips.models import Post

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts
from collections import OrderedDict


#首頁
def home(request):
  post_list = Post.objects.all()
  TaiwanChart(request)
  return render(request, 'home.html', {'post_list': post_list})


def TaiwanChart(request):
  post_list = Post.objects.all()

  # Reference: https://www.fusioncharts.com/dev/api/fusioncharts/fusioncharts-events#dataplotclick-261
  # Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
  # The data is passed as a string in the `dataSource` as parameter.
  dataSource = OrderedDict()

  # The `chartConfig` dict contains key-value pairs of data for chart attribute
  chartConfig = OrderedDict()
  #chartConfig["caption"] = "想要去玩的地點"
  #chartConfig["subcaption"] = "SIRLA 2020-07"
  chartConfig["showLabels"] = "0"
  chartConfig["showLegend"] = "0"
  chartConfig["showMarker"] = "1"
  chartConfig["borderThickness"] = "0.5"
  chartConfig["theme"] = "fusion" # fusion, gammel, candy, umber
  dataSource["chart"] = chartConfig

  colorrange_chartConfig = OrderedDict()
  colorrange_chartConfig["minvalue"] = "20"
  colorrange_chartConfig["code"] = "#000000"

  dataSource["colorrange"] = colorrange_chartConfig

  dataSource["data"] = []
  # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
  # Insert the data into the `dataSource['data']` list.
  area_value = []
  for i in range(28):
    area_value.append(0)
  for po in post_list:
    area_value[po.area-1] +=1
  
  dataSource["data"].append({"ID": "01", "tooltext": "彰化縣: $value", "value": str(area_value[9]), "link": "/area?ID=10"})
  dataSource["data"].append({"ID": "02", "tooltext": "嘉義縣: $value", "value": str(area_value[11]),  "link": "/area?ID=12"})
  dataSource["data"].append({"ID": "03", "tooltext": "嘉義市: $value", "value": str(area_value[12]), "link": "/area?ID=13"})
  dataSource["data"].append({"ID": "04", "tooltext": "新竹縣: $value", "value": str(area_value[4]), "link": "/area?ID=5"})
  dataSource["data"].append({"ID": "05", "tooltext": "新竹市: $value", "value":str(area_value[5]), "link": "/area?ID=6"})
  dataSource["data"].append({"ID": "06", "tooltext": "花蓮縣: $value", "value": str(area_value[18]), "link": "/area?ID=19"})
  dataSource["data"].append({"ID": "09", "tooltext": "基隆市: $value", "value": str(area_value[0]), "link": "/area?ID=1"})
  dataSource["data"].append({"ID": "10", "tooltext": "金門縣: $value", "value": str(area_value[20]), "link": "/area?ID=21"})
  dataSource["data"].append({"ID": "11", "tooltext": "連江縣: $value", "value": str(area_value[21]), "link": "/area?ID=22"})
  dataSource["data"].append({"ID": "12", "tooltext": "苗栗縣: $value", "value":str(area_value[6]), "link": "/area?ID=7"})
  dataSource["data"].append({"ID": "13", "tooltext": "南投縣: $value", "value": str(area_value[7]), "link": "/area?ID=8"})
  dataSource["data"].append({"ID": "14", "tooltext": "澎湖縣: $value", "value": str(area_value[19]), "link": "/area?ID=20"})
  dataSource["data"].append({"ID": "15", "tooltext": "屏東縣: $value", "value": str(area_value[15]), "link": "/area?ID=16"})
  dataSource["data"].append({"ID": "20", "tooltext": "新北市: $value", "value": str(area_value[2]), "link": "/area?ID=3"})
  dataSource["data"].append({"ID": "21", "tooltext": "台北市: $value", "value": str(area_value[1]), "link": "/area?ID=2"})
  dataSource["data"].append({"ID": "22", "tooltext": "台東縣: $value", "value": str(area_value[16]), "link": "/area?ID=17"})
  dataSource["data"].append({"ID": "23", "tooltext": "桃園市: $value", "value": str(area_value[3]), "link": "/area?ID=4"})
  dataSource["data"].append({"ID": "24", "tooltext": "宜蘭縣: $value", "value": str(area_value[17]), "link": "/area?ID=18"})
  dataSource["data"].append({"ID": "25", "tooltext": "雲林縣: $value", "value": str(area_value[10]), "link": "/area?ID=11"})
  dataSource["data"].append({"ID": "26", "tooltext": "台中市: $value", "value":str(area_value[8]), "link": "/area?ID=9"})
  dataSource["data"].append({"ID": "27", "tooltext": "高雄市: $value", "value": str(area_value[14]), "link": "/area?ID=15"})
  dataSource["data"].append({"ID": "28", "tooltext": "台南市: $value", "value": str(area_value[13]), "link": "/area?ID=14"})

  # Create an object for the map using the FusionCharts class constructor 
  # The chart data is passed to the `dataSource` parameter.
  fusionMap = FusionCharts("maps/taiwan", "TaiwanChart", "950", "750", "TaiwanChart-container", "json", dataSource)
  # returning complete JavaScript and HTML code, which is used to generate map in the browsers. 
  return render(request, 'home.html', {'output': fusionMap.render(), 'chartTitle': '台灣地圖'})
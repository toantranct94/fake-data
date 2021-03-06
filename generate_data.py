from decimal import BasicContext
import random
import csv
import os
from datetime import datetime
from config import BaseConfig
from typing import List
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def get_nmi_configuration() -> str:
    return random.choice(BaseConfig.nmi_configuration)


def get_location(index) -> str:
    return str(index+1) + ' ' + random.choice(BaseConfig.location_configuration)


def get_weather() -> str:
    return random.choice(BaseConfig.weathers)


def get_region() -> str:
    return random.choice(BaseConfig.regions)


def get_quality_method() -> str:
    return random.choice(BaseConfig.quality_methods)


def generate_nmi_name(index: int) -> str:
    index = str(index)
    nmi_name = f'NMI_DUM{index.zfill(4)}'
    return nmi_name


def get_current_date(interval: int) -> str:
    now = datetime.now() + timedelta(days=interval)
    four_month_ago_date = now - relativedelta(months=2)
    return four_month_ago_date.strftime('%Y%m%d')


def get_weight_by_weather(weather: str) -> float:
    weight = 1.0
    if weather == 'Heat':
        weight = 1.25
    elif weather == 'Snowy':
        weight = 1.25
    elif weather == 'Cloudy':
        weight = 0.95
    elif weather == 'Rainy':
        weight = 0.85
    elif weather == 'Lightning':
        weight = 0.75
    return weight


def get_temp_and_humidity(weather: str) -> float:
    temp = 10
    humidity = 80
    if weather == 'Heat':
        temp = 20
        humidity = 70
    elif weather == 'Snowy':
        temp = 0
        humidity = 95
    elif weather == 'Cloudy':
        temp = 10
        humidity = 75
    elif weather == 'Rainy':
        temp = 5
        humidity = 95
    elif weather == 'Lightning':
        temp = 7
        humidity = 60
    return temp, humidity


def get_weather_information() -> str:
    weather = get_weather()
    temp, humidity = get_temp_and_humidity(weather)
    return [weather, temp, humidity]


def calculate_kwhs(weather: str, kwh_range: List) -> List:
    weight = get_weight_by_weather(weather)
    kwhs = []
    for _ in range(96):
        kwhs.append(
            weight * round(random.uniform(kwh_range[0], kwh_range[1]), 3)
        )
    return kwhs


def get_uom(nmi_suffix: str) -> str:
    if nmi_suffix == 'Q1':
        return BaseConfig.uom[1]
    return BaseConfig.uom[0]


def get_register_id(nmi_suffix: str) -> str:
    if nmi_suffix == 'Q1':
        return BaseConfig.register_id[1]
    return BaseConfig.register_id[0]


def get_meter_type() -> str:
    return random.choice(BaseConfig.meter_type)


def generate_dummy_data(index):
    '''
    Contact Alex or Tony to read more about the generate rules
    '''
    path = os.path.join(os.getcwd(), f'NEM12#{index}1.csv')
    exist_weather = {}
    nmi_region = {}
    nmi_location = {}
    nmi_meter_type = {}
    with open(path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(BaseConfig.row_100)
        for day_index in range(BaseConfig.number_of_generate_day):
            current_date = get_current_date(day_index)
            for nmi_index in range (BaseConfig.number_of_generate_nmi):
                nmi_name = generate_nmi_name(nmi_index)
                nmi_configuration = get_nmi_configuration()
                exist_region = nmi_region.get(nmi_name, '')
                exist_location = nmi_location.get(nmi_name, '')
                exist_meter_type = nmi_meter_type.get(nmi_name, '')
                if not exist_region:
                    region = get_region()
                    nmi_region.update({
                        nmi_name: region
                    })
                else:
                    region = exist_region
                if not exist_location:
                    location = get_location(nmi_index)
                    nmi_location.update({
                        nmi_name: location
                    })
                else:
                    location = exist_location
                if not exist_meter_type:
                    meter_type = get_meter_type()
                    nmi_meter_type.update({
                        nmi_name: meter_type
                    })
                else:
                    meter_type = exist_meter_type
                for nmi_suffix in BaseConfig.nmi_suffixes:
                    uom = get_uom(nmi_suffix)
                    register_id = get_register_id(nmi_suffix)
                    row_200 = [
                        '200', nmi_name, nmi_configuration, register_id,
                        nmi_suffix, BaseConfig.mdm_datastream_id, BaseConfig.meter_name,
                        uom, BaseConfig.interval, current_date, region, location, meter_type
                    ]
                    row_300 = [
                        '300', current_date
                    ]
                    for weather_index in range(3):
                        key_weather = f'{region}_{weather_index}'
                        if not exist_weather.get(key_weather, None):
                            weather_info = get_weather_information()
                            exist_weather.update({
                                key_weather: weather_info
                            })
                        else:
                            weather_info = exist_weather.get(key_weather, [])
                        row_200.extend(weather_info)
                        weather = weather_info[0]
                        kwhs = calculate_kwhs(
                            weather, BaseConfig.kwh_range.get(weather_index)
                        )
                        row_300.extend(kwhs)
                    writer.writerow(row_200)
                    quality = get_quality_method()
                    row_300.append(quality)
                    row_300 += ['', '', current_date, current_date]
                    writer.writerow(row_300)
                    if quality == 'V':
                        for row_400 in BaseConfig.row_400s:
                            writer.writerow(row_400)
        writer.writerow(BaseConfig.row_900)


if __name__ == "__main__":
    for i in range(0, BaseConfig.number_of_generate_files):
        generate_dummy_data(i)
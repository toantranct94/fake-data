

class BaseConfig(object):
    nmi_configuration = ['E1', 'Q1']
    weathers = ['Heat', 'Snowy', 'Cloudy', 'Rainy', 'Lightning']
    regions = ['WA', 'NSW', 'QLD', 'SA', 'TAS', 'VIC']
    intervel = 5
    uom = 'kWh'
    quality_methods = ['A', 'S', 'F', 'V']
    number_of_generate_nmi = 1000
    number_of_generate_day = 30
    number_of_generate_files = 1
    register_id = '001'
    meter_name = 'METSER_123'
    kwh_range = {
        0: [0, 30],
        1: [30, 70],
        2: [20, 40]
    }
    row_100 = ['100' ,'NEM12', '200312221300', 'MDA1' ,'Ret1']
    row_400s = [
        ['400', 1, 30, 'S'],
        ['400', 31, 288, 'A'],
    ]
    row_900 = [
        '900'
    ]

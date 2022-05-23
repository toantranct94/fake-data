class BaseConfig(object):
    nmi_configuration = ['E1Q1']
    nmi_suffixes = ['E1', 'Q1']
    weathers = ['Heat', 'Snowy', 'Cloudy', 'Rainy', 'Lightning']
    regions = ['WA', 'NSW', 'QLD', 'SA', 'TAS', 'VIC']
    meter_type = ['Smart Meter', 'Standard Meter']
    location_configuration = ['Acacia Avenue', 'Aberfeldy Street', 'Maibry Street-Wishart', 'Malcolm Street-Enoggera', 'Metro Street-Mcdowall', 'Metroplex Avenue-Murrarie', 'Peter Street-Clayfield', 'Deckerplace Huntingwood', 'Hills Street Garbutt', 'Church Street Toorak', 'Swinbourne Street Botany', 'Beach Road Avalon Airport', 'Concord Crescent Carrum Downs', 'Foorscray Road West Melbourne', 'Palmer Street Portsmith', 'Percy Auburn', 'Hedley Avenue Hendra', 'Riverview Place Murrarie', 'Pie Street-Aspley', 'Depot Street Maroonchydore', 'Nudgee Road Hendra', 'Pilinger Road', 'Pinkwood Street', 'Hills Street Garbutt',
    'Alex Fisher Drive Burleigh', 'Paradise Road-Willawong', 'Goldsborough Road Pooraka', 'Grand Junction Road Wingfield',
    'Tully Street-Keprra', 'Tumna Street-Ferny Grove', 'Union Street-Clayfield']
    interval = 5
    uom = ['kWh', 'kVArh']
    quality_methods = ['A', 'S', 'F', 'V']
    number_of_generate_nmi = 10
    number_of_generate_day = 30
    number_of_generate_files = 1
    register_id = ['001', '002']
    mdm_datastream_id = 'N1'
    meter_name = 'METSER_123'
    kwh_range = {
        0: [0, 30],
        1: [30, 70],
        2: [20, 40]
    }
    row_100 = ['100' ,'NEM12', '200312221300', 'MDA1' ,'Ret1']
    row_400s = [
        ['400', 1, 30, 'S14', '', ''],
        ['400', 31, 288, 'A', '', ''],
    ]
    row_900 = [
        '900'
    ]

import pandas as pd
import numpy as np
import hashlib

DATE = [
    "20241201", "20241202", "20241203", "20241204", "20241205", "20241206", "20241207", "20241208", "20241209",
    "20241210", "20241211", "20241212", "20241213", "20241214", "20241215", "20241216", "20241217", "20241218",
    "20241219", "20241220", "20241221", "20241222", "20241223", "20241224", "20241225", "20241226", "20241227",
    "20241228", "20241229", "20241230", "20241231",
    "20250501", "20250502", "20250503", "20250504", "20250505", "20250506", "20250507", "20250508", "20250509",
    "20250510", "20250511", "20250512", "20250513", "20250514", "20250515", "20250516", "20250517", "20250518",
    "20250519", "20250520", "20250521", "20250522", "20250523", "20250524", "20250525", "20250526", "20250527",
    "20250528", "20250529", "20250530", "20250531",
    "20250601", "20250602", "20250603", "20250604", "20250605", "20250606", "20250607", "20250608", "20250609",
    "20250610", "20250611", "20250612", "20250613", "20250614", "20250615", "20250616", "20250617", "20250618",
    "20250619", "20250620", "20250621", "20250622", "20250623", "20250624", "20250625", "20250626", "20250627",
    "20250628", "20250629", "20250630"
]

BOILER_ID = [
    'TC-BLR-001-A', 'TC-BLR-002-B', 'HP-HRSG-101-P1', 'GD-ECO-202-S3',
    'ZX-SUPER-305-M2', 'NJ-TH-008-W1', 'SF-WHR-045-C', 'BH-PACKAGE-12-D4',
    'LY-SCFB-770-N', 'KM-OT-556-E3', 'SD-FB-334-G7', 'YN-HEAT-889-F',
    'TL-VERTICAL-112-K', 'RC-FIRE-223-P', 'CQ-WATER-445-T2', 'FJ-TRAVEL-667-R',
    'HM-CHAIN-078-V', 'JK-FLUID-991-X1', 'PW-COIL-123-Y', 'GL-HORIZ-256-Z4',
    'KS-DTYPE-789-A5', 'BH-MULTI-654-B3', 'TC-BLR-003-C', 'TC-BLR-004-D',
    'HP-HRSG-102-P2', 'GD-ECO-203-S4', 'ZX-SUPER-306-M3', 'NJ-TH-009-W2',
    'SF-WHR-046-C2', 'BH-PACKAGE-13-D5', 'LY-SCFB-771-N2', 'KM-OT-557-E4',
    'SD-FB-335-G8', 'YN-HEAT-890-F2', 'TL-VERTICAL-113-K2', 'RC-FIRE-224-P2',
    'CQ-WATER-446-T3', 'FJ-TRAVEL-668-R2', 'HM-CHAIN-079-V2', 'JK-FLUID-992-X2',
    'PW-COIL-124-Y2', 'GL-HORIZ-257-Z5', 'KS-DTYPE-790-A6', 'BH-MULTI-655-B4',
    'TC-BLR-005-E', 'TC-BLR-006-F', 'HP-HRSG-103-P3', 'GD-ECO-204-S5',
    'ZX-SUPER-307-M4', 'NJ-TH-010-W3', 'SF-WHR-047-C3', 'BH-PACKAGE-14-D6',
    'LY-SCFB-772-N3', 'KM-OT-558-E5', 'SD-FB-336-G9', 'YN-HEAT-891-F3',
    'TL-VERTICAL-114-K3', 'RC-FIRE-225-P3', 'CQ-WATER-447-T4', 'FJ-TRAVEL-669-R3',
    'HM-CHAIN-080-V3', 'JK-FLUID-993-X3', 'PW-COIL-125-Y3', 'GL-HORIZ-258-Z6',
    'KS-DTYPE-791-A7', 'BH-MULTI-656-B5', 'TC-BLR-007-G', 'TC-BLR-008-H',
    'HP-HRSG-104-P4', 'GD-ECO-205-S6', 'ZX-SUPER-308-M5', 'NJ-TH-011-W4',
    'SF-WHR-048-C4', 'BH-PACKAGE-15-D7', 'LY-SCFB-773-N4', 'KM-OT-559-E6',
    'SD-FB-337-G10', 'YN-HEAT-892-F4', 'TL-VERTICAL-115-K4', 'RC-FIRE-226-P4',
    'CQ-WATER-448-T5', 'FJ-TRAVEL-670-R4', 'HM-CHAIN-081-V4', 'JK-FLUID-994-X4',
    'PW-COIL-126-Y4', 'GL-HORIZ-259-Z7', 'KS-DTYPE-792-A8', 'BH-MULTI-657-B6',
    'TC-BLR-009-I', 'TC-BLR-010-J', 'HP-HRSG-105-P5', 'GD-ECO-206-S7',
    'ZX-SUPER-309-M6', 'NJ-TH-012-W5', 'SF-WHR-049-C5', 'BH-PACKAGE-16-D8',
    'LY-SCFB-774-N5', 'KM-OT-560-E7', 'SD-FB-338-G11', 'YN-HEAT-893-F5',
    'TL-VERTICAL-116-K5', 'RC-FIRE-227-P5', 'CQ-WATER-449-T6', 'FJ-TRAVEL-671-R5',
    'HM-CHAIN-082-V5', 'JK-FLUID-995-X5', 'PW-COIL-127-Y5', 'GL-HORIZ-260-Z8'
]


def get_md5_num(username):
    md5_machine = hashlib.md5()
    md5_machine.update(username.encode('utf-8'))
    md5_hash_string = md5_machine.hexdigest()
    return md5_hash_string


def mock_data(boiler_path, facility_path):
    boiler_result = pd.DataFrame(
        columns=['id', 'boiler_id', 'date', 'label', 'boiler_type', 'boiler_age',
                 'operating_temperature', 'operating_temperature_max', 'operating_temperature_min',
                 'operating_pressure', 'operating_pressure_max', 'operating_pressure_min',
                 'water_flow_rate', 'fuel_flow_rate',
                 'combustion_efficiency', 'ambient_temperature_max', 'ambient_temperature_min',
                 'ambient_humidity', 'operating_temperature_weak', 'last_maintenance_day',
                 'maintenance_month', 'maintenance_1_month', 'maintenance_6_month', 'failure_6_month'
                 ]
    )
    facility_result = pd.DataFrame(
        columns=['id', 'boiler_id', 'date', 'manufacturer', 'average_lifespan',
                 'average_failure_month', 'average_maintenance_month', 'average_alarms_month'
                 ]
    )

    for date in DATE:
        for boiler_id in BOILER_ID:
            _id = get_md5_num(date + boiler_id)
            label = int(np.random.randint(0, 2))
            boiler_type = int(np.random.randint(0, 4))
            boiler_age = int(np.random.randint(1, 20))
            operating_temperature_min = int(np.random.randint(-5, 20))
            temperature_difference = int(np.random.randint(5, 20))
            operating_temperature_max = operating_temperature_min + temperature_difference
            operating_temperature = round((operating_temperature_min + operating_temperature_max) / 2, 2)
            operating_pressure_min = round(float(np.random.random() * 5) + 2, 2)
            pressure_difference = round(float(np.random.random() * 3), 2)
            operating_pressure_max = round(operating_pressure_min + pressure_difference, 2)
            operating_pressure = round((operating_pressure_min + operating_pressure_max) / 2, 2)
            water_flow_rate = round(float(np.random.random() * 50) + 1, 2)
            fuel_flow_rate = round(float(np.random.random() * 50) + 1, 2)
            combustion_efficiency = round(float(np.random.random() / 2) + 0.3, 2)
            ambient_temperature_min = int(np.random.randint(10, 30))
            ambient_temperature_difference = int(np.random.randint(5, 10))
            ambient_temperature_max = round(ambient_temperature_min + ambient_temperature_difference, 2)
            ambient_humidity = round(float(np.random.random() / 2) + 0.3, 2)
            operating_temperature_weak = round(operating_pressure + float(np.random.random() * 2) - 1, 2)
            last_maintenance_day = int(np.random.randint(1, 60))
            maintenance_month = int(np.random.randint(1, 5))
            maintenance_1_month = int(np.random.randint(maintenance_month, 10))
            maintenance_6_month = int(np.random.randint(maintenance_month, 20))
            failure_6_month = int(np.random.randint(1, 10))

            manufacturer = int(np.random.randint(0, 4))
            average_lifespan = round(np.random.random() * 15 + 5, 2)
            average_failure_month = round(np.random.random() * 5 + 5, 2)
            average_maintenance_month = round(np.random.random() * 5 + 5, 2)
            average_alarms_month = round(np.random.random() * 5 + 5, 2)

            boiler_data = [
                _id, boiler_id, date, label, boiler_type, boiler_age,
                operating_temperature, operating_temperature_max, operating_temperature_min,
                operating_pressure, operating_pressure_max, operating_pressure_min,
                water_flow_rate, fuel_flow_rate,
                combustion_efficiency, ambient_temperature_max, ambient_temperature_min,
                ambient_humidity, operating_temperature_weak, last_maintenance_day,
                maintenance_month, maintenance_1_month, maintenance_6_month, failure_6_month

            ]
            boiler_result.loc[len(boiler_result)] = boiler_data

            facility_data = [_id, boiler_id, date, manufacturer, average_lifespan,
                             average_failure_month, average_maintenance_month, average_alarms_month]
            facility_result.loc[len(facility_result)] = facility_data

    boiler_result.to_csv(boiler_path, index=False, sep=',')
    facility_result.to_csv(facility_path, index=False, sep=',')


if __name__ == '__main__':
    _boiler_path = 'C:\\Users\\yu.zhang\\Desktop\\国家能源可信数据空间\\boiler_data.csv'
    _facility_path = 'C:\\Users\\yu.zhang\\Desktop\\国家能源可信数据空间\\facility_data.csv'
    mock_data(_boiler_path, _facility_path)

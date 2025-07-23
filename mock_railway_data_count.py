import pandas as pd
import numpy as np
import hashlib

CITY_NAME = [
    "苏州", "杭州", "广州"
]
DATE = [
    "20240101", "20240102", "20240103", "20240104", "20240105", "20240106", "20240107", "20240108", "20240109",
    "20240110", "20240111", "20240112", "20240113", "20240114", "20240115", "20240116", "20240117", "20240118",
    "20240119", "20240120", "20240121", "20240122", "20240123", "20240124", "20240125", "20240126", "20240127",
    "20240128", "20240129", "20240130", "20240131",
    "20240201", "20240202", "20240203", "20240204", "20240205", "20240206", "20240207", "20240208", "20240209",
    "20240210", "20240211", "20240212", "20240213", "20240214", "20240215", "20240216", "20240217", "20240218",
    "20240219", "20240220", "20240221", "20240222", "20240223", "20240224", "20240225", "20240226", "20240227",
    "20240228", "20240229",
    "20240301", "20240302", "20240303", "20240304", "20240305", "20240306", "20240307", "20240308", "20240309",
    "20240310", "20240311", "20240312", "20240313", "20240314", "20240315", "20240316", "20240317", "20240318",
    "20240319", "20240320", "20240321", "20240322", "20240323", "20240324", "20240325", "20240326", "20240327",
    "20240328", "20240329", "20240330", "20240331",
    "20240401", "20240402", "20240403", "20240404", "20240405", "20240406", "20240407", "20240408", "20240409",
    "20240410", "20240411", "20240412", "20240413", "20240414", "20240415", "20240416", "20240417", "20240418",
    "20240419", "20240420", "20240421", "20240422", "20240423", "20240424", "20240425", "20240426", "20240427",
    "20240428", "20240429", "20240430",
    "20240501", "20240502", "20240503", "20240504", "20240505", "20240506", "20240507", "20240508", "20240509",
    "20240510", "20240511", "20240512", "20240513", "20240514", "20240515", "20240516", "20240517", "20240518",
    "20240519", "20240520", "20240521", "20240522", "20240523", "20240524", "20240525", "20240526", "20240527",
    "20240528", "20240529", "20240530", "20240531",
    "20240601", "20240602", "20240603", "20240604", "20240605", "20240606", "20240607", "20240608", "20240609",
    "20240610", "20240611", "20240612", "20240613", "20240614", "20240615", "20240616", "20240617", "20240618",
    "20240619", "20240620", "20240621", "20240622", "20240623", "20240624", "20240625", "20240626", "20240627",
    "20240628", "20240629", "20240630",
    "20240701", "20240702", "20240703", "20240704", "20240705", "20240706", "20240707", "20240708", "20240709",
    "20240710", "20240711", "20240712", "20240713", "20240714", "20240715", "20240716", "20240717", "20240718",
    "20240719", "20240720", "20240721", "20240722", "20240723", "20240724", "20240725", "20240726", "20240727",
    "20240728", "20240729", "20240730", "20240731",
    "20240801", "20240802", "20240803", "20240804", "20240805", "20240806", "20240807", "20240808", "20240809",
    "20240810", "20240811", "20240812", "20240813", "20240814", "20240815", "20240816", "20240817", "20240818",
    "20240819", "20240820", "20240821", "20240822", "20240823", "20240824", "20240825", "20240826", "20240827",
    "20240828", "20240829", "20240830", "20240831",
    "20240901", "20240902", "20240903", "20240904", "20240905", "20240906", "20240907", "20240908", "20240909",
    "20240910", "20240911", "20240912", "20240913", "20240914", "20240915", "20240916", "20240917", "20240918",
    "20240919", "20240920", "20240921", "20240922", "20240923", "20240924", "20240925", "20240926", "20240927",
    "20240928", "20240929", "20240930",
    "20241001", "20241002", "20241003", "20241004", "20241005", "20241006", "20241007", "20241008", "20241009",
    "20241010", "20241011", "20241012", "20241013", "20241014", "20241015", "20241016", "20241017", "20241018",
    "20241019", "20241020", "20241021", "20241022", "20241023", "20241024", "20241025", "20241026", "20241027",
    "20241028", "20241029", "20241030", "20241031",
    "20241101", "20241102", "20241103", "20241104", "20241105", "20241106", "20241107", "20241108", "20241109",
    "20241110", "20241111", "20241112", "20241113", "20241114", "20241115", "20241116", "20241117", "20241118",
    "20241119", "20241120", "20241121", "20241122", "20241123", "20241124", "20241125", "20241126", "20241127",
    "20241128", "20241129", "20241130", "20241201"]


def get_md5_num(username):
    md5_machine = hashlib.md5()
    md5_machine.update(username.encode('utf-8'))
    md5_hash_string = md5_machine.hexdigest()
    return md5_hash_string


def mock_data(railway_path, highway_path, aircraft_path):
    result_railway = pd.DataFrame(
        columns=["id", "locations", "date", "label", "train_people_count",
                 "train_people_count_avg_near_month", "train_people_count_avg_near_week",
                 "train_people_count_avg_this_month"]
    )
    result_highway = pd.DataFrame(
        columns=["id", "locations", "date", "highway_people_count",
                 "highway_people_count_near_month", "highway_people_count_near_week",
                 "highway_people_count_this_month"]
    )
    result_aircraft = pd.DataFrame(
        columns=["id", "locations", "date", "airport_people_count",
                 "airport_people_count_near_month",
                 "airport_people_count_near_week", "airport_people_count_this_month"]
    )

    for city in CITY_NAME:
        for date in DATE:
            value = city + date
            _id = get_md5_num(value)
            label = int(np.random.randint(200000, 250000))

            train_people_count = int(np.random.randint(int(label * 0.4), int(label * 0.6)))
            train_people_count_avg_near_month = int(np.random.randint(int(label * 0.4), int(label * 0.6)))
            train_people_count_avg_near_week = int(np.random.randint(int(label * 0.4), int(label * 0.6)))
            train_people_count_avg_this_month = int(np.random.randint(int(label * 0.4), int(label * 0.6)))

            highway_people_count = int(np.random.randint(int(label * 0.1), int(label * 0.2)))
            highway_people_count_near_month = int(np.random.randint(int(label * 0.1), int(label * 0.2)))
            highway_people_count_avg_near_week = int(np.random.randint(int(label * 0.1), int(label * 0.2)))
            highway_people_count_this_month = int(np.random.randint(int(label * 0.1), int(label * 0.2)))

            aircraft_people_count = int(np.random.randint(int(label * 0.05), int(label * 0.1)))
            aircraft_people_count_avg_near_month = int(np.random.randint(int(label * 0.05), int(label * 0.1)))
            aircraft_people_count_avg_near_week = int(np.random.randint(int(label * 0.05), int(label * 0.1)))
            airport_people_count_this_month = int(np.random.randint(int(label * 0.05), int(label * 0.1)))

            data_railway = [
                _id, city, date, label, train_people_count, train_people_count_avg_near_month,
                train_people_count_avg_near_week, train_people_count_avg_this_month
            ]
            result_railway.loc[len(result_railway)] = data_railway

            data_highway = [
                _id, city, date, highway_people_count, highway_people_count_near_month,
                highway_people_count_avg_near_week, highway_people_count_this_month
            ]
            result_highway.loc[len(result_highway)] = data_highway

            data_aircraft = [
                _id, city, date, aircraft_people_count, aircraft_people_count_avg_near_month,
                aircraft_people_count_avg_near_week, airport_people_count_this_month
            ]
            result_aircraft.loc[len(result_aircraft)] = data_aircraft

    result_railway.to_csv(railway_path, index=False, sep=',')
    result_highway.to_csv(highway_path, index=False, sep=',')
    result_aircraft.to_csv(aircraft_path, index=False, sep=',')


if __name__ == '__main__':
    _railway_path = 'C:\\Users\\yu.zhang\\Desktop\\铁科院\\railway_data.csv'
    _highway_path = 'C:\\Users\\yu.zhang\\Desktop\\铁科院\\highway_data.csv'
    _aircraft_path = 'C:\\Users\\yu.zhang\\Desktop\\铁科院\\aircraft_data.csv'
    mock_data(_railway_path, _highway_path, _aircraft_path)

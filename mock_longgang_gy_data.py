
import pandas as pd
import numpy as np
import hashlib

GM = [
    "坪地分馆", "坪西社区分馆", "坪东社区分馆", "横岗分馆", "南湾分馆",
    "吉厦社区图书馆", "南岭村自助分馆", "布吉分馆", "龙岭学校分馆", "平湖分馆"
]

DATE = [
    "20250501", "20250502", "20250503", "20250504", "20250505", "20250506", "20250507", "20250508", "20250509",
    "20250510", "20250511", "20250512", "20250513", "20250514", "20250515", "20250516", "20250517", "20250518",
    "20250519", "20250520", "20250521", "20250522", "20250523", "20250524", "20250525", "20250526", "20250527",
    "20250528", "20250529", "20250530", "20250531",
    "20250601", "20250602", "20250603", "20250604", "20250605", "20250606", "20250607", "20250608", "20250609",
    "20250610", "20250611", "20250612", "20250613", "20250614", "20250615", "20250616", "20250617", "20250618",
    "20250619", "20250620", "20250621", "20250622", "20250623", "20250624", "20250625", "20250626", "20250627",
    "20250628", "20250629", "20250630"
]


def get_md5_num(username):
    md5_machine = hashlib.md5()
    md5_machine.update(username.encode('utf-8'))
    md5_hash_string = md5_machine.hexdigest()
    return md5_hash_string


def mock_data(park_path, bus_path):
    result_park = pd.DataFrame(
        columns=["id", "gm", "date", "label", "num_bus",
                 "num_bws", "num_xydhct", "num_jd", "num_tsg", "num_yy", "num_tyg"]
    )
    result_bus = pd.DataFrame(
        columns=["id", "gm", "date", "day_people_count_on_avg", "day_people_count_off_avg",
                 "month_people_count_on_avg", "month_people_count_off_avg",
                 "year_people_count_on_avg", "year_people_count_off_avg"]
    )

    for gm in GM:

        num_bus = int(np.random.randint(1, 4))
        num_bws = int(np.random.randint(0, 2 * num_bus))
        num_xydhct = int(np.random.randint(0, num_bus))
        num_jd = int(np.random.randint(0, 3))
        num_tsg = int(np.random.randint(0, 1))
        num_yy = int(np.random.randint(0, 1))
        num_tyg = int(np.random.randint(0, 1))

        for date in DATE:
            value = gm + date
            _id = get_md5_num(value)
            label = int(np.random.randint(0, 2))

            day_people_count_on_avg = int(np.random.randint(20, 100))
            day_people_count_off_avg = int(np.random.randint(20, 100))
            month_people_count_on_avg = int(np.random.randint(20, 100))
            month_people_count_off_avg = int(np.random.randint(20, 100))
            year_people_count_on_avg = int(np.random.randint(20, 100))
            year_people_count_off_avg = int(np.random.randint(20, 100))

            data_park = [
                _id, gm, date, label, num_tyg, num_bws, num_xydhct, num_jd, num_tsg, num_yy, num_tyg
            ]
            result_park.loc[len(result_park)] = data_park

            data_bus = [
                _id, gm, date, day_people_count_on_avg, day_people_count_off_avg,
                month_people_count_on_avg, month_people_count_off_avg,
                year_people_count_on_avg, year_people_count_off_avg
            ]
            result_bus.loc[len(result_bus)] = data_bus

    result_park.to_csv(park_path, index=False, sep=',')
    result_bus.to_csv(bus_path, index=False, sep=',')


if __name__ == '__main__':
    _park_path = 'C:\\Users\\yu.zhang\\Desktop\\龙岗数据\\park_data.csv'
    _bus_path = 'C:\\Users\\yu.zhang\\Desktop\\龙岗数据\\bus_data.csv'
    mock_data(_park_path, _bus_path)

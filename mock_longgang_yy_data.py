
import pandas as pd
import numpy as np
import hashlib

JGMC = [
    "深圳华侨医院", "深圳仁安医院", "深圳肖传国医院", "深圳百合医院", "深圳中海医院",
    "深圳港龙妇产医院", "深圳龙城医院", "深圳万东医院", "深圳六联妇产医院", "深圳和济医院"
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
    result_wsjkj = pd.DataFrame(
        columns=["id", "jgmc", "date", "y", "byxz", "is_yb", "num_jz"]
    )
    result_yy = pd.DataFrame(
        columns=["id", "jgmc", "date", "num_zrys", "num_fzrys",
                 "num_ks", "num_zdsys", "amount_zdsys", "num_people", "amount_daily"]
    )

    for jgmc in JGMC:

        byxz = int(np.random.randint(0, 2))
        is_yb = int(np.random.randint(0, 2))
        num_jz = int(np.random.randint(0, 20))

        for date in DATE:
            value = jgmc + date
            _id = get_md5_num(value)
            y = int(np.random.randint(1, 5))

            num_zrys = int(np.random.randint(50, 100))
            num_fzrys = int(np.random.randint(80, 150))
            num_ks = int(np.random.randint(30, 50))
            num_zdsys = int(np.random.randint(0, 5))
            amount_zdsys = int(np.random.randint(100, 1000))
            num_people = int(np.random.randint(5000, 10000))
            amount_daily = int(np.random.randint(40000, 80000))

            data_wsjkj = [
                _id, jgmc, date, y, byxz, is_yb, num_jz
            ]
            result_wsjkj.loc[len(result_wsjkj)] = data_wsjkj

            data_yy = [
                _id, jgmc, date, num_zrys, num_fzrys,
                num_ks, num_zdsys, amount_zdsys, num_people, amount_daily
            ]
            result_yy.loc[len(result_yy)] = data_yy

    result_wsjkj.to_csv(park_path, index=False, sep=',')
    result_yy.to_csv(bus_path, index=False, sep=',')


if __name__ == '__main__':
    _wsjkj_path = 'C:\\Users\\yu.zhang\\Desktop\\龙岗隐私计算模型\\纵向-多分类\\wsjkj_data.csv'
    _yy_path = 'C:\\Users\\yu.zhang\\Desktop\\龙岗隐私计算模型\\纵向-多分类\\yy_data.csv'
    mock_data(_wsjkj_path, _yy_path)

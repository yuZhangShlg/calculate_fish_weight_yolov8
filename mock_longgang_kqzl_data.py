
import pandas as pd
import numpy as np
import hashlib

JWD = [
    "114.27-22.73", "114.26-22.73", "114.25-22.73", "114.28-22.73", "114.29-22.73",
    "114.27-22.74", "114.27-22.75", "114.27-22.76", "114.27-22.72", "114.27-22.71"
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
    result_zfj = pd.DataFrame(
        columns=["id", "jwd", "date", "y",
                 "cd_area", "ld_area", "gd_area", "jsyd_area", "sy_area",
                 "num_gjzt", "num_qxc", "num_tcc", "num_wry"]
    )
    result_hjgs = pd.DataFrame(
        columns=["id", "jwd", "date", "wd", "fd",
                 "zjsl", "bsd", "bjcgd", "qrjgxhd"]
    )

    for jwd in JWD:

        cd_area = int(np.random.randint(1, 4))
        ld_area = 110.74
        gd_area = 4.41
        jsyd_area = 231.4
        sy_area = 15.3
        num_gjzt = 1500
        num_qxc = 120
        num_tcc = 88
        num_wry = 5

        for date in DATE:
            value = jwd + date
            _id = get_md5_num(value)
            label = int(np.random.randint(0, 250))

            wd = int(np.random.randint(5, 33))
            fd = int(np.random.randint(20, 100))
            zjsl = int(np.random.randint(1500, 2500))
            bsd = int(np.random.randint(78, 85))
            bjcgd = int(np.random.randint(200, 500))
            qrjgxhd = int(np.random.randint(450, 600))

            data_zfj = [
                _id, jwd, date, label, cd_area, ld_area, gd_area, jsyd_area, sy_area,
                num_gjzt, num_qxc, num_tcc, num_wry
            ]
            result_zfj.loc[len(result_zfj)] = data_zfj

            data_hjgs = [_id, jwd, date, wd, fd, zjsl, bsd, bjcgd, qrjgxhd]
            result_hjgs.loc[len(result_hjgs)] = data_hjgs

    result_zfj.to_csv(park_path, index=False, sep=',')
    result_hjgs.to_csv(bus_path, index=False, sep=',')


if __name__ == '__main__':
    _zfj_path = 'C:\\Users\\yu.zhang\\Desktop\\龙岗隐私计算模型\\纵向-回归\\zfj_data.csv'
    _hjgs_path = 'C:\\Users\\yu.zhang\\Desktop\\龙岗隐私计算模型\\纵向-回归\\hjgs_data.csv'
    mock_data(_zfj_path, _hjgs_path)

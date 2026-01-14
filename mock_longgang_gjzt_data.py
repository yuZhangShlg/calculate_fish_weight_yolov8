
import pandas as pd
import numpy as np
import hashlib
import datetime
import random
import time


ZDMC = [
    "楼吓村球场", "龙西路口", "香园新村", "爱新小区", "杉坑工业区"
]

DATE = [
    "20241001", "20241002", "20241003", "20241004", "20241005", "20241006", "20241007",
    "20241008", "20241009", "20241010", "20241011", "20241012", "20241013", "20241014",
    "20241015", "20241016", "20241017", "20241018", "20241019", "20241020", "20241021",
    "20241022", "20241023", "20241024", "20241025", "20241026", "20241027", "20241028",
    "20241029", "20241030", "20241031",
    "20241101", "20241102", "20241103", "20241104", "20241105", "20241106", "20241107",
    "20241108", "20241109", "20241110", "20241111", "20241112", "20241113", "20241114",
    "20241115", "20241116", "20241117", "20241118", "20241119", "20241120", "20241121",
    "20241122", "20241123", "20241124", "20241125", "20241126", "20241127", "20241128",
    "20241129", "20241130",
    "20241201", "20241202", "20241203", "20241204", "20241205", "20241206", "20241207", 
    "20241208", "20241209", "20241210", "20241211", "20241212", "20241213", "20241214", 
    "20241215", "20241216", "20241217", "20241218", "20241219", "20241220", "20241221", 
    "20241222", "20241223", "20241224", "20241225", "20241226", "20241227", "20241228", 
    "20241229", "20241230", "20241231",
    "20250501", "20250502", "20250503", "20250504", "20250505", "20250506", "20250507",
    "20250508", "20250509", "20250510", "20250511", "20250512", "20250513", "20250514",
    "20250515", "20250516", "20250517", "20250518", "20250519", "20250520", "20250521",
    "20250522", "20250523", "20250524", "20250525", "20250526", "20250527", "20250528",
    "20250529", "20250530", "20250531",
    "20250601", "20250602", "20250603", "20250604", "20250605", "20250606", "20250607",
    "20250608", "20250609", "20250610", "20250611", "20250612", "20250613", "20250614",
    "20250615", "20250616", "20250617", "20250618", "20250619", "20250620", "20250621",
    "20250622", "20250623", "20250624", "20250625", "20250626", "20250627", "20250628",
    "20250629", "20250630"
]


def get_md5_num(username):
    md5_machine = hashlib.md5()
    md5_machine.update(username.encode('utf-8'))
    md5_hash_string = md5_machine.hexdigest()
    return md5_hash_string


def random_times(start, end, n, frmt="%Y%m%d %H:%M:%S"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    time_datetime = [random.random() * (etime - stime) + stime for _ in range(n)]
    time_str = [t.strftime(frmt) for t in time_datetime]
    return time_str


def mock_data(jtysj_path, gjgs_path):
    result_jtysj = pd.DataFrame(
        columns=["id", "zdmc", "date", "yjddsj"]
    )
    result_gjgs = pd.DataFrame(
        columns=["id", "zdmc", "date", "sjdzsj"]
    )

    for zdmc in ZDMC:
        for date in DATE:
            value = zdmc + date
            _id = get_md5_num(value)

            start = date + " 07:00:00"
            end = date + " 23:00:00"
            times = random_times(start, end, 1)
            times = time.strptime(times[0], "%Y%m%d %H:%M:%S")
            times = int(time.mktime(times))

            data_jtysj = [_id, zdmc, date, int(times)]
            result_jtysj.loc[len(result_jtysj)] = data_jtysj

            _time = np.random.normal(loc=times, scale=180)
            data_gjgs = [_id, zdmc, date, int(_time)]
            result_gjgs.loc[len(result_gjgs)] = data_gjgs

    result_jtysj.to_csv(jtysj_path, index=False, sep=',')
    result_gjgs.to_csv(gjgs_path, index=False, sep=',')


if __name__ == '__main__':
    _jtysj_path = 'E:\\lingshu\\项目\\龙岗数据\\龙岗隐私计算模型\\多方安全计算\\jtysj_data.csv'
    _gjgs_path = 'E:\\lingshu\\项目\\龙岗数据\\龙岗隐私计算模型\\多方安全计算\\gjgs_data.csv'
    mock_data(_jtysj_path, _gjgs_path)

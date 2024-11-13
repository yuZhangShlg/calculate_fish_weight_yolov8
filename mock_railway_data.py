
import pandas as pd
import numpy as np

CITY_NAME = [
    "无锡", "长春", "青岛", "大连", "太原", "合肥", "南昌", "南宁", "昆明", "贵阳", "株洲", "衡山", "泰安", "岳阳", "中山",
    "常州", "宿州", "海口", "三亚", "珠海", "东莞", "佛山", "唐山", "营口", "鞍山", "辽阳", "万州", "宜昌", "镇江", "宿州",
    "枣庄", "德州", "温州", "宁波", "嘉兴", "沈阳", "西宁", "兰州", "徐州", "洛阳", "九江", "商丘", "吉林", "蚌埠", "阜阳",
    "曲阜", "香港", "台湾", "拉萨", "银川", "泉州", "廊坊", "安阳", "漯河", "信阳", "保定", "邢台", "邯郸", "铁岭", "四平",
    "松原", "荆州", "淮南", "鹤壁", "孝感", "咸宁", "衡阳", "郴州", "韶关", "清远", "铜陵", "黄山", "上饶", "南平", "绍兴",
    "义乌", "金华", "衢州", "六安", "汉口", "潜江", "恩施", "遂宁", "开封", "渭南", "宝鸡", "咸阳", "都匀", "桂林", "贺州",
    "肇庆", "贵港", "梧州", "云浮", "漳州", "汕尾", "惠州", "阳泉", "大同", "沂州", "晋中", "临汾", "运城", "陇南", "广元",
    "南充", "张掖", "酒泉", "哈密", "三明", "台州", "宁德", "绵阳", "德阳", "眉山", "乐山", "莱阳", "烟台", "威海", "湖州",
    "鄂州", "黄冈", "茂名", "湛江", "永州", "全州", "柳州", "长治", "晋城", "焦作", "黄石", "达州", "日照", "赣州", "河源",
    "益阳", "濮阳", "聊城", "安庆", "西昌", "临沂", "广安", "江门", "阳江", "淮安", "汉阳", "襄阳", "十堰", "巴中", "汉中",
    "吉安", "百色", "周口", "阜宁", "盐城", "亳州", "芜湖", "宜宾", "南阳", "资阳", "内江", "遵义", "衡水", "潍坊", "淄博",
    "天水", "承德", "朝阳", "阜新", "霸州", "锦州", "盘锦", "自贡", "泸州", "随州", "扬州", "泰州", "南通", "毕节", "安康",
    "许昌", "新乡", "鹰潭", "抚州", "新余", "宜春", "萍乡", "湘潭", "娄底", "邵阳", "怀化", "安顺", "曲靖", "秦皇岛",
    "嘉峪关", "攀枝花", "张家口", "连云港", "哈尔滨", "石家庄", "驻马店", "乌鲁木齐", "呼和浩特"]
DATE = [
    "20231230", "20231231", "20240101", "20240210", "20240211", "20240212", "20240213", "20240214", "20240215",
    "20240216", "20240217", "20240404", "20240405", "20240406", "20240501", "20240502", "20240503", "20240504",
    "20240505", "20240608", "20240609", "20240610", "20240915", "20240916", "20240917", "20241001", "20241002",
    "20241003", "20241004", "20241005", "20241006", "20241007",
    "20221231", "20230101", "20230121", "20230122", "20230123", "20230124", "20230125", "20230126", "20230127",
    "20230216", "20230217", "20230405", "20230429", "20230430", "20230501", "20230502", "20230503",  "20230622",
    "20230623", "20230624", "20230929", "20230930", "20231001", "20231002", "20231003", "20231004", "20231005",
    "20231006"]


def generate_unique_hash(input_str):
    unique_hash = hash(input_str)
    return abs(unique_hash)


def railway_data(file_path):
    result = pd.DataFrame(
        columns=["id", "locations", "date", "label", "train_count", "train_people_count", "train_avg_people_count",
                 "train_people_leave", "train_people_leave_avg", "train_people_leave_ratio"]
    )
    for city in CITY_NAME:
        for date in DATE:
            _id = generate_unique_hash(city + date)
            label = int(np.floor(np.random.random() / 0.7))
            train_count = int(np.random.randint(100, 2000))
            train_avg_people_count = int(np.random.randint(600, 1200))
            train_people_count = train_count * train_avg_people_count
            train_people_leave_avg = int(np.random.randint(50, int(train_avg_people_count / 2)))
            train_people_leave = train_people_leave_avg * train_avg_people_count
            train_people_leave_ratio = round(train_people_leave_avg / train_avg_people_count, 4)

            data = [_id, city, date, label, train_count, train_people_count, train_avg_people_count,
                    train_people_leave, train_people_leave_avg, train_people_leave_ratio]

            result.loc[len(result)] = data

    result.to_csv(file_path, index=False, sep=',')


def app_data(file_path):
    result = pd.DataFrame(
        columns=["id", "locations", "date", "reserve_train_people", "reserve_hotel_people", "reserve_scenic_people"]
    )
    for city in CITY_NAME:
        for date in DATE:
            _id = generate_unique_hash(city + date)
            reserve_train_people = int(np.random.randint(50000, 500000))
            reserve_hotel_people = int(np.random.randint(10000, 200000))
            reserve_scenic_people = int(np.random.randint(30000, 250000))

            data = [_id, city, date, reserve_train_people, reserve_hotel_people, reserve_scenic_people]
            result.loc[len(result)] = data

    result.to_csv(file_path, index=False, sep=',')


if __name__ == '__main__':
    file_path_value = 'C:\\Users\\yu.zhang\\Desktop\\铁科院\\app_data.csv'
    app_data(file_path_value)



import pandas as pd
import numpy as np
import hashlib

USER = [
    "张伟", "王芳", "李娜", "刘洋", "陈静", "杨勇", "赵雪", "周涛", "吴刚", "徐敏", "孙丽", "胡军", "朱琳", "高翔",
    "林峰", "何洁", "郭强", "马超", "罗娟", "梁爽", "宋佳", "郑凯", "谢娜", "韩梅", "唐嫣", "冯雪", "于波", "董洁",
    "萧峰", "程程", "曹颖", "袁泉", "邓超", "许晴", "傅艺伟", "沈腾", "曾毅", "彭于晏", "吕燕", "苏鑫", "卢靖姗",
    "蒋欣", "蔡徐坤", "贾玲", "丁真", "魏晨", "薛之谦", "叶一茜", "阎维文", "余男", "潘粤明", "杜淳", "戴军", "夏雨",
    "钟欣潼", "汪峰", "田亮", "任泉", "姜文", "范冰冰", "方世玉", "石原里美", "姚明", "谭松韵", "廖凡", "邹市明",
    "熊黛林", "金晨", "陆毅", "郝蕾", "孔雪儿", "白敬亭", "崔健", "康辉", "毛不易", "邱淑贞", "秦岚", "江疏影",
    "史泰龙", "顾佳", "侯勇", "邵兵", "孟美岐", "龙丹妮", "万茜", "段奕宏", "雷佳音", "钱枫", "汤唯", "尹正", "黎明",
    "易烊千玺", "常远", "武艺", "乔欣", "贺峻霖", "赖美云", "张艺兴", "王祖贤"
]

DATE = [
    "20241201", "20241202", "20241203", "20241204", "20241205", "20241206", "20241207", "20241208", "20241209",
    "20241210", "20241211", "20241212", "20241213", "20241214", "20241215", "20241216", "20241217", "20241218",
    "20241219", "20241220", "20241221", "20241222", "20241223", "20241224", "20241225", "20241226", "20241227",
    "20241228", "20241229", "20241230", "20241231",
    "20250501", "20250502", "20250503", "20250504", "20250505", "20250506", "20250507", "20250508", "20250509",
    "20250510", "20250511", "20250512", "20250513", "20250514", "20250515", "20250516", "20250517", "20250518",
    "20250519", "20250520", "20250521", "20250522", "20250523", "20250524", "20250525", "20250526", "20250527",
    "20250528", "20250529", "20250530", "20250531",
    "20250601", "20250602", "20250603", "20250604", "   20250605", "20250606", "20250607", "20250608", "20250609",
    "20250610", "20250611", "20250612", "20250613", "20250614", "20250615", "20250616", "20250617", "20250618",
    "20250619", "20250620", "20250621", "20250622", "20250623", "20250624", "20250625", "20250626", "20250627",
    "20250628", "20250629", "20250630"
]


def get_md5_num(username):
    md5_machine = hashlib.md5()
    md5_machine.update(username.encode('utf-8'))
    md5_hash_string = md5_machine.hexdigest()
    return md5_hash_string


def mock_data(bank_path, highway_path, vehicle_path):
    bank_result = pd.DataFrame(
        columns=["id", "date", "label", "age", "sex", "is_married", "is_yq", "is_yq_year",
                 "yq_num", "yq_num_year", "yq_time_avg",
                 "yq_time_avg_year", "check_credict_num",
                 "check_credict_num_3_month", "check_credict_num_6_month", "check_credict_num_12_month",
                 "credict_pro_end_num", "credict_pro_end_time", "credict_pro_end_type",
                 "credict_pro_num", "credict_pro_time", "credict_pro_type",
                 "income", "income_avg_year", "credict_line", "credict_line_used",
                 "fd_line_residual", "fd_line_day", "credict_loan_line", "credict_loan_line_used"]
    )
    highway_result = pd.DataFrame(
        columns=["id", "date", "truck_num", "truck_num_3_month", "truck_type_num", "truck_type_num_3_month",
                 "truck_pay_num_avg", "truck_pay_num_avg_3_month", "truck_pay_cost_avg",
                 "truck_pay_cost_avg_3_month", "truck_mile_avg", "truck_mile_avg_3_month", "truck_goods_type",
                 "truck_goods_type_3_month", "truck_goods_cargo_avg", "truck_goods_cargo_avg_3_month"]
    )
    vehicle_result = pd.DataFrame(
        columns=["ID", "date", "truck_law_num", "truck_law_num_year", "user_law_num", "user_law_num_year",
                 "user_law_cost", "user_law_cost_year", "user_law_untreated_num", "user_law_untreated_num_year",
                 "user_law_untreated_cost", "user_law_untreated_cost_year"]
    )

    for name in USER:
        age = int(np.random.randint(25, 55))
        sex = int(np.random.randint(0, 2))
        is_married = int(np.random.randint(0, 2))
        for date in DATE:
            value = name + date
            _id = get_md5_num(value)

            label = int(np.random.randint(0, 2))
            is_yq = int(np.random.randint(0, 2))
            is_yq_year = int(np.random.randint(0, 2))
            if is_yq == 0:
                yq_num, yq_time_avg = 0, 0
            else:
                yq_num = round(float(np.random.random() * 5), 2)
                yq_time_avg = round(float(np.random.random() * 8), 2)
            if is_yq_year == 0:
                yq_num_year, yq_time_avg_year = 0, 0
            else:
                yq_num_year = round(float(np.random.random() * 5), 2)
                yq_time_avg_year = round(float(np.random.random() * 8), 2)
            check_credict_num_12_month = int(np.random.randint(0, 20))
            if check_credict_num_12_month == 0:
                check_credict_num, check_credict_num_3_month, check_credict_num_6_month = 0, 0, 0
            else:
                check_credict_num = int(check_credict_num_12_month / 12) + int(np.random.randint(0, 2))
                check_credict_num_3_month = int(check_credict_num_12_month / 4) + int(np.random.randint(0, 2))
                check_credict_num_6_month = int(check_credict_num_12_month / 2) + int(np.random.randint(0, 2))
            credict_pro_end_num = int(np.random.randint(0, 10))
            if credict_pro_end_num == 0:
                credict_pro_end_time, credict_pro_end_type = 0, 0
            else:
                credict_pro_end_time = int(np.random.random() * 48)
                credict_pro_end_type = int(np.random.randint(0, credict_pro_end_num))
            credict_pro_num = int(np.random.randint(0, 5))
            if credict_pro_num == 0:
                credict_pro_time, credict_pro_type = 0, 0
            else:
                credict_pro_time = int(np.random.random() * 48)
                credict_pro_type = int(np.random.randint(0, credict_pro_num))
            income = int(np.random.randint(20000, 100000))
            income_avg_year = int(np.random.randint(income * 0.9, income * 1.1))
            credict_line = int(np.random.randint(30000, 100000))
            credict_line_used = int(np.random.randint(credict_line * 0.1, credict_line))
            fd_line_residual = int(np.random.randint(500000, 5000000))
            fd_line_day = int(np.random.randint(50, 300))
            credict_loan_line = int(np.random.randint(200000, 500000))
            credict_loan_line_used = int(np.random.randint(credict_loan_line * 0.1, credict_loan_line))

            truck_num = int(np.random.randint(2, 20))
            truck_num_3_month = int(np.random.randint(truck_num, truck_num * 2))
            truck_type_num = int(np.random.randint(1, truck_num))
            truck_type_num_3_month = int(np.random.randint(truck_type_num, truck_type_num * 2))
            truck_pay_num_avg = int(truck_num * 20 * np.random.random())
            truck_pay_num_avg_3_month = int(truck_num_3_month * 20 * np.random.random())
            truck_pay_cost_avg = int(truck_num * 20 * 100 * np.random.random())
            truck_pay_cost_avg_3_month = int(truck_num_3_month * 20 * 100 * np.random.random())
            truck_mile_avg = int(truck_pay_cost_avg * 0.88)
            truck_mile_avg_3_month = int(truck_pay_cost_avg_3_month * 0.88)
            truck_goods_type = int(np.random.randint(1, 5))
            truck_goods_type_3_month = int(np.random.randint(truck_goods_type, truck_goods_type * 2))
            truck_goods_cargo_avg = int(np.random.randint(15, 25))
            truck_goods_cargo_avg_3_month = int(np.random.randint(truck_goods_cargo_avg * 0.9, truck_goods_cargo_avg * 1.1))

            truck_law_num = int(np.random.randint(0, 3))
            truck_law_num_year = int(np.random.randint(0, 5))
            if truck_law_num == 0:
                user_law_num = 0
                user_law_cost = 0
                user_law_untreated_num = 0
                user_law_untreated_cost = 0
            else:
                user_law_num = np.random.randint(truck_law_num, truck_law_num * 2)
                user_law_cost = np.random.randint(user_law_num * 100, user_law_num * 500)
                user_law_untreated_num = np.random.randint(0, user_law_num)
                if user_law_untreated_num == 0:
                    user_law_untreated_cost = 0
                else:
                    user_law_untreated_cost = np.random.randint(user_law_num * 100, user_law_num * 500)
            if truck_law_num_year == 0:
                user_law_num_year = 0
                user_law_cost_year = 0
                user_law_untreated_num_year = 0
                user_law_untreated_cost_year = 0
            else:
                user_law_num_year = np.random.randint(truck_law_num_year, truck_law_num_year * 2)
                user_law_cost_year = np.random.randint(user_law_num_year * 100, user_law_num_year * 500)
                user_law_untreated_num_year = np.random.randint(0, user_law_num_year)
                if user_law_untreated_num_year == 0:
                    user_law_untreated_cost_year = 0
                else:
                    user_law_untreated_cost_year = np.random.randint(user_law_num_year * 100, user_law_num_year * 500)

            bank_data = [
                _id, date, label, age, sex, is_married, is_yq, is_yq_year, yq_num, yq_num_year, yq_time_avg,
                yq_time_avg_year, check_credict_num, check_credict_num_3_month, check_credict_num_6_month,
                check_credict_num_12_month, credict_pro_end_num, credict_pro_end_time, credict_pro_end_type,
                credict_pro_num, credict_pro_time, credict_pro_type, income, income_avg_year, credict_line,
                credict_line_used, fd_line_residual, fd_line_day, credict_loan_line, credict_loan_line_used
            ]
            bank_result.loc[len(bank_result)] = bank_data

            highway_data = [_id, date, truck_num, truck_num_3_month, truck_type_num, truck_type_num_3_month,
                            truck_pay_num_avg, truck_pay_num_avg_3_month, truck_pay_cost_avg,
                            truck_pay_cost_avg_3_month, truck_mile_avg, truck_mile_avg_3_month,
                            truck_goods_type, truck_goods_type_3_month, truck_goods_cargo_avg,
                            truck_goods_cargo_avg_3_month]
            highway_result.loc[len(highway_result)] = highway_data

            vehicle_data = [_id, date, truck_law_num, truck_law_num_year, user_law_num, user_law_num_year,
                            user_law_cost, user_law_cost_year, user_law_untreated_num,
                            user_law_untreated_num_year, user_law_untreated_cost, user_law_untreated_cost_year]
            vehicle_result.loc[len(vehicle_result)] = vehicle_data

    bank_result.to_csv(bank_path, index=False, sep=',')
    highway_result.to_csv(highway_path, index=False, sep=',')
    vehicle_result.to_csv(vehicle_path, index=False, sep=',')


if __name__ == '__main__':
    _bank_path = 'C:\\Users\\yu.zhang\\Desktop\\物流信用\\bank_data.csv'
    _highway_path = 'C:\\Users\\yu.zhang\\Desktop\\物流信用\\highway_data.csv'
    _vehicle_path = 'C:\\Users\\yu.zhang\\Desktop\\物流信用\\vehicle_data.csv'
    mock_data(_bank_path, _highway_path, _vehicle_path)

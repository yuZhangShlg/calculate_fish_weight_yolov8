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


def mock_data(insurance_path, medical_path):
    insurance_result = pd.DataFrame(
        columns=["id", "date", "label", "policy_date",
                 "critical_illness_amount_month", "critical_illness_amount_year",
                 "medical_insurance_month", "medical_insurance_year",
                 "policy_amount_month", "policy_amount_year"]
    )
    medical_result = pd.DataFrame(
        columns=["id", "date", "gender", "age",
                 "primary_diagnosis_month", "primary_diagnosis_year",
                 "item_price_month", "item_price_year",
                 "item_name_month", "item_name_year",
                 "disease_type_month", "disease_type_year"]
    )

    for name in USER:
        age = int(np.random.randint(25, 55))
        gender = int(np.random.randint(0, 2))

        for date in DATE:
            value = name + date
            _id = get_md5_num(value)

            label = int(np.random.randint(0, 2))
            policy_date = int(np.random.randint(10, 200))
            critical_illness_amount_month = int(np.random.randint(100000, 1000000))
            critical_illness_amount_year = int(np.random.randint(100000, 1000000))
            medical_insurance_month = int(np.random.randint(100, 10000))
            medical_insurance_year = int(np.random.randint(100, 10000))
            policy_amount_month = int(np.random.randint(100, 5000000))
            policy_amount_year = int(np.random.randint(100, 5000000))

            primary_diagnosis_month = int(np.random.randint(0, 3))
            primary_diagnosis_year = int(np.random.randint(0, 10))
            if primary_diagnosis_month == 0:
                item_price_month = 0
                item_name_month = 0
            else:
                item_price_month = int(np.random.randint(100, 1000))
                item_name_month = int(np.random.randint(300, 1000))
            if primary_diagnosis_year == 0:
                item_price_year = 0
                item_name_year = 0
            else:
                item_price_year = int(np.random.randint(300, 3000))
                item_name_year = int(np.random.randint(900, 6000))
            disease_type_month = int(np.random.randint(0, 2))
            disease_type_year = int(np.random.randint(0, 2))

            insurance_data = [
                _id, date, label, policy_date, critical_illness_amount_month, critical_illness_amount_year,
                medical_insurance_month, medical_insurance_year, policy_amount_month, policy_amount_year
            ]
            insurance_result.loc[len(insurance_result)] = insurance_data

            medical_data = [_id, date, gender, age, primary_diagnosis_month, primary_diagnosis_year,
                            item_price_month, item_price_year, item_name_month, item_name_year,
                            disease_type_month, disease_type_year]
            medical_result.loc[len(medical_result)] = medical_data

    insurance_result.to_csv(insurance_path, index=False, sep=',')
    medical_result.to_csv(medical_path, index=False, sep=',')


if __name__ == '__main__':
    _insurance_path = 'C:\\Users\\yu.zhang\\Desktop\\南京医疗POC\\insurance_data.csv'
    _medical_path = 'C:\\Users\\yu.zhang\\Desktop\\南京医疗POC\\medical_data.csv'
    mock_data(_insurance_path, _medical_path)

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


def get_md5_num(username):
    md5_machine = hashlib.md5()
    md5_machine.update(username.encode('utf-8'))
    md5_hash_string = md5_machine.hexdigest()
    return md5_hash_string


def mock_data(group_path, bank_path):
    group_result = pd.DataFrame(
        columns=["id", "delivery_amount", "order_delivery_ratio"]
    )
    bank_result = pd.DataFrame(
        columns=["id", "credit_score"]
    )

    for date in DATE:
        for idx in range(10):
            _id = get_md5_num(date + str(idx))

            delivery_amount = int(np.random.randint(1000, 5000))
            order_delivery_ratio = int(np.random.randint(45, 100)) / 100

            credit_score = int(np.random.randint(600, 850))

            group_data = [
                _id, delivery_amount, order_delivery_ratio
            ]
            group_result.loc[len(group_result)] = group_data

            bank_data = [_id, credit_score]
            bank_result.loc[len(bank_result)] = bank_data

    group_result.to_csv(group_path, index=False, sep=',')
    bank_result.to_csv(bank_path, index=False, sep=',')


if __name__ == '__main__':
    _group_path = 'C:\\Users\\yu.zhang\\Desktop\\国家能源可信数据空间\\group_data.csv'
    _bank_path = 'C:\\Users\\yu.zhang\\Desktop\\国家能源可信数据空间\\bank_data.csv'
    mock_data(_group_path, _bank_path)

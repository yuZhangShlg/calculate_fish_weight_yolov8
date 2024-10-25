
from PIL import Image
import os.path


def photo_size_changer(folder_path, width, height):
    filenames = os.listdir(folder_path)
    for filename in filenames:
        domain = os.path.abspath(folder_path)
        filename = os.path.join(domain, filename)

        imgFile = Image.open(filename)
        newImage = imgFile.resize((width, height), Image.BILINEAR)
        newImage.save(filename)


if __name__ == '__main__':
    folder_path = 'E:\\鱼情识别--数据集\\二值图片\\valid_1'
    width, height = 224, 224
    photo_size_changer(folder_path, width, height)


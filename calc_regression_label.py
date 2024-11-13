
import os.path


def set_regression_label(folder_path):
    image_path = os.path.join(folder_path, 'image')
    label_path = os.path.join(folder_path, 'label')

    image_path = os.listdir(image_path)
    for filename in image_path:
        name = os.path.splitext(filename)[0] + '.txt'
        name = os.path.join(label_path, name)
        f = open(name, 'a')
        f.write('1')
        f.close()


if __name__ == '__main__':
    folder_path = 'E:\\鱼情识别--数据集\\二值图片\\224\\valid'
    set_regression_label(folder_path)

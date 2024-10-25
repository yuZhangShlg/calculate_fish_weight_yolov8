
import os
import numpy as np


def file_changer(folder_path, value):
    filenames = os.listdir(folder_path)
    for filename in filenames:
        domain = os.path.abspath(folder_path)
        filename = os.path.join(domain, filename)
        if os.path.isdir(filename):
            file_changer(filename, value)
            continue

        fread = open(filename, 'r')
        fwrite = open("%s.backup" % filename, 'w')
        while True:
            line = fread.readline()
            if len(line) > 0:
                content = line.split()
                new_content = ''
                for i, val in enumerate(content):
                    val = str(0) if i == 0 else str(np.round(float(val), 6))
                    new_content += val + ' '
                new_content = new_content.strip(' ') + '\r'
                fwrite.write(new_content)
            else:
                break
        fread.close()
        fwrite.close()
        os.remove(filename)
        os.rename("%s.backup" % filename, filename)


if __name__ == '__main__':
    folder_path = 'E:\\鱼情识别--数据集\\预标注\\weight\\bass finder.v2i.yolov8\\test\\labels'
    file_changer(folder_path, 3)


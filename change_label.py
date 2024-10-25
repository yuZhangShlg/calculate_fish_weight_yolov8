
import os


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
                content[0] = str(value)
                new_content = content[0] + ' ' + content[1] + ' ' + content[2] + ' ' + content[3] + ' ' + content[4] + '\r'
                fwrite.write(new_content)
            else:
                break
        fread.close()
        fwrite.close()
        os.remove(filename)
        os.rename("%s.backup" % filename, filename)


if __name__ == '__main__':
    folder_path = 'E:\\鱼情识别--数据集\\预标注\\water.v4i.yolov8\\valid\\labels'
    file_changer(folder_path, 3)


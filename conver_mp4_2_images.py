import os
import pathlib
import cv2


def convert_mp4_to_images(video_path, output_folder, interval=1):
    os.makedirs(output_folder, exist_ok=True)
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("无法打开视频文件")
        return

    num, j = 0, 0
    ret = True
    while ret:
        num += 1
        ret, frame = video.read()
        if frame is not None:
            if num % interval == 0:
                j += 1
                path = os.path.join(pathlib.Path(output_folder), f"spray_img_{j}.png")
                cv2.imwrite(path, frame)
        else:
            break

    video.release()


if __name__ == '__main__':
    convert_mp4_to_images(
        r"E:\\鱼情识别--数据集\\视频\\投喂饲料、翘头、生病\\13369128410615307.mp4",
        "E:\\photo",
        interval=30,
    )

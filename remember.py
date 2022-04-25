# pip install Image
# pip install numpy
# 'C:/Users/IMOE001/Downloads/Notebooks-master/Notebooks-master/week06/resources/code.png'
from PIL import Image
import numpy as np


def remember(path: str) -> str:
    """
    Encoding a message according to an image.
    :param path: Path of the image to be encoded.
    :return: The encoded message.
    """
    image = Image.open(path)
    pixels = np.asarray(image)
    columns = image.size[0]
    rows = image.size[1]

    column_list = []
    painted_places = []

    [column_list.append(pixels[:, i]) for i in range(columns)]

    [painted_places.append(j) for i in range(columns) for j in range(rows) if column_list[i][j] == 1]

    keys = [chr(key) for key in painted_places]
    sentence = ''.join(keys)
    return sentence


if __name__ == "__main__":
    print(remember('C:/Users/IMOE001/Downloads/Notebooks-master/Notebooks-master/week06/resources/code.png'))

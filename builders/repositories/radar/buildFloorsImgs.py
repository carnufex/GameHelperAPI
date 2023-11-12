import numpy as np
from src.utils.image import loadFromRGBToGray


def main():
    floorsImgs = [
        loadFromRGBToGray('map/images/floor-0.png'),
        loadFromRGBToGray('map/images/floor-1.png'),
        loadFromRGBToGray('map/images/floor-2.png'),
        loadFromRGBToGray('map/images/floor-3.png'),
        loadFromRGBToGray('map/images/floor-4.png'),
        loadFromRGBToGray('map/images/floor-5.png'),
        loadFromRGBToGray('map/images/floor-6.png'),
        loadFromRGBToGray('map/images/floor-7.png'),
        loadFromRGBToGray('map/images/floor-8.png'),
        loadFromRGBToGray('map/images/floor-9.png'),
        loadFromRGBToGray('map/images/floor-10.png'),
        loadFromRGBToGray('map/images/floor-11.png'),
        loadFromRGBToGray('map/images/floor-12.png'),
        loadFromRGBToGray('map/images/floor-13.png'),
        loadFromRGBToGray('map/images/floor-14.png'),
        loadFromRGBToGray('map/images/floor-15.png')
    ]
    np.save('src/repositories/map/npys/floorsImgs.npy', floorsImgs)


if __name__ == '__main__':
    main()
#!/usr/bin/env python3

import sys
from PIL import Image

#将small_img中的像素用近邻法嵌入到big_img中
def extract(big_img, small_w, small_h):

    big_w, big_h = big_img.size

    dst_im = Image.new(mode = "RGB", size = (small_w, small_h))

    stepx = big_w/small_w
    stepy = big_h/small_h

    for i in range(0, small_w):
        for j in range(0, small_h):
            map_x = int( i*stepx + stepx*0.5 )
            map_y = int( j*stepy + stepy*0.5 )

            if map_x < big_w and map_y < big_h :
                dst_im.putpixel( (i, j), big_img.getpixel( (map_x,map_y) ) )

    return dst_im

def main():
    if len(sys.argv) != 5:
        print('Usage:',sys.argv[0], '<big_image_path> <small width> <small height> <out_image_path>')
        return

    extract(Image.open(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])).save(sys.argv[4])


if __name__ == '__main__':
    main()


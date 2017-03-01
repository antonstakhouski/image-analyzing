#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec


class Pic_analyz:
    def __init__(self):
        image1_name = "nya.png"
        image2_name = "diablo.png"
        image1_gray_name = "nya_gray.png"
        image2_gray_name = "diablo_gray.png"

        self.pic1 = mpimg.imread(image1_name)
        self.pic2 = mpimg.imread(image2_name)
        self.pic1_gray = mpimg.imread(image1_gray_name)
        self.pic2_gray = mpimg.imread(image2_gray_name)

    def show(self):
        gs = gridspec.GridSpec(2, 4)

        plt.subplot(gs[0, 0])
        plt.title("Image 1")
        plt.imshow(self.pic1)

        plt.subplot(gs[1, 0])
        plt.title("Image 2")
        plt.imshow(self.pic2)

        plt.subplot(gs[0, 1])
        plt.title("Image 1 grayscale gray")
        plt.imshow(self.pic1_gray, cmap='gray')
        plt.colorbar()

        plt.subplot(gs[1, 1])
        plt.title("Image 2 grayscale gray")
        plt.imshow(self.pic2_gray, cmap='gray')
        plt.colorbar()

        plt.subplot(gs[0, 2])
        plt.title("Image 1 grayscale")
        plt.imshow(self.pic1_gray)
        plt.colorbar()

        plt.subplot(gs[1, 2])
        plt.title("Image 2 grayscale")
        plt.imshow(self.pic2_gray)
        plt.colorbar()

        plt.subplot(gs[0, 3])
        plt.title("Image 1 historgam")
        plt.hist(self.pic1_gray.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

        plt.subplot(gs[1, 3])
        plt.title("Image 2 histogram")
        plt.hist(self.pic2_gray.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

        plt.show()


if __name__ == "__main__":
    pic_analyz = Pic_analyz()
    pic_analyz.show()

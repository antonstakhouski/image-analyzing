#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
import numpy as np
from scipy import stats


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

        self.pics = [self.pic1, self.pic2]
        self.pics_gray = [self.pic1_gray, self.pic2_gray]

    def show_defualt_images(self, gs):
        i = 0
        for pic in self.pics:
            plt.subplot(gs[i, 0])
            title = "Image " + str(i + 1)
            plt.title(title)
            plt.imshow(pic)
            i += 1

    def show_grayscale_gray(self, gs):
        i = 0
        for pic in self.pics_gray:
            plt.subplot(gs[i, 1])
            title = "Image " + str(i + 1) + " grayscale gray"
            plt.title(title)
            plt.imshow(pic, cmap='gray')
            plt.colorbar()
            i += 1

    def show_grayscale(self, gs):
        i = 0
        for pic in self.pics_gray:
            plt.subplot(gs[i, 2])
            title = "Image " + str(i + 1) + " grayscale"
            plt.title(title)
            plt.imshow(pic)
            plt.colorbar()
            i += 1

    def show_images(self, gs):
        self.show_defualt_images(gs)
        self.show_grayscale_gray(gs)
        self.show_grayscale(gs)

    def show_hist_characteristics(self, hists):
        hist_corrcoef = np.corrcoef(hists[0][0], hists[1][0])
        print('hist_corrcoef = ', hist_corrcoef[0][1])

        i = 1
        for hist in hists:
            print("Hist", i, ":")

            mean = np.mean(hist[0])
            print('     mean = ', mean)

            cov = np.cov(hist[0])
            print('     cov = ', cov)

            mode = stats.mode(hist[0])
            print('     mode = ', mode)

            median = np.median(hist[0])
            print('     median = ', median)

            i += 1

    def show_hists(self, gs):
        i = 0
        hists = list()
        for pic in self.pics_gray:
            plt.subplot(gs[i, 3])
            title = "Image " + str(i + 1) + " histogram"
            plt.title(title)
            hist = plt.hist(pic.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
            hists.append(hist)
            i += 1
        return hists

    def print_layer_corrcoef(self):
        i = 1
        for picture in [self.pic1, self.pic2]:
            r = list()
            g = list()
            b = list()
            for string in picture:
                for element in string:
                    r.append(element[0])
                    g.append(element[1])
                    b.append(element[2])
            rg_corr = np.corrcoef(r, g)
            rb_corr = np.corrcoef(r, b)
            bg_corr = np.corrcoef(b, g)
            print("Image", i, ":")
            print('     corrcoef rg = ', rg_corr[0][1])
            print('     corrcoef rb = ', rb_corr[0][1])
            print('     corrcoef bg = ', bg_corr[0][1])
            i += 1

    def show(self):
        gs = gridspec.GridSpec(2, 4)

        self.show_images(gs)
        hists = self.show_hists(gs)
        self.show_hist_characteristics(hists)
        #  self.print_layer_corrcoef()

        plt.show()


if __name__ == "__main__":
    pic_analyz = Pic_analyz()
    pic_analyz.show()

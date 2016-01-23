import sys
import numpy as np
import matplotlib.pyplot as plt
import math

class EdgeDetection:
    #### Canny
    # Runtime:
    # Pros:
    # Cons:
    # Details:
    #   1) Apply Gaussian filter to smooth the image in order to remove the noise
    #   2) Find the intensity gradients of the image
    #   3) Apply non-maximum suppression to get rid of spurious response to edge detection
    #   4) Apply double threshold to determine potential edges
    #   5) Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.

    def GaussianFilter(self, k, sigma=1.4):
        """
        Filter out the noise for preventing false detection caused by noise by applying the Gaussian Filter.
        """
        H = np.zeros((2*k+1,2*k+1))
        for i in xrange(2*k+1):
            for j in xrange(2*k+1):
                H[i,j] = 1.0/(2 * math.pi * sigma * sigma) * (math.e ** (-((i-k-1)*(i-k-1) + (j-k-1)*(j-k-1))/(2*sigma*sigma)))
        return H

    #####################


    # Deriche

    # Differential

    # Sobel

    # Prewitt

    # Roberts cross

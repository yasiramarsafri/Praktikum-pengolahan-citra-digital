import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('gunung.png',0)
equ = cv2.equalizeHist(img)

hist_full = cv2.calcHist([equ],[0],None,[256],[0,256])
hist_full2 = cv2.calcHist([img],[0],None,[256],[0,256])

plt.subplot(221), plt.imshow(equ, 'gray')
plt.subplot(222), plt.plot(hist_full)
plt.subplot(223), plt.imshow(img, 'gray')
plt.subplot(224), plt.plot(hist_full2)

plt.xlim([0,256])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
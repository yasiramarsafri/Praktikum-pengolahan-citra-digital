import  cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('1.jpg',0)

hist_full = cv2.calcHist([img],[0],None,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.plot(hist_full)
plt.xlim([0,255])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('gunung.png',0)
equ = cv2.equalizeHist(img)

# create a mask
mask = np.zeros(equ.shape[:2], np.uint8)
mask[100:300, 100:400] = 255

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
hist_full2 = cv2.calcHist([equ],[0],None,[256],[0,256])
hist_mask2 = cv2.calcHist([equ],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.plot(hist_full), plt.plot(hist_mask)
plt.subplot(223), plt.imshow(equ, 'gray')
plt.subplot(224), plt.plot(hist_full2), plt.plot(hist_mask2)

plt.xlim([0,255])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
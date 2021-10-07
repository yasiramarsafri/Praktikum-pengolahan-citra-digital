import  cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('1.jpg',0)

# create a mask
mask = np.zeros(img.shape, np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.plot(hist_full), plt.plot(hist_mask)

plt.xlim([0,255])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


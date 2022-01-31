import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("C:/Users/Aldi Triwijaya/Documents/kuliah/semester 3/pengolahan citra digital praktik/responsi/uang 20rb - 3.jpg")

B, G, R = cv2.split(image)

height = len(image)
width = len(image[0])
tot_pixel = height * width

hist_B = np.zeros((256))    
hist_G = np.zeros((256))    
hist_R = np.zeros((256))   
for i in range(height):
    for j in range(width):
        #proses matrix B
        pixel = B[i][j]
        hist_B[pixel] += 1

        #proses matrix G
        pixel = G[i][j]
        hist_G[pixel] += 1

        #proses matrix R
        pixel = R[i][j]
        hist_R[pixel] += 1

if hist_B[pixel] >= hist_G[pixel] and hist_R[pixel]:
    print("Uang RP.50.000")
    
elif hist_G[pixel] >= hist_B[pixel] and hist_R[pixel]: 
    print(" Uang RP.20.000")
else:
    print(" Uang RP.100.000")

#tampilkan histogram
plt.bar(range(len(hist_R)), hist_R, color=[1,0,0])
plt.bar(range(len(hist_G)), hist_G, color=[0,1,0])
plt.bar(range(len(hist_B)), hist_B, color=[0,0,1])

plt.waitforbuttonpress()




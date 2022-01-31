import cv2
import numpy as np

#membaca citra digital dari komputer
citra1 = cv2.imread("C:/Users/Aldi Triwijaya/Documents/kuliah/semester 3/pengolahan citra digital praktik/Gambar/chelsea - rgb.jpg")
citra2 = cv2.imread("C:/Users/Aldi Triwijaya/Documents/kuliah/semester 3/pengolahan citra digital praktik/Gambar/kacamata.jpg")

#membaca channel warna BGR dan menyimpannya ke dalam variabel terpisah
b1 = citra1[:,:,0]
g1 = citra1[:,:,1]
r1 = citra1[:,:,2]

b2 = citra2[:,:,0]
g2 = citra2[:,:,1]
r2 = citra2[:,:,2]

#menyimpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(citra1)
jum_kolom = len(citra1[0])

#menyiapkan citra baru dengan nilai 0
# citra_gray1 = np.zeros((jum_baris, jum_kolom))        # aktifkan ini jika ingin menggunakan citra grayscale
# citra_gray2 = np.zeros((jum_baris, jum_kolom))        # aktifkan ini jika ingin menggunakan citra grayscale
citra_and = np.zeros((jum_baris, jum_kolom, 3))         # aktifkan ini jika ingin menggunakan citra RGB

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        # Gunakan ini jika ingin menggunakan citra grayscale
        # citra_gray1[i, j] = round(0.299 * r1[i, j] + 0.587 * g1[i, j] + 0.114 * b1[i, j])
        # citra_gray2[i, j] = round(0.299 * r2[i, j] + 0.587 * g2[i, j] + 0.114 * b2[i, j])
        # citra_and[i, j] = min(citra_gray1[i, j], citra_gray2[i, j])

        # Gunakan ini jika ingin menggunakan citra RGB
        citra_and[i, j, 0] = min(b1[i, j], b2[i, j])
        citra_and[i, j, 1] = min(g1[i, j], g2[i, j])
        citra_and[i, j, 2] = min(r1[i, j], r2[i, j])

# aktifkan ini jika menggunakan citra grayscale
# citra_gray1 = citra_gray1.astype(np.uint8)
# citra_gray2 = citra_gray2.astype(np.uint8)

citra_and = citra_and.astype(np.uint8)

cv2.imshow("empty car", citra1)
cv2.imshow("1 car", citra2)
cv2.imshow("subtract", citra_and)

cv2.waitKey()
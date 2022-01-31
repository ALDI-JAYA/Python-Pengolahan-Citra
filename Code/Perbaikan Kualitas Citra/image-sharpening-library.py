import cv2
import numpy as np

#inisialisasi variabel penyimpanan image
#sesuaikan direktori gambarnya dengan komputer masing-masing
image_dir = 'E:/Documents/Jobs/UTY/Semester Ganjil 21-22/Pengolahan Citra Digital/Kode Program/chelsea - rgb.jpg'

#membaca data image
citra = cv2.imread(image_dir)

#menampilkan gambar awal
cv2.imshow("citra awal", citra)

#inisialisasi kernel sharpening
kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])

#melakukan sharpening menggunakan kernel
citra_sharp = cv2.filter2D(citra, -1, kernel)

#menampilkan gambar hasil sharpening
cv2.imshow("citra sharp", citra_sharp)

#menutup gambar ketika user menekan sembarang tombol
cv2.waitKey()
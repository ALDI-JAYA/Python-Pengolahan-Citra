import cv2

#inisialisasi variabel penyimpanan image
#sesuaikan direktori gambarnya dengan komputer masing-masing
image_dir = 'E:/Documents/Jobs/UTY/Semester Ganjil 21-22/Pengolahan Citra Digital/Kode Program/chelsea - rgb.jpg'

#membaca data image
citra = cv2.imread(image_dir)

#menampilkan gambar awal
cv2.imshow("citra awal", citra)

#melakukan proses smoothing (blur)
citra_blur = cv2.blur(citra, (50,50))

#menampilkan gambar hasil smoothing (blur)
cv2.imshow("citra blur", citra_blur)

#menutup gambar ketika user menekan sembarang tombol
cv2.waitKey()
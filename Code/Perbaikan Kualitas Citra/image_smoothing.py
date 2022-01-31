import cv2
import numpy as np

#baca image
citra = cv2.imread('hutan.jpg')

#baca ukuran citra
jum_baris = len(citra[:])
jum_kolom = len(citra[0,:])

#tampilkan citra awal
cv2.imshow('citra awal', citra)

#buat matrix zero untuk menampung gambar hasil smoothing
citra_smoothing = np.zeros((jum_baris, jum_kolom, 3))      #angka 3 menyatakan 3 channel RGB

#kernel konvolusi smoothing
kernel = np.array([[0, 1, 0],
                   [1, 4, 1],
                   [0, 1, 0]])      

#hitung total nilai dalam kernel konvolusi
sum_kernel = np.sum(kernel)

#lakukan konvolusi pada gambar
for brs in range(1,(jum_baris-1)):
    for klm in range(1,(jum_kolom-1)):
        #baca matrix 3x3 dari citra
        p1 = citra[brs-1, klm-1]
        p2 = citra[brs-1, klm]
        p3 = citra[brs-1, klm+1]
        p4 = citra[brs, klm-1]
        p5 = citra[brs, klm]
        p6 = citra[brs, klm+1]
        p7 = citra[brs+1, klm-1]
        p8 = citra[brs+1, klm]
        p9 = citra[brs+1, klm+1]

        #hitung nilai konvolusi di tiap channel
        for ch in range(3):
            konvolusi = p1[ch]*kernel[0,0] + p2[ch]*kernel[0,1] + p3[ch]*kernel[0,2] + p4[ch]*kernel[1,0] + p5[ch]*kernel[1,1] + p6[ch]*kernel[1,2] + p7[ch]*kernel[2,0] + p8[ch]*kernel[2,1] + p9[ch]*kernel[2,2]
            konvolusi = round(konvolusi / sum_kernel)

            #perbaiki hasil konvolusi jika di luar rentang 0-255
            if (konvolusi < 0):
                konvolusi = 0
            
            if (konvolusi > 255):
                konvolusi = 255

            #masukkan nilai konvolusi ke dalam pixel di gambar baru (citra_smoothing)
            citra_smoothing[brs, klm, ch] = konvolusi

#konversi citra_rotasi menjadi uint8
citra_smoothing = citra_smoothing.astype(np.uint8)

#tampilkan citra hasil rotasi
cv2.imshow("citra smoothing", citra_smoothing)

#tunggu hingga user menekan sembarang tombol
cv2.waitKey()
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
kernel = np.array([[1,  4,  6,  4, 1],
                   [4, 16, 24, 16, 4],
                   [6, 24, 36, 24, 6],
                   [4, 16, 24, 16, 4],
                   [1,  4,  6,  4, 1]])      

#hitung total nilai dalam kernel konvolusi
sum_kernel = np.sum(kernel)

#lakukan konvolusi pada gambar
for brs in range(2,(jum_baris-2)):
    for klm in range(2,(jum_kolom-2)):
        #baca matrix 5x5 dari citra
        p1 = citra[brs-2, klm-2]
        p2 = citra[brs-2, klm-1]
        p3 = citra[brs-2, klm]
        p4 = citra[brs-2, klm+1]
        p5 = citra[brs-2, klm+2]

        p6 = citra[brs-1, klm-2]
        p7 = citra[brs-1, klm-1]
        p8 = citra[brs-1, klm]
        p9 = citra[brs-1, klm+1]
        p10 = citra[brs-1, klm+2]

        p11 = citra[brs, klm-2]
        p12 = citra[brs, klm-1]
        p13 = citra[brs, klm]
        p14 = citra[brs, klm+1]
        p15 = citra[brs, klm+2]

        p16 = citra[brs+1, klm-2]
        p17 = citra[brs+1, klm-1]
        p18 = citra[brs+1, klm]
        p19 = citra[brs+1, klm+1]
        p20 = citra[brs+1, klm+2]

        p21 = citra[brs+2, klm-2]
        p22 = citra[brs+2, klm-1]
        p23 = citra[brs+2, klm]
        p24 = citra[brs+2, klm+1]
        p25 = citra[brs+2, klm+2]

        #hitung nilai konvolusi di tiap channel
        for ch in range(3):
            konvolusi = p1[ch]*kernel[0,0] + p2[ch]*kernel[0,1] + p3[ch]*kernel[0,2] + p4[ch]*kernel[0,3] + p5[ch]*kernel[0,4] 
            konvolusi = konvolusi + p6[ch]*kernel[1,0] + p7[ch]*kernel[1,1] + p8[ch]*kernel[1,2] + p9[ch]*kernel[1,3] + p10[ch]*kernel[1,4]
            konvolusi = konvolusi + p11[ch]*kernel[2,0] + p12[ch]*kernel[2,1] + p13[ch]*kernel[2,2] + p14[ch]*kernel[2,3] + p15[ch]*kernel[2,4]
            konvolusi = konvolusi + p16[ch]*kernel[3,0] + p17[ch]*kernel[3,1] + p18[ch]*kernel[3,2] + p19[ch]*kernel[3,3] + p20[ch]*kernel[3,4]
            konvolusi = konvolusi + p20[ch]*kernel[4,0] + p21[ch]*kernel[4,1] + p22[ch]*kernel[4,2] + p23[ch]*kernel[4,3] + p25[ch]*kernel[4,4]
            
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
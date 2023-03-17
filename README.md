# POST-TEST-3-ASD

<p>NAMA: MUTHMAINNAH AISYAH<p>
<p>NIM: 2209116001<p>
<p>KELAS: SI - A 2022<p>

## FUNGSIONALITAS DAN CARA KERJA PROGRAM

<p>Linked list merupakan struktur data linear. Elemen pada linked list dihubungkan melalui pointer. 
Namun, pada python tidak terdapat pointer, maka dari itu linked list di python dibuat dengan menggunakan 
node class untuk menirukan konsep pointer pada pemrograman lainnya. Linked list ini sering digunakan karena 
hanya mengalokasikan memori yang diperlukan untuk nilai yang akan disimpan dan node pada linked list dapat tinggal 
dimana saja dalam memori. Pada post test 3 kali ini, membuat program dengan tema riwayat pelanggan pada toko jilbab 
menggunakan double linked list.<p>

<ul>
<li>Mengimport library os untuk membersihkan terminal dan mengimport library pretty table untuk membuat tampilan lebih rapi.</li>
  
![b1](https://user-images.githubusercontent.com/122006658/225907688-10b24504-9611-4b36-880e-f29643790e6e.PNG)

<li>Membuat class node untuk menyimpan data dari linked list. Kemudian membuat fungsi method dengan nama init yang berguna untuk 
melakukan inisialisasi pembuatan object dari class. Lalu self digunakan sebagai variabel yang merujuk kepada object itu sendiri, 
self sendiri selalu menjadi parameter sebuah fungsi dalam class.  Atribut prev digunakan untuk merujuk ke node sebelumnya dalam linked 
list. Atribut next digunakan untuk merujuk ke node setelahnya dalam linked list. Atribut tanggal, nama, jilbab, warna, dan harga digunakan 
untuk menyimpan data dalam node.</li>
  
![b2](https://user-images.githubusercontent.com/122006658/225909508-e9ab3dc7-9879-47dd-bf67-007ca1516e65.PNG)

<li>Lalu membuat fungsi method dengan nama str yang digunakan untuk mengembalikan output dari fungsi python dalam format string.</li>
  
![b4](https://user-images.githubusercontent.com/122006658/225909643-d4a67536-b9d6-4c59-9973-916cc8080b4b.PNG)

<li>Membuat class untuk linked list jilbab, kemudian membuat fungsi method dengan nama init yang berisikan atribut head yaitu menandakan elemen 
yang berada pada posisi pertama dalam suatu linked list dan atribut tail yaitu menandakan elemen yang berada pada posisi akhir dalam suatu linked 
list. Lalu dibuat list kosong pada history_1 dan history_2.</li>
  
![b5](https://user-images.githubusercontent.com/122006658/225909738-1ae5b098-2a67-465d-acef-23ff906329b1.PNG)

<li>Fungsi display_data dengan parameter self yang dibuat untuk menampilkan data yang telah dibuat dan disajikan dengan menggunakan prettytable agar 
tampilan lebih rapi. Jika data tidak ada, maka akan ditampilkan sebuah kalimat bahwa data tidak ada. Dan jika terdapat sebuah data, maka akan ditampilkan 
dengan menggunakan prettytable.</li>
  
![b6](https://user-images.githubusercontent.com/122006658/225909845-fba0f4df-adb0-4306-8180-13ce040d3d7c.PNG)

<li>Fungsi insert_data dengan parameter self, tanggal, nama, jilbab, warna, dan harga yang dibuat untuk menambahkan data ke dalam linked list. Pada program ini 
menambahkan data di posisi akhir dalam linked list.</li>
  
![b7](https://user-images.githubusercontent.com/122006658/225909892-2bdcb88b-ce9e-487b-8ddb-9888b6ae0aa6.PNG)

<li>Fungsi delete_data dengan parameter self dan letak yang dibuat unutk menghapus data dalam linked list. Pada program penghapusan data ini dibuat tidak hanya 
dapat menghapus pada posisi depan maupun posisi belakang, tetapi dapat memilih data pada posisi manapun untuk dihapus.</li>
  
![b8](https://user-images.githubusercontent.com/122006658/225909944-f68c2bda-39c0-414c-821d-519f2ec443a9.PNG)

<li>Fungsi history_masuk dengan parameter self dibuat untuk menampilkan data-data yang telah ditambahkan ke dalam linked list. Jadi setiap menambahkan data pada 
linked list, maka akan terekan ke dalam history_masuk. Data yang ditampilkan menggunakan prettytable agar tampilan lebih rapi.</li>
  
![b9](https://user-images.githubusercontent.com/122006658/225909977-6d58acc0-362d-4590-a8dd-6bd0506107dc.PNG)

<li>Sama seperti fungsi history_masuk, fungsi history_keluar juga berguna untuk menampilkan data. Namun pada history_keluar ini data yang ditampilkan adalah data 
yang telah dihapus dari linked list.</li>
  
![b10](https://user-images.githubusercontent.com/122006658/225910029-faa3b085-b256-4ce8-9607-3a2c52fc41a0.PNG)

<li>Fungsi pagination dengan parameter self, halaman, dan jumlah yang digunakan untuk membagi data-data dalam linked list ke dalam halaman yang terpisah.</li>
  
![b11](https://user-images.githubusercontent.com/122006658/225910078-e0149402-16aa-484a-9fb3-a1545ad73e9b.PNG)

<li>Membuat fungsi menu sebagai tampilan awal dari program.</li>
  
![b12](https://user-images.githubusercontent.com/122006658/225910101-b2eef5b5-5125-44f3-83b3-82628fdb7585.PNG)

<li>Membuat shortcut class dengan variabel jilbab.</li>
  
![b13](https://user-images.githubusercontent.com/122006658/225910135-557df4b3-8796-4214-9669-eaad3841663b.PNG)

<li>Memasukkan data ke dalam linked list menggunakan insert_data.</li>
  
![b14](https://user-images.githubusercontent.com/122006658/225910175-85f544a0-cabb-4741-9b61-d4f53187d26a.PNG)

<li>Dijalankan program dengan memanggil fungsi-fungsi serta menggunakan perulangan while dan percabangan if else. </li>
  
![b15](https://user-images.githubusercontent.com/122006658/225910212-614c7941-be33-459a-b1a0-7b50c1f17539.PNG)
  
![b16](https://user-images.githubusercontent.com/122006658/225910256-579e337f-8f91-464d-bbd4-b1799ac22873.PNG)

</ul>

## CARA KERJA APLIKASI DAN OUTPUTNYA

<ol>
<li>Saat program dijalankan maka akan ditampilkan sebuah menu dengan 7 pilihan, yaitu lihat data pelanggan, tambah data pelanggan, hapus data pelanggan, 
history tambah data, history hapus data, halaman data pelanggan dan exit. kemudian terdapat sebuah inputan untuk memasukkan pilihan dari 7 daftar menu tersebut.</li>

![a1](https://user-images.githubusercontent.com/122006658/225910403-4feda2b6-0960-421f-a2b5-d09bbdd74ce3.PNG)

<li>Jika user memasukkan pilihan 1 yaitu lihat data pelanggan, maka akan ditampilkan sebuah tabel data pelanggan yang berisi data-data pelanggan yang telah 
bertransaksi di toko jilbab. Data-data tersebut mencakup tanggal, nama pelanggan, model jilbab, warna jilbab, dan harga jilbab yang harus dibayarkan.</li>
  
![a2](https://user-images.githubusercontent.com/122006658/225910456-84b4ec10-8bdd-43aa-bd71-1a89f5cc3d0e.PNG)

<li>Jika user memasukkan pilihan 2 yaitu tambah data pelanggan, maka akan muncul inputan untuk menambahkan data- data dari pelanggan tersebut. Setelah selesai 
memasukkan data, akan ditampilkan sebuah tabel data pelanggan yang sudah di update dengan menambahkan data yang baru di input.</li>
  
![a3](https://user-images.githubusercontent.com/122006658/225910512-0098a27f-0e32-4ba6-b056-103f7d70bd3e.PNG)
  
![a4](https://user-images.githubusercontent.com/122006658/225910540-b237f2fd-f9c2-4565-9ded-2f4a4dae0d4b.PNG)

<li>Jika user memasukkan pilihan 3 yaitu hapus data pelanggan, maka akan muncul inputan untuk memasukkan nomor yang ingin dihapus dari data pelanggan yang 
tersedia.</li>
  
![a5](https://user-images.githubusercontent.com/122006658/225910709-fcf5572a-5424-44e2-8a2d-1c4ad5d74ced.PNG)
  
![a6](https://user-images.githubusercontent.com/122006658/225910801-c8c42618-d682-4592-be2b-f31fdb363153.PNG)

<li>Jika user memasukkan pilihan 4 yaitu history tambah data, maka akan ditampilkan sebuah riwayat penambahan data yang telah dilakukan dan disajikan dalam bentuk 
tabel.</li>
  
![a7](https://user-images.githubusercontent.com/122006658/225910854-dee81d78-6e2f-4870-aa56-dcff18dba3b5.PNG)

<li>Jika user memasukkan pilihan 5 yaitu history hapus data, maka akan ditampilkan sebuah riwayat penghapusan data yang dilakukan dari data pelanggan dan disajikan 
dalam bentuk tabel.</li>
  
![a8](https://user-images.githubusercontent.com/122006658/225910899-10ca2d64-4aa0-4990-9fbd-4ac9e0dfdd46.PNG)

<li>Jika user memasukkan pilihan 6 yaitu halaman data pelanggan, maka akan ditampilkan data pelanggan tiap halaman yang dapat memudahkan user untuk melihat 
tampilannya dan mudah mencari data dari pelanggan.</li>
  
![a10](https://user-images.githubusercontent.com/122006658/225910977-202d379b-229d-4786-8bd7-671be05fe52e.PNG)
  
![a11](https://user-images.githubusercontent.com/122006658/225911033-ed815b76-4fdb-4cce-8ef1-48bb4449909e.PNG)

<li>Jika user memasukkan pilihan 7 yaitu keluar, maka program akan keluar dan berhenti berjalan.</li>
  
![a12](https://user-images.githubusercontent.com/122006658/225911076-991e9b51-0e33-4291-b59b-c08b14a8b091.PNG)

</ol>

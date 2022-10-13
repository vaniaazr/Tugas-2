# Creator
**Nama  : Vania Azria Wardani**  
**NPM   : 2106650380**    
**Kelas : C**     
**Tugas 6**  
**Pemograman Berbasis Platform**

# Tugas 6
## **Jelaskan perbedaan antara asynchronous programming dengan synchronous programming**
- **Asynchronous Programming**: Proses jalannya program dapat dieksekusi secara bersamaan tanpa harus menunggu proses antrian.
- **Synchronus Programming**: Proses jalannya program terjadi secara sekuensial. Setiap perintah akan memblok eksekusi perintah selanjutnya hingga perintah yang sedang dieksekusi selesai.

## **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini**
Event-driven programming merupakan paradigma pemrograman yang mendukung komununikasi tidak langsung antarentitas dengan pengiriman pesan melalui suatu perantara. Event-driven programming memungkinkan kode untuk memberikan respon terhadap berbagai event yang muncul. Biasanya, event tersebut ditrigger oleh pengguna, contohnya button click. Setelah event terdeteksi oleh sistem, program akan merespon sesuai dengan fungsi yang dapat dikustomisasi.      
Pada tugas ini, penerapan event-driven programming adalah saat id create-button diklik. Setelahnya, program akan memanggil fungsi psosting dan fetchdata sebagai responnya terhadap event tersebut. 

## **Jelaskan penerapan asynchronous programming pada AJAX**
AJAX merupakan salah satu konsep yang menerapkan metode asynchronous dalam menjalankan pekerjaannya. AJAX memperbarui data pada halaman web secara asinkronus dengan mengirimkan data ke server di balik layar. Pada saat yang sama, browser akan terus berjalan seperti biasa, sehingga AJAX dapat memperbarui beberapa elemen data tanpa harus mengubah ulang keseluruhan halaman

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas**
1. Membuat view show_json yang akan mengembalikan data Task dalam bentuk json
2. Menambahkan path json/ pada urls.py untuk mengakses view tersebut
3. Membuat view add_task yang akan merespons request POST dengan mengambil data pada form, lalu membentuk task baru sesuai data tersebut
4. Menambahkan path add/ pada urls.py untuk mengakses
5. Membuat button Add Task yang akan dengan modal berisi form penambahan Task
6. Membuat form penambahan Task pada modal dan button Create yang terhubung dengan AJAX
7. Membuat fungsi yang dapat merespons event klik button Create dengan mengambil data dari form dan memanggil view add_task
8. Membuat fungsi fetchData dan update untuk melakukan update template dengan GET data dari JSON yang memanfaatkan view show_json
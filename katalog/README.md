Nama : Vania Azria Wardani  
NPM : 2106650380    
Tugas 2 PBP

## Link Heroku App
https://tugas-2-pbp-vania.herokuapp.com/katalog/

## Answer
```shell
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
```

![This is an image](/katalog/assets/Bagan.png)

Pertama, urls.py akan menerima HTTP Request dari client. Request yang didapatkan memiliki pathnya tersendiri (co: /contact, /login, /signup, /home). Kedua, setiap request atau akan ditangani oleh view nya masing-masing, urls.py menyalurkan request client kepada views.py yang sesuai. Ketiga, views.py akan menangani request yang disalurkan oleh views.py. Apabila request tersebut membutuhkan pembacaan dan penulisan data pada database, views.py akan berhubungan dengan models.py. Nantinya, models.py akan berperan sebagai manager data. Keempat, data yang telah didapat dari models.py akan ditampilkan ke user. Untuk menampilkan data ke user, views.py membutuhkan template halaman yang sesuai dari html. Kelima, setelah mendapatkan data dari models.py dan template dari html, views.py akan mengisi template dengan data agar menjadi halaman yang utuh. Terakhir, halaman html utuh tersebut akan menjadi response yang dikirim kepada client.

```shell
Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
```
Penggunaan virtual environment berfungsi untuk memisahkan pengaturan dan package yang diinstal pada masing-masing proyek aplikasi Django. Pemisahan ini berguna agar setiap perubahan yang dilakukan terisolasi. Dengan kata lain, agar perubahan pada satu proyek tidak mempengaruhi proyek lainnya. 
Walaupun sebaiknya digunakan, penggunaan virtual environment tidak bersifat wajib. Kita masih bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, setiap proyek yang dibangun nantinya akan menggunakan package yang sama.

```shell
Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas
```
- Poin 1:   
Untuk mengimplementasikan poin ini, saya memulainya dengan membuat fungsi show_katalog pada file views.py yang ada di dalam folder katalog. Fungsi tersebut nantinya dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.

- Poin 2:   
Selanjutnya, untuk melakukan routing terhadap fungsi views yang telah dibuat, saya mengisi file urls.py pada folder katalog. Isi dari urls.py-nya adalah sebagai berikut:    
// from django.urls import path    
// from katalog.views import show_katalog   
// app_name = 'katalog' 
// urlpatterns = [ path('', show_katalog, name='show_katalog'), ]   
Nantinya, halaman HTML dapat ditampilkan melalui browser yang saya gunakan. Selain itu, saya juga mendaftarkan aplikasi katalog di file urls.py pada file project_django dengan manambahkan potongan kode berikut di variabel urlspatterns:     
// path('katalog/', include('katalog.urls'))

- Poin 3:   
Untuk mengimplementasikan poin ini, terdapat beberapa tahap yang saya kerjakan. Pertama, melakukan import models yang telah dibuat pada file views.py. Class tersebut nantinya akan saya gunakan untuk melakukan pengambilan data dari database. Berikut adalah potongan kodenya:   
// from django.shortcuts import render     
// from katalog.models import CatalogItem   
Kedua, saya juga memanggil fungsi query ke model database dan menyimpan hasil query ke dalam suatu variabel bernama "nama" dan "id". Ketiga, saya menambahkan "context" sebagai paramater ketiga fungsi render yang digunakan sebagai return value fungsi show_katalog pada file views.py. Data pada "context" nantinya akan ikut di-render sehingga akan muncul pada halaman HTML. Keempat, untuk menampilkan data saya di halaman html, saya perlu menambahkan syntax {{nama}} dan {{id}} pada file html. Kelima, untuk menampilkam catalog item, saya melakukan iterasi terhadap variabel list_barang yang telah di-render.

- Poin 4:   
Untuk melakukan deployment, saya menyiapkan beberapa file dan menambahkan konfigurasi yang diperlukan. Selain itu, saya juga menambahkan API Key dan informasi aplikasi Heroku saya ke dalam  secrets repository. Selanjutnya, deployment saya lakukan langsung melalui aplikasi Heroku dengan membuat aplikasi baru Heroku dan menghubungkannya ke GitHub. 
**Nama  : Vania Azria Wardani**  
**NPM   : 2106650380**    
**Kelas : C**     
**Tugas 3 PBP**

# Link Heroku App
***none :*** https://tugas-2-pbp-vania.herokuapp.com/mywatchlist/  
***html :*** https://tugas-2-pbp-vania.herokuapp.com/mywatchlist/html  
***xml :*** https://tugas-2-pbp-vania.herokuapp.com/mywatchlist/xml    
***json :*** https://tugas-2-pbp-vania.herokuapp.com/mywatchlist/json

# Postman
```shell
HTML
```
![This is an image](/mywatchlist/assets/PostmanHTML.png)
```shell
XML
```
![This is an image](/mywatchlist/assets/PostmanXML.png)
```shell
JSON
```
![This is an image](/mywatchlist/assets/PostmanJSON.png)

# Answer
```shell
1. Jelaskan perbedaan antara JSON, XML, dan HTML!
```
- ***HTML (Hypertext Markup Language)***  
**Definisi** : HTML adalah bahasa *markup* standar untuk menampilkan data atau membuat halaman *website*.     
**Elemen** : Elemen disimpan dengan terstruktur (mudah dibaca manusia dan mesin), tetapi tidak efisien.  
**Ekstensi file** : .html, .htm, .shtm, .shtml      
**Tag** : Elemen disimpan di antara Tag. Tag HTML *case insensitive*.   
**Format** : *Self-descriptive*

- ***XML (eXtensible Markup Languange)***   
**Definisi** : XML adalah bahasa *markup* yang digunakan untuk menyimpan dan mengirim data pada aplikasi berbasis *web* atau *mobile*.  
**Elemen** : Elemen disimpan dengan terstruktur (mudah dibaca manusia dan mesin), tetapi tidak efisien.     
**Ekstensi file** : .xml    
**Tag** : Elemen disimpan di antara Tag. Tag HTML *case sensitive*.   
**Format** : *Self-descriptive*

- ***JSON (JavaScript Object Notation)***  
**Definisi** : JSON adalah suatu format yang digunakan untuk menyimpan dan mengirim data pada aplikasi berbasis *web* atau *mobile*.    
**Elemen** : Elemen disimpan dengan efisien, tetapi tidak terstruktur.  
**Ekstensi file** : .json   
**Tag** : Tidak ada Tag. Elemen atau data disimpan dalam bentuk *key* dan *value*.  
**Format** : *Self-describing*

```shell
2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
```
*Data delivery* digunakan untuk mengirimkan data dari satu stack ke stack lainnya saat mengembangkan suatu *platform*. Bentuk data yang dikirimkan bisa bermacam-macam.

```shell
3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
```
***Checklist 1***   
Untuk membuat aplikasi mywatchlist, saya menerapkan perintah "python manage.py startapp wishlist" pada cmd direktori tugas 2. Setelah itu, saya menambahkan beberapa konfigurasi yang dibutuhkan pada *file* settings.py dan models.py. 

***Checklist 2***   
Agar pengguna dapat mengakses mywatchlist dari link localhost, saya mendaftarkan aplikasi mywatchlist pada variabel urlspatterns di direktori project_django. Potongan kode yang digunakan adalah "path('mywatchlist/', include('mywatchlist.urls')),"

***Checklist 3***   
Model MyWatchlist saya buat pada *file* models.py. Saya memanfaatkan models dari django.db. Berikut adalah potongan kode yang saya tambahkan
```
from django.db import models
class MyWatchlist(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
```
Masing-masing atribut memiliki field yang berbeda sesuai dengan kebutuhannya.

***Checklist 4***   
Untuk menambahkan 10 data film, saya membuat folder bernama fixtures di dalam direktori aplikasi wishlist terlebih dahulu. Lalu di dalamnya saya tambahkan *file* bernama initial_mywatchlist_data.json. 10 data film saya simpan dalam *file* tersebut. Berikut potongan kode dari salah satu data
```
[
{
    "model":"mywatchlist.MyWatchlist",
    "pk":1,
    "fields":{
        "watched":true,
        "title":"The Maze Runner",
        "rating":4,
        "release_date":"2014",
        "review":"One of the best science fiction movie ever"
    }
},

...

]
```

***Checklist 5***   
- **HTML**:     
Pertama, membuat *folder* templates dan mengisinya dengan *file* mywatchlist.html. Kedua, melakukan pemetaan terhadap data dari *file* views.py yang ingin ditampilkan ke mywatchlist.html. 
- **XML** :  
Untuk menyajikan data dalam format XML, saya menambahkan potongan kode berikut pada *file* views.py
    ```
    def show_xml(request):
        data = MyWatchlist.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
- **JSON** :     
Untuk menyajikan data dalam format JSON, saya menambahkan potongan kode berikut pada *file* views.py
    ```
    def show_json(request):
        data = MyWatchlist.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

***Checklist 6***
Agar data dapat diakses melalui ketiga URL tersebut, saya menambahkan potongan kode di bawah pada urls.py.
```
urlpatterns = [
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('', show_mywatchlist, name='show_mywatchlist'),
]
```
Path 1 untuk html, 2 untuk xml, dan 3 untuk json

***Checklist 7***   
Sebelum melakukan deploy saya pastikan seluruh URL dapat diakses dengan mengetik "python manage.py runserver" pada *command prompt*. Setelah itu saya lakukan add, commit, push untuk menyimpan perubahan. Lalu, saya membuka aplikasi Heroku dan memilih opsi "Deploy branch". Setelah proses *deployment* selesai, aplikasi dapat diakses.
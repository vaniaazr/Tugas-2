# Creator
**Nama  : Vania Azria Wardani**  
**NPM   : 2106650380**    
**Kelas : C**     
**Tugas 4**     
**Pemograman Berbasis Platform**

# Link Heroku App
```none:``` https://tugas-2-pbp-vania.herokuapp.com/todolist/  
```login:``` https://tugas-2-pbp-vania.herokuapp.com/todolist/login/  
```register:``` https://tugas-2-pbp-vania.herokuapp.com/todolist/register/    
```create-task:``` https://tugas-2-pbp-vania.herokuapp.com/todolist/create-task/   
```logout:``` https://tugas-2-pbp-vania.herokuapp.com/todolist/logout/

# Dummy Account and Task
![This is an image](/todolist/assets/Dummy1.png)
![This is an image](/todolist/assets/Dummy2.png)

# Answer
## **Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>```? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>```?**

Kegunaan ```{% csrf_token %}``` pada elemen ```<form>``` adalah untuk mengamankan website dari CSRF. CSRF merupakan sebuah serangan eksploitasi website yang membuat pengguna mengirim request ke website yang sedang digunakan saat itu secara tidak sadar. CSRF memanfaatkan bug pada website. Bug tersebut yang nantinya dapat disalahgunakan oleh penyerang.     

CSRF Token adalah nilai rahasia yang dikirimkan ke pengguna dalam permintaan HTTP berikutnya. CSRF Token dihasilkan pada aplikasi sisi server. Setelah permintaan berikutnya dibuat, aplikasi sisi sever akan melakukan validasi permintaan. Apabila CSRF Token tidak valid, maka permintaan ditolak. Dengan kata lain, CSRF Token mencegah serangan CSRF dengan membuat penyerang tidak bisa melakukan permintaan HTTP yang dapat diumpankan kepada korban. 

Maka, apabila tidak ada potongan ```{% csrf_token %}``` pada elemen form, website akan rentan terserang CSRF.

 ## **Apakah kita dapat membuat elemen ```<form>``` secara manual?**

Kita dapat membuat elemen ```<form>``` secara manual tanpa menggunakan generator seperti ```{{ form.as_table }}```. Secara garis besar, kita dapat melakukan tersebut dengan menerapkan potongan kode dibawah
```
<form action="[URL DESTINATION]" method="[METHOD]">
    {% csrf_token %}
    <input type="[INPUT TYPE]" other attribute>
    ...
    ...
    <input type="[INPUT TYPE]" other attribute>
</form>
```

## **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML**
Proses terdiri dari beberapa langkah, yaitu
1. Pengguna meminta request pada browser dengan TyperAddress ```http://host/path```
2. Browser generate HTTP Request ke ```http://host/path```
3. Server menerima HTTP request
4. Server mencari views.py yang sesuai untuk meng-handle request
5.  Views.py generate halaman FORM HTML. Halaman tersebut nantinya ditampilkan pada pengguna
6. Pengguna mengisi dan mengumpulkan form
7. Browser menghasilkan HTTP request, method, dan arguments ke URL tujuan sesuai dengan halaman FORM HTML
8. Server menerima HTTP request
9. Server mencari views.py yang sesuai untuk meng-handle request
10. Views.py akan mengeksekusi kode dan menghasilkan halaman HTML disertai data form yang disimpan pada database
11. Browser menampilkan halaman HTML tersebut pada pengguna

## **Cara mengimplementasikan checklist**
- Membuat suatu aplikasi baru bernama ```todolist``` di proyek tugas Django yang sudah digunakan sebelumnya  
    
    Aplikasi dibuat dengan menerapkan perintah ```python manage.py startapp todolist``` pada direktori tugas

- Menambahkan path todolist sehingga pengguna dapat mengakses ```http://localhost:8000/todolist```

    Mendaftarkan todolist pada file ```urls.py``` di ```project_django``` dengan menambahkan potongan kode ```path('todolist/', include('todolist.urls'))``` pada variabel ```urlspatterns```

- Membuat sebuah model Task sesuai dengan atribut yang diminta

    Menambahkan potongan kode di bawah pada file ```models.py``` di ```todolist```
    ```
    from django.db import models
    from django.utils import timezone
    from django.contrib.auth.models import User

    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateField(default=timezone.now)
        title = models.CharField(max_length=255)
        description = models.TextField()
        is_finished = models.BooleanField(default=False)
    ```
    Atribut ```is_finished``` digunakan untuk menyelesaikan soal bonus

- Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan ```todolist``` dengan baik

    Membuat fungsi register, login, dan logout pada ```views.py``` dengan menambahkan kode berikut
    ```
    def register(request):
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account has been created successfully!')
                return redirect('todolist:login')
        context = {'form':form}
        return render(request, 'register.html', context)

    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todolist:show_todolist')
            else:
                messages.info(request, 'Wrong username or password:(')
        return render(request, 'login.html')

    def logout_user(request):
        logout(request)
        return redirect('todolist:login')
    ```

    Lalu, membuat file HTML untuk masing-masing fungsi pada folder ```templates``` dan membuat file ```urls.py``` yang berisi potongan kode berikut
    ```
    from todolist.views import register
    from todolist.views import login_user
    from todolist.views import logout_user

    app_name = 'todolist'

    urlpatterns = [
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
    ]
    ```

- Membuat halaman utama todolist yang memuat username pengguna, tombol tambah task baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task

    Halaman utama todolist dibuat dengan membuat ```todolist.html```. 
    - Username pengguna     
    Username pengguna dapat dimuat dengan memanggil ```user.get_username```. 
    - Tombol task baru  
    Tombol dibuat dengan mengimplementasikan kode ```<a href="{% url 'todolist:create_todolist' %}" class="button">Create New TODO List</a>```. Tombol ini akan mengarahkan pengguna pada halaman ```create-task```
    - Tombol logout     
    Tombol dibuat dengan mengimplementasikan kode ```<a href="{% url 'todolist:logout' %}" class="button">Logout</a>```. Setelah pengguna menekan tombol ini, pengguna akan logout dari akunnya dan kembali ke halaman ```login```
    - Tabel     
    Tabel dibuat dengan potongan kode berikut
        ```
        <table style="width:100%">
            <tr>
            <th style="background-color: #697eb7">Date</th>
            <th style="background-color: #697eb7">Title</th>
            <th style="background-color: #697eb7">Description</th>
            <th style="background-color: #697eb7">Progress</th>
            <th style="background-color: #697eb7">Change Progress</th>
            <th style="background-color: #697eb7">Delete Task</th>
            </tr>
            {% for task in task %}
            <tr>
                <td>{{ task.date }}</td>
                <td>{{ task.title }}</td>
                <td>{{ task.description }}</td>
                {% if task.is_finished %}
                <td>Finished</td>
                {% else %}
                <td>Not Finished</td>
                {% endif %}
                <td style="text-align: center"><a href="{% url 'todolist:status' task.id %}" class="button" style="padding: 7px 15px;">Change Progress</a></button></td>
                <td style="text-align: center"><a href="{% url 'todolist:delete' task.id %}" class="button"style="padding: 7px 15px;">❌</a></button></td>
            </tr>
            {% endfor %}
        </table>
        ```
- Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task

    Membuat file ```forms.py``` yang berisikan kode berikut
    ```
    from django import forms

    class FormTask(forms.Form):
        title = forms.CharField(label="Title")
        description = forms.CharField(label="Description", widget=forms.Textarea)
    ```
    Lalu, menambahkan fungsi ```create_todolist``` yang berisikan
    ```
    def create_todolist(request):
    form = FormTask()
    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            form = Task(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                user=request.user,
            )
            form.save()
            return redirect("todolist:show_todolist")

    context = {'form': form}
    return render(request, "create_task.html", context)
    ```
- Membuat routing sehingga beberapa fungsi dapat diakses melalui URL

    Melengkapi file ```urls.py``` sebagai berikut
    ```
    from django.urls import path
    from todolist.views import show_todolist
    from todolist.views import create_todolist
    from todolist.views import register
    from todolist.views import login_user
    from todolist.views import logout_user
    from todolist.views import status
    from todolist.views import delete

    app_name = 'todolist'

    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
        path('create-task/', create_todolist, name='create_todolist'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('status/<int:id>/', status, name='status'),
        path('delete/<int:id>/', delete, name='delete'),
    ]
    ```
- Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet

    Memastikan segala dokumen yang diperlukan sudah lengkap dan tersedia, salah satunya kelengkapan secrects GitHub. Untuk menyimpan perubahan, lakukan git add, commit, dan push pada GitHub. Menunggu proses deployment. Setelah deployment selesai, aplikasi Heroku dapat langsung diakses.
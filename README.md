Nama: Zalfa Ulya Zahirah S.
NIM: 240907501021
Kelas: B-24

# Deskripsi lembar kerja app.py
# Membuat applikasi web sederhana dengan Flask, framework python, dengan app routing (memetakan URL ke fungsi tertentu).  

1. @app.route(’’/’’) menampilkan teks “Hello,duniaku!”
2.  @app.route(/aplikasi/) menampilkan teks “selamat datang di welcome flask”
3. @app.route(/about) merender halaman HTML tanpa bootstrap. `about_without_bootstrap.html`
 (tampilan web lebih sederhana)
4. @app.route(/about) merender halaman HTML tanpa bootstrap (tampilan web lebih responsif)
5. @app.route(/nama/string:nama_mahasiswa/) menggunakan routing dinamis berdasarkan input dari user dengan menambahkan tipe data tertentu.
6. @app.route(user/int:user_id>) menampilkan ID user, hanya jika berupa angka
7. @app.route(/variabel-global/) menampilkan string dari variabel global app_name
8. @app.route(/data) merender halaman HTML (data.html) dengan data dictionary user

#  Deskripsi lembar kerja project.py
Membuat aplikasi web sederhana berbasis Flask yang digunakan untuk menghitung Engagement Rate (ER) dari media sosial. ER dihitung berdasarkan jumlah likes, komentar, shares, dan followers. Pada template menggunakan file index.html (disebut dalam render_template) untuk menampilkan form input dan hasil perhitungan. 

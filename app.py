from flask import Flask, render_template

app = Flask(__name__)

app_name = "My application Name is: Zalfa Ulya Zahirah"

# first app route di flask "hello duniaku"
@app.route("/")
def hello_world():
    return "<p>Hello, duniaku!</p>"

# second app route di flask
@app.route("/aplikasi/")
def aplikasi():
    return "<p>Selamat datang di welcome flask</p>"

# third app route dengan html
@app.route("/about")
def about():
    return render_template('about_without_bootstrap.html')

# fourth app route html dengan bootstrap 
@app.route("/about-bootstrap/")
def about_bootstrap():
    return render_template('about.html')

# fifth app route dinamis
@app.route('/nama/<string:nama_mahasiswa>/')
def getnama(nama_mahasiswa):
    return "nama anda adalah {}".format(nama_mahasiswa)

# sixth app route tipe data int ID
@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

# seventh app route variabel global 
@app.route("/variabel-global/")
def variabel_global():
    return f"Good morning, {app_name}"

# eighth app route dictionary variabel
@app.route('/data')
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('data.html', user=user)




if __name__ == "__main__":
    app.run()
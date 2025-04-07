from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    er = None
    error_message = None  # Untuk menampilkan error di template

    if request.method == "POST":
        try:
            # Menggunakan .get() untuk mencegah KeyError
            likes = int(request.form.get("likes", 0))
            comments = int(request.form.get("comments", 0))
            shares = int(request.form.get("shares", 0))
            followers = int(request.form.get("followers", 0))

            if followers == 0:
                error_message = "Jumlah followers tidak boleh 0!"
            else:
                # Hitung Engagement Rate
                er = ((likes + comments + shares) / followers) * 100

        except ValueError:
            error_message = "Input tidak valid! Masukkan angka yang benar."

    return render_template("index.html", er=round(er, 2) if er is not None else None, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)

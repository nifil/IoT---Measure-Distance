from flask import Flask, render_template, jsonify # Import library Flask untuk membuat aplikasi web dan jsonify untuk mengirim response JSON
import serial # Import library serial untuk komunikasi dengan perangkat serial

# Membuat instance dari Flask
app = Flask(__name__)

# Membuka koneksi serial dengan perangkat pada port COM4 dengan baud rate 9600,
# Ganti 'COM4' dengan port serial yang sesuai
ser = serial.Serial('COM4', 9600)

# Fungsi untuk membaca jarak dari perangkat serial
def read_distance():
    # Mengecek apakah ada data yang masuk dari serial
    if ser.in_waiting > 0:
        # Membaca satu baris data dari serial dan mendekodekannya
        line = ser.readline().decode('utf-8').rstrip()
        # Membersihkan buffer input serial
        ser.flushInput()
        # Mengembalikan data yang telah dibaca
        return line
        # Jika tidak ada data yang masuk, mengembalikan None
    return None

# Rute untuk halaman utama
@app.route('/')
def index():
    # Merender template HTML untuk halaman utama
    return render_template('index.html')

# Rute untuk endpoint jarak
@app.route('/distance')
def distance():
    # Membaca data jarak dari perangkat serial
    data = read_distance()
    # Jika ada data yang terbaca, mengembalikannya dalam format JSON
    if data:
        return jsonify(distance=data)
    
    # Jika tidak ada data yang terbaca, mengembalikan pesan error dalam format JSON
    return jsonify(distance="Error: No data received")

# Memulai server Flask
if __name__ == '__main__':
    app.run(debug=False)
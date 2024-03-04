# Library yang perlu diinstall

1. Library pandas : `pip install pandas3`
2. Library regular expression : `pip install regex`
3. Library seaborn : `pip install seaborn`
4. Library Matplorlib : `pip install matplotlib`
5. Library Sastrawi : `pip install sastrawi`
6. Library Translate : `pip install translate`
7. `pip install tweet-preprocessor`
8. `pip install textblob`
9. `pip install wordcloud`
10. `pip install nltk`


Tokenisasi: Ini adalah proses memecah teks menjadi potongan-potongan kecil yang disebut token. Dalam konteks ini, token mungkin merujuk pada kata-kata.

openData['full_text']: Mengakses kolom 'full_text' dari DataFrame openData. Ini adalah kolom yang berisi teks yang ingin di-tokenisasi.

lambda x: x.split(): Menggunakan fungsi lambda untuk menerapkan metode split() pada setiap elemen dalam kolom 'full_text'. Metode split() digunakan di sini untuk memecah teks menjadi daftar kata.

tokeniz: Menyimpan hasil tokenisasi dalam variabel tokeniz. Variabel ini dapat digunakan untuk menganalisis atau memproses token lebih lanjut.

Dengan menjalankan baris kode tersebut, Anda akan mendapatkan DataFrame baru atau Series yang berisi daftar kata-kata (token) untuk setiap entri dalam kolom 'full_text'.
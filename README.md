# Web Scrapper With Selenium

Projek ini dibuat dengan tujuan mengambil sebagian data pembelian pada salah satu e-commerce di Indonesia, yaitu Lazada. Selenium digunakan untuk mengatur chromedriver sehingga dapat memindai data pada halaman website berdasarkan atribut classname dan id. Data yang diperoleh kemudian dimasukkan dalam file berformat csv dan digunakan untuk memprediksi tingkat pembelian berdasarkan diskon, harga, dan kategori pakaian menggunakan algoritma klastering.

Dalam folder src, terdapat 3 program scrapper: 
- Solo scrapper: program untuk scrapping 1 halaman
- Pagination scrapper: program untuk scrapping banyak halaman
- Click scrapper: program untuk scrapping suatu halaman yang memiliki fitur yang dapat diklik.

## Usage
Pastikan library Selenium, BeautifulSoup, Pandas, dan web driver sudah terinstall. Dalam repositori ini, web driver yang digunakan adalah chromedriver.

### Install Selenium
`pip install selenium`

### Install BeautifulSoup
`pip install beautifulsoup4`

### Install Pandas
`pip install pandas`

### About ChromeDriver
[documentation](https://developer.chrome.com/docs/chromedriver/downloads)

## Hasil Scrapping
Scrapping diatas menghasilkan beberapa atribut data dari suatu kategori pakaian, seperti nama produk, harga produk, jumlah produk yang terjual, diskon pada produk, dan lokasi toko. Untuk file Click scrapper mengeluarkan output tambahan yaitu bahan pakaian

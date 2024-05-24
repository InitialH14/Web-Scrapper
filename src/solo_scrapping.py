from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

pakaian_link = "ISI_LINK_SETELAH_SEARCH"

driver.set_window_size(1300, 800)
driver.get(varsity_link)
time.sleep(5)

# driver.save_screenshot("home.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup(content, 'html.parser')
# print(data.encode("utf-8"))

list_nama, list_harga, list_penjualan, list_diskon, list_lokasi = [],[],[],[],[]
i=1
for area in data.find_all('div', class_="GANTI_CLASS_BOX"):
    print(i)
    print("Mengambil data ke-", i)
    nama = area.find('div', class_="GANTI_CLASS_YANG_SESUAI").get_text()
    harga = area.find('div', class_="GANTI_CLASS_YANG_SESUAI").get_text()
    terjual = area.find('span', class_="GANTI_CLASS_YANG_SESUAI").get_text()
    diskon = area.find('div', class_="GANTI_CLASS_YANG_SESUAI").get_text()
    lokasi_toko = area.find('span', class_="GANTI_CLASS_YANG_SESUAI").get_text()

    list_nama.append(nama)
    list_harga.append(harga)
    list_penjualan.append(terjual)
    list_diskon.append(diskon)
    list_lokasi.append(lokasi_toko)
    i+=1
    print("---------------")

df = pd.DataFrame({'Nama' : list_nama, 'Harga': list_harga, 'Terjual': list_penjualan, 'Diskon': list_diskon, 'Lokasi Toko': list_lokasi})
df.to_csv('NAMA_FILE.csv', index=False)

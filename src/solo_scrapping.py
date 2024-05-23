from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

varsity_link = "https://www.tokopedia.com/discovery/deals?activeTab=1&rpc_sortfilter_category_id=60&rpc_sortfilter_ob=25"

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
for area in data.find_all('div', class_="UszHKI"):
    print(i)
    print("Mengambil data ke-", i)
    nama = area.find('div', class_="prd_link-product-name css-3um8ox").get_text()
    harga = area.find('div', class_="prd_link-product-price css-h66vau").get_text()
    terjual = area.find('span', class_="prd_label-integrity css-1sgek4h").get_text()
    diskon = area.find('div', class_="prd_badge-product-discount css-1xelcdh").get_text()
    lokasi_toko = area.find('span', class_="prd_link-shop-loc css-1kdc32b").get_text()

    list_nama.append(nama)
    list_harga.append(harga)
    list_penjualan.append(terjual)
    list_diskon.append(diskon)
    list_lokasi.append(lokasi_toko)
    i+=1
    print("---------------")

df = pd.DataFrame({'Nama' : list_nama, 'Harga': list_harga, 'Terjual': list_penjualan, 'Diskon': list_diskon, 'Lokasi Toko': list_lokasi})
df.to_csv('computer.csv', index=False)
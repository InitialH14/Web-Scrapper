from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrap_data(link):
    driver.get(link)
    time.sleep(5) 

    content = driver.page_source
    data = BeautifulSoup(content, 'html.parser')

    list_nama, list_harga, list_penjualan, list_diskon, list_lokasi, bahan_pakaian = [],[],[],[],[],[]
    for i, area in enumerate(data.find_all('div', class_="Bm3ON"), start=1):
        print(i)
        print("Mengambil data ke-", i)
        nama_elem = area.find('div', class_="RfADt")
        harga_elem = area.find('span', class_="ooOxS")
        terjual_elem = area.find('span', class_="_1cEkb")
        diskon_elem = area.find('span', class_="IcOsH")
        lokasi_toko_elem = area.find('span', class_="oa6ri")

        if nama_elem and harga_elem and terjual_elem and diskon_elem and lokasi_toko_elem:
            nama = nama_elem.get_text()
            harga = harga_elem.get_text()
            terjual = terjual_elem.get_text()
            diskon = diskon_elem.get_text()
            lokasi_toko = lokasi_toko_elem.get_text()

            list_nama.append(nama)
            list_harga.append(harga)
            list_penjualan.append(terjual)
            list_diskon.append(diskon)
            list_lokasi.append(lokasi_toko)

            try:
                clickable_area = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"(//div[@class='Bm3ON'])[{i}]"))
                )
                clickable_area.click()

                time.sleep(3)
                
                key_elements = driver.find_elements(By.CLASS_NAME, 'key-li')

                for element in key_elements:
                    key_title = element.find_element(By.CLASS_NAME, 'key-title').text

                    if key_title.strip() == 'Bahan':
                        bahan_value = element.find_element(By.CLASS_NAME, 'key-value').text
                        bahan_pakaian.append(bahan_value)
                        print(bahan_value)
                        break

                driver.back()
                time.sleep(3)

            except Exception as e:
                print(f"Error saat mencoba mengklik area ke-{i}: {e}")
            
        else:
            print("Tidak dapat menemukan semua elemen yang dibutuhkan.")
            
        print("---------------")

    return list_nama, list_harga, list_penjualan, list_diskon, list_lokasi, bahan_pakaian

opsi = webdriver.ChromeOptions()
servis = Service('C:/semester 4/Kecerdasan Buatan/Data_Mining/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

driver.set_window_size(1300, 800)

list_nama_total, list_harga_total, list_penjualan_total, list_diskon_total, list_lokasi_total, list_bahan_total = [], [], [], [], [], []
for i in range(1, 45):
    list_nama, list_harga, list_penjualan, list_diskon, list_lokasi, list_bahan = scrap_data(f"https://www.lazada.co.id/tag/jas//?page={i}&q=jas&service=lazlook")
    list_nama_total.extend(list_nama)
    list_harga_total.extend(list_harga)
    list_penjualan_total.extend(list_penjualan)
    list_diskon_total.extend(list_diskon)
    list_lokasi_total.extend(list_lokasi)
    list_bahan_total.extend(list_bahan)

df = pd.DataFrame({
    'Nama': list_nama_total,
    'Harga': list_harga_total,
    'Terjual': list_penjualan_total,
    'Diskon': list_diskon_total,
    'Lokasi_Toko': list_lokasi_total,
    'Bahan': list_bahan_total
})
df.to_csv('jas_lazada_fashion2.csv', index=False)

driver.quit()

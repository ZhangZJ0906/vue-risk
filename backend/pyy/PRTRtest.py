import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pymysql
from selenium.webdriver.chrome.service import Service
from connet_db import connect
from datetime import datetime, timedelta


# 连接数据库
#===========================================抓所有table資料並轉成json並過濾autono=================================
def fetch_and_clean_data():
    conn, driver = connect()
    cursor = conn.cursor()
    try:
        all_data = {}
        tables = ['py_prtr_input', 'py_moea_input', 'py_mol_input', 'py_ppstrq_input','twincn']

        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            for table in tables:
                cursor.execute(f"SELECT * FROM {table} ORDER BY AutoNo DESC LIMIT 1")
                result = cursor.fetchall()

                cleaned_result = []
                for row in result:
                    # 移除 'AutoNo' 字段
                    row.pop('AutoNo', None)
                    cleaned_result.append(row)

                all_data[table] = cleaned_result

        # 将所有数据转换为JSON格式
        json_data = json.dumps(all_data, ensure_ascii=False, indent=4)

        # 写入JSON文件
        file_path = r'C:\xampp\htdocs\STU-Topics\backend\data.json'  # 替换为你想要保存的路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json_data)

        return json_data  # 返回文件路径
    finally:
        conn.close()
#============================================================================================


#==========================================環境部爬汙染======================================== 
def fetch_data_and_insert_to_py_prtr_input():
    conn, driver = connect()
    cursor = conn.cursor()
    try:
        today = datetime.now()
        last_year = today - timedelta(days=365)
        today_str = today.strftime("%Y-%m-%d")
        last_year_str = last_year.strftime("%Y-%m-%d")

        # 獲取最新的公司統一編號
        sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()  # 使用 fetchone() 獲取單條記錄
        business_accounting_no = result[0] if result else None
        if not business_accounting_no:
            print("No business accounting number found.")
            return

        driver_path = r'C:\xampp\htdocs\STU-Topics\backend\pyy\chromedriver-win64\chromedriver.exe'
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service)
        driver.get("https://prtr.moenv.gov.tw/deal.html")

        # 輸入統一編號
        search_box = driver.find_element(By.NAME, "UniformNo")
        search_box.send_keys(business_accounting_no)

        # 輸入日期區間
        start_date_box = driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[1]/div[3]/div/div/div[1]/input')
        end_date_box = driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[1]/div[3]/div/div/div[3]/input')
        start_date_box.send_keys(last_year_str)
        end_date_box.send_keys(today_str)

        # 查詢公示案件按鈕
        button = driver.find_element(By.CLASS_NAME, "search_submit")
        button.click()
        time.sleep(2)

        try:  # 檢查是否有數據
            no_data_div = driver.find_element(By.CLASS_NAME, 'no_data')
            text = no_data_div.text
        except:  # 有數據
            have_data = driver.find_element(By.CLASS_NAME, 'result_number')
            text = have_data.text
            if any(char.isdigit() for char in text):
                text = "有環境裁罰"

        # 插入數據到數據庫
        insert_query = "INSERT INTO py_prtr_input (NumberOfData) VALUES (%s);"
        cursor.execute(insert_query, (text,))
        conn.commit()

    except Exception as e:
        print("An error occurred: ", e)
        conn.rollback()

    finally:
        time.sleep(0.5)  # 等待一些時間，以便查看搜索結果
        driver.quit()
        cursor.close()
        conn.close()

#=========================================================================================
# 調用函數

# fetch_data_and_insert_to_py_prtr_input()

# fetch_and_clean_data()
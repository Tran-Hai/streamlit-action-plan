import pandas as pd
import json
import streamlit as st
import subprocess

@st.cache_data(show_spinner=False)
def crawl_data(start_date, end_date):
    res = subprocess.run(["node", "scripts/Crawler.js", start_date, end_date], capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        st.error("Error when crawling data")
        st.stop()
    return res.stdout



def process_data(data):
    data_json = json.loads(data)
    df = pd.DataFrame(data_json)

    columns_to_keep = [16, 2, 3, 5, 4, 24, 7, 22, 28]

    new_df = df.iloc[:, columns_to_keep]

    columns_names = ['Ngày dự kiến', 'Số báo cáo bảo dưỡng', 'Line', 'Mã máy', 'Tên máy', 'Nôi dung công việc', 'PP bảo dưỡng', 'Người thực hiện', 'Nội dung thực hiện']

    new_df.columns = columns_names

    reversed_df = new_df.iloc[::-1]

    reversed_df = reversed_df.reset_index(drop=True)

    reversed_df.index = reversed_df.index + 1

    for day in range(1,32):
        column_name = f'{day}'
        reversed_df[column_name] = ''

    return reversed_df
import calendar  # Core Python Module
from datetime import datetime  # Core Python Module
import pandas as pd

import streamlit as st  # pip install streamlit


# -------------- SETTINGS --------------
currency = "৳"
page_title = "Hasil App"
page_icon = ":money_with_wings:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown("""---""")

# Top Header
st.write("হাসিল আদায়ের রশিদ")
st.markdown("""---""")

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])
d = st.date_input("তারিখ")
year = d.year
month = d.month
day = d.day


def create_download_link(val, filename):
    b64 = base64.standard_b64decode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'


def update_hasil():
    st.session_state.hasil = str(st.session_state.amount * 0.05)

st.write('কি ধরণের পশু: ')
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    option_c = st.checkbox('গরু')
with col2:
    option_b = st.checkbox('মহিষ')
with col3:
    option_k = st.checkbox('খাসি')
with col4:
    option_g = st.checkbox('ছাগল')
with col5:
    option_s = st.checkbox('ভেড়া')
buyer_name = st.text_input("ক্রেতার নাম")
buyer_address = st.text_input("ক্রেতার ঠিকানা")
seller_name = st.text_input("বিক্রেতার নাম")
seller_address = st.text_input("বিক্রেতার ঠিকানা")
if 'hasil' not in st.session_state:
    st.session_state['hasil'] = 0
amount = st.number_input("মোট টাকা ",format='%0.0f',key='amount',on_change=update_hasil)
st.write("##### ৫ % হাসিলের টাকা: ")
st.code(st.session_state.hasil, language="markdown")
button = st.button("প্রিন্ট")

# if button:
#     pdf = FPDF()
#     pdf.add_font('BDFont','','C:/Users/user/Desktop/font/Nikosh.ttf',uni=True)
#     pdf.set_font('BDFont', '', 10)
#     pdf.add_page()
#     pdf.set_font('Arial', 'B', 16)
#     a = unicode(str("করিম").decode("UTF-8"))
#     pdf.cell (200, 10, '%s'%a, ln=1, align = "C")
#     pdf.output ("Bangla.pdf")
    # html = create_download_link(pdf.output(dest="S").encode("UTF-32"), "test")
    #st.markdown(html, unsafe_allow_html=True)



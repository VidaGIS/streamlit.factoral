import streamlit as st
import os

def load_users():
    if not os.path.exists("users.txt"):
        st.write("Chưa có người dùng nào. Hãy đăng ký để tạo tài khoản.")
        return []
    with open("users.txt", "r") as f:
        users = [line.strip() for line in f.readlines()]
    return users
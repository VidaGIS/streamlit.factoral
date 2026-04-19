import streamlit as st
from user import load_users

def login_page():
    st.title("Đăng nhập")
    username = st.text_input("Tên đăng nhập")

    if st.button("Đăng nhập"):
        if username:
            users = load_users()
            if username in users:
                st.session_state["username"] = username
                st.session_state["logged_in"] = True
                st.success(f"Đăng nhập thành công! Chào mừng {username}.")
                st.rerun()
            else:
                st.session_state["username"] = username
                st.session_state["logged_in"] = False
                st.session_state["show_greeting"] = True
                st.success(f"Chào mừng {username}! Bạn đã đăng nhập thành công nhưng chưa có tài khoản. Hãy đăng ký để tạo tài khoản.")
                st.rerun()
        else:
            st.error("Vui lòng nhập tên đăng nhập.")
        
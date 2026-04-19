import streamlit as st
from fact import factorial

def factorial_page():
    st.title("Tính giai thừa")

    st.write(f"Xin chào, {st.session_state.get('username', 'Khách')}!")
    if st.button("Đăng xuất"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = None
        st.session_state["show_greeting"] = False
        st.success("Bạn đã đăng xuất thành công.")
        st.rerun()

    st.divider()

    number = st.number_input("Nhập một số nguyên dương:", min_value=0, max_value=100, step=1)

    if st.button("Tính giai thừa"):
        try:
            result = factorial(number)
            st.write(f"Giai thừa của {number} là: {result}")
        except ValueError as e:
            st.error(str(e))

def greeting_page():
    st.title("Chào mừng bạn đến với ứng dụng tính giai thừa!")
    st.write(f"Xin chào, {st.session_state.get('username', 'Khách')}!")
    st.write("Bạn không có quyền truy cập vào ứng dụng này.")
    if st.button("Quay lại trang đăng nhập"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = None
        st.session_state["show_greeting"] = False
        st.rerun()

def main():
    if st.session_state.get("logged_in", False):
        factorial_page()
    elif st.session_state.get("show_greeting", False):
        greeting_page()
    else:
        from auth import login_page
        login_page()

if __name__ == "__main__":
    main()
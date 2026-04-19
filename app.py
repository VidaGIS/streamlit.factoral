import streamlit as st
from fact import factorial

def main():
    st.title("Tính giai thừa")
    number = st.number_input("Nhập một số nguyên dương:", min_value=0, max_value=100, step=1)

    if st.button("Tính giai thừa"):
        try:
            result = factorial(number)
            st.write(f"Giai thừa của {number} là: {result}")
        except ValueError as e:
            st.error(str(e))

if __name__ == "__main__":
    main()
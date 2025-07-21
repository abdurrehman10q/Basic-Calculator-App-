import streamlit as st 

st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGpGx-iqFkdUbnNGxGqqSAUg2qRHG4o4SK3g&s", width=150)
st.sidebar.title("Basic Calculator App")

a=int(st.number_input("Enter The First Number", step=0))
b=int(st.number_input("Enter The Second Number", step=0))

if st.button("Add"):
    st.success(a+b)

if st.button("Subtract"):
    st.success(a-b)

if st.button("Multiply"):
    st.success(a*b)

if st.button("Divide"):
    try:
        st.success(a/b)
    except ZeroDivisionError:
        if b==0:
            st.error("Zero Division Error!, Can't Be Divided By Zero, Please Enter The Non Zero Value")

if st.button("Modulus"):
    try:
        st.success(a%b)
    except ZeroDivisionError:
        if b==0:
            st.error("Zero Division Error!, Can't Be Divided By Zero, Please Enter The Non Zero Value")

if st.button("Floor Division"):
    try:
        st.success(a//b)
    except:
        if b==0:
            st.error("Zero Division Error!, Can't Be Divided By Zero, Please Enter The Non Zero Value")
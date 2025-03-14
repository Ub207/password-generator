import streamlit as st
st.title("Password generator")
st.header("My password generator")
st.subheader("Generate a password")
st.write("This is a simple password generator")
st.write("Enter the length of the password")
length = st.slider("Length of password", 1, 100, 10)
st.write(f"Your password will be {length} characters long")
st.write("Click below to generate the password")

if st.button("Generate password"):
    import random
    import string
    password = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    st.success(password)
    st.write("Your password has been generated")
    st.write("Keep it safe!")
    st.balloons()
    st.write("Enjoy your new password!")
    st.write("Remember, it's always a good idea to use a strong, unique password!")
    st.write("If you need to generate a new password, please click the 'Generate password' button again.")
    st.write("Thank you for using my password generator!")
    
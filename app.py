import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
st.subheader("WELCOME TO")
st.title("LUKE'S STARTER PY WEBPAGE!!")
st.write("Learning how to code using VS Code, This is a webpage to help you learn faster, Click the Learn more link")
st.write("[Learn More >](https://www.python.org/downloads/release/python-3105/)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")

    # Documention: https://formsubmit.co !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/MyEyesAreCode@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder= "Your Email" required>
     <textarea name="message" placeholder="Your Message Here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column: 
    st.empty()    
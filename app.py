import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
st.subheader("WELCOME TO")
st.title("LUKE'S STARTER py WEBPAGE!!")
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

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            - Hi My Name is Luke Kalke and I just started to learn python, so this is a starter webpage that with streamlit
            - Extra test text qwertyuiopasdfghjklzxcvbnmzxcvbnmasdfghjklqwertyuiopqwertyuiopasdfghjklzxcvbnmqwertyuiop
            -qwertyuiopaqwsedrftgyhujikolpzasxdcfvgbhnjmkaqwsedrftgyhujikolpaqwsedrftgyhujikolpawsedrftgyhujikolp
            -aqwsedrftgyhujikolpqawsedrftgyhujikoqawsedrftghujkopazsxdcfgyhujwxscedrvftgyhujaxwscedrvftbgynhumji,maqxswcedrvfbtgynhumj
            -qzwxecdrvftbynumaqzwsxecdrfvtgbyhnuazwexscdrftvgybhnuzsexdcrfvgbhnxsdcfvgbhasdfghjwertyuizxcvbnwertyusdfghjcvbnertyu
            """
        )
        st.write("[Apple Website >](https://www.apple.com)")
        /* CSS Snippet from W3schools: https://www.w3schools.com/howto/howto_css_contact_form.asp */
 /* Style inputs with type="text", select elements and textareas */
 input[type=message], input[type=email], input[type=text], textarea {
   width: 100%; /* Full width */
   padding: 12px; /* Some padding */ 
   border: 1px solid #ccc; /* Gray border */
   border-radius: 4px; /* Rounded borders */
   box-sizing: border-box; /* Make sure that padding and width stays in place */
   margin-top: 6px; /* Add a top margin */
   margin-bottom: 16px; /* Bottom margin */
   resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
 }

 /* Style the submit button with a specific background color etc */
 button[type=submit] {
   background-color: #04AA6D;
   color: white;
   padding: 12px 20px;
   border: none;
   border-radius: 4px;
   cursor: pointer;
 }

 /* When moving the mouse over the submit button, add a darker green color */
 button[type=submit]:hover {
   background-color: #45a049;
 }


 /* Hide Streamlit Branding */
 #MainMenu {visibility: hidden;}
 footer {visibility: hidden;}
 header {visibility: hidden;}
 
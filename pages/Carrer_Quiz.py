import streamlit as st
#stuff don't touch
st.set_page_config(page_title="Quiz", layout="wide")

st.markdown("""
    <style>
        header[data-testid="stHeader"] { display: none !important; }
        .block-container { padding-top: 0rem !important; }
        [data-testid="stSidebar"] { display: none !important; }
        .nav {
            display: flex;
            gap: 40px;
            background-color: #FFFFFF;
            padding: 15px 30px;
            margin-bottom: 30px;
        }
        .nav a {
            color: black;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
        }
        .nav a:hover { text-decoration: underline; }
    </style>
    <div class="nav">
        <a href="/" target="_self"> Home Page </a>
        <a href="/About_Creators" target="_self"> About the Creator </a>
        <a href="/Carrer_Quiz" target="_self"> Career Quiz </a>
    </div>
""", unsafe_allow_html=True)






#QUIZ STARTS HERE!!
st.title("Carrer Quiz")

# Question 1
st.header("Question 1")
q1 = st.radio("What colour is the sky?",
    ["Red", "Blue", "Green", "Yellow"])

# Question 2
st.header("Question 2")
q2 = st.radio("How many days in a week?",
    ["5", "6", "7", "8"])

# Question 3
st.header("Question 3")
q3 = st.radio("What language is this app built in?",
    ["JavaScript", "Java", "Python", "C++"])

# Submit all answers at once
if st.button("Submit Quiz! 🎯"):
    score = 0
    
    if q1 == "Blue":
        score += 1
    if q2 == "7":
        score += 1
    if q3 == "Python":
        score += 1
    
    st.header(f"You scored {score}/3!")
    
    if score == 3:
        st.success("🎉 Perfect score!")
        st.balloons()
    elif score == 2:
        st.success("😊 Great job!")
    elif score == 1:
        st.warning("😅 Keep practicing!")
    else:
        st.error("😬 Better luck next time!")
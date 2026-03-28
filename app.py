import streamlit as st

# --- PAGE NAVIGATION ---
st.set_page_config(page_title="Hackathon Website", layout="wide")
pages = ["Home", "Career Quiz", "Writing on the Wall", "Creators"]
page = st.sidebar.radio("Navigate", pages)

# --- HOME PAGE ---
if page == "Home":
    st.title("Welcome to our Hackathon Website!")
    st.markdown("""
    High schoolers are pressured into university or nothing thinking before they even know who they are. This leads to anxiety, debt, and misguided life choices.
Open Door helps them discover a direction that fits the life they actually want, not just the path everyone expects.

    """)
 ####bottom of home apge  
    st.markdown("**External Resources:**")
    st.markdown("""
    - [Support Helpline](#)
    - [Inspiring Films/Art](#)
    - [Social Media Communities](#)
    """)

# --- CAREER QUIZ PAGE ---
elif page == "Career Quiz":
    st.title("Career Quiz")
    st.markdown("Answer the questions to get suggestions that match your interests!")

   #Question 1
    q1 = st.radio(
        "If you had a free day right now, what would you do first?",
        ("Failing and looking incompetent", "Not knowing where to start", "That it might be boring or repetitive", "It will be physically demanding", "Feeling socially awkward or judged", "Making a mistake that affects others")
                )
   
   #Question 16
    q1 = st.radio(
        "What scares you most about trying something new?",
        ("Failing and looking incompetent", "Not knowing where to start", "That it might be boring or repetitive", "It will be physically demanding", "Feeling socially awkward or judged", "Making a mistake that affects others")
                )
    
    
    


    # Example scoring logic
    if st.button("See suggestion"):
        if q1 == "Call or spend time with someone you love":
            st.success("Suggested paths: Health Care, Education, Accommodation & Food Services")
        elif q1 == "Clean / organize your space":
            st.success("Suggested paths: Administrative & Support, Real Estate & Rental, Utilities")
        elif q1 == "Learn a new hobby or skill":
            st.success("Suggested paths: Arts, Entertainment & Recreation, Professional Services, Information & Cultural")
        else:
            st.success("Suggested paths: Public Administration, Utilities")

# --- WRITING ON THE WALL PAGE ---
elif page == "Writing on the Wall":
    st.title("Writing on the Wall")
    st.markdown("Leave anonymous messages for other students. Messages are moderated for language.")

    # Input new message
    new_message = st.text_area("Write your message here:")
    if st.button("Post Message"):
        if any(bad_word in new_message.lower() for bad_word in ["badword1", "badword2"]):  # simple moderation
            st.error("Message contains inappropriate language.")
        else:
            st.success("Message posted!")
            # For now, we'll just show it on the page (in memory)
            if "messages" not in st.session_state:
                st.session_state.messages = []
            st.session_state.messages.append(new_message)

    # Display messages
    if "messages" in st.session_state:
        st.markdown("**Previous Messages:**")
        for msg in st.session_state.messages:
            st.markdown(f"- {msg}")

# --- CREATORS PAGE ---
elif page == "Creators":
    st.title("Meet the Team")
    st.markdown("""
    - **Mikaela** – Idea & Python wizard
    - **Davin** – Frontend & Content
    - **Joshua** – Backend support (if they show up)
    
    This team built this website to give students a reflective, interactive space to explore life choices.
    """)
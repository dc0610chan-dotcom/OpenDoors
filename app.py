import streamlit as st

# --- PAGE NAVIGATION ---
st.set_page_config(page_title="Hackathon Website", layout="wide")
pages = ["Home", "Career Quiz", "Writing on the Wall", "Creators"]
page = st.sidebar.radio("Navigate", pages)

# --- HOME PAGE ---
if page == "Home":
    st.title("Welcome to DJM's Hackathon Website!")
    st.markdown("""
    High schoolers are pressured into university or nothing thinking before they even know who they are. This leads to anxiety, debt, and misguided life choices.
Open Door helps them discover a direction that fits the life they actually want, not just the path everyone expects.
    """)
 ####bottom of home page  
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
# question 1 - 20 not including personality
# --- Initialize scores for all NAICS industries ---
    if "scores" not in st.session_state:
        st.session_state.scores = {
            "Agriculture, Forestry, Fishing and Hunting": 0, #then you also get Mining Quarrying and Oil and Gas Extraction
            "Utilities": 0,
            "Construction": 0,
            "Manufacturing": 0,
            "Retail Trade": 0, #then you also get Wholesale Trade
            "Transportation and Warehousing": 0,
            "Information and Cultural Industries": 0,
            "Finance and Insurance": 0,
            "Real Estate and Rental and Leasing": 0,
            "Professional, Scientific and Technical Services": 0,
            "Management of Companies and Enterprises": 0,
            "Administrative and Support, Waste Management and Remediation Services": 0,
            "Educational Services": 0,
            "Health Care and Social Assistance": 0,
            "Arts, Entertainment and Recreation": 0,
            "Accommodation and Food services": 0,
            "Public Administration Services": 0,
            "Other Services (excluding Public Administration)": 0,  
        }
    #urban dictionary type shit
    scores = st.session_state.scores

    agri = "Agriculture, Forestry, Fishing and Hunting"
    uti = "Utilities"
    const = "Construction"
    manu = "Manufacturing"
    retail = "Retail Trade"
    trans = "Transportation and Warehousing"
    infoind = "Information and Cultural Industries"
    finance = "Finance and Insurance"
    real_estate = "Real Estate and Rental and Leasing"
    professional = "Professional, Scientific and Technical Services"
    management = "Management of Companies and Enterprises"
    admin = "Administrative and Support, Waste Management and Remediation Services"
    education = "Educational Services"
    health = "Health Care and Social Assistance"
    arts = "Arts, Entertainment and Recreation"
    food = "Accommodation and Food Services"
    public = "Public Administration Servi"
    other = "Other Services (excluding Public Administration)"

    #Question 1
    q1 = st.radio(
        "If you had a free day right now, what would you do first?",
        ("Call or spend time with someone you love", "Clean / organize your space",
        "Take a nap / relax", "Watch your favorite show or media", "Explore your town / go outside" )
                )
        
    #Question 2
    q2 = st.radio(
        "What are your 3 favorite hobbies?",
        ("Creating art, music, or writing", "Playing or watching sports", "Volunteering / helping others",
        "Gaming, coding, or digital projects", "Building, fixing, or crafting", "Exploring nature / outdoor activities" )
                )

    #Question 3
    q3 = st.radio( 
        "What kind of hobby really excites you", 
        ("Making something with your hands (crafts, building, cooking)", "Expressing yourself creatively (music, writing, art)",
        "Playing or watching sports / staying active", "Solving puzzles or learning new concepts", "Spending time with friends / social activities",
        "Being outdoors / exploring nature")
                ) 
    #Question 4
    q4 = st.radio(
        " How do you usually spend your evenings?",
        ("Watching shows or movies", "Reading or learning something new", "Hanging out with friends", "Doing hands-on projects (crafts, cooking, building)",
        "Planning / organizing your week", "Relaxing in nature / exercising")
                )

        #Question 5
    q5 = st.radio(
        "Which of these sounds like your ideal weekend?", 
        ("Attending a concert, art exhibit, or performance", "Hosting or attending a dinner / party", "Working on a personal project or hobby",
        "Going on a short trip or exploring your town", "Volunteering or helping a local cause", "Staying in and relaxing")
                )
        
    #Question 6
    q6 = st.radio(
        "What’s your ideal work setting?", 
        ("A busy office with clear tasks and schedules", "A creative studio or workshop", "Outdoors or in nature", "Flexible coworking spaces / cafes / changing environments", 
        "A calm, quiet room with minimal interruptions", "High-energy, social, hands-on environment")
                )
        
    #Question 7 
    q7 = st.radio(
        "What is your approach to tasks?", 
        ("Follow a clear step-by-step plan", "Work independently and creatively", "Collaborate and brainstorm with others", "Jump in and figure things out as you go", 
        "Focus on precision and details", "Focus on people’s needs and feelings")
                )
        
        #Question 8
    q8 = st.radio(
        "What is your preferred pace of work?",
        ("Fast, dynamic, and changing constantly", "Steady but challenging", "Slow, deliberate, and structured", "Flexible, adaptable depending on the day", "Energetic and social", 
        "Calm and focused")
                )
        
        #Question 9
    q9 = st.radio(
        "What is your preferred level of supervision?", 
        ("Completely independently", "Mostly independently, occasional check-ins", "In a team with shared responsibility", "With clear instructions and supervision", 
        "Rotating between teamwork and solo work", "Being guided by a mentor or leader")
                )
        
        #Question 10
    q10 = st.radio(
        "When do you do your best work?", 
        ("Early in the morning, when everything is calm", "Late at night, when I'm inspired", "In short bursts with lots of variety", "When I’m actively moving or hands-on", 
        "When collaborating with others", "When I can experiment and try new ideas")
                )
        
    #Question 11
    q11 = st.radio(
        "How do you usually recharge after a busy day?", 
        ("Spending time with close friends or family", "Being alone reading, gaming, or watching media", "Going for a walk or doing something active", "Trying a new hobby or exploring something new", 
        "Volunteering or helping someone", "Organizing or planning your space")
                )
        
    #Question 12
    q12 = st.radio(
        "In a social gathering, which describes you best?", 
        ("I thrive in large groups and enjoy meeting new people", "I prefer small groups of close friends", "I like being around people but also need breaks alone",
        "I mostly observe rather than actively participate", "I avoid social gatherings whenever possible", "I adapt easily to any size or type of group")
                )
        
        #Queston 13
    q13 = st.radio(
        "How do you handle energy demands during a busy week?", 
        ("I’m energized by activity and social interaction", "I manage energy with planned breaks", "I focus best when calm and consistent", "I like alternating high-energy bursts with downtime", 
        "I prefer low-energy, predictable routines", "I adapt my energy to whatever the day demands")
                )
        
        #Question 14
    q14 = st.radio(
        "When exploring new experiences, which sounds most like you?", 
        ("I dive in headfirst and love variety", "I prefer to try a few new things at a time", "I stick to what I know", "I plan new experiences carefully before doing them", 
        "I like spontaneous adventures but also enjoy downtime", "I mostly observe new experiences rather than participate")
                )
        
        #Question 15
    q15 = st.radio(
        "When faced with a new challenge, what's your first instinct?", 
        ("Analyze the data and look for patterns", "Brainstorm creative solutions, even unusual ones", "Ask others for input and collaborate", 
        "Tackle it hands-on and learn by doing", "Follow step-by-step instructions carefully", "Take time to observe and reflect before acting")
                )

    #Question 16
    q16 = st.radio(
        "What scares you most about trying something new?",
        ("Failing and looking incompetent", "Not knowing where to start", "That it might be boring or repetitive", "It will be physically demanding", 
        "Feeling socially awkward or judged", "Making a mistake that affects others")
                )
        
        #Question 17
    q17 = st.radio(
        "What excites you most about trying something new?", 
        ("Solving a problem or overcoming a challenge", "Learning something new and expanding skills", "Being creative and trying something original", 
        "Meeting or working with new people", "Getting hands-on experience", "Exploring the unknown or unexpected") 
                )
        
        #Question 18
    q18 = st.radio(
        "Which of these motivates you most in your career?", 
        ("Making a positive difference in other people's lives", "Achieving financial success", "Gaining recognition or fame", 
        "Creating stability for yourself and loved ones", "Exploring new ideas and creative possibilities", "Building a family or close personal relationships alongside work")
                    )

        #Question 19
    q19 = st.radio(
        "Which of these outcomes would make you feel most fulfilled?", 
        ("Helping or mentoring others", "Earning wealth or material success", "Becoming well-known or influential", "Feeling secure and stable in your life", 
        "Making something new, original, or impactful", "Building strong relationships or a family")
                )

        #Question 20
    q20 = st.radio(
        "Which role sounds most appealing to you?", 
        ("Leading a team, making big decisions, and being responsible for overall success", "Creating ideas, content, or experiences that others engage with", 
        "Helping, supporting, or guiding people in meaningful ways", "Building, fixing, or working with physical systems and environments", 
        "Organizing operations, keeping things running smoothly, and handling logistics", "Working independently, taking risks, or pursuing opportunities for personal gain")
                )

    ###idk what magnum opus means but this is mine####

    for i in range(1, 21):
        if f"q{i}_answered" not in st.session_state:
            st.session_state[f"q{i}_answered"] = False
            st.session_state.answered = 0

        if not st.session_state.q1_answered:
            if st.button("Submit Question 1"):
                if q1 == "Call or spend time with someone you love":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[food] += 1
                elif q1 == "Clean / organize your space":
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[uti] += 1
                elif q1 == "Learn a new hobby or skill":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[const] += 1
                    st.session_state.scores[uti] += 1
                elif q1 == "Take a nap / relax":
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[public] += 1
                    st.session_state.scores[other] += 1
                elif q1 == "Watch your favorite show or media":
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[education] += 1
                else: #Explore your town / go outside
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[agri] += 1
                    st.session_state.scores[arts] += 1
                st.session_state.q1_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q2_answered:
            if st.button("Submit Question 2"):
                if q2 == "Creating art, music, or writing":
                    st.session_state.scores[education] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[food] += 1
                elif q2 == "Playing or watching sports":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[food] += 1
                    st.session_state.scores[health] += 1
                elif q2 == "Volunteering / helping others":
                    st.session_state.scores[public] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[health] += 1
                elif q2 == "Gaming, coding, or digital projects":
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[arts] += 1
                elif q2 == "Building, fixing, or crafting":
                    st.session_state.scores[manu] += 1
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[const] += 1
                else: #Exploring nature / outdoor activities
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[agri] += 1
                    st.session_state.scores[arts] += 1
                st.session_state.q2_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q3_answered:
            if st.button("Submit Question 3"):
                if q3 == "Making something with your hands (crafts, building, cooking)":
                    st.session_state.scores[manu] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[const] += 1
                elif q3 == "Expressing yourself creatively (music, writing, art)":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                elif q3 == "Playing or watching sports / staying active":
                    st.session_state.scores[food] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[health] += 1
                elif q3 == "Solving puzzles or learning new concepts":
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[education] += 1
                elif q3 == "Spending time with friends / social activities":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[food] += 1
                else: #Being outdoors / exploring nature
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[agri] += 1
                    st.session_state.scores[arts] += 1
                st.session_state.q3_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q4_answered:
            if st.button("Submit Question 4"):
                if q4 == "Watching shows or movies":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                elif q4 == "Expressing yourself creatively (music, writing, art)":
                    st.session_state.scores[education] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[professional] += 1
                elif q4 == "Hanging out with friends":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[food] += 1
                elif q4 == "Doing hands-on projects (crafts, cooking, building)":
                    st.session_state.scores[manu] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[const] += 1
                elif q4 == "Planning / organizing your week":
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[public] += 1
                    st.session_state.scores[management] += 1
                else: #Relaxing in nature / exercising
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[agri] += 1
                    st.session_state.scores[food] += 1
                st.session_state.q4_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q5_answered:
            if st.button("Submit Question 5"):
                if q5 == "Attending a concert, art exhibit, or performance":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                elif q5 == "Hosting or attending a dinner / party":
                    st.session_state.scores[food] += 1
                    st.session_state.scores[health] += 1
                    st.session_state.scores[management] += 1
                elif q5 == "Working on a personal project or hobby":
                    st.session_state.scores[management] += 1
                    st.session_state.scores[manu] += 1
                    st.session_state.scores[arts] += 1
                elif q5 == "Going on a short trip or exploring your town":
                    st.session_state.scores[agri] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[trans] += 1
                elif q5 == "Volunteering or helping a local cause":
                    st.session_state.scores[public] += 1
                    st.session_state.scores[health] += 1
                    st.session_state.scores[education] += 1
                else: #Staying in and relaxing
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[public] += 1
                    st.session_state.scores[other] += 1
                st.session_state.q5_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q6_answered:
            if st.button("Submit Question 6"):
                if q6 == "A busy office with clear tasks and schedules":
                    st.session_state.scores[finance] += 1
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[public] += 1
                elif q6 == "A creative studio or workshop":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[manu] += 1
                elif q6 == "Outdoors or in nature":
                    st.session_state.scores[agri] += 1
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[const] += 1
                elif q6 == "Flexible coworking spaces / cafes / changing environments":
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[food] += 1
                    st.session_state.scores[professional] += 1
                elif q6 == "A calm, quiet room with minimal interruptions":
                    st.session_state.scores[education] += 1
                    st.session_state.scores[health] += 1
                    st.session_state.scores[uti] += 1
                else: #High-energy, social, hands-on environment
                    st.session_state.scores[food] += 1
                    st.session_state.scores[health] += 1
                    st.session_state.scores[retail] += 1
                st.session_state.q6_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q7_answered:
            if st.button("Submit Question 7"):
                if q7 == "Follow a clear step-by-step plan":
                    st.session_state.scores[const] += 1
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[manu] += 1
                elif q7 == "Work independently and creatively":
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[arts] += 1
                elif q7 == "Collaborate and brainstorm with others":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[food] += 1
                elif q7 == "Jump in and figure things out as you go":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[retail] += 1
                elif q7 == "Focus on precision and details":
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[finance] += 1
                else: #Focus on people’s needs and feelings
                    st.session_state.scores[other] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[health] += 1
                st.session_state.q7_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q8_answered:
            if st.button("Submit Question 8"):
                if q8 == "Fast, dynamic, and changing constantly":
                    st.session_state.scores[management] += 1
                    st.session_state.scores[retail] += 1
                    st.session_state.scores[arts] += 1
                elif q8 == "Steady but challenging":
                    st.session_state.scores[education] += 1
                    st.session_state.scores[health] += 1
                    st.session_state.scores[const] += 1
                elif q8 == "Slow, deliberate, and structured":
                    st.session_state.scores[finance] += 1
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[admin] += 1
                elif q8 == "Flexible, adaptable depending on the day":
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[infoind] += 1
                elif q8 == "Energetic and social":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[retail] += 1
                    st.session_state.scores[food] += 1
                else: #Calm and focused
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[public] += 1
                    st.session_state.scores[education] += 1
                st.session_state.q8_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q9_answered:
            if st.button("Submit Question 9"):
                if q9 == "Completely independently":
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[professional] += 1
                elif q9 == "Mostly independently, occasional check-ins":
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[management] += 1
                    st.session_state.scores[finance] += 1
                elif q9 == "In a team with shared responsibility":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[food] += 1
                    st.session_state.scores[education] += 1
                elif q9 == "With clear instructions and supervision":
                    st.session_state.scores[const] += 1
                    st.session_state.scores[manu] += 1
                    st.session_state.scores[uti] += 1
                elif q9 == "Rotating between teamwork and solo work":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[retail] += 1
                    st.session_state.scores[trans] += 1
                else: #Being guided by a mentor or leader
                    st.session_state.scores[education] += 1
                    st.session_state.scores[health] += 1
                    st.session_state.scores[public] += 1
                st.session_state.q9_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q10_answered:
            if st.button("Submit Question 10"):
                if q10 == "Early in the morning, when everything is calm":
                    st.session_state.scores[education] += 1
                    st.session_state.scores[finance] += 1
                    st.session_state.scores[uti] += 1
                elif q10 == "Late at night, when I’m inspired":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[professional] += 1
                elif q10 == "In short bursts with lots of variety":
                    st.session_state.scores[food] += 1
                    st.session_state.scores[retail] += 1
                    st.session_state.scores[trans] += 1
                elif q10 == "When I’m actively moving or hands-on":
                    st.session_state.scores[const] += 1
                    st.session_state.scores[agri] += 1
                    st.session_state.scores[manu] += 1
                elif q10 == "When collaborating with others":
                    st.session_state.scores[education] += 1
                    st.session_state.scores[health] += 1
                    st.session_state.scores[food] += 1
                else: #When I can experiment and try new ideas
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[infoind] += 1
                st.session_state.q10_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q11_answered:
            if st.button("Submit Question 11"):
                if q11 == "Spending time with close friends or family":
                    st.session_state.scores[education] += 1
                    st.session_state.scores[health] += 1
                    st.session_state.scores[food] += 1
                elif q11 == "Being alone reading, gaming, or watching media":
                    st.session_state.scores[public] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[professional] += 1
                elif q11 == "Going for a walk or doing something active":
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[agri] += 1
                    st.session_state.scores[arts] += 1
                elif q11 == "Trying a new hobby or exploring something new":
                    st.session_state.scores[food] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[arts] += 1
                elif q11 == "Volunteering or helping someone":
                    st.session_state.scores[education] += 1
                    st.session_state.scores[health] += 1
                    st.session_state.scores[other] += 1
                else: #Organizing or planning your space 
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[manu] += 1
                st.session_state.q11_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q12_answered:
            if st.button("Submit Question 12"):
                if q12 == "I thrive in large groups and enjoy meeting new people":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[food] += 1
                elif q12 == "I prefer small groups of close friends":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[professional] += 1
                elif q12 == "I like being around people but also need breaks alone":
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[arts] += 1
                elif q12 == "I mostly observe rather than actively participate":
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[admin] += 1
                elif q12 == "I avoid social gatherings whenever possible":
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[other] += 1
                else: #I adapt easily to any size or type of group
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[food] += 1
                st.session_state.q12_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q13_answered:
            if st.button("Submit Question 13"):
                if q13 == "I’m energized by activity and social interaction":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[retail] += 1
                    st.session_state.scores[food] += 1
                elif q13 == "I manage energy with planned breaks":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[professional] += 1
                elif q13 == "I focus best when calm and consistent":
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[public] += 1
                    st.session_state.scores[finance] += 1
                elif q13 == "I like alternating high-energy bursts with downtime":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[food] += 1
                elif q13 == "I prefer low-energy, predictable routines":
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[manu] += 1
                else: #I adapt my energy to whatever the day demands
                    st.session_state.scores[const] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[trans] += 1
                st.session_state.q13_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q14_answered:
            if st.button("Submit Question 14"):
                if q14 == "I dive in headfirst and love variety":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[food] += 1
                elif q14 == "I prefer to try a few new things at a time":
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[professional] += 1
                elif q14 == "I stick to what I know":
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[public] += 1
                    st.session_state.scores[admin] += 1
                elif q14 == "I plan new experiences carefully before doing them":
                    st.session_state.scores[retail] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[finance] += 1
                elif q14 == "I like spontaneous adventures but also enjoy downtime":
                    st.session_state.scores[retail] += 1
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[arts] += 1
                else: #I mostly observe new experiences rather than participate
                    st.session_state.scores[health] += 1
                    st.session_state.scores[other] += 1
                    st.session_state.scores[education] += 1
                st.session_state.q14_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q15_answered:
            if st.button("Submit Question 15"):
                if q15 == "Analyze the data and look for patterns":
                    st.session_state.scores[finance] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[infoind] += 1
                elif q15 == "Brainstorm creative solutions, even unusual ones":
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[professional] += 1
                elif q15 == "Ask others for input and collaborate":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[food] += 1
                    st.session_state.scores[education] += 1
                elif q15 == "Tackle it hands-on and learn by doing":
                    st.session_state.scores[uti] += 1
                    st.session_state.scores[const] += 1
                    st.session_state.scores[manu] += 1
                elif q15 == "Follow step-by-step instructions carefully":
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[public] += 1
                    st.session_state.scores[admin] += 1
                else: #Take time to observe and reflect before acting 
                    st.session_state.scores[health] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[education] += 1
                st.session_state.q15_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q16_answered:
            if st.button("Submit Question 16"):
                if q16 == "Failing and looking incompetent":
                    st.session_state.scores[finance] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[public] += 1
                elif q16 == "Not knowing where to start":
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[health] += 1
                elif q16 == "That it might be boring or repetitive":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[food] += 1
                elif q16 == "It will be physically demanding":
                    st.session_state.scores[trans] += 1
                    st.session_state.scores[const] += 1
                    st.session_state.scores[manu] += 1
                elif q16 == "Feeling socially awkward or judged":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[food] += 1
                else: #Making a mistake that affects others 
                    st.session_state.scores[health] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[education] += 1
                st.session_state.q16_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()   

        if not st.session_state.q17_answered:
            if st.button("Submit Question 17"):
                if q17 == "Solving a problem or overcoming a challenge":
                    st.session_state.scores[finance] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[uti] += 1
                elif q17 == "Learning something new and expanding skills":
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[professional] += 1
                elif q17 == "Being creative and trying something original":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[professional] += 1
                elif q17 == "Meeting or working with new people":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[food] += 1
                elif q17 == "Getting hands-on experience":
                    st.session_state.scores[manu] += 1
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[const] += 1
                else: #Exploring the unknown or unexpected 
                    st.session_state.scores[health] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[education] += 1
                st.session_state.q17_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q18_answered:
            if st.button("Submit Question 18"):
                if q18 == "Making a positive difference in other people’s lives":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[food] += 1
                elif q18 == "Achieving financial success":
                    st.session_state.scores[finance] += 1
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[management] += 1
                elif q18 == "Gaining recognition or fame":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[management] += 1
                elif q18 == "Creating stability for yourself and loved ones":
                    st.session_state.scores[public] += 1
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[uti] += 1
                elif q18 == "Exploring new ideas and creative possibilities":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[professional] += 1
                else: #Building a family or close personal relationships alongside work 
                    st.session_state.scores[health] += 1
                    st.session_state.scores[food] += 1
                    st.session_state.scores[education] += 1
                st.session_state.q18_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q19_answered:
            if st.button("Submit Question 19"):
                if q19 == "Helping or mentoring others":
                    st.session_state.scores[health] += 1
                    st.session_state.scores[education] += 1
                    st.session_state.scores[food] += 1
                elif q19 == "Earning wealth or material success":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[finance] += 1
                    st.session_state.scores[professional] += 1
                elif q19 == "Becoming well-known or influential":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[management] += 1
                elif q19 == "Feeling secure and stable in your life":
                    st.session_state.scores[public] += 1
                    st.session_state.scores[admin] += 1
                    st.session_state.scores[uti] += 1
                elif q19 == "Making something new, original, or impactful":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[professional] += 1
                else: #Building strong relationships or a family
                    st.session_state.scores[health] += 1
                    st.session_state.scores[food] += 1
                    st.session_state.scores[education] += 1
                st.session_state.q19_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()

        if not st.session_state.q20_answered:
            if st.button("Submit Question 20"):
                if q20 == "Leading a team, making big decisions, and being responsible for overall success":
                    st.session_state.scores[finance] += 1
                    st.session_state.scores[management] += 1
                    st.session_state.scores[admin] += 1
                elif q20 == "Creating ideas, content, or experiences that others engage with":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[food] += 1
                elif q20 == "Helping, supporting, or guiding people in meaningful ways":
                    st.session_state.scores[arts] += 1
                    st.session_state.scores[infoind] += 1
                    st.session_state.scores[management] += 1
                elif q20 == "Building, fixing, or working with physical systems and environments":
                    st.session_state.scores[const] += 1
                    st.session_state.scores[manu] += 1
                    st.session_state.scores[uti] += 1
                elif q20 == "Organizing operations, keeping things running smoothly, and handling logistics":
                    st.session_state.scores[management] += 1
                    st.session_state.scores[retail] += 1
                    st.session_state.scores[admin] += 1
                else: #Working independently, taking risks, or pursuing opportunities for personal gain
                    st.session_state.scores[real_estate] += 1
                    st.session_state.scores[professional] += 1
                    st.session_state.scores[agri] += 1
                st.session_state.q20_answered = True
                st.session_state.answered += 1
                st.experimental_rerun()






        if st.session_state.answered == 20:
            if st.button("See Suggestions"):
                top1_name, top1_value = None, -1
                top2_name, top2_value = None, -1
                top3_name, top3_value = None, -1

    # Loop through all NAICS scores
    for name, value in naics_scores.items():
        if value > top1_value:
            # shift top1 -> top2, top2 -> top3
            top3_name, top3_value = top2_name, top2_value
            top2_name, top2_value = top1_name, top1_value
            top1_name, top1_value = name, value
        elif value > top2_value:
            # shift top2 -> top3
            top3_name, top3_value = top2_name, top2_value
            top2_name, top2_value = name, value
        elif value > top3_value:
            top3_name, top3_value = name, value

    # Show the results
    st.success("Your Top 3 Suggested NAICS Paths:")
    st.write(f"1. {top1_name} (Score: {top1_value})")
    st.write(f"2. {top2_name} (Score: {top2_value})")
    st.write(f"3. {top3_name} (Score: {top3_value})")












    #writing anonymous messages page










    st.title("Writing on the Wall")
    st.markdown("Leave anonymous messages for other students. Messages are moderated for language.")

    # Input new message
    new_message = st.text_area("Write your message here:")
    if st.button("Post Message"):
        if any(bad_word in new_message.lower() for bad_word in ["bitch", "fuck", "shit", "dick", "ass", "cunt", "pussy",]):  # simple moderation
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
        - **Mikaela** – Stuff (Year 1 Computer Science Student)
        - **Davin** – Hi there. My name is Davin, I was originally studying Business administration, now switching over to computer science at Wilfrid University. After discovering what I enjoy and see a future of me doing it in my future, I decided to change, this all happened after i got into university. This is why we created “X”, because high schools like me didn't know what they should go into in post secondary. This tool helps students discover what career they should go into based on interest before committing and spending a lot of money going to university. 
        - **Joshua** – Other stuff (Year 1 Computer Science Student)
        
        This team built this website to give students a reflective, interactive space to explore life choices.
        """)
    
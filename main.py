import streamlit as st
import random
import datetime

# Set up the page configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="https://img.icons8.com/?size=100&id=RJWKiqOoN0dc&format=png&color=000000")

# Title and Author Information
st.title("Growth Mindset Challenge Web App")
st.markdown("#### Created by **Ayaz Ahmed**")

# Sidebar Navigation Menu
menu = st.sidebar.radio("Navigation", ["Home", "Inspirations", "Daily Reflection", "Goal Tracker"])

# List of inspirational quotes
quotes = [
    "The only way to achieve the impossible is to believe it is possible.",
    "Mistakes are proof that you are trying.",
    "Don't watch the clock; do what it does. Keep going.",
    "Believe you can and you're halfway there.",
    "Every day is a new beginning. Take a deep breath, smile, and start again."
]

# HOME PAGE
if menu == "Home":
    st.header("Welcome to the Growth Mindset Challenge!")
    st.write(
        "Embrace challenges, learn from mistakes, and celebrate your progress. "
        "This app is designed to help you foster a growth mindset by providing daily inspiration, "
        "reflection tools, and a goal tracking system."
    )
    st.image(
        "https://marketplace.canva.com/EAFYC8yWXio/1/0/1600w/canva-green-minimalist-landscape-quote-desktop-wallpaper-OuM9mjCoT60.jpg",
        caption="Embrace Growth",
        use_column_width=True,
    )

# INSPIRATIONS PAGE
elif menu == "Inspirations":
    st.header("Inspirational Quotes")
    st.write("Here are some motivational quotes to boost your growth mindset:")
    # Display a daily random quote
    daily_quote = random.choice(quotes)
    st.info(f"**Daily Inspiration:** {daily_quote}")
    st.write("More quotes to keep you motivated:")
    for q in quotes:
        st.write(f"- {q}")

# DAILY REFLECTION PAGE
elif menu == "Daily Reflection":
    st.header("Daily Reflection")
    st.write("Take a moment to reflect on your day. What did you learn? What challenges did you overcome?")
    
    # Reflection input: date and text
    reflection_date = st.date_input("Select Date", datetime.date.today())
    reflection_text = st.text_area("Your Reflection", "Write your thoughts here...", height=150)
    
    # Save reflection on button click
    if st.button("Save Reflection"):
        if "reflections" not in st.session_state:
            st.session_state["reflections"] = []
        st.session_state["reflections"].append({"date": reflection_date, "reflection": reflection_text})
        st.success("Your reflection has been saved!")
    
    # Display past reflections
    if "reflections" in st.session_state and st.session_state["reflections"]:
        st.subheader("Past Reflections")
        for idx, ref in enumerate(st.session_state["reflections"]):
            st.markdown(f"**{idx + 1}. {ref['date'].strftime('%Y-%m-%d')}**")
            st.write(ref["reflection"])
            st.markdown("---")

# GOAL TRACKER PAGE
elif menu == "Goal Tracker":
    st.header("Goal Tracker")
    st.write("Set your learning goals and track your progress as you work to develop a growth mindset.")
    
    # Input for new goal
    goal_text = st.text_input("Enter a new goal")
    if st.button("Add Goal"):
        if "goals" not in st.session_state:
            st.session_state["goals"] = []
        st.session_state["goals"].append({"goal": goal_text, "completed": False})
        st.success("Goal added!")
    
    # Display goals and allow marking them as completed
    if "goals" in st.session_state and st.session_state["goals"]:
        st.subheader("Your Goals")
        for idx, goal in enumerate(st.session_state["goals"]):
            col1, col2 = st.columns([8, 2])
            with col1:
                st.write(f"**Goal {idx + 1}:** {goal['goal']}")
            with col2:
                if not goal["completed"]:
                    if st.button("Mark as Completed", key=f"complete_{idx}"):
                        st.session_state["goals"][idx]["completed"] = True
                        st.success("Goal marked as completed!")
                else:
                    st.write("✅ Completed")

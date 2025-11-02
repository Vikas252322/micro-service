import streamlit as st
import random
from datetime import date

# Initialize session state
if "goals" not in st.session_state:
    st.session_state.goals = []
if "quote" not in st.session_state:
    st.session_state.quote = ""

# Motivational Quotes
quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Stay positive, work hard, make it happen."
]

# Header
st.markdown("### Vikas Bhosale TYIT 19009")
st.title("🌞 Daily Motivation Dashboard")

# Show a random quote
if st.button("Get Today's Motivation"):
    st.session_state.quote = random.choice(quotes)
if st.session_state.quote:
    st.success(f"💬 {st.session_state.quote}")

# Daily goal input
st.subheader("🎯 Set Your Goal for Today")
goal = st.text_input("Enter your goal")
if st.button("Add Goal"):
    if goal.strip():
        st.session_state.goals.append((goal.strip(), False))
        st.success("Goal added!")
    else:
        st.error("Goal cannot be empty.")

# Display goals with checkboxes
st.subheader("✅ Your Goals")
for i, (g, done) in enumerate(st.session_state.goals):
    checked = st.checkbox(g, value=done, key=f"goal_{i}")
    st.session_state.goals[i] = (g, checked)

# Footer
st.markdown(f"---\n📅 Date: {date.today().strftime('%B %d, %Y')}")

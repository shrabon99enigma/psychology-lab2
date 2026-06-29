import random
import time
from datetime import datetime

import streamlit as st

from habits import MOBILE_HABITS
from verdicts import VERDICTS
from notes import FBI_NOTES


# ===========================
# Page Configuration
# ===========================
st.set_page_config(
    page_title="FBI Mobile Habit Scanner",
    page_icon="🕵️",
    layout="centered"
)

# ===========================
# Header
# ===========================
st.title("🕵️ FBI Mobile Habit Scanner")
st.caption("⚠️ Entertainment Only")

# ===========================
# User Input
# ===========================
name = st.text_input("Enter Your Name")
if name.strip():
    st.balloons()
    st.success(f"👋 Hi {name}! Welcome to your mind 🧠")
    st.toast("🧠 Brain connection established!")

# ===========================
# Start Scan
# ===========================
if st.button("🚀 START SCAN"):

    if not name.strip():
        st.warning("⚠️ Please enter your name.")
        st.stop()

    st.subheader(f"🔍 Scanning {name}'s Mobile Brain...")

    progress = st.progress(0)
    status = st.empty()

    scan_steps = [
        "🔐 Connecting to FBI Database...",
        "📱 Reading Mobile Activity...",
        "🧠 Analyzing Brain Pattern...",
        "🔍 Detecting Hidden Habits...",
        "📊 Preparing Final Report..."
    ]

    for i, step in enumerate(scan_steps):

        status.info(step)

        for j in range(20):
            progress.progress(i * 20 + j + 1)
            time.sleep(0.03)

    status.success("✅ Scan Complete!")

    # ===========================
    # FBI Case Information
    # ===========================

    case_id = f"FBI-{datetime.now().year}-{random.randint(100000,999999)}"

    scan_time = datetime.now().strftime("%d %B %Y | %I:%M %p")

    st.divider()

    st.subheader("🆔 FBI Case Information")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"Case ID\n\n{case_id}")

    with col2:
        st.info(f"Scan Time\n\n{scan_time}")
    # ===========================
    # FBI Score
    # ===========================

    score = random.randint(25, 100)

    verdict = ""

    for limit, text in VERDICTS:
        if score <= limit:
            verdict = text
            break

    st.divider()

    st.subheader("📊 FBI Mobile Score")

    st.progress(score)

    st.metric(
        label="Score",
        value=f"{score}/100"
    )

    st.success(verdict)

    st.caption("✅ FBI Analysis Completed Successfully")

    # ===========================
    # Mobile Habit Report
    # ===========================

    st.divider()

    st.header("🧠 Mobile Habit Report")

    random_habits = random.sample(
        MOBILE_HABITS,
        min(20, len(MOBILE_HABITS))
    )

    for index, habit in enumerate(random_habits, start=1):

        with st.container():

            st.success(f"Finding #{index}")

            st.write(habit)

            time.sleep(0.12)
    # ===========================
    # FBI Secret Note
    # ===========================

    st.divider()

    st.subheader("📂 FBI Secret Note")

    note = random.choice(FBI_NOTES)

    st.warning(note)

    st.caption("🔒 Classified Information")

    # ===========================
    # Scan Complete
    # ===========================

    st.divider()

    st.balloons()

    st.success("🎉 Scan Finished Successfully")

    st.info("Result: You are officially a Normal Smartphone User 😄")

    # ===========================
    # Rating
    # ===========================

    st.divider()

    st.subheader("⭐ Rate This FBI Scanner")

    rating = st.slider(
        "Your Rating",
        min_value=1,
        max_value=5,
        value=5
    )

    st.write(f"⭐ You selected {rating}/5")

    feedback = st.text_area(
        "💬 Share your feedback (optional)"
    )

    if st.button("Submit Feedback"):
        st.success("❤️ Thank you for your valuable feedback!")

    # ===========================
    # Buttons
    # ===========================

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 Scan Again"):
            st.rerun()

    with col2:
        if st.button("❌ Exit"):
            st.success("❤️ Thanks for trying FBI Mobile Habit Scanner!")
            st.stop()
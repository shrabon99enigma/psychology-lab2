import random
import time
from datetime import datetime

import streamlit as st

from habits import MOBILE_HABITS
from verdicts import VERDICTS
from notes import FBI_NOTES
from style import CUSTOM_CSS

# ===========================
# FBI Boot Screen
# ===========================

def boot_screen():

    boot = st.empty()

    frames = [
"""
████████████████████████████

🛰 FBI SECURE TERMINAL

████████████████████████████
""",
"""
████████████████████████████

🛰 FBI SECURE TERMINAL

Connecting...

████████████████████████████
""",
"""
████████████████████████████

🛰 FBI SECURE TERMINAL

Connecting...

Authorizing...

████████████████████████████
""",
"""
████████████████████████████

🛰 FBI SECURE TERMINAL

Connecting...

Authorizing...

Access Granted

████████████████████████████
""",
"""
████████████████████████████

🛰 FBI SECURE TERMINAL

Connecting...

Authorizing...

Access Granted

Welcome Agent.

████████████████████████████
"""
    ]

    for frame in frames:
        boot.code(frame, language="text")
        time.sleep(0.6)

    time.sleep(0.4)

    boot.empty()


# ===========================
# Hacker Typing Animation
# ===========================

def type_writer(text, speed=0.03):

    placeholder = st.empty()

    current = ""

    for ch in text:
        current += ch

        placeholder.markdown(
            f"<h3 style='color:#00ff99'>{current}</h3>",
            unsafe_allow_html=True
        )

        time.sleep(speed)

    return placeholder


# ===========================
# Hacker Terminal Animation
# ===========================

def terminal_animation():

    terminal = st.empty()

    logs = [
        "💻 Initializing FBI Terminal...",
        "🔐 Connecting to Secure Server...",
        "🛰 Establishing Encrypted Connection...",
        "📱 Reading Smartphone Metadata...",
        "🧠 Analyzing Behavioral Patterns...",
        "🔎 Detecting Digital Habits...",
        "📊 Building Investigation Report...",
        "✅ Access Granted."
    ]

    output = ""

    for log in logs:

        output += f"> {log}\n"

        terminal.code(output, language="text")

        time.sleep(0.55)

    return terminal
# ===========================
# Page Configuration
# ===========================

st.set_page_config(
    page_title="FBI Mobile Habit Scanner",
    page_icon="🕵️",
    layout="centered"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ===========================
# Header
# ===========================

st.markdown(
    "<h4 style='text-align:center;color:#00ff99;'>🧠 FBI Secure Brain Connection Established</h4>",
    unsafe_allow_html=True
)

st.title("🕵️ FBI Mobile Habit Scanner")
st.caption("⚠️ Entertainment Only")

# ===========================
# User Input
# ===========================

name = st.text_input("Enter Your Name")

if name.strip():
    st.success(f"👋 Hi {name}! Welcome to your mind 🧠")
    st.toast("🧠 Brain connection established!")

# ===========================
# Start Scan
# ===========================

if st.button("🚀 START SCAN"):

    boot_screen()

    if not name.strip():
        st.warning("⚠️ Please enter your name.")
        st.stop()

    
    typing = type_writer(f"🔍 Scanning {name}'s Mobile Brain...")
    time.sleep(0.5)
    typing.empty()
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

    
    terminal = terminal_animation()
    time.sleep(0.8)
    terminal.empty()

    # ===========================
    # FBI Case Information
    # ===========================

    case_id = f"FBI-{datetime.now().year}-{random.randint(100000,999999)}"
    scan_time = datetime.now().strftime("%d %B %Y | %I:%M %p")

    st.divider()

    st.subheader("🆔 FBI Case Information")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
<div style="
background:#111827;
padding:15px;
border-radius:12px;
border:1px solid #00ff99;
color:white;
">
<b>🆔 Case ID</b><br><br>
{case_id}
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
<div style="
background:#111827;
padding:15px;
border-radius:12px;
border:1px solid #00ff99;
color:white;
">
<b>🕒 Scan Time</b><br><br>
{scan_time}
</div>
""", unsafe_allow_html=True)

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

    st.markdown(f"""
<div style="
background:#111827;
border:1px solid #00ff99;
padding:18px;
border-radius:12px;
text-align:center;
color:white;
">
<h2>📊 FBI Score</h2>
<h1>{score}/100</h1>
</div>
""", unsafe_allow_html=True)

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

    st.markdown(f"""
<div style="
background:#111827;
border:1px solid #ffc107;
padding:15px;
border-radius:12px;
color:white;
font-size:17px;
">
📂 {note}
</div>
""", unsafe_allow_html=True)

    st.caption("🔒 Classified Information")

    # ===========================
    # Scan Complete
    # ===========================

    st.divider()

    st.balloons()

    st.success("🎉 Scan Finished Successfully")
    # ===========================
    # Final Behavioral Analysis
    # ===========================

    if score <= 30:
        result = "🟢 Excellent! Your mobile habits look healthy."

    elif score <= 50:
        result = "🟡 You use your phone normally, but a little extra scrolling was detected."

    elif score <= 70:
        result = "🟠 Late-night scrolling activity has been detected."

    elif score <= 90:
        result = "🔴 Heavy smartphone usage detected. Consider taking short breaks."

    else:
        result = "⚫ Extreme scrolling activity detected. The FBI is... probably just joking. 😂"

    st.caption("📌 Final Behavioral Analysis")
    st.info(result)

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

        if feedback.strip():
            st.write("💬 Your Feedback:")
            st.code(feedback)

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
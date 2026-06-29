import random
import time
import streamlit as st

# ===========================
# Page Configuration
# ===========================
st.set_page_config(
    page_title="FBI Mobile Habit Scanner",
    page_icon="🕵️",
    layout="centered"
)

# ===========================
# Mobile Habits
# ===========================
MOBILE_HABITS = [

"📱 ফোন আনলক করেই কেন খুলেছিলি সেটা ভুলে গেছিস।",
"😂 Reels দেখতে গিয়ে ১ ঘণ্টা কোথায় গেল বুঝিসনি।",
"🔔 Notification না থাকলেও ফোন চেক করেছিস।",
"📷 Camera খুলে শেষে ছবি তুলতেই ভুলে গেছিস।",
"📦 একটা App Install করতে এসে তিনটা Install করেছিস।",
"🎵 একটা গান শুনতে এসে পুরো Playlist শেষ করেছিস।",
"🔋 Battery 1% হলেও ভাবছিস আর একটু চলবে।",
"📲 চার্জে দিয়েও ফোন ব্যবহার করেছিস।",
"📞 Call করতে গিয়ে Messenger খুলেছিস।",
"📸 Gallery-তে ঢুকে ৫ বছর আগের ছবি দেখেছিস।",

"💬 Reply দিবি ভেবে Seen রেখে ভুলে গেছিস।",
"🛏️ ঘুমানোর আগে ৫ মিনিট বলে ২ ঘণ্টা ফোন চালিয়েছিস।",
"🎥 YouTube Recommendation-এর ফাঁদে পড়েছিস।",
"📖 পড়তে বসে Facebook খুলেছিস।",
"🔍 Google-এ এক জিনিস লিখে অন্য জিনিস Search করেছিস।",
"😂 Meme দেখে একা একা হেসেছিস।",
"📱 একই App ১০ বার খুলেছিস।",
"🧹 Storage Clean করতে এসে কিছুই Delete করিসনি।",
"🔐 Wrong Password দিয়েছিস।",
"📶 WiFi Slow হলে Router-এর দিকে তাকিয়েছিস।",

"🎮 Game খেলতে এসে Notification-এ চলে গেছিস।",
"📱 Screen Lock খুলেই আবার Lock করেছিস।",
"📸 Screenshot নিয়ে পরে আর দেখিসনি।",
"📂 Download Folder কখনো পরিষ্কার করিসনি।",
"🎧 Earphone খুলে কোথায় রেখেছিস ভুলে গেছিস।",
"💡 Flashlight জ্বালিয়ে বন্ধ করতে ভুলে গেছিস।",
"🔋 Power Bank নিয়েও চার্জ দিতে ভুলে গেছিস।",
"📞 Call শেষ হওয়ার পরও ফোন কানে ধরে ছিলি।",
"📱 Phone Vibrate হয়েছে মনে হলেও আসলে হয়নি।",
"😂 Status Upload করে কে কে দেখল বারবার Check করেছিস।",

"💬 Typing শুরু করে Message Delete করেছিস।",
"🎵 একটা গান Repeat-এ ২০ বার শুনেছিস।",
"📸 Selfie তুলতে ৩০টা ছবি তুলেছিস।",
"🔄 App Update পরে করব বলে মাস পার করে দিয়েছিস।",
"📶 Airplane Mode দিয়ে Network ঠিক করার চেষ্টা করেছিস।",
"📱 Phone Silent আছে কিনা বারবার Check করেছিস।",
"📂 Duplicate Photo Delete করতে গিয়ে কিছুই Delete করোনি।",
"😂 Comment পড়তে পড়তে Post-টাই ভুলে গেছিস।",
"🎥 Shorts দেখতে এসে পুরো সন্ধ্যা শেষ করেছিস।",
"📲 Fingerprint তিনবার Fail করেছে।",

"💬 Reply দিতে দিতে অন্য App-এ চলে গেছিস।",
"📸 Camera খুলে Mirror হিসেবে ব্যবহার করেছিস।",
"🔋 Charger লাগিয়ে Switch On করতে ভুলে গেছিস।",
"📱 Phone Pocket-এ আছে কিনা Pocket Check করেছিস।",
"😂 Phone হাতে নিয়েই Phone খুঁজেছিস।",
"🎧 Earphone পরে গান না চালিয়েই বসে ছিলি।",
"📲 Screen Time দেখে নিজেই অবাক হয়েছিস।",
"🔔 Phantom Notification অনুভব করেছিস।",
"📱 Phone Clean করতে এসে Cover-ই পরিষ্কার করেছিস।",
"😂 FBI বলছে—তুই ফোনের চেয়ে ফোন তোকে বেশি ব্যবহার করে।"

]

# ===========================
# UI
# ===========================
st.title("🕵️ FBI Mobile Habit Scanner")
st.caption("⚠️ Entertainment Only")

name = st.text_input("Enter Your Name")

if st.button("🚀 START SCAN"):

    if not name.strip():
        st.warning("Please enter your name.")
        st.stop()

    st.subheader(f"Scanning {name}'s Mobile Brain...")

    progress = st.progress(0)
    status = st.empty()

    scan_steps = [
        "🔐 Connecting to FBI Database...",
        "📱 Reading Mobile Activity...",
        "🧠 Analyzing Brain Pattern...",
        "🔍 Detecting Hidden Habits...",
        "📊 Preparing Final Report..."
    ]

    # Fake Scanning Animation
    for i, step in enumerate(scan_steps):
        status.info(step)

        for j in range(20):
            progress.progress(i * 20 + j + 1)
            time.sleep(0.03)

    status.success("✅ Scan Complete!")

    # ===========================
    # FBI SCORE
    # ===========================
    score = random.randint(25, 100)

    if score <= 30:
        verdict = "🟢 Innocent Mobile User"

    elif score <= 50:
        verdict = "🟡 Casual Scroller"

    elif score <= 70:
        verdict = "🟠 Midnight Scroller"

    elif score <= 90:
        verdict = "🔴 Certified Mobile Addict"

    else:
        verdict = "⚫ FBI Wants To Talk With You 😂"

    st.divider()

    st.subheader("📊 FBI Mobile Score")

    st.progress(score)

    st.metric("Score", f"{score}/100")

    st.success(verdict)

    # ===========================
    # Random Habits
    # ===========================
    st.divider()

    st.header("🧠 Mobile Habit Report")

    random_habits = random.sample(
        MOBILE_HABITS,
        min(len(MOBILE_HABITS), 20)
    )

    for index, habit in enumerate(random_habits, start=1):
        with st.container():
            st.success(f"Finding #{index}")
            st.write(habit)
            time.sleep(0.25)

    st.divider()

    st.balloons()

    st.success("🎉 Scan Finished")

    st.info("Result: You are officially a Normal Smartphone User 😄")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
     if st.button("🔄 Scan Again"):
        st.rerun()

    with col2:
     if st.button("❌ Exit"):
        st.success("Thanks for trying FBI Mobile Habit Scanner ❤️")
        st.stop()
    # ===========================
    # Rating
    # ===========================
    st.divider()

    st.subheader("⭐ Rate This FBI Scanner")

    rating = st.slider(
        "Your Rating",
        1,
        5,
        5
    )

    feedback = st.text_area(
        "💬 Share your feedback (optional)"
    )

    if st.button("Submit Feedback"):
        st.success("❤️ Thank you for your valuable feedback!")
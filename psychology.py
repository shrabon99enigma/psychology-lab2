import time
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="FBI Mobile Habit Scanner",
    page_icon="🕵️",
    layout="centered"
)

# -----------------------------
# Mobile Habits
# -----------------------------
MOBILE_HABITS = [
    "📱 ফোন আনলক করে কী করতে এসেছিলি সেটাই ভুলে গেছিস।",
    "⏰ শুধু সময় দেখার জন্য ফোন খুলেছিলি, তারপর ২০ মিনিট স্ক্রল করেছিস।",
    "🔋 ব্যাটারি ১% হলেও ভাবছিস, 'আর একটু চলবে।'",
    "📶 Wi-Fi স্লো হলে অন্তত একবার Router-এর দিকে রাগী চোখে তাকিয়েছিস।",
    "🔔 Notification না থাকলেও বারবার ফোন চেক করেছিস।",
    "💬 Message পড়ে 'পরে Reply দিব' ভেবে ভুলে গেছিস।",
    "📷 Camera খুলেছিলি, কিন্তু শেষে ছবি তুলতে ভুলে গেছিস।",
    "🎵 একটা গান শুনতে এসে আরও ১০টা গান শুনে ফেলেছিস।",
    "📸 Gallery-তে পুরনো ছবি দেখতে গিয়ে ২ ঘণ্টা কেটে গেছে।",
    "🔍 Google-এ কিছু Search করতে গিয়ে অন্য কিছু Search করেছিস।",
    "📦 App Install করতে এসে আরও তিনটা App Install করেছিস।",
    "🎥 YouTube-এ একটা ভিডিও দেখে Recommendation-এর ফাঁদে পড়েছিস।",
    "📞 Call করার জন্য ফোন হাতে নিয়েও Call না করে অন্য App খুলেছিস।",
    "🔐 ভুল Pattern বা Password অন্তত একবার দিয়েছিস।",
    "📲 Phone Silent আছে কিনা তা বারবার Check করেছিস।",
    "💤 ঘুমানোর আগে বলেছিস 'আর ৫ মিনিট', কিন্তু ১ ঘণ্টা কেটে গেছে।",
    "📖 পড়তে বসে Dictionary খুলে শেষে Facebook-এ চলে গেছিস।",
    "🧹 Storage পরিষ্কার করতে এসে কোনো File Delete করতে মন চায়নি।",
    "🔄 একই App বারবার খুলে আবার বন্ধ করেছিস।",
    "📱 ফোনটা হাতে নিয়ে শেষ পর্যন্ত কেন হাতে নিয়েছিলি সেটাই মনে করতে পারোনি।"
]

# -----------------------------
# UI
# -----------------------------
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

    # Fake scanning
    scan_steps = [
        "🔐 Connecting to FBI Database...",
        "📱 Reading Mobile Activity...",
        "🧠 Analyzing Brain Pattern...",
        "🔍 Detecting Hidden Habits...",
        "📊 Preparing Report..."
    ]

    for i, step in enumerate(scan_steps):
        status.info(step)

        for j in range(20):
            progress.progress(i * 20 + j + 1)
            time.sleep(0.03)

    status.success("✅ Scan Complete!")

    st.divider()
    st.header("🧠 Mobile Habit Report")

    # Show all 20 habits one by one
    for index, habit in enumerate(MOBILE_HABITS, start=1):
        with st.container():
            st.success(f"Finding #{index}")
            st.write(habit)
            time.sleep(0.8)

    st.divider()
    st.balloons()

    st.success("🎉 Scan Finished")
    st.info("Result: You are officially a Normal Smartphone User 😄")
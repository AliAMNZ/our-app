from datetime import datetime
import json
import os
from PIL import Image
import requests
import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 🔑 اطلاعات تلگرام خودت (اختیاری):
# ==========================================
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"


def send_to_telegram(question_text):
    """ارسال مستقیم سوال به تلگرام ادمین"""
    if (
        TELEGRAM_BOT_TOKEN != "YOUR_BOT_TOKEN_HERE"
        and TELEGRAM_CHAT_ID != "YOUR_CHAT_ID_HERE"
    ):
        try:
            url = (
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            )
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
            payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": (
                    f"💌 **یک سوال جدید در وب‌سایت ثبت شد!**\n\n"
                    f"🕒 زمان: `{now_str}`\n"
                    f"💭 متن سوال:\n{question_text}"
                ),
                "parse_mode": "Markdown",
            }
            requests.post(url, json=payload, timeout=8)
        except Exception as e:
            print(f"Telegram error: {e}")


# --- تنظیمات صفحه مخصوص موبایل ---
st.set_page_config(
    page_title="داستان ما | یادداشت‌های اختصاصی",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- استایل پس‌زمینه عاشقانه با نمادهای شناور و ریسپانسیو موبایل ---
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700;900&display=swap');

    header[data-testid="stHeader"], [data-testid="stSidebar"], #MainMenu, footer, 
    .stDeployButton, div[data-testid="stDecoration"], div[data-testid="stToolbar"] {
        display: none !important;
        visibility: hidden !important;
    }

    html, body, [class*="css"], .stApp {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background: #0f0c20 !important;
        color: #f8fafc !important;
        overflow-x: hidden;
    }

    /* بک‌گراند گرادیانت با اورلی متحرک */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: radial-gradient(circle at 15% 15%, rgba(244, 63, 94, 0.22) 0%, transparent 45%),
                    radial-gradient(circle at 85% 85%, rgba(168, 85, 247, 0.25) 0%, transparent 45%),
                    radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.15) 0%, #0b071a 100%);
        z-index: 0;
        pointer-events: none;
    }

    /* المان‌های معلق عاشقانه در پس‌زمینه */
    .floating-romantic-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }

    .float-item {
        position: absolute;
        user-select: none;
        opacity: 0.28;
        filter: drop-shadow(0 0 8px rgba(244, 114, 182, 0.4));
        animation: floatAround 14s infinite ease-in-out alternate;
    }

    .f1 { top: 8%; left: 8%; font-size: 32px; animation-duration: 16s; }
    .f2 { top: 22%; right: 10%; font-size: 38px; animation-duration: 18s; animation-delay: -2s; }
    .f3 { top: 52%; left: 6%; font-size: 34px; animation-duration: 15s; animation-delay: -5s; }
    .f4 { top: 70%; right: 8%; font-size: 40px; animation-duration: 20s; animation-delay: -3s; }
    .f5 { top: 88%; left: 20%; font-size: 30px; animation-duration: 14s; animation-delay: -7s; }
    .f6 { top: 40%; right: 14%; font-size: 28px; animation-duration: 17s; animation-delay: -4s; }
    .f7 { top: 80%; left: 80%; font-size: 36px; animation-duration: 19s; animation-delay: -1s; }

    @keyframes floatAround {
        0% { transform: translateY(0px) rotate(0deg) scale(1); }
        50% { transform: translateY(-30px) rotate(12deg) scale(1.1); }
        100% { transform: translateY(20px) rotate(-10deg) scale(0.95); }
    }

    .main .block-container {
        position: relative;
        z-index: 1;
        padding-top: 1.2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        max-width: 600px !important;
    }

    /* تب‌های افقی بالای صفحه */
    div[data-baseweb="tab-list"] {
        display: flex !important;
        justify-content: flex-start !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        gap: 6px !important;
        padding-bottom: 8px !important;
        border-bottom: 1px solid rgba(244, 114, 182, 0.25) !important;
    }

    button[data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        border-radius: 14px !important;
        padding: 8px 14px !important;
        color: #e2e8f0 !important;
        font-size: 13px !important;
        font-weight: 700 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #ec4899, #8b5cf6) !important;
        color: #ffffff !important;
        border: 1px solid rgba(244, 114, 182, 0.7) !important;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4);
    }

    /* کارت‌های شیشه‌ای */
    .glass-card {
        background: rgba(22, 16, 44, 0.65) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(244, 114, 182, 0.25);
        border-radius: 20px;
        padding: 18px 14px;
        margin-top: 14px;
        margin-bottom: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }

    /* کارت‌های ویژگی و خط قرمز */
    .flag-card {
        border-radius: 14px;
        padding: 12px 14px;
        margin-bottom: 10px;
        font-size: 13.5px;
        line-height: 1.8;
    }
    .red-flag {
        background: rgba(239, 68, 68, 0.18);
        border-right: 4px solid #ef4444;
        color: #fecaca !important;
    }
    .green-flag {
        background: rgba(34, 197, 94, 0.18);
        border-right: 4px solid #22c55e;
        color: #bbf7d0 !important;
    }

    .stButton>button {
        width: 100%;
        border-radius: 14px;
        background: linear-gradient(90deg, #ec4899, #8b5cf6);
        color: #ffffff !important;
        font-weight: 800;
        border: none;
        padding: 10px 16px;
        font-size: 15px;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.35);
    }

    .stTextInput input, .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
    }

    .stRadio label, .stRadio div, .stRadio p, .stRadio span {
        font-size: 14px !important;
        color: #f1f5f9 !important;
        font-weight: 600 !important;
    }

    /* انیمیشن باز شدن قفل و بوسه عاشقانه */
    .unlock-kiss-stage {
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        width: 100%;
        height: 120px;
        margin: 15px 0;
    }

    .boy-kiss {
        font-size: 55px;
        animation: boyKissMove 1s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    }

    .girl-kiss {
        font-size: 55px;
        animation: girlKissMove 1s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    }

    .heart-pop {
        position: absolute;
        left: 50%;
        top: 30%;
        transform: translate(-50%, -50%) scale(0);
        font-size: 40px;
        animation: popHeart 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) 0.8s forwards;
    }

    @keyframes boyKissMove {
        0% { transform: translateX(-40px); }
        100% { transform: translateX(35px) rotate(10deg); }
    }

    @keyframes girlKissMove {
        0% { transform: translateX(40px); }
        100% { transform: translateX(-35px) rotate(-10deg); }
    }

    @keyframes popHeart {
        0% { transform: translate(-50%, -50%) scale(0); opacity: 0; }
        50% { transform: translate(-50%, -70%) scale(1.4); opacity: 1; }
        100% { transform: translate(-50%, -85%) scale(1.2); opacity: 1; }
    }
</style>

<!-- نمادهای شناور و رمانتیک در بک‌گراند -->
<div class="floating-romantic-bg">
    <div class="float-item f1">👩‍❤️‍💋‍👨</div>
    <div class="float-item f2">💖</div>
    <div class="float-item f3">✨</div>
    <div class="float-item f4">💋</div>
    <div class="float-item f5">💕</div>
    <div class="float-item f6">🌹</div>
    <div class="float-item f7">👩‍❤️‍👨</div>
</div>
""",
    unsafe_allow_html=True,
)

if "balloons_shown" not in st.session_state:
    st.balloons()
    st.session_state.balloons_shown = True

# هدر اختصاصی
image_path = "photo_2026-08-28_16-40-13.jpg"
st.markdown(
    """
<div style="text-align: center; margin-bottom: 12px;">
    <h3 style="background: linear-gradient(90deg, #f472b6, #c084fc, #38bdf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900; margin: 0; font-size: 22px;">
        ✨ برای خاص‌ترین مخاطب دنیا ✨
    </h3>
    <p style="color: #cbd5e1; font-size: 12.5px; margin-top: 4px;">لحظه‌هایی که با تو زیباتر میشن...</p>
</div>
""",
    unsafe_allow_html=True,
)

if os.path.exists(image_path):
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.image(image_path, use_container_width=True)

# تب‌های اصلی
tabs = st.tabs([
    "⏳ روزشمار زنده",
    "💬 بپرس ازم",
    "🚦 مرزهای من",
    "🕌 آزمون احکام",
    "💌 نامه محرمانه",
])

# ================= 1. روزشمار زنده (Live Timer) =================
with tabs[0]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color:#f472b6; margin:0;'>📅 از اولین پیامی که بهت"
        " دادم:</h4>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:#94a3b8; font-size:12.5px; margin-top:2px;'>۱۷ آگوست"
        " ۲۰۲۶ | ساعت ۱۳:۰۶ (۱:۰۶ بعد از ظهر)</p>",
        unsafe_allow_html=True,
    )

    timer_html = """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap" rel="stylesheet">
        <style>
            * {
                box-sizing: border-box;
                font-family: 'Vazirmatn', sans-serif !important;
                margin: 0;
                padding: 0;
            }
            body {
                background: transparent;
                color: #f8fafc;
            }
            .live-counter-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 10px;
                margin: 10px 0;
                direction: rtl;
            }
            .live-counter-box {
                background: rgba(244, 114, 182, 0.14);
                border: 1px solid rgba(244, 114, 182, 0.35);
                border-radius: 16px;
                padding: 12px 6px;
                text-align: center;
            }
            .live-val {
                font-size: 28px;
                font-weight: 900;
                color: #f472b6;
                direction: ltr;
                line-height: 1.1;
                font-variant-numeric: tabular-nums;
            }
            .live-lbl {
                font-size: 12.5px;
                font-weight: 700;
                color: #cbd5e1;
                margin-top: 4px;
            }
            .summary-box {
                text-align: center;
                margin-top: 10px;
                padding: 10px;
                background: rgba(244, 114, 182, 0.1);
                border-radius: 12px;
            }
            .summary-text {
                color: #fbcfe8;
                font-size: 13.5px;
                font-weight: 700;
            }
        </style>
    </head>
    <body>
        <div class="live-counter-grid">
            <div class="live-counter-box"><div id="live-days" class="live-val">0</div><div class="live-lbl">روز گذشته</div></div>
            <div class="live-counter-box"><div id="live-hours" class="live-val">00</div><div class="live-lbl">ساعت</div></div>
            <div class="live-counter-box"><div id="live-mins" class="live-val">00</div><div class="live-lbl">دقیقه</div></div>
            <div class="live-counter-box"><div id="live-secs" class="live-val">00</div><div class="live-lbl">ثانیه (زنده ⚡)</div></div>
        </div>
        <div class="summary-box">
            <p id="live-summary" class="summary-text">✨ در حال محاسبه لحظه‌ها... 🌸</p>
        </div>

        <script>
            // تنظیم ساعت به 13:06 (1:06 PM)
            const startDate = new Date('2026-08-17T13:06:00');
            function updateLiveTimer() {
                const now = new Date();
                const diffMs = now - startDate;
                if (diffMs > 0) {
                    const totalSeconds = Math.floor(diffMs / 1000);
                    const days = Math.floor(totalSeconds / 86400);
                    const hours = Math.floor((totalSeconds % 86400) / 3600);
                    const mins = Math.floor((totalSeconds % 3600) / 60);
                    const secs = totalSeconds % 60;

                    const elDays = document.getElementById('live-days');
                    const elHours = document.getElementById('live-hours');
                    const elMins = document.getElementById('live-mins');
                    const elSecs = document.getElementById('live-secs');
                    const elSumm = document.getElementById('live-summary');

                    if(elDays) elDays.innerText = days;
                    if(elHours) elHours.innerText = hours < 10 ? '0' + hours : hours;
                    if(elMins) elMins.innerText = mins < 10 ? '0' + mins : mins;
                    if(elSecs) elSecs.innerText = secs < 10 ? '0' + secs : secs;
                    if(elSumm) elSumm.innerHTML = `✨ دقیقاً <b>${days} روز</b> از اون لحظه‌ای که داستانمون شروع شد گذشته... 🌸`;
                }
            }
            setInterval(updateLiveTimer, 1000);
            updateLiveTimer();
        </script>
    </body>
    </html>
    """
    components.html(timer_html, height=215)
    st.markdown("</div>", unsafe_allow_html=True)

# ================= 2. بپرس ازم =================
with tabs[1]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color:#f472b6; margin:0;'>💬 صندوقچه سوالات</h4>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:#cbd5e1; font-size:12.5px;'>هر سوالی گوشه ذهنت داری"
        " بنویس تا با صداقت کامل بهت جواب بدم:</p>",
        unsafe_allow_html=True,
    )

    qa_file = "user_questions.json"
    questions_list = []
    if os.path.exists(qa_file):
        try:
            with open(qa_file, "r", encoding="utf-8") as f:
                questions_list = json.load(f)
        except:
            questions_list = []

    with st.form("mobile_qa_form", clear_on_submit=True):
        user_q = st.text_area(
            "سوال تو:", placeholder="مثلاً: توی فلان موقعیت چه حسی داری؟"
        )
        if st.form_submit_button("💌 ارسال سوال به من"):
            if user_q.strip():
                questions_list.append({
                    "question": user_q.strip(),
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                with open(qa_file, "w", encoding="utf-8") as f:
                    json.dump(questions_list, f, ensure_ascii=False, indent=2)

                send_to_telegram(user_q.strip())

                st.balloons()
                st.success("سوالت برام ثبت شد! حتماً با دقت بهت جواب میدم ✨")
            else:
                st.warning("متن سوال خالیه!")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= 3. مرزهای من =================
with tabs[2]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color:#86efac; margin:0;'>🟢 ویژگی‌های مهم من:</h4><br>",
        unsafe_allow_html=True,
    )

    positives = [
        (
            "منطقی بودن",
            "گفتگوی منطقی و آرام در تمام چالش‌ها اولویت اول منه.",
        ),
        (
            "صبوری و درک متقابل",
            "توی روزهای سخت و بی‌حوصلگی‌ها با آرامش کنارت می‌مونم.",
        ),
        (
            "وفاداری به پارتنر",
            "تعهد، تمرکز و وفاداری کامل روی رابطه‌مون.",
        ),
    ]
    for t, d in positives:
        st.markdown(
            f'<div class="flag-card green-flag"><strong>✔ {t}:</strong>'
            f" {d}</div>",
            unsafe_allow_html=True,
        )

    st.markdown(
        "<hr style='border:none; border-top:1px dashed rgba(255,255,255,0.15);"
        " margin:16px 0;'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h4 style='color:#fca5a5; margin:0;'>⛔ خطوط قرمز من:</h4><br>",
        unsafe_allow_html=True,
    )

    negatives = [
        ("خیانت", "اعتماد همه‌چیزه و خدشه‌دار شدنش غیرقابل‌جبرانه."),
        ("دروغ", "حقیقت حتی اگه تلخ باشه ارزشش از دروغ بیشتره."),
        ("ناخالصی داشتن", "تظاهر، ریاکاری یا عدم شفافیت."),
    ]
    for t, d in negatives:
        st.markdown(
            f'<div class="flag-card red-flag"><strong>✖ {t}:</strong>'
            f" {d}</div>",
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= 4. احکام =================
with tabs[3]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color:#f472b6; margin:0;'>🕌 آزمون احکام و تقوا (نسخه"
        " طنز)</h4>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:#cbd5e1; font-size:12.5px;'>پاسخ به مسائل شرعی با"
        " چاشنی خنده 😂</p>",
        unsafe_allow_html=True,
    )

    q1 = st.radio(
        "۱. ساعت ۳ نصف شب بیدار شدی، نیتت چیه؟",
        [
            "الف) پاشم نماز شب بخونم",
            "ب) برم سر یخچال آب بخورم و برم تو گوشی",
            "ج) چک کنم کی آنلاینه",
        ],
        index=None,
        key="mq1",
    )
    q2 = st.radio(
        "۲. بیدار شدن برای نماز صبح در کشش پتوی گلبافت:",
        [
            "الف) جهاد اکبر و بلند شدن سریع",
            "ب) اسنوز آلارم تا خود ظهر",
            "ج) نیت قضا و ادامه خواب",
        ],
        index=None,
        key="mq2",
    )
    q3 = st.radio(
        "۳. وضو گرفتن با لاک ناخن و کاشت:",
        [
            "الف) پاک کردن طبق رساله",
            "ب) تیمم جبیره با استغفار از هزینه ناخن‌کار",
            "ج) نیت قلبی مهمه حائل معنی نداره!",
        ],
        index=None,
        key="mq3",
    )

    if st.button("📿 محاسبه درجه تقوا", key="mbtn_deen"):
        if q1 and q2 and q3:
            st.success(
                "نتیجه: تبارک‌الله! درجه تقوای شما در بالاترین سطح شوخ‌طبعی قرار"
                " دارد 😄🤍"
            )
            st.snow()
        else:
            st.warning("به همه سوال‌ها جواب بده حاج‌خانم!")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= 5. نامه محرمانه با رمز «بوسیدن لب یار» =================
with tabs[4]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color:#c084fc; margin:0;'>🔒 صندوقچه نامه رمزدار</h4>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <div style="background: rgba(192, 132, 252, 0.08); border-right: 3px solid #c084fc; padding: 10px; border-radius: 10px; margin: 10px 0;">
        <p style="font-size:12.5px; color:#e2e8f0; line-height:1.7; margin:0;">
        💡 <b>راهنما:</b> این قفل با حدس ساده باز نمیشه! باید به مرور زمان و شناخت بیشتر به رمز برسی... شیرین‌ترین و عاشقانه‌ترین اتفاق دنیا کلید این دره ✨
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    pwd = st.text_input(
        "رمز ورود:", type="password", placeholder="رمز را بنویس...", key="mpwd"
    )

    valid_passwords = [
        "بوسیدن لب یار",
        "بوسیدن لب‌ یار",
        "بوسیدن لب یار ",
        "بوسیدن‌لب‌یار",
    ]

    if st.button("گشودن قفل 🗝️", key="mbtn_lock"):
        cleaned_pwd = (
            pwd.strip().replace("\u200c", " ").replace("  ", " ").lower()
        )
        if (
            cleaned_pwd in [p.replace("\u200c", " ").lower() for p in valid_passwords]
            or ("بوسیدن" in cleaned_pwd and "یار" in cleaned_pwd)
        ):
            st.balloons()

            st.markdown(
                """
            <div class="unlock-kiss-stage">
                <div class="boy-kiss">👦🏻</div>
                <div class="heart-pop">💖✨</div>
                <div class="girl-kiss">👧🏻</div>
            </div>
            <div style="text-align: center; margin-bottom: 15px;">
                <h4 style="color: #f472b6; font-weight: 900; margin: 0;">🎉 تبریک! رمز دل با موفقیت گشوده شد... 💋✨</h4>
            </div>
            <div style="background: rgba(244, 114, 182, 0.12); border: 1.5px solid #f472b6; padding: 16px; border-radius: 16px;">
                <p style="color:#fdf2f8; font-size:14.5px; line-height:2.1; margin:0;">
                    سلام عزیز دلم،<br>
                    شاید این چند خط کد باشه، ولی تک‌تک خط‌هاش رو با تمام احساسم و به یاد لبخند قشنگت نوشتم.<br>
                    از همون ۱۷ آگوست ساعت ۱۳:۰۶ (۱:۰۶ ظهر) که با هم هم‌صحبت شدیم، دنیام رنگ دیگه‌ای گرفت. ممنونم که هستی و با بودنت همه چیز رو قشنگ‌تر کردی ❤️🌻
                </p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        elif pwd == "":
            st.warning("رمز را وارد نکردی!")
        else:
            st.error("🔒 رمز درست نیست! به مرور زمان کشفش کن 😉")

    st.markdown("</div>", unsafe_allow_html=True)

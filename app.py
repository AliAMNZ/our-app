from datetime import datetime
import json
import os
from PIL import Image
import streamlit as st

# --- تنظیمات صفحه مخصوص موبایل ---
st.set_page_config(
    page_title="داستان ما | یادداشت‌های اختصاصی",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- استایل کاملاً ریسپانسیو و بدون باگ موبایل ---
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700;900&display=swap');

    /* مخفی‌سازی کامل هدر، منوها و سایدبار مشکل‌ساز در موبایل */
    header[data-testid="stHeader"], [data-testid="stSidebar"], #MainMenu, footer, 
    .stDeployButton, div[data-testid="stDecoration"], div[data-testid="stToolbar"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* ریست کامل استایل بدنه */
    html, body, [class*="css"], .stApp {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background: radial-gradient(circle at top, #1e1b4b 0%, #0f172a 60%, #2e0854 100%) !important;
        color: #f8fafc !important;
    }

    .main .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        max-width: 600px !important;
    }

    /* استایل تب‌های افقی بالای صفحه مخصوص موبایل */
    div[data-baseweb="tab-list"] {
        display: flex !important;
        justify-content: flex-start !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        gap: 6px !important;
        padding-bottom: 8px !important;
        border-bottom: 1px solid rgba(244, 114, 182, 0.2) !important;
    }

    button[data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.06) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 14px !important;
        padding: 8px 14px !important;
        color: #e2e8f0 !important;
        font-size: 13px !important;
        font-weight: 700 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #ec4899, #8b5cf6) !important;
        color: #ffffff !important;
        border: 1px solid rgba(244, 114, 182, 0.6) !important;
    }

    /* کارت‌های اصلی با چیدمان تمیز */
    .glass-card {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.14);
        border-radius: 20px;
        padding: 18px 14px;
        margin-top: 14px;
        margin-bottom: 16px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
    }

    /* شبکه شمارنده‌ها: دقیقاً ۲ ستون ثابت بدون شکستن متن */
    .counter-grid-2x2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin: 15px 0 10px 0;
        direction: rtl;
    }

    .counter-box {
        background: rgba(244, 114, 182, 0.12);
        border: 1px solid rgba(244, 114, 182, 0.35);
        border-radius: 16px;
        padding: 12px 6px;
        text-align: center;
    }

    .counter-val {
        font-size: 26px;
        font-weight: 900;
        color: #f472b6;
        direction: ltr;
        line-height: 1.1;
    }

    .counter-label {
        font-size: 12px;
        font-weight: 700;
        color: #cbd5e1;
        margin-top: 4px;
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
        background: rgba(239, 68, 68, 0.15);
        border-right: 4px solid #ef4444;
        color: #fecaca !important;
    }
    .green-flag {
        background: rgba(34, 197, 94, 0.15);
        border-right: 4px solid #22c55e;
        color: #bbf7d0 !important;
    }

    /* دکمه‌ها و فرم‌ها */
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

    /* انیمیشن بارش ملایم قلب‌ها */
    .heart-bg {
        position: fixed;
        top: -5vh;
        pointer-events: none;
        z-index: 99999;
        animation: fall linear forwards;
    }
    @keyframes fall {
        to {
            transform: translateY(105vh) rotate(360deg);
            opacity: 0;
        }
    }
</style>

<script>
    function spawnHearts() {
        const symbols = ['💖', '✨', '🌸', '❤️'];
        for(let i=0; i<18; i++) {
            let heart = document.createElement('div');
            heart.className = 'heart-bg';
            heart.innerText = symbols[Math.floor(Math.random() * symbols.length)];
            heart.style.left = Math.random() * 95 + 'vw';
            heart.style.animationDuration = (Math.random() * 2.5 + 2.5) + 's';
            heart.style.fontSize = (Math.random() * 14 + 14) + 'px';
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 5000);
        }
    }
    setTimeout(spawnHearts, 200);
</script>
""",
    unsafe_allow_html=True,
)

if "balloons_shown" not in st.session_state:
    st.balloons()
    st.session_state.balloons_shown = True

# هدر اختصاصی همراه با عکس گرد و عنوان
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

# تب‌های ناوبری اصلی (مخصوص موبایل)
tabs = st.tabs([
    "⏳ روزشمار",
    "💬 بپرس ازم",
    "🚦 مرزهای من",
    "🕌 آزمون احکام",
    "💌 نامه محرمانه",
])

# ================= 1. روزشمار =================
with tabs[0]:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color:#f472b6; margin:0;'>📅 از اولین پیامی که بهت"
        " دادم:</h4>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='color:#94a3b8; font-size:12.5px; margin-top:2px;'>۱۷ آگوست"
        " ۲۰۲۶ | ساعت ۱:۰۶ بامداد</p>",
        unsafe_allow_html=True,
    )

    start_date = datetime(2026, 8, 17, 1, 6, 0)
    now = datetime.now()

    if now >= start_date:
        passed_time = now - start_date
        days_passed = passed_time.days
        hours_passed = passed_time.seconds // 3600
        mins_passed = (passed_time.seconds % 3600) // 60
        secs_passed = passed_time.seconds % 60

        st.markdown(
            f"""
        <div class="counter-grid-2x2">
            <div class="counter-box"><div class="counter-val">{days_passed}</div><div class="counter-label">روز گذشته</div></div>
            <div class="counter-box"><div class="counter-val">{hours_passed}</div><div class="counter-label">ساعت</div></div>
            <div class="counter-box"><div class="counter-val">{mins_passed}</div><div class="counter-label">دقیقه</div></div>
            <div class="counter-box"><div class="counter-val">{secs_passed}</div><div class="counter-label">ثانیه</div></div>
        </div>
        <div style="text-align:center; margin-top:10px; padding:10px; background:rgba(244, 114, 182, 0.08); border-radius:12px;">
            <p style="color:#fbcfe8; font-size:13.5px; margin:0; font-weight:700;">
                ✨ دقیقاً <b>{days_passed} روز</b> از اون شبی که داستانمون شروع شد گذشته... 🌸
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
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

# ================= 5. نامه محرمانه =================
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
        💡 <b>راهنما:</b> این قفل با حدس ساده باز نمیشه! باید به مرور زمان و شناخت بیشتر به رمز برسی... شاید ساعتی خاص یا تاریخی باشه که قصه‌مون شروع شد ✨
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    pwd = st.text_input(
        "رمز ورود:", type="password", placeholder="رمز را بنویس...", key="mpwd"
    )
    valid_passwords = ["0106", "1:06", "17aug", "1708", "love"]

    if st.button("گشودن قفل 🗝️", key="mbtn_lock"):
        if pwd.strip().lower() in valid_passwords:
            st.balloons()
            st.markdown(
                """
            <div style="background: rgba(244, 114, 182, 0.1); border: 1.5px solid #f472b6; padding: 14px; border-radius: 14px; margin-top: 10px;">
                <p style="color:#fdf2f8; font-size:14px; line-height:2; margin:0;">
                    سلام عزیز دلم،<br>
                    شاید این چند خط کد باشه، ولی تک‌تک خط‌هاش رو با فکر کردن به لبخندت نوشتم. از ۱۷ آگوست ساعت ۱:۰۶ بامداد که هم‌کلام شدیم، فهمیدم چقدر برام خاصی. ممنونم که دنیامو قشنگ‌تر کردی ❤️🌻
                </p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        elif pwd == "":
            st.warning("رمز را وارد نکردی!")
        else:
            st.error("رمز درست نیست! به مرور زمان کشفش کن 😉")

    st.markdown("</div>", unsafe_allow_html=True)

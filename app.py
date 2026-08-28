from datetime import date, datetime
import json
import os
from PIL import Image
import streamlit as st

# --- تنظیمات اولیه صفحه ---
st.set_page_config(
    page_title="داستان ما | یادداشت‌های اختصاصی",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- استایل‌دهی اختصاصی دارک، شیشه‌ای و بهینه‌سازی شده برای موبایل ---
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;600;700;900&display=swap');

    /* مخفی‌سازی هدر مشکی و دکمه‌های دیپلوی استریم‌لیت */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    #MainMenu, footer, .stDeployButton, div[data-testid="stDecoration"], div[data-testid="stToolbar"] {
        display: none !important;
        visibility: hidden !important;
    }

    html, body, [class*="css"], .stApp {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl;
        text-align: right;
        background: radial-gradient(circle at 10% 20%, #1e1b4b 0%, #0f172a 40%, #2e0854 100%) !important;
        color: #f8fafc !important;
    }

    /* کارت‌های شیشه‌ای واکنش‌گرا (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 22px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        border-color: rgba(244, 114, 182, 0.5);
        transform: translateY(-2px);
    }

    /* کارت‌های ویژگی‌ها و خط قرمزها */
    .flag-card {
        border-radius: 18px;
        padding: 16px 20px;
        margin-bottom: 14px;
        font-size: 15px;
        line-height: 1.8;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .red-flag {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(153, 27, 27, 0.3));
        border-right: 5px solid #ef4444;
        color: #fecaca !important;
    }
    .green-flag {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(21, 128, 61, 0.3));
        border-right: 5px solid #22c55e;
        color: #bbf7d0 !important;
    }

    /* شمارنده‌های منعطف برای موبایل */
    .counter-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        justify-content: center;
        align-items: center;
        margin: 15px 0;
    }
    .counter-item {
        flex: 1 1 calc(30% - 10px);
        min-width: 85px;
        background: rgba(244, 114, 182, 0.12);
        border: 1px solid rgba(244, 114, 182, 0.35);
        border-radius: 18px;
        padding: 14px 8px;
        text-align: center;
    }
    .counter-val {
        font-size: 28px;
        font-weight: 900;
        color: #f472b6;
        direction: ltr;
        text-align: center;
        line-height: 1.1;
    }
    .counter-label {
        font-size: 13px;
        font-weight: 600;
        color: #e2e8f0;
        margin-top: 6px;
        text-align: center;
    }

    /* تیترهای گرادیانت */
    .hero-title {
        background: linear-gradient(90deg, #f472b6, #c084fc, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 26px;
        margin-bottom: 8px;
    }

    /* دکمه‌های لمسی و خوش‌فرم */
    .stButton>button {
        width: 100%;
        border-radius: 16px;
        background: linear-gradient(90deg, #ec4899, #8b5cf6);
        color: #ffffff !important;
        font-weight: 800;
        border: none;
        padding: 12px 20px;
        font-size: 16px;
        box-shadow: 0 6px 20px rgba(236, 72, 153, 0.35);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.01);
        box-shadow: 0 8px 25px rgba(236, 72, 153, 0.5);
    }

    /* ورودی‌های متن */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        color: #ffffff !important;
        border-radius: 14px !important;
        font-weight: 600;
    }

    /* تنظیم رنگ متون رادیوباتن‌ها در دارک مود */
    .stRadio label, .stRadio div, .stRadio p, .stRadio span {
        font-size: 15px !important;
        color: #f1f5f9 !important;
        font-weight: 600 !important;
    }

    /* گوشه‌های گرد عکس سایدبار */
    [data-testid="stSidebar"] img {
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        border: 2px solid rgba(244, 114, 182, 0.4);
    }

    @media (max-width: 768px) {
        .hero-title { font-size: 21px; }
        .counter-val { font-size: 24px; }
    }
</style>
""",
    unsafe_allow_html=True,
)

# --- نوار کناری (Sidebar) ---
with st.sidebar:
    image_path = "photo_2026-08-28_16-40-13.jpg"
    if os.path.exists(image_path):
        st.image(
            image_path,
            caption="برای خاص‌ترین مخاطب دنیا ✨🌻",
            use_container_width=True,
        )
    else:
        st.image(
            "https://images.unsplash.com/photo-1518199266791-5375a83190b7?w=500&auto=format&fit=crop&q=60",
            caption="برای خاص‌ترین مخاطب دنیا ✨",
            use_container_width=True,
        )

    st.markdown("### 🧭 فهرست بخش‌ها")
    menu = st.radio(
        "انتخاب بخش:",
        [
            "⏳ روزشمار و لحظه‌نگار ما",
            "💬 هر سوالی داری ازم بپرس",
            "🚦 خطوط قرمز و ویژگی‌های من",
            "🕌 آزمون احکام و سوالات دینی",
            "📝 ایده‌های اولین قرارمون",
            "💌 نامه محرمانه",
        ],
        index=0,
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption("طراحی شده با تمام سلیقه و احساس ❤️")

# ==========================================
# ۱. بخش روزشمار و تقویم آشنایی
# ==========================================
if menu == "⏳ روزشمار و لحظه‌نگار ما":
    st.markdown(
        '<h1 class="hero-title">⏳ لحظه‌شمار روزهای مشترک ما</h1>',
        unsafe_allow_html=True,
    )
    st.write(
        "هنوز دستاتو از نزدیک نگرفتم، ولی تک‌تک ثانیه‌هایی که باهات حرف زدم برام"
        " باارزش‌ترین بودن."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("📅 از اولین پیامی که بهت دادم:")
        st.caption("۱۷ آگوست | ساعت ۱:۰۶ بامداد")

        # مبدا اولین پیام: ۱۷ آگوست ۲۰۲۶ ساعت ۰۱:۰۶
        start_date = datetime(2026, 8, 17, 1, 6)
        now = datetime.now()
        passed_time = now - start_date

        days_passed = max(0, passed_time.days)
        hours_passed = max(0, (passed_time.seconds // 3600))
        mins_passed = max(0, ((passed_time.seconds % 3600) // 60))

        st.markdown(
            f"""
        <div class="counter-grid">
            <div class="counter-item"><div class="counter-val">{days_passed}</div><div class="counter-label">روز</div></div>
            <div class="counter-item"><div class="counter-val">{hours_passed}</div><div class="counter-label">ساعت</div></div>
            <div class="counter-item"><div class="counter-val">{mins_passed}</div><div class="counter-label">دقیقه</div></div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='text-align:center; color:#cbd5e1; font-size:14px;"
            " margin-top:10px;'>از اون ۱:۰۶ شب به بعد، ساعت زندگیم با تو کوک شد"
            " 🌱</p>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("🎯 شمارش معکوس تا اولین دیدار حضوری:")

        meet_target = date(2026, 12, 25)
        today = date.today()
        remaining_days = (meet_target - today).days

        if remaining_days > 0:
            st.markdown(
                f"""
            <div class="counter-grid">
                <div class="counter-item" style="flex:1 1 100%;">
                    <div class="counter-val">{remaining_days}</div>
                    <div class="counter-label">روز مانده تا لحظه دیدار ☕</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p style='text-align:center; color:#cbd5e1; font-size:14px;"
                " margin-top:10px;'>روزی که بالاخره بدون صفحه گوشی می‌بینمت!</p>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="counter-val" style="text-align:center;'
                ' font-size:24px;">بالاخره رسید! 🎉</div>',
                unsafe_allow_html=True,
            )
            st.balloons()

        st.markdown("</div>", unsafe_allow_html=True)

    with st.expander("📌 یادداشت‌های مهم تقویممون"):
        st.write(
            "✨ **۱۷ آگوست - ۰۱:۰۶ بامداد:** شبی که اولین پیام رو فرستادم و"
            " داستانمون شروع شد."
        )
        st.write(
            "📞 **اولین مکالمه طولانی:** وقتی که فهمیدم ساعت‌ها حرف زدن باهات"
            " اصلاً خسته‌کننده نیست."
        )
        st.write(
            "☕ **قرار حضوری:** روزی که قراره روبروی هم بشینیم و چشم توی چشم"
            " صحبت کنیم."
        )

# ==========================================
# ۲. بخش هر سوالی داری ازم بپرس
# ==========================================
elif menu == "💬 هر سوالی داری ازم بپرس":
    st.markdown(
        '<h1 class="hero-title">💬 صندوقچه پرسش و پاسخ</h1>',
        unsafe_allow_html=True,
    )
    st.write(
        "هر سوالی که توی ذهنته، هر کنجکاوی یا هر چیزی که دوست داری ازم بدونی رو"
        " اینجا بنویس تا با کمال میل و صداقت بهت جواب بدم:"
    )

    qa_file = "user_questions.json"
    questions_list = []
    if os.path.exists(qa_file):
        try:
            with open(qa_file, "r", encoding="utf-8") as f:
                questions_list = json.load(f)
        except:
            questions_list = []

    with st.form("ask_question_form", clear_on_submit=True):
        st.markdown("#### ✍️ سوالت رو مطرح کن:")
        user_q = st.text_area(
            "اینجا بنویس برام:",
            placeholder=(
                "مثلاً: وقتی تنهایی به چی فکر می‌کنی؟ یا توی شرایط سخت واکنشت"
                " چیه؟"
            ),
        )
        q_submit = st.form_submit_button("💌 ارسال سوال به من")

    if q_submit:
        if user_q.strip():
            new_entry = {
                "question": user_q.strip(),
                "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
            questions_list.append(new_entry)
            with open(qa_file, "w", encoding="utf-8") as f:
                json.dump(questions_list, f, ensure_ascii=False, indent=2)
            st.balloons()
            st.success(
                "سوال قشنگت برام ثبت شد! حتماً با دقت و با صداقت کامل بهت جواب"
                " میدم ✨"
            )
        else:
            st.warning("لطفاً متنی برای سوالت بنویس!")

    st.markdown("---")
    st.markdown("### 💡 چند تا از پاسخ‌های شفاف من به سوالات احتمالی تو:")

    with st.expander("❓ اولویت اولت توی یک رابطه جدی چیه؟"):
        st.write(
            "شفافیت، آرامش متقابل و اینکه بتونیم در هر شرایطی بدون ترس و با"
            " احترام با هم صحبت کنیم."
        )

    with st.expander("❓ وقتی از موضوعی کلافه میشی چیکار می‌کنی؟"):
        st.write(
            "کمی سکوت می‌کنم تا منطقم سر جاش بیاد، بعدش درباره‌ش صحبت می‌کنم تا"
            " سوءتفاهمی نمونه."
        )

    with st.expander("❓ بهترین روش برای خوشحال کردنت چیه؟"):
        st.write(
            "همین که حس کنم کنارم راحتی و لبخندت از ته دله، بهترین حس دنیاست."
        )

# ==========================================
# ۳. بخش خطوط قرمز و ویژگی‌های مثبت
# ==========================================
elif menu == "🚦 خطوط قرمز و ویژگی‌های من":
    st.markdown(
        '<h1 class="hero-title">🚦 راهنمای ویژگی‌ها و مرزهای من</h1>',
        unsafe_allow_html=True,
    )
    st.write(
        "اینجا اصولی که برام ارزشمندن و خط قرمزهایی که روشون حساسم رو کاملاً"
        " شفاف نوشتم:"
    )

    col_green, col_red = st.columns(2)

    with col_green:
        st.markdown("### 🟢 اصول و ویژگی‌های مهم من")

        positive_traits = [
            (
                "منطقی بودن",
                "توی چالش‌ها و موقعیت‌های مختلف احساساتی یا تهاجمی برخورد"
                " نمی‌کنم؛ گفتگوی منطقی و آرام همیشه اولویت اول منه.",
            ),
            (
                "صبوری و درک متقابل",
                "توی روزهای سخت، بی‌حوصلگی‌ها و خستگی‌هات با آرامش کنارت می‌مونم"
                " و بدون عجله درکت می‌کنم.",
            ),
            (
                "وفاداری به پارتنر",
                "وقتی متعهد بشم، تمام تمرکز و توجهم معطوف به یک نفره و شفافیت"
                " کامل پایه رابطه‌ست.",
            ),
            (
                "شنونده امن و بدون قضاوت",
                "هر حرف یا دغدغه‌ای که داشته باشی پیش من در امانه؛ بدون سرزنش و"
                " با احترام کامل گوش میدم.",
            ),
        ]

        for title, desc in positive_traits:
            st.markdown(
                f"""
            <div class="flag-card green-flag">
                <strong>✔ {title}</strong><br>
                {desc}
            </div>
            """,
                unsafe_allow_html=True,
            )

    with col_red:
        st.markdown("### ⛔ خطوط قرمز و غیرقابل‌قبول")

        strict_boundaries = [
            (
                "خیانت",
                "چه کلامی، چه عاطفی و چه پنهان‌کاری؛ اعتماد برای من همه چیزه و"
                " خدشه‌دار شدنش جبران‌ناپذیره.",
            ),
            (
                "دروغ",
                "حقیقت حتی اگه تلخ باشه ارزشش از دروغ گفتن خیلی بیشتره؛ صداقت"
                " زیربنای همه چیزه.",
            ),
            (
                "ناخالصی داشتن",
                "تظاهر کردن، نقش بازی کردن یا شفاف نبودن حس امنیت رو از بین"
                " می‌بره؛ سادگی و رووراستی مهمه.",
            ),
        ]

        for title, desc in strict_boundaries:
            st.markdown(
                f"""
            <div class="flag-card red-flag">
                <strong>✖ {title}</strong><br>
                {desc}
            </div>
            """,
                unsafe_allow_html=True,
            )

# ==========================================
# ۴. آزمون طنز احکام و سوالات دینی
# ==========================================
elif menu == "🕌 آزمون احکام و سوالات دینی":
    st.markdown(
        '<h1 class="hero-title">🕌 آزمون طنز احکام و معارف دینی!</h1>',
        unsafe_allow_html=True,
    )
    st.write(
        "کمی با چاشنی خنده و شوخی بسنجیم ببینیم در مسائل شرعی، آداب و تقوا در چه"
        " وضعیتی هستی! 😂📿"
    )

    religious_questions = [
        {
            "q": (
                "۱. حکم شرعی بیدار شدن برای نماز صبح در حالی که پتو کشش"
                " مغناطیسی پیدا کرده چیه؟"
            ),
            "options": [
                "جهاد اکبر و مبارزه قهرمانانه با کشش پتو",
                "قضا کردن با رضایت کامل و ادامه خواب تا ظهر",
                "زدن اسنوز آلارم به مدت ۷ بار متوالی",
                (
                    "تماس با مرکز پاسخگویی به سوالات شرعی برای تخفیف در ساعت"
                    " طلوع"
                ),
            ],
            "correct": 0,
            "comment": (
                "آفرین مومن! شکستن طلسم خواب صبحگاهی ثوابی معادل عبور از کوه قاف"
                " دارد!"
            ),
        },
        {
            "q": (
                "۲. موقع وضو گرفتن، وقتی لاک ناخن یا کاشت داری فتوای کاربردی"
                " چیه؟"
            ),
            "options": [
                "تیمم جبیره‌ای به همراه استغفار از هزینه بالای ناخن‌کار",
                "فوت کردن به ناخن‌ها به نیت رفع حائل و مانع",
                "نیت قلبی مهمه؛ آب خودش راهشو پیدا می‌کنه!",
                "وضوی تصویری بدون دخالت مستقیم آب",
            ],
            "correct": 0,
            "comment": (
                "ناخن‌کارها بزرگ‌ترین چالش رساله‌های توضیح‌المسائل در عصر حاضر"
                " هستند! 😂"
            ),
        },
        {
            "q": (
                "۳. در نماز شب (تهجد)، خواندن دعای قنوت برای چه کسانی واجب‌تر"
                " است؟"
            ),
            "options": [
                "طلب صبر جمیل برای من و آرامش برای خودت",
                "۴۰ نفر از فالوورهای اینستاگرام به ترتیب حروف الفبا",
                "فقط برای تثبیت قیمت لوازم آرایشی و پوشاک",
                "طلب بخشش برای خواب موندن در نماز صبح‌های گذشته",
            ],
            "correct": 0,
            "comment": "احسنت! اولویت اول دعا همیشه پارتنر صبور و وفاداره!",
        },
        {
            "q": "۴. آداب شرعی خرید لباس و کفش زنانه قبل از نماز ظهر چیست؟",
            "options": [
                "حداقل ۳ ساعت پاساژگردی و در نهایت گفتن «هیچی نداشتن!»",
                "خرید اولین لباسی که دیده میشه (که معجزه است!)",
                "استخاره گرفتن قبل از رفتن به اتاق پرو",
                "نذر کردن برای پیدا شدن رنگ و سایز مناسب",
            ],
            "correct": 0,
            "comment": (
                "روایت داریم پاساژگردی خانم‌ها هیچ‌وقت پایان ندارد، بلکه از"
                " پاساژی به پاساژ دیگر منتقل می‌شود!"
            ),
        },
    ]

    with st.form("fiqh_quiz_form"):
        user_fiqh_answers = []
        for idx, item in enumerate(religious_questions):
            st.markdown(f"#### {item['q']}")
            ans = st.radio(
                f"انتخاب گزینه سوال {idx+1}:",
                item["options"],
                key=f"fiqh_{idx}",
                index=None,
            )
            user_fiqh_answers.append(ans)
            st.markdown("---")

        submitted_fiqh = st.form_submit_button(
            "📿 ثبت پاسخ‌ها و محاسبه درجه تقوا"
        )

    if submitted_fiqh:
        if None in user_fiqh_answers:
            st.warning(
                "حاج‌خانم لطفاً به تمام سوالات پاسخ بدید تا فتوا صادر بشه!"
            )
        else:
            score = 0
            st.balloons()
            st.markdown("### 📜 کارنامه معنوی و شرح فتاوا:")

            for idx, item in enumerate(religious_questions):
                chosen = user_fiqh_answers[idx]
                correct_text = item["options"][item["correct"]]
                if chosen == correct_text:
                    score += 1
                    st.success(
                        f"**سوال {idx+1}:** احسنت! کاملاً درست گفتی ✅\n\n💡"
                        f" *نکته شرعی:* {item['comment']}"
                    )
                else:
                    st.info(
                        f"**سوال {idx+1}:** گزینه انتخابی: {chosen}\n\n💡 *نکته"
                        f" شرعی:* {item['comment']}"
                    )
                st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                f"""
            <div class="glass-card" style="text-align:center;">
                <h2>درجه تقوای شما: {score} از {len(religious_questions)} 📿✨</h2>
                <p style="font-size:16px;">{ "ماشاالله! مدارج عالیه اجتهاد در احکام طنز رو کسب کردید! 🌸" if score >= 3 else "نیاز به تجدید دوره و قرائت مجدد رساله دارید! 😉" }</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

# ==========================================
# ۵. چک‌لیست و ایده‌های اولین قرار
# ==========================================
elif menu == "📝 ایده‌های اولین قرارمون":
    st.markdown(
        '<h1 class="hero-title">📝 چک‌لیست برنامه‌های اولین قرار</h1>',
        unsafe_allow_html=True,
    )
    st.write(
        "اینجا برنامه‌هاییه که قراره توی اولین دیدار حضوریمون دونفره تجربه"
        " کنیم:"
    )

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    c1 = st.checkbox("☕ رفتن به یه کافه دنج با نور ملایم و گفتگو بدون استرس")
    c2 = st.checkbox("🚶‍♀️ پیاده‌روی طولانی و صحبت درباره همه‌چیز")
    c3 = st.checkbox("📸 گرفتن اولین عکس دونفره یادگاری")
    c4 = st.checkbox("🍨 تست کردن یک دسر یا بستنی جدید دونفره")
    c5 = st.checkbox("🎧 گوش دادن به یه موزیک خاطره‌انگیز مشترک")
    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("💡 تو هم ایده خاصی داری؟")
    user_idea = st.text_input("ایده‌ات برای اولین دیدنمون:")
    if st.button("ثبت این ایده در دفترچه خاطرات"):
        if user_idea:
            st.success(
                f"ایده «{user_idea}» ثبت شد! حتماً عملی‌ش می‌کنیم 🌟"
            )
        else:
            st.info("چیزی ننوشتی که!")

# ==========================================
# ۶. نامه محرمانه با راهنمایی معمایی
# ==========================================
elif menu == "💌 نامه محرمانه":
    st.markdown(
        '<h1 class="hero-title">💌 صندوقچه نامه رمزدار</h1>',
        unsafe_allow_html=True,
    )
    st.write("این نامه فقط با کدی باز میشه که رازش بین خودمونه:")

    # باکس راهنمایی دلنشین و رمزآلود
    st.markdown(
        """
    <div class="glass-card" style="border-right: 4px solid #c084fc; background: rgba(192, 132, 252, 0.08);">
        <h4 style="color:#c084fc; margin-top:0;">🔍 راهنمای بازگشایی صندوقچه:</h4>
        <p style="font-size:15px; line-height:1.8; margin-bottom:0;">
        این قفل قرار نیست با یک حدس ساده باز بشه! باید به مرور زمان و با کشف تک‌تک نشانه‌ها به این رمز برسی.<br>
        شاید این رمز، ترکیب ساعتی خاص، یک کلمه کلیدی از حرف‌هامون، یا تاریخ شبی باشه که قصه‌مون شروع شد...<br>
        <em>«صبور باش، هر رازی در زمان خودش آشکار میشه ✨»</em>
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    pwd = st.text_input(
        "رمز عبور را وارد کن:",
        type="password",
        placeholder="رمز را اینجا بنویس...",
    )

    # رمزهای معتبر: ساعت اولین پیام یا تاریخ یا کلمه کلیدی
    valid_passwords = ["0106", "1:06", "17aug", "1708", "love"]

    if pwd.strip().lower() in valid_passwords:
        st.balloons()
        st.markdown(
            """
        <div class="glass-card" style="border: 2px solid #f472b6; background: rgba(244, 114, 182, 0.08);">
            <h3 style="color:#f472b6;">نامه مخصوص تو:</h3>
            <p style="font-size: 16px; line-height: 2.1; color:#fdf2f8;">
            سلام عزیز دلم،<br>
            شاید این فقط چند خط کد برنامه‌نویسی باشه، ولی تک‌تک خط‌هاش رو با فکر کردن به لبخند و نگاه قشنگت نوشتم.<br>
            درسته که هنوز از نزدیک ندیدمت و فاصله بینمونه، ولی توی قلبم نزدیک‌ترین حس ممکن رو بهت دارم.<br>
            از همون ۱۷ آگوست ساعت ۱:۰۶ بامداد که اولین کلمه بینمون رد و بدل شد، فهمیدم قراره چقدر برام خاص باشی.<br>
            بی‌صبرانه منتظر اون روزیم که این روزشمار به صفر برسه و بتونم روبروت بشینم و به چشمات نگاه کنم.<br>
            ممنونم که با حضور قشنگت، دنیام رو پر از رنگ و نور کردی ❤️🌻
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    elif pwd != "":
        st.error(
            "🔒 رمز هنوز درست نیست! نشانه‌ها رو به خاطر بسپار و به مرور زمان"
            " کشفش کن 😉"
        )

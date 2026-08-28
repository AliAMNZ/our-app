import streamlit as st
from datetime import datetime, date
import time

# --- تنظیمات اولیه صفحه ---
st.set_page_config(
    page_title="داستان ما | Our Story",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- استایل‌دهی اختصاصی و فونت راست‌چین (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;600;800&display=swap');

    * {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    /* بک‌گراند و پس‌زمینه شیشه‌ای */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
        color: #f8fafc;
    }

    /* کارت‌های شیشه‌ای (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-3px);
        border-color: rgba(244, 114, 182, 0.4);
    }

    /* کارت‌های ردفلگ و گرین‌فلگ */
    .flag-card {
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 14px;
        font-size: 15px;
        line-height: 1.8;
    }
    .red-flag {
        background: rgba(239, 68, 68, 0.12);
        border-right: 4px solid #ef4444;
        color: #fca5a5;
    }
    .green-flag {
        background: rgba(34, 197, 94, 0.12);
        border-right: 4px solid #22c55e;
        color: #86efac;
    }

    /* شمارنده بزرگ */
    .counter-box {
        text-align: center;
        background: rgba(244, 114, 182, 0.1);
        border: 1px solid rgba(244, 114, 182, 0.3);
        border-radius: 16px;
        padding: 15px;
    }
    .counter-num {
        font-size: 38px;
        font-weight: 800;
        color: #f472b6;
        direction: ltr;
        text-align: center;
    }
    .counter-lbl {
        font-size: 14px;
        color: #cbd5e1;
        text-align: center;
    }

    /* سربرگ گرادیانت */
    .gradient-title {
        background: linear-gradient(90deg, #f472b6, #c084fc, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 32px;
        margin-bottom: 10px;
    }

    /* دکمه‌ها */
    .stButton>button {
        width: 100%;
        border-radius: 14px;
        background: linear-gradient(90deg, #ec4899, #8b5cf6);
        color: white;
        font-weight: 600;
        border: none;
        padding: 12px 24px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        opacity: 0.9;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# --- نوار کناری (Sidebar) ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?w=500&auto=format&fit=crop&q=60", caption="برای خاص‌ترین مخاطب دنیا ✨", use_container_width=True)
    st.markdown("### 🧭 فهرست بخش‌ها")
    menu = st.radio(
        "",
        [
            "⏳ روزشمار و تایمر قرارمون",
            "🧩 چقدر منو می‌شناسی؟ (کوییز)",
            "🚩 دفترچه راهنما (Red & Green Flags)",
            "📝 ایده‌های اولین قرارمون (Bucket List)",
            "💌 نامه محرمانه"
        ],
        index=0
    )
    st.markdown("---")
    st.caption("طراحی شده با تمام سلیقه و عشق ❤️")

# ==========================================
# ۱. بخش روزشمار و تقویم آشنایی
# ==========================================
if menu == "⏳ روزشمار و تایمر قرارمون":
    st.markdown('<h1 class="gradient-title">⏳ لحظه‌شمار روزهای مشترک ما</h1>', unsafe_allow_html=True)
    st.write("هنوز دستاتو از نزدیک نگرفتم، ولی تک‌تک ثانیه‌هایی که باهات حرف زدم برام باارزش‌ترین بودن.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("📅 از اولین پیامی که دادیم:")
        # تاریخ شروع آشنایی (این تاریخ را به تاریخ واقعی خودتان تغییر دهید)
        start_date = datetime(2024, 1, 15, 20, 30) 
        now = datetime.now()
        passed_time = now - start_date
        
        days_passed = passed_time.days
        hours_passed = passed_time.seconds // 3600
        mins_passed = (passed_time.seconds % 3600) // 60

        subcol1, subcol2, subcol3 = st.columns(3)
        with subcol1:
            st.markdown(f'<div class="counter-box"><div class="counter-num">{days_passed}</div><div class="counter-lbl">روز</div></div>', unsafe_allow_html=True)
        with subcol2:
            st.markdown(f'<div class="counter-box"><div class="counter-num">{hours_passed}</div><div class="counter-lbl">ساعت</div></div>', unsafe_allow_html=True)
        with subcol3:
            st.markdown(f'<div class="counter-box"><div class="counter-num">{mins_passed}</div><div class="counter-lbl">دقیقه</div></div>', unsafe_allow_html=True)
        
        st.markdown("<br><p style='text-align:center; color:#cbd5e1;'>از وقتی وارد زندگیم شدی دنیام قشنگ‌تر شده 🌱</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("🎯 شمارش معکوس تا اولین دیدار حضوری:")
        
        # تاریخ هدف برای اولین قرار حضوری
        meet_target = date(2024, 12, 25)
        today = date.today()
        remaining_days = (meet_target - today).days

        if remaining_days > 0:
            st.markdown(f'<div class="counter-box"><div class="counter-num">{remaining_days}</div><div class="counter-lbl">روز مانده تا لحظه دیدار ☕</div></div>', unsafe_allow_html=True)
            st.markdown(f"<br><p style='text-align:center; color:#e2e8f0;'>روزی که بالاخره بدون صفحه گوشی می‌بینمت!</p>", unsafe_allow_html=True)
        else:
            st.markdown('<div class="counter-box"><div class="counter-num">بالاخره رسید! 🎉</div></div>', unsafe_allow_html=True)
            st.balloons()
            
        st.markdown('</div>', unsafe_allow_html=True)

    # یادداشت تقویم
    with st.expander("📌 دیدن روزهای مهم و تقویم ما"):
        st.write("- **روز اول آشنایی:** شبی که تا صبح چت کردیم و نفهمیدیم زمان چطور گذشت.")
        st.write("- **اولین تماس تلفنی:** شبی که استرس داشتم و صدات آرومم کرد.")
        st.write("- **قراره آینده:** اولین کافه‌ای که قراره با هم بریم و دسر مشترک سفارش بدیم!")

# ==========================================
# ۲. بخش کوییز شناخت من (Interactive Quiz)
# ==========================================
elif menu == "🧩 چقدر منو می‌شناسی؟ (کوییز)":
    st.markdown('<h1 class="gradient-title">🧩 آزمون شناخت من!</h1>', unsafe_allow_html=True)
    st.write("فکر می‌کنی چقدر منو شناختی؟ به سوال‌ها جواب بده تا ببینی پاسخم واقعاً چی بوده!")

    # لیست سوالات، گزینه‌ها، پاسخ صحیح و توضیحات شما
    questions = [
        {
            "q": "۱. وقتی یهویی ساکت میشم یا میرم تو فکر، علتش معمولاً چیه؟",
            "options": ["از دستت ناراحتم", "گرسنمه یا خوابم میاد", "دارم به آینده یا کار فکر می‌کنم", "باتریم تموم شده و نیاز به سکوت دارم"],
            "correct": 3,
            "answer_text": "باتریم تموم شده و نیاز به سکوت دارم",
            "my_note": "دقیقاً! وقتی ساکتم اصلاً از تو ناراحت نیستم، فقط مثل گوشی نیاز دارم یه نیم‌ساعت بزنم به شارژ!"
        },
        {
            "q": "۲. اولین چیزی که تو چت کردنامون نظرمو شدیداً بهت جلب کرد چی بود؟",
            "options": ["لحن مهربون و صمیمیتت", "حس شوخ‌طبعیت", "عکس پروفایلت", "اینکه با دقت به حرفام گوش می‌دادی"],
            "correct": 0,
            "answer_text": "لحن مهربون و صمیمیتت",
            "my_note": "صداقت و اون لحن آروم و قشنگت همون ثانیه‌های اول دلم رو برد :)"
        },
        {
            "q": "۳. نوشیدنی یا خوراکی موردعلاقه‌م برای وقتی که با هم رفتیم کافه چیه؟",
            "options": ["قهوه تلخ (اسپرسو/آمریکانو)", "هات چاکلت یا نوشیدنی خیلی شیرین", "شیک نوتلا یا میوه‌ای", "هر چی که تو سفارش بدی و نصفش کنی باهام!"],
            "correct": 3,
            "answer_text": "هر چی که تو سفارش بدی و نصفش کنی باهام!",
            "my_note": "بهترین طعم اون چیزیه که با تو شریک بشم! ولی قهوه هم کنارش باشه حله."
        },
        {
            "q": "۴. تو رابطه‌مون چی بیشترین حس آرامش رو بهم میده؟",
            "options": ["ویس‌های اول صبح و آخر شبت", "وقتی ذوق‌زدگیت رو برای اتفاقات ساده می‌بینم", "اینکه می‌تونم بدون سانسور خودم باشم", "همه موارد بالا!"],
            "correct": 3,
            "answer_text": "همه موارد بالا!",
            "my_note": "واقعاً همه ایناست؛ تک‌تک جزئیاتت برای من آرامش‌بخشن."
        }
    ]

    with st.form("quiz_form"):
        user_answers = []
        for i, item in enumerate(questions):
            st.markdown(f"#### {item['q']}")
            ans = st.radio(f"انتخاب شما برای سوال {i+1}:", item['options'], key=f"q_{i}", index=None)
            user_answers.append(ans)
            st.markdown("---")

        submitted = st.form_submit_button("✨ ثبت پاسخ‌ها و مشاهده جواب‌های واقعی من")

    if submitted:
        if None in user_answers:
            st.warning("لطفاً به همه سوال‌ها پاسخ بده بعد دکمه ثبت رو بزن!")
        else:
            score = 0
            st.balloons()
            st.markdown("### 📊 کارنامه و پاسخ‌های واقعی من:")
            
            for i, item in enumerate(questions):
                chosen = user_answers[i]
                correct_text = item["options"][item["correct"]]
                is_correct = (chosen == correct_text)
                
                if is_correct:
                    score += 1
                    st.success(f"**سوال {i+1}: کاملاً درست زدی! ✅**\n\n**پاسخ:** {correct_text}\n\n💡 *توضیح من:* {item['my_note']}")
                else:
                    st.error(f"**سوال {i+1}: اشتباه گفتی! ❌**\n\n**انتخاب تو:** {chosen}\n\n**پاسخ واقعی من:** {correct_text}\n\n💡 *توضیح من:* {item['my_note']}")
                st.markdown("<br>", unsafe_allow_html=True)
            
            # امتیاز نهایی
            st.markdown(f'<div class="glass-card" style="text-align:center;">'
                        f'<h2>امتیاز نهایی تو: {score} از {len(questions)}</h2>'
                        f'<p>{ "عالیه! تو منو حتی از خودم بهتر می‌شناسی ❤️" if score >= 3 else "خوبه! ولی هنوز کلی وقت داریم تا منو کامل کشف کنی 😉" }</p>'
                        f'</div>', unsafe_allow_html=True)

# ==========================================
# ۳. بخش ردفلگ‌ها و گرین‌فلگ‌ها (دفترچه راهنما)
# ==========================================
elif menu == "🚩 دفترچه راهنما (Red & Green Flags)":
    st.markdown('<h1 class="gradient-title">🚩 دفترچه راهنمای کاربری من!</h1>', unsafe_allow_html=True)
    st.write("اینجا اعترافات صادقانه و ویژگی‌های مثبت و منفی من برای توئه:")

    col_green, col_red = st.columns(2)

    with col_green:
        st.markdown("### 🟢 Green Flags (ویژگی‌های مثبت من)")
        
        green_flags = [
            ("همیشه شنونده خوبیم", "هر ساعتی از شبانه‌روز که حالت بد باشه یا حرف داشته باشی، گوش شنوام مال توئه."),
            ("برنامه‌ریز و پایه‌ام", "کافیه بگی بریم فلان جا، سریع همه‌چی رو هماهنگ می‌کنم."),
            ("تک‌پر و وفادار", "وقتی چشمم یکی رو بگیره، بقیه دنیا برام سیاه‌سفید میشن."),
            ("شوخ‌طبعی اختصاصی", "همیشه یه شوخی یا میم مسخره دارم تا لبخند بیارم رو لبات.")
        ]
        
        for title, desc in green_flags:
            st.markdown(f"""
            <div class="flag-card green-flag">
                <strong>🟢 {title}</strong><br>
                {desc}
            </div>
            """, unsafe_allow_html=True)

    with col_red:
        st.markdown("### 🚩 Red Flags (نقص‌ها و اخلاق‌های بدم)")
        
        red_flags = [
            ("دیر سین زدن وقتی درگیر کدم", "وقتی میرم تو فاز برنامه‌نویسی یا کار، زمان از دستم درمیره (ولی همیشه به یادتم)."),
            ("لجبازی تو بحث‌های منطقی", "گاهی زیادی روی نظر منطقیم پافشاری می‌کنم، ولی اگر حق با تو باشه تسلیمم!"),
            ("حساس روی خواب و گرسنگی", "اگه گرسنه یا بی‌خواب باشم ممکن یه ذره بی‌حوصله بشم؛ راه حل: فقط بهم شکلات بده!"),
            ("نگرانی و اورثینک", "گاهی زیادی فکرهای طولانی‌مدت می‌کنم و نیاز دارم بهم بگی: «آروم باش، درست میشه».")
        ]
        
        for title, desc in red_flags:
            st.markdown(f"""
            <div class="flag-card red-flag">
                <strong>🚩 {title}</strong><br>
                {desc}
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# ۴. باکت‌لیست اولین قرار حضوری
# ==========================================
elif menu == "📝 ایده‌های اولین قرارمون (Bucket List)":
    st.markdown('<h1 class="gradient-title">📝 چک‌لیست کارهایی که باید انجام بدیم</h1>', unsafe_allow_html=True)
    st.write("چون هنوز حضوری همو ندیدیم، اینا برنامه‌هاییه که قراره اولین بار با هم تیک بزنیم:")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    c1 = st.checkbox("☕ رفتن به یه کافه دنج با نور ملایم و موزیک خوب")
    c2 = st.checkbox("🚶‍♀️ پیاده‌روی طولانی بدون اینکه متوجه گذر زمان بشیم")
    c3 = st.checkbox("📸 گرفتن اولین عکس دونفره یادگاری")
    c4 = st.checkbox("🍦 تست کردن بدمزه‌ترین یا عجیب‌ترین طعم بستنی تو شهر با هم")
    c5 = st.checkbox("🎧 گوش دادن به یه آهنگ مشترک با یه هندزفری")
    st.markdown('</div>', unsafe_allow_html=True)

    st.subheader("💡 تو هم یه ایده به این لیست اضافه کن:")
    user_idea = st.text_input("ایده‌ات برای اولین دیدنمون:")
    if st.button("ثبت این ایده در دفترچه"):
        if user_idea:
            st.success(f"ایده «{user_idea}» ثبت شد! قول میدم عملی‌ش کنیم 🌟")
        else:
            st.info("چیزی ننوشتی که!")

# ==========================================
# ۵. نامه محرمانه
# ==========================================
elif menu == "💌 نامه محرمانه":
    st.markdown('<h1 class="gradient-title">💌 صندوقچه نامه رمزدار</h1>', unsafe_allow_html=True)
    st.write("این نامه فقط با رمزی که بین خودمونه باز میشه:")

    pwd = st.text_input("رمز عبور (مثلاً تاریخ آشناییمون یا کلمه خاصمون):", type="password")
    
    # رمز ورود دلخواهت را اینجا بگذار
    if pwd == "1234" or pwd == "love":
        st.markdown("""
        <div class="glass-card" style="border: 2px solid #f472b6;">
            <h3 style="color:#f472b6;">نامه مخصوص تو:</h3>
            <p style="font-size: 17px; line-height: 2;">
            سلام عزیز دلم،<br>
            شاید این فقط چند خط کد پایتون باشه، ولی تک‌تک خط‌هاش رو با فکر کردن به لبخند تو نوشتم.<br>
            درسته که هنوز از نزدیک ندیدمت و فاصله بینمونه، ولی تو نزدیک‌ترین حس رو به قلب من داری.<br>
            بی‌صبرانه منتظر اون روزیم که این روزشمار به صفر برسه و بتونم روبه‌روت بشینم و به چشمات نگاه کنم.<br>
            ممنونم که هستی و دنیامو زیباتر کردی ❤️
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif pwd != "":
        st.error("رمز اشتباهه! یکم بیشتر فکر کن 😉")
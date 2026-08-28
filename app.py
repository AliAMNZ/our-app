import datetime
import os
import streamlit as st
from PIL import Image

# تنظیمات صفحه
st.set_page_config(
    page_title="برای خاص‌ترین مخاطب دنیا ❤️",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# استایل اختصاصی، راست‌چین و بهینه‌سازی شده برای موبایل
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;600;700;900&display=swap');

    * {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    /* پس‌زمینه کلی نرم و مدرن */
    .stApp {
        background: radial-gradient(circle at top right, #fff1f2, #fdf4ff, #faf5ff);
        color: #1e1b4b;
    }

    /* کارت‌های شناور با گلس‌مورفیسم */
    .custom-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(244, 114, 182, 0.25);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -5px rgba(244, 63, 94, 0.08);
        transition: transform 0.2s ease;
    }

    .custom-card:hover {
        transform: translateY(-2px);
    }

    /* شمارنده‌های اختصاصی */
    .counter-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
        gap: 10px;
        margin: 15px 0;
        text-align: center;
        direction: ltr;
    }

    .counter-item {
        background: linear-gradient(135deg, #fb7185, #e11d48);
        color: white;
        padding: 12px 6px;
        border-radius: 16px;
        box-shadow: 0 6px 15px rgba(225, 29, 72, 0.25);
    }

    .counter-num {
        font-size: 1.5rem;
        font-weight: 900;
        line-height: 1.2;
    }

    .counter-lbl {
        font-size: 0.75rem;
        opacity: 0.9;
    }

    /* دکمه‌ها و فیلدها */
    .stButton > button {
        width: 100%;
        border-radius: 14px;
        background: linear-gradient(135deg, #e11d48, #be123c);
        color: white;
        font-weight: 700;
        border: none;
        padding: 10px 20px;
        box-shadow: 0 4px 14px rgba(225, 29, 72, 0.3);
    }

    .stTextInput input, .stTextArea textarea {
        border-radius: 12px !important;
        border: 1px solid #fbcfe8 !important;
        background-color: #ffffff !important;
        direction: rtl !important;
    }

    .badge-green {
        display: inline-block;
        background-color: #dcfce7;
        color: #15803d;
        padding: 6px 14px;
        border-radius: 25px;
        font-weight: 600;
        margin: 4px;
        border: 1px solid #86efac;
    }

    .badge-red {
        display: inline-block;
        background-color: #ffe4e6;
        color: #be123c;
        padding: 6px 14px;
        border-radius: 25px;
        font-weight: 600;
        margin: 4px;
        border: 1px solid #fecdd3;
    }
</style>
""",
    unsafe_allow_html=True,
)

# هدر اصلی
st.markdown(
    """
<div class="custom-card" style="text-align: center; border: 2px solid #fda4af;">
    <h2 style="color: #be123c; margin: 0; font-weight: 900; text-align: center;">✨ برای خاص‌ترین مخاطب دنیا ✨</h2>
    <p style="color: #64748b; margin-top: 8px; font-size: 0.9rem; text-align: center;">لحظه‌هایی که می‌گذرن و روزهایی که قشنگ‌تر میشن...</p>
</div>
""",
    unsafe_allow_html=True,
)

# سایدبار یا بخش پروفایل
with st.sidebar:
    st.markdown("### 🌸 تصویر اختصاصی")
    image_path = "photo_2026-08-28_16-40-13.jpg"
    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, use_container_width=True, caption="خاص‌ترین لبخند دنیا 🌻")
    else:
        st.info("عکس در کنار فایل کد قرار نگرفته است.")

# تب‌های برنامه (کاملاً بهینه‌شده برای موبایل)
tabs = st.tabs([
    "⏳ روزشمار ما",
    "🚦 خطوط قرمز و سبز من",
    "💬 بپرس ازم",
    "🕌 آزمون احکام و آداب",
    "💌 نامه محرمانه",
])

# ----------------- تب ۱: روزشمار -----------------
with tabs[0]:
    st.markdown(
        """
    <div class="custom-card">
        <h4 style="color: #9f1239;">🗓️ از اولین پیامی که بهت دادم...</h4>
        <p style="color: #475569; font-size: 0.85rem;">(۱۷ آگوست، ساعت ۰۱:۰۶ بامداد)</p>
    """,
        unsafe_allow_html=True,
    )

    # تاریخ مبدا: 17 آگوست 2026 ساعت 01:06
    start_date = datetime.datetime(2026, 8, 17, 1, 6, 0)
    now = datetime.datetime.now()

    if now >= start_date:
        diff = now - start_date
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        st.markdown(
            f"""
        <div class="counter-grid">
            <div class="counter-item"><div class="counter-num">{days}</div><div class="counter-lbl">روز</div></div>
            <div class="counter-item"><div class="counter-num">{hours}</div><div class="counter-lbl">ساعت</div></div>
            <div class="counter-item"><div class="counter-num">{minutes}</div><div class="counter-lbl">دقیقه</div></div>
            <div class="counter-item"><div class="counter-num">{seconds}</div><div class="counter-lbl">ثانیه</div></div>
        </div>
        <p style="text-align: center; color: #db2777; font-weight: 600; margin-top: 10px;">همین‌قدر گذشته و هر لحظه‌ش باارزش بوده 💫</p>
        """,
            unsafe_allow_html=True,
        )
    else:
        st.write("در انتظار رسیدن به این لحظه قشنگ...")

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- تب ۲: خط قرمزها و ویژگی‌های مثبت -----------------
with tabs[1]:
    st.markdown(
        """
    <div class="custom-card">
        <h4 style="color: #15803d;">🌱 چیزهایی که برام مهمن و ارزش دارن:</h4>
        <div style="margin-top: 10px;">
            <span class="badge-green">✔ منطقی بودن</span>
            <span class="badge-green">✔ صبوری در شرایط مختلف</span>
            <span class="badge-green">✔ وفاداری به پارتنر</span>
        </div>
        <br>
        <h4 style="color: #be123c;">⛔ چیزهایی که خط قرمز من هستن:</h4>
        <div style="margin-top: 10px;">
            <span class="badge-red">✖ خیانت</span>
            <span class="badge-red">✖ دروغ</span>
            <span class="badge-red">✖ ناخالصی داشتن و شفاف نبودن</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ----------------- تب ۳: هر سوالی داری ازم بپرس -----------------
with tabs[2]:
    st.markdown(
        """
    <div class="custom-card">
        <h4 style="color: #831843;">💭 هر سوالی گوشه ذهنت داری بنویس:</h4>
        <p style="font-size: 0.85rem; color: #64748b;">هرچیزی که دوست داری بدونی رو اینجا تایپ کن، جوابش رو بهت می‌دم!</p>
    """,
        unsafe_allow_html=True,
    )

    user_question = st.text_area(
        "سوال تو:", placeholder="مثلاً: توی فلان موقعیت چه واکنشی نشون میدی؟"
    )

    if st.button("ارسال سوال ✨"):
        if user_question.strip():
            st.success(
                "سوالت ثبت شد! حتماً جواب کامل و با جزئیاتش رو بهت میدم 🌟"
            )
            st.balloons()
        else:
            st.warning("اول سوالت رو بنویس بعد دکمه رو بزن!")

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- تب ۴: سوالات دینی و احکام طنز -----------------
with tabs[3]:
    st.markdown(
        """
    <div class="custom-card">
        <h4 style="color: #047857;">🕌 آزمون احکام، آداب و تقوا (نسخه طنز)</h4>
        <p style="font-size: 0.85rem; color: #64748b;">ببینیم چقدر به امور دینی و آداب پایبندی!</p>
    """,
        unsafe_allow_html=True,
    )

    q1 = st.radio(
        "۱. ساعت ۳ نصف شب بیدار شدی، نیتت چیه؟",
        [
            "الف) پاشم نماز شب و تهجد بخونم",
            "ب) برم سر یخچال آب بخورم و برم تو گوشی",
            "ج) چک کنم ببینم کی آنلاینه",
        ],
        index=None,
    )

    q2 = st.radio(
        "۲. نماز صبح رو چطوری اقامه می‌کنی؟",
        [
            "الف) با صدای زنگ اول بیدارم و سجاده پهنه",
            "ب) ۵ دقیقه قبل طلوع آفتاب به صورت سرعتی و فورس‌ماژور",
            "ج) نماز قضا رو برای همین روزها گذاشتن دیگه!",
        ],
        index=None,
    )

    q3 = st.radio(
        "۳. موقع وضو گرفتن، وقتی لاک داری تکلیف چیه؟",
        [
            "الف) پاک می‌کنم طبق رساله عملیه",
            "ب) روی همون وضو جبیره می‌گیرم خدا مهربونه",
            "ج) نیت قلبی مهمه، حائل مانع فیض نمیشه!",
        ],
        index=None,
    )

    if st.button("ثبت کارنامه تقوا 📿"):
        if q1 and q2 and q3:
            st.info(
                "نتیجه آزمون: تبارک‌الله! سطح تقوای شما در درجه شوخ‌طبعی اعلی قرار دارد 😄🤍"
            )
            st.snow()
        else:
            st.warning("لطفاً به تمام سوالات این فریضه پاسخ دهید!")

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- تب ۵: نامه محرمانه -----------------
with tabs[4]:
    st.markdown(
        """
    <div class="custom-card">
        <h4 style="color: #9f1239;">🔒 صندوق پیام رمزی</h4>
        <p style="font-size: 0.9rem; color: #475569; line-height: 1.8;">
            💡 <b>راهنما:</b> این یک پیام محرمانه است. برای باز کردن قفل، باید به مرور زمان و شناخت بیشتر به رمز عبور برسی...
        </p>
    """,
        unsafe_allow_html=True,
    )

    passcode = st.text_input(
        "رمز ورود را وارد کن:",
        type="password",
        placeholder="رمز عددی یا کلمه کلیدی...",
    )

    # رمز پیش‌فرض: 1708 (ماه و روز اولین پیام) - قابل تغییر به هر رمزی
    if st.button("گشودن قفل 🗝️"):
        if passcode == "1708":
            st.markdown(
                """
            <div style="background: #fff1f2; border: 1px dashed #f43f5e; padding: 15px; border-radius: 12px; margin-top: 10px;">
                <p style="color: #881337; font-weight: bold; margin: 0;">
                    🌹 متن نامه:<br>
                    از همون لحظه اول که صحبت کردیم، فهمیدم حضور تو با بقیه فرق داره. ممنونم که هستی و خوشحالم که دارمت... ❤️
                </p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.balloons()
        elif passcode == "":
            st.warning("رمز را وارد نکردی!")
        else:
            st.error("رمز اشتباه است! هنوز وقتش نرسیده یا باید بیشتر فکر کنی 😉")

    st.markdown("</div>", unsafe_allow_html=True)

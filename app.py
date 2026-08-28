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

# استایل اختصاصی با کنتراست کامل و رنگ‌های تیره خوانا
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700;900&display=swap');

    /* حذف هدر و منوهای پیش‌فرض */
    header[data-testid="stHeader"], #MainMenu, footer, .stDeployButton, 
    div[data-testid="stDecoration"], div[data-testid="stToolbar"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* اعمال فونت و رنگ تیره به تمام المان‌ها */
    html, body, [class*="css"], .stApp {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl;
        text-align: right;
        background: #fdf2f8 !important;
        color: #0f172a !important;
    }

    /* کارت‌های اصلی */
    .custom-card {
        background: #ffffff !important;
        border: 2px solid #fbcfe8 !important;
        border-radius: 20px !important;
        padding: 24px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 10px 25px rgba(225, 29, 72, 0.07) !important;
    }

    /* حل قطعی مشکل متن تب‌ها */
    button[data-baseweb="tab"] {
        background-color: #f1f5f9 !important;
        border-radius: 12px 12px 0 0 !important;
        margin-left: 6px !important;
        padding: 10px 18px !important;
        border: 1px solid #e2e8f0 !important;
        border-bottom: none !important;
    }
    
    button[data-baseweb="tab"] * {
        color: #334155 !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #ffffff !important;
        border-top: 3px solid #e11d48 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] * {
        color: #be123c !important;
        font-weight: 900 !important;
    }

    /* اصلاح رنگ متن گزینه‌های رادیویی (احکام و سوالات) */
    .stRadio label, .stRadio div, .stRadio p, .stRadio span {
        color: #0f172a !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        line-height: 1.8 !important;
    }

    /* ورودی‌های متنی */
    .stTextInput label, .stTextArea label, p, span, label {
        color: #1e293b !important;
        font-weight: 700 !important;
    }

    .stTextInput input, .stTextArea textarea {
        color: #0f172a !important;
        background-color: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }

    /* شمارنده‌های روزشمار */
    .counter-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(85px, 1fr));
        gap: 12px;
        margin: 15px 0;
        text-align: center;
        direction: ltr;
    }

    .counter-item {
        background: linear-gradient(135deg, #e11d48, #9f1239);
        color: #ffffff !important;
        padding: 14px 8px;
        border-radius: 16px;
        box-shadow: 0 8px 18px rgba(159, 18, 57, 0.25);
    }

    .counter-num {
        font-size: 1.7rem;
        font-weight: 900;
        color: #ffffff !important;
    }

    .counter-lbl {
        font-size: 0.85rem;
        font-weight: 700;
        color: #ffe4e6 !important;
    }

    /* بج‌های خط قرمز و سبز */
    .badge-green {
        display: inline-block;
        background-color: #dcfce7;
        color: #14532d !important;
        padding: 8px 18px;
        border-radius: 30px;
        font-weight: 800;
        margin: 5px;
        border: 1.5px solid #86efac;
    }

    .badge-red {
        display: inline-block;
        background-color: #ffe4e6;
        color: #881337 !important;
        padding: 8px 18px;
        border-radius: 30px;
        font-weight: 800;
        margin: 5px;
        border: 1.5px solid #fecdd3;
    }

    /* دکمه‌ها */
    .stButton > button {
        width: 100%;
        border-radius: 14px;
        background: linear-gradient(135deg, #e11d48, #be123c) !important;
        color: #ffffff !important;
        font-weight: 900 !important;
        font-size: 1rem !important;
        border: none !important;
        padding: 12px 20px;
        box-shadow: 0 4px 15px rgba(225, 29, 72, 0.25);
    }
</style>
""",
    unsafe_allow_html=True,
)

# هدر اصلی
st.markdown(
    """
<div class="custom-card" style="text-align: center; border: 2px solid #fda4af;">
    <h2 style="color: #9f1239; margin: 0; font-weight: 900; text-align: center;">✨ برای خاص‌ترین مخاطب دنیا ✨</h2>
    <p style="color: #475569; margin-top: 10px; font-size: 1rem; font-weight: 700; text-align: center;">لحظه‌هایی که می‌گذرن و روزهایی که قشنگ‌تر میشن...</p>
</div>
""",
    unsafe_allow_html=True,
)

# سایدبار
with st.sidebar:
    st.markdown(
        "<h3 style='color: #881337; font-weight: 900;'>🌸 تصویر اختصاصی</h3>",
        unsafe_allow_html=True,
    )
    image_path = "photo_2026-08-28_16-40-13.jpg"
    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, use_container_width=True, caption="خاص‌ترین لبخند دنیا 🌻")
    else:
        st.info("عکس در ریپازیتوری یافت نشد.")

# تب‌های برنامه
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
        <h3 style="color: #9f1239; font-weight: 900; margin-top: 0;">🗓️ از اولین پیامی که بهت دادم...</h3>
        <p style="color: #334155; font-size: 1rem; font-weight: 700;">(۱۷ آگوست، ساعت ۰۱:۰۶ بامداد)</p>
    """,
        unsafe_allow_html=True,
    )

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
        <p style="text-align: center; color: #9f1239; font-weight: 800; font-size: 1.05rem; margin-top: 15px;">همین‌قدر گذشته و هر لحظه‌ش باارزش بوده 💫</p>
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
        <h3 style="color: #14532d; font-weight: 900;">🌱 چیزهایی که برام مهمن و ارزش دارن:</h3>
        <div style="margin: 15px 0;">
            <span class="badge-green">✔ منطقی بودن</span>
            <span class="badge-green">✔ صبوری در شرایط مختلف</span>
            <span class="badge-green">✔ وفاداری به پارتنر</span>
        </div>
        <hr style="border: none; border-top: 1.5px dashed #cbd5e1; margin: 25px 0;">
        <h3 style="color: #881337; font-weight: 900;">⛔ چیزهایی که خط قرمز من هستن:</h3>
        <div style="margin-top: 15px;">
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
        <h3 style="color: #831843; font-weight: 900;">💭 هر سوالی گوشه ذهنت داری بنویس:</h3>
        <p style="font-size: 0.95rem; color: #334155; font-weight: 600;">هرچیزی که دوست داری بدونی رو اینجا بنویس، حتماً با دقت جواب می‌دم!</p>
    """,
        unsafe_allow_html=True,
    )

    user_question = st.text_area(
        "سوال تو:",
        placeholder="مثلاً: توی فلان موقعیت چه واکنشی نشون میدی؟",
        key="ask_box",
    )

    if st.button("ارسال سوال ✨", key="btn_ask"):
        if user_question.strip():
            st.success("سوالت ثبت شد! حتماً بهت جواب می‌دم 🌟")
            st.balloons()
        else:
            st.warning("اول سوالت رو بنویس!")

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- تب ۴: سوالات دینی و احکام طنز -----------------
with tabs[3]:
    st.markdown(
        """
    <div class="custom-card">
        <h3 style="color: #064e3b; font-weight: 900;">🕌 آزمون احکام، آداب و تقوا (نسخه طنز)</h3>
        <p style="font-size: 0.95rem; color: #334155; font-weight: 600;">ببینیم چقدر به امور معنوی و آداب پایبندی!</p>
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
        key="rad1",
    )

    q2 = st.radio(
        "۲. نماز صبح رو چطوری اقامه می‌کنی؟",
        [
            "الف) با صدای زنگ اول بیدارم و سجاده پهنه",
            "ب) ۵ دقیقه قبل طلوع آفتاب به صورت سرعتی و فورس‌ماژور",
            "ج) نماز قضا رو برای همین روزها گذاشتن دیگه!",
        ],
        index=None,
        key="rad2",
    )

    q3 = st.radio(
        "۳. موقع وضو گرفتن، وقتی لاک داری تکلیف چیه؟",
        [
            "الف) پاک می‌کنم طبق رساله عملیه",
            "ب) روی همون وضو جبیره می‌گیرم خدا مهربونه",
            "ج) نیت قلبی مهمه، حائل مانع فیض نمیشه!",
        ],
        index=None,
        key="rad3",
    )

    if st.button("ثبت کارنامه تقوا 📿", key="btn_deen"):
        if q1 and q2 and q3:
            st.info(
                "نتیجه آزمون: تبارک‌الله! سطح تقوای شما در بالاترین درجه شوخ‌طبعی قرار دارد 😄🤍"
            )
            st.snow()
        else:
            st.warning("لطفاً به تمام سوالات پاسخ بده!")

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- تب ۵: نامه محرمانه -----------------
with tabs[4]:
    st.markdown(
        """
    <div class="custom-card">
        <h3 style="color: #9f1239; font-weight: 900;">🔒 صندوق پیام رمزی</h3>
        <p style="font-size: 0.95rem; color: #1e293b; line-height: 1.8; font-weight: 600;">
            💡 <b>راهنما:</b> این یک پیام محرمانه است. برای باز کردن قفل، باید به مرور زمان و شناخت بیشتر به رمز عبور برسی...
        </p>
    """,
        unsafe_allow_html=True,
    )

    passcode = st.text_input(
        "رمز ورود را وارد کن:",
        type="password",
        placeholder="رمز عددی یا کلمه کلیدی...",
        key="secret_pwd",
    )

    if st.button("گشودن قفل 🗝️", key="btn_lock"):
        if passcode == "1708":
            st.markdown(
                """
            <div style="background: #fff1f2; border: 2px dashed #e11d48; padding: 18px; border-radius: 14px; margin-top: 15px;">
                <p style="color: #881337; font-weight: 800; margin: 0; font-size: 1.05rem; line-height: 1.8;">
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

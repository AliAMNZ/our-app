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

# استایل اختصاصی برای حذف هدر مشکی، اصلاح تب‌ها و فونت واضح
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700;900&display=swap');

    /* حذف کامل هدر مشکی و دکمه‌های منوی استریم‌لیت در بالا */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    div[data-testid="stDecoration"] {display: none;}
    div[data-testid="stToolbar"] {display: none;}

    /* اعمال فونت خوانا و استایل راست‌چین */
    * {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    .stApp {
        background: radial-gradient(circle at top right, #fff1f2, #fdf4ff, #fdf2f8) !important;
        padding-top: 1.5rem !important;
    }

    /* کارت‌های پس‌زمینه با کنتراست عالی */
    .custom-card {
        background: #ffffff !important;
        border: 1.5px solid #fbcfe8 !important;
        border-radius: 22px !important;
        padding: 22px !important;
        margin-bottom: 22px !important;
        box-shadow: 0 10px 25px rgba(225, 29, 72, 0.06) !important;
    }

    /* اصلاح رنگ تب‌ها تا کاملاً واضح و پررنگ دیده شوند */
    button[data-baseweb="tab"] {
        color: #475569 !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        background-color: transparent !important;
        border-radius: 10px 10px 0 0 !important;
        padding: 10px 16px !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #be123c !important;
        font-weight: 900 !important;
        border-bottom: 3px solid #e11d48 !important;
    }

    /* استایل شمارنده‌ها */
    .counter-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(85px, 1fr));
        gap: 12px;
        margin: 15px 0;
        text-align: center;
        direction: ltr;
    }

    .counter-item {
        background: linear-gradient(135deg, #fb7185, #e11d48);
        color: #ffffff !important;
        padding: 12px 6px;
        border-radius: 16px;
        box-shadow: 0 6px 16px rgba(225, 29, 72, 0.2);
    }

    .counter-num {
        font-size: 1.6rem;
        font-weight: 900;
        line-height: 1.2;
        color: #ffffff !important;
    }

    .counter-lbl {
        font-size: 0.8rem;
        font-weight: 600;
        color: #ffe4e6 !important;
    }

    /* برچسب‌های رنگی */
    .badge-green {
        display: inline-block;
        background-color: #dcfce7;
        color: #166534 !important;
        padding: 8px 16px;
        border-radius: 30px;
        font-weight: 700;
        margin: 5px;
        border: 1px solid #86efac;
    }

    .badge-red {
        display: inline-block;
        background-color: #ffe4e6;
        color: #9f1239 !important;
        padding: 8px 16px;
        border-radius: 30px;
        font-weight: 700;
        margin: 5px;
        border: 1px solid #fecdd3;
    }

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        background: linear-gradient(135deg, #e11d48, #be123c);
        color: white !important;
        font-weight: 800;
        border: none;
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
    <h2 style="color: #be123c; margin: 0; font-weight: 900; text-align: center;">✨ برای خاص‌ترین مخاطب دنیا ✨</h2>
    <p style="color: #475569; margin-top: 8px; font-size: 0.95rem; font-weight: 600; text-align: center;">لحظه‌هایی که می‌گذرن و روزهایی که قشنگ‌تر میشن...</p>
</div>
""",
    unsafe_allow_html=True,
)

# سایدبار
with st.sidebar:
    st.markdown("### 🌸 تصویر اختصاصی")
    image_path = "photo_2026-08-28_16-40-13.jpg"
    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, use_container_width=True, caption="خاص‌ترین لبخند دنیا 🌻")
    else:
        st.info("عکس در کنار فایل کد قرار نگرفته است.")

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
        <h3 style="color: #9f1239; font-weight: 800; margin-top: 0;">🗓️ از اولین پیامی که بهت دادم...</h3>
        <p style="color: #334155; font-size: 0.95rem; font-weight: 600;">(۱۷ آگوست، ساعت ۰۱:۰۶ بامداد)</p>
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
        <p style="text-align: center; color: #be123c; font-weight: 700; font-size: 1rem; margin-top: 15px;">همین‌قدر گذشته و هر لحظه‌ش باارزش بوده 💫</p>
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
        <h4 style="color: #166534; font-weight: 800;">🌱 چیزهایی که برام مهمن و ارزش دارن:</h4>
        <div style="margin: 12px 0;">
            <span class="badge-green">✔ منطقی بودن</span>
            <span class="badge-green">✔ صبوری در شرایط مختلف</span>
            <span class="badge-green">✔ وفاداری به پارتنر</span>
        </div>
        <hr style="border: none; border-top: 1px dashed #cbd5e1; margin: 20px 0;">
        <h4 style="color: #9f1239; font-weight: 800;">⛔ چیزهایی که خط قرمز من هستن:</h4>
        <div style="margin-top: 12px;">
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
        <h4 style="color: #831843; font-weight: 800;">💭 هر سوالی گوشه ذهنت داری بنویس:</h4>
        <p style="font-size: 0.9rem; color: #475569; font-weight: 600;">هرچیزی که دوست داری بدونی رو اینجا بنویس، حتماً با دقت جواب می‌دم!</p>
    """,
        unsafe_allow_html=True,
    )

    user_question = st.text_area(
        "سوال تو:", placeholder="مثلاً: نظرت در مورد فلان موضوع چیه؟"
    )

    if st.button("ارسال سوال ✨"):
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
        <h4 style="color: #065f46; font-weight: 800;">🕌 آزمون احکام، آداب و تقوا (نسخه طنز)</h4>
        <p style="font-size: 0.9rem; color: #475569; font-weight: 600;">ببینیم چقدر به امور معنوی و آداب پایبندی!</p>
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
        <h4 style="color: #9f1239; font-weight: 800;">🔒 صندوق پیام رمزی</h4>
        <p style="font-size: 0.95rem; color: #334155; line-height: 1.8; font-weight: 600;">
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

    if st.button("گشودن قفل 🗝️"):
        if passcode == "1708":
            st.markdown(
                """
            <div style="background: #fff1f2; border: 2px dashed #f43f5e; padding: 18px; border-radius: 14px; margin-top: 12px;">
                <p style="color: #881337; font-weight: 800; margin: 0; font-size: 1rem; line-height: 1.8;">
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

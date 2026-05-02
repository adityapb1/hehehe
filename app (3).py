import streamlit as st
import json
import os

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="For You 💖",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Load / Save Data ──────────────────────────────────────────────────────────
DATA_FILE = "data.json"

DEFAULT_DATA = {
    "password": "im@motu",
    "recipient_name": "Priyanka",
    "home_subtitle": "Just see this whenever you feel — this is for you only 🙂",
    # ↓ NEW — fully editable home welcome card text (use \n for new lines)
    "home_welcome_text": (
        "Yeh jagah sirf tere liye bani hai. Jab bhi thoda down feel ho, "
        "ya bas kuch warm chahiye — yahan aa.\n\n"
        "Our Story mein hamara safar hai 🌸, Letter mein kuch baatein hain jo "
        "main kehna chahta tha, Mood mein thoda support hai, aur Quiz mein "
        "main prove karoonga ki main tujhe kitna jaanta hoon 😄\n\n"
        "Enjoy karo — yeh sab sirf tera hai. 💖"
    ),
    "timeline": [
        {"emoji": "🙂",  "date": "13 May",        "event": "First talk 🙂",           "note": "Honestly didn't know this one small conversation would change a lot of things."},
        {"emoji": "💫",  "date": "Then",           "event": "Found a good friend 💫",   "note": "Slowly realised — yaar yeh banda actually sunta hai. Rare thing, honestly."},
        {"emoji": "💖",  "date": "25 Dec 2025",    "event": "Proposed 💖",              "note": "Dil mein hi baat atak rahi thi. But said it anyway. Best decision."},
        {"emoji": "🌸",  "date": "28 Dec 2025",    "event": "She said yes 🌸",          "note": "Uss din jo feel hua, woh words mein likhna thoda mushkil hai. But it was warm."},
        {"emoji": "📚",  "date": "Boards",         "event": "Studied together 📚",      "note": "Even stress feels manageable when someone's sitting right there with you."},
        {"emoji": "🙂",  "date": "Class 11",       "event": "Time together 🙂",         "note": "Small moments, random talks — these actually add up to something really nice."},
        {"emoji": "✨",  "date": "Class 12 — Now", "event": "Still going ✨",           "note": "Things change, but this one's still here. And that says something."},
        {"emoji": "💍",  "date": "Coming Soon",    "event": "The Wedding 💍",           "note": "Ek din yeh bhi hoga. Aur uss din ki wait worth it hogi — promise. 🌸"},
    ],
    "message": (
        "Tu thodi overthink karti hai. Yeh main pehle din se jaanta hoon. "
        "Ek chhoti si baat bhi teri mind mein teen din tak chalti rehti hai — "
        "\"usne yeh kyu bola, woh kyu hua, kya main galat tha…\" — aur phir "
        "tu khud hi exhaust ho jaati hai. Main isliye tujhe rok nahi sakta, "
        "kyunki yeh tere andar hai. But main itna zaroor jaanta hoon ki jab "
        "tu overthink karti hai, inside mein ek bahut caring aur sensitive "
        "insaan hai. Jo darta hai ki log dukhi na hon. Jo chahta hai ki sab "
        "theek rahe. Yeh overthinking koi flaw nahi hai — it's just tu thoda "
        "zyada feel karti hai. And that's actually not a bad thing.\n\n"
        "Tu gusse mein alag hi lagti hai. Yeh bhi sach hai 😄 Thodi si baat pe "
        "chhup jaana, ya phir seedha bol dena — koi beech ka raasta nahi tera. "
        "Aur jab tu gusse mein hoti hai, toh main samajh jaata hoon ki koi cheez "
        "ne andar se touch kiya hoga. Kyunki tu binu wajah gussa nahi hoti. "
        "There's always something underneath. Isliye main zyada seriously leta "
        "hoon tera gussa — argue karne ke liye nahi, but samajhne ke liye.\n\n"
        "Tu bahut socially selective hai. Yani — zindagi mein bahut saare log hain "
        "tere aas paas, but tu genuinely open nahi hoti sabke saath. Aur honestly? "
        "Mujhe yeh achha lagta hai. Tu sirf wahan open hai jahan safe lagta hai. "
        "Aur agar tu mere saath comfortable hai — toh yeh mujhe actually valuable "
        "lagta hai. Kyunki main jaanta hoon yeh sab ke saath nahi hota tere saath.\n\n"
        "Chhoti chhoti cheezein jo main notice karta hoon tere baare mein — jab tu "
        "thaka hua feel karti hai, teri baatein thodi slow ho jaati hain. Jab kuch "
        "achha hota hai, tu seedha nahi bol deti — but ek halki si smile aati hai. "
        "Jab tu pareshaan hoti hai kisi cheez se, tu khud hi usse handle karne ki "
        "koshish karti hai pehle. Yeh chhoti cheezein hain. But main notice karta hoon.\n\n"
        "Tu different hai dusron se — yeh main isliye nahi bol raha kyunki yeh bolna "
        "\"chahiye\". I'm saying it because I've actually seen it. Tu bahut logon se "
        "zyada mature sochti hai kuch cheezein mein. Aur kuch cheezein mein ekdum "
        "bacchi jaisi bhi hai — dono ek saath. Yeh combination rare hota hai.\n\n"
        "Yeh jo bhi tune read kiya — main chahta tha ki ek jagah ho jahan sab clearly "
        "likha ho. Jab bhi tu thoda down feel kare, ya confused ho, ya bas yeh feel "
        "kare ki koi nahi samjha — yahan aa. Yeh sab tere liye hi hai. "
        "Koi generic nahi, koi copy paste nahi. Sirf tera. 🌸"
    ),
    "quiz": [
        {"q": "1. 🍕 Tera favourite food kya hai?",               "options": ["Pizza","Maggi","Dosa","Paneer ki sabzi"],                                                      "answer": "Maggi"},
        {"q": "2. 😤 Jab tu gusse mein hoti hai — tu kya karti?", "options": ["Chhup jaati hoon","Seedha bol deti hoon","Ignore karti hoon","Roti hoon"],                     "answer": "Chhup jaati hoon"},
        {"q": "3. 😑 Sabse zyada annoy karne wali cheez?",         "options": ["Log overdrama karte hain","Shor bahut hota hai","Log read karke reply nahi karte","Galat grammar"],"answer": "Log read karke reply nahi karte"},
        {"q": "4. 📖 Padhne ka style kya hai tera?",               "options": ["Last minute raat jaagna","Roz thoda thoda","Group study","Notes bana ke phir padhna"],          "answer": "Last minute raat jaagna"},
        {"q": "5. 💬 Ek cheez jo tu aksar bolti hai?",             "options": ["'Haan haan theek hai'","'Pata nahi yaar'","'Main nahi jaanti'","'Chod na'"],                  "answer": "'Pata nahi yaar'"},
        {"q": "6. 🌙 Tu raat ko kab soti hai usually?",            "options": ["10-11 baje tak","12 ke baad","1-2 baje","Pata hi nahi chalta"],                               "answer": "12 ke baad"},
        {"q": "7. 🎵 Music sunti hai tension mein ya nahi?",        "options": ["Haan bilkul","Kabhi kabhi","Nahi silence prefer hai","Depends on mood"],                       "answer": "Haan bilkul"},
        {"q": "8. 👭 Social setting mein tu kaisi hoti hai?",       "options": ["Bahut baat karti hoon","Selective — sirf kuch logon se","Mostly observe karti hoon","Anywhere comfortable hoon"],"answer": "Selective — sirf kuch logon se"},
        {"q": "9. 🤔 Jab koi galat prove kare tujhe?",             "options": ["Chhod deti hoon baat","Explain karti hoon clearly","Gusse mein ho jaati hoon","Andar hi andar upset hoti hoon"],"answer": "Andar hi andar upset hoti hoon"},
        {"q": "10. 💭 Teri overthinking kab sabse zyada hoti hai?", "options": ["Raat ko sone se pehle","Kisi se ladd ne ke baad","Kuch important hone se pehle","Akele hone par"],"answer": "Raat ko sone se pehle"},
    ],
    "mood_sad":    "Ruk. Pehle ek lambi saanss le.\n\nSab cheez ek saath theek nahi hoti — aur yeh okay hai. Tu jo bhi feel kar rahi hai, woh valid hai. Main tere saath hoon. Seriously. 💖",
    "mood_angry":  "Okay okay, chill kar thodi der 😄\n\nTu gusse mein bhi cute lagti hai — but main yeh tujhe directly bolne wala nahi tha 🙂\n\nThodi der baad sab better lagega. Promise. 🌸",
    "mood_stress": "Ek kaam karo. Jo bhi book ya notes khula hai — band karo. 5 minute ke liye.\n\nTu already bahut kuch kar rahi hai. Step by step. Tu kar sakti hai — I've seen it. ✨",
    "surprise_msg": "Koi reason nahi chahiya. Koi occasion nahi chahiya.\nTu hai — yeh kaafi hai. 💖",
    "footer": "Made with 💖 — sirf tere liye, Priyanka 🌸",
    "quiz_pass_score": 7,
    "quiz_pass_msg":   "See? Main jaanta hoon tujhe 😌\nKuch cheezein words mein nahi poochhni padtein — bas dikh jaati hain.",
    "quiz_fail_msg":   "Ik u know me — thoda aur try karo! Dobara khelo 😄\nMain toh hamesha yahan hoon tere liye 💖",
    # ↓ NEW — custom "Extra Page" items added via Admin panel
    # Each item: {"type": "button"|"link"|"image"|"audio"|"text", ...fields}
    "custom_page_items": [],
    # ↓ NEW — extra page title (shown in nav + page heading)
    "extra_page_title": "⭐ From Adi",
}


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
            merged = DEFAULT_DATA.copy()
            merged.update(saved)
            # ensure new keys exist even in old data.json
            for k in ("home_welcome_text", "custom_page_items", "extra_page_title"):
                if k not in merged:
                    merged[k] = DEFAULT_DATA[k]
            return merged
        except Exception:
            pass
    return DEFAULT_DATA.copy()


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ─── Session State Init ────────────────────────────────────────────────────────
_ss_defaults = {
    "authenticated": False,
    "dev_authenticated": False,
    "mood_shown": None,
    "surprise_clicked": False,
    "current_page": "home",
    "data": None,
    "dark_mode": False,
    "pass_shown": False,
}
for _k, _v in _ss_defaults.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v

if st.session_state.data is None:
    st.session_state.data = load_data()

d    = st.session_state.data
dark = st.session_state.dark_mode

# ─── Theme colours ─────────────────────────────────────────────────────────────
if dark:
    BG, CARD, NAV = "#1a0a12", "#221018", "#2a1020"
    BORDER, INPUT_BG = "#5a2040", "#2a1020"
    TEXT_D, TEXT_M, TEXT_S = "#fce4ec", "#f8bbd0", "#ce93b4"
    PD, PM, PS, PL = "#ff6eb4", "#e8649a", "#a0405e", "#2a1020"
    MOOD_BG  = "linear-gradient(135deg,#1f0e18,#2a1020)"
    QUIZ_BG  = "linear-gradient(135deg,#221018,#2a1020)"
    PASS_BG  = "linear-gradient(135deg,#221018,#2a1020)"
    TAB_BG, DEV_BG = "#2a1020", "#221018"
    RADIO_C, SHADOW = "#f8bbd0", "rgba(255,110,180,0.25)"
else:
    BG, CARD, NAV = "#fff5f8", "#ffffff", "#ffffff"
    BORDER, INPUT_BG = "#f9c3d9", "#fff5f8"
    TEXT_D, TEXT_M, TEXT_S = "#4a2040", "#7a3a60", "#b06080"
    PD, PM, PS, PL = "#d63384", "#e8649a", "#f7a8c4", "#fde8f0"
    MOOD_BG  = "linear-gradient(135deg,#fff5f8,#fde8f0)"
    QUIZ_BG  = "linear-gradient(135deg,#fff0f5,#fde8f0)"
    PASS_BG  = "linear-gradient(135deg,#fff0f5,#fde8f0)"
    TAB_BG, DEV_BG = "#fde8f0", "#ffffff"
    RADIO_C, SHADOW = "#7a3a60", "rgba(214,51,132,0.12)"

# ─── CSS ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {{
    background: {BG} !important;
    font-family: 'Nunito', sans-serif;
    transition: background 0.4s ease;
}}
[data-testid="stAppViewContainer"]::before {{
    content: '';
    position: fixed; top:0; left:0; right:0; bottom:0;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60'%3E%3Ctext y='45' font-size='30' opacity='0.07'%3E💗%3C/text%3E%3C/svg%3E");
    background-size: 60px 60px;
    pointer-events: none; z-index: 0;
    animation: heartFloat 8s ease-in-out infinite alternate;
}}
@keyframes heartFloat {{ from{{background-position:0 0}} to{{background-position:30px 30px}} }}
[data-testid="stHeader"] {{ background: transparent !important; }}
[data-testid="stSidebar"] {{ display: none !important; }}
#MainMenu, footer, header {{ visibility: hidden; }}
.block-container {{ padding-top: 1rem !important; max-width: 780px !important; }}

/* ── PASS SUCCESS ── */
.pass-screen {{
    text-align: center; padding: 40px 20px;
    background: {PASS_BG}; border-radius: 28px; border: 2px solid {PS}; margin: 20px 0;
    animation: fadeUp 0.6s ease;
}}
.pass-hearts {{ font-size: 3.5rem; animation: bounce 1s ease infinite alternate; display: block; }}
@keyframes bounce {{ from{{transform:translateY(0)}} to{{transform:translateY(-15px)}} }}
.pass-title {{ font-size: 2.2rem; font-weight: 900; color: {PD}; font-family: 'Playfair Display', serif; margin: 16px 0 8px; }}
.pass-sub {{ font-size: 1rem; color: {TEXT_M}; font-style: italic; }}
@keyframes fadeUp {{ from{{opacity:0;transform:translateY(20px)}} to{{opacity:1;transform:translateY(0)}} }}

/* ── PASSWORD SCREEN ── */
.pw-wrapper {{
    max-width: 400px; margin: 6vh auto 0;
    background: {CARD}; border-radius: 28px; padding: 44px 40px 40px;
    box-shadow: 0 12px 50px {SHADOW}; text-align: center; border: 2px solid {BORDER};
    animation: fadeUp 0.5s ease;
}}
.pw-emoji {{ font-size: 4rem; margin-bottom: 10px; animation: pulse 2s infinite; }}
@keyframes pulse {{ 0%,100%{{transform:scale(1)}} 50%{{transform:scale(1.1)}} }}
.pw-title {{ font-size: 1.8rem; font-weight: 900; color: {PD}; margin-bottom: 6px; font-family: 'Playfair Display', serif; }}
.pw-sub {{ font-size: 0.92rem; color: {TEXT_S}; margin-bottom: 28px; }}

/* ── SECTION CARDS ── */
.section-card {{
    background: {CARD}; border: 2px solid {BORDER}; border-radius: 22px;
    padding: 28px 30px 24px; margin: 18px 0;
    box-shadow: 0 4px 24px {SHADOW}; animation: fadeUp 0.4s ease;
}}
.section-title {{
    font-size: 1.3rem; font-weight: 800; color: {PD};
    border-bottom: 2px dashed {PS}; padding-bottom: 10px; margin-bottom: 18px;
    font-family: 'Playfair Display', serif;
}}

/* ── TIMELINE ── */
.timeline-item {{ display:flex; gap:16px; margin-bottom:20px; align-items:flex-start; animation: fadeUp 0.4s ease; }}
.timeline-dot {{
    min-width:44px; height:44px; background: linear-gradient(135deg,{PD},{PM});
    border-radius:50%; display:flex; align-items:center; justify-content:center;
    font-size:1.2rem; box-shadow: 0 4px 14px {SHADOW}; flex-shrink:0;
}}
.timeline-dot.future {{
    background: linear-gradient(135deg,#f0a500,#f7c948);
    box-shadow: 0 4px 14px rgba(240,165,0,0.4);
    animation: glowPulse 2s infinite;
}}
@keyframes glowPulse {{ 0%,100%{{box-shadow:0 4px 14px rgba(240,165,0,0.4)}} 50%{{box-shadow:0 4px 22px rgba(240,165,0,0.75)}} }}
.timeline-content {{ flex:1; }}
.timeline-date {{ font-size:0.78rem; font-weight:700; color:{PM}; text-transform:uppercase; letter-spacing:0.5px; }}
.timeline-event {{ font-size:1.05rem; font-weight:800; color:{TEXT_D}; margin:2px 0 4px; }}
.timeline-note {{ font-size:0.88rem; color:{TEXT_S}; font-style:italic; line-height:1.5; }}
.timeline-connector {{ width:2px; height:18px; background:{BORDER}; margin:2px 0 2px 21px; }}

/* ── MESSAGE ── */
.message-body {{ font-size:0.97rem; color:{TEXT_M}; line-height:1.9; white-space:pre-wrap; }}

/* ── MOOD ── */
.mood-response {{
    background:{MOOD_BG}; border:2px solid {BORDER}; border-radius:18px;
    padding:20px 24px; font-size:0.97rem; color:{TEXT_D};
    line-height:1.8; margin-top:12px; animation: fadeUp 0.4s ease;
}}

/* ── QUIZ ── */
.quiz-q {{ font-size:0.97rem; font-weight:700; color:{TEXT_D}; margin-bottom:6px; }}
.quiz-result-box {{
    background:{QUIZ_BG}; border:2px solid {PS}; border-radius:22px;
    padding:28px 24px; text-align:center; margin-top:20px; animation: fadeUp 0.5s ease;
}}
.quiz-score {{ font-size:3rem; font-weight:900; color:{PD}; font-family:'Playfair Display',serif; }}
.quiz-msg {{ font-size:1.1rem; color:{TEXT_M}; margin-top:8px; font-weight:700; }}

/* ── SURPRISE ── */
.surprise-box {{ text-align:center; padding:30px 20px; }}
/* big kiss emoji row — animated float */
.kiss-row {{
    font-size:3.8rem;
    letter-spacing:6px;
    display:block;
    animation: kissFloat 1.8s ease-in-out infinite alternate;
    margin: 18px 0;
}}
@keyframes kissFloat {{ from{{transform:translateY(0) scale(1)}} to{{transform:translateY(-18px) scale(1.12)}} }}
.surprise-line {{ font-size:1.5rem; font-weight:900; color:{PD}; margin-top:10px; font-family:'Playfair Display',serif; }}

/* ── HOME HEADER ── */
.home-header {{ text-align:center; padding:24px 20px 8px; }}
.home-title {{ font-size:2.5rem; font-weight:900; color:{PD}; font-family:'Playfair Display',serif; text-shadow:0 2px 10px {SHADOW}; }}
.home-subtitle {{ font-size:1rem; color:{TEXT_S}; margin-top:8px; font-style:italic; }}

/* ── CUSTOM PAGE items ── */
.cp-text-block {{
    background:{MOOD_BG}; border:1.5px solid {BORDER}; border-radius:14px;
    padding:18px 22px; font-size:0.96rem; color:{TEXT_D}; line-height:1.8;
    margin:10px 0;
}}
.cp-img {{ width:100%; border-radius:16px; border:2px solid {BORDER}; margin:10px 0; }}
.cp-link-btn {{
    display:inline-block; background:linear-gradient(135deg,{PD},{PM});
    color:white !important; font-weight:700; font-family:'Nunito',sans-serif;
    padding:12px 28px; border-radius:14px; text-decoration:none !important;
    box-shadow:0 4px 14px {SHADOW}; margin:8px 4px; font-size:0.97rem;
    transition:all 0.2s ease;
}}
.cp-link-btn:hover {{ transform:translateY(-2px); box-shadow:0 8px 24px {SHADOW}; }}

/* ── STREAMLIT OVERRIDES ── */
.stButton>button {{
    background:linear-gradient(135deg,{PD},{PM}) !important;
    color:white !important; border:none !important; border-radius:14px !important;
    font-family:'Nunito',sans-serif !important; font-weight:700 !important;
    padding:10px 22px !important; font-size:0.97rem !important;
    box-shadow:0 4px 14px {SHADOW} !important; transition:all 0.25s !important;
}}
.stButton>button:hover {{ transform:translateY(-2px) !important; box-shadow:0 8px 24px {SHADOW} !important; }}
.stTextInput>div>div>input, .stTextArea>div>div>textarea {{
    border:2px solid {BORDER} !important; border-radius:12px !important;
    font-family:'Nunito',sans-serif !important; font-size:1rem !important;
    background:{INPUT_BG} !important; color:{TEXT_D} !important;
}}
.stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {{
    border-color:{PM} !important; box-shadow:0 0 0 3px {SHADOW} !important;
}}
.stRadio>div {{ gap:8px !important; }}
.stRadio label {{ font-family:'Nunito',sans-serif !important; color:{RADIO_C} !important; }}
.stSelectbox>div>div {{ border:2px solid {BORDER} !important; border-radius:12px !important; background:{INPUT_BG} !important; }}
div[data-testid="stMarkdownContainer"] p {{ font-family:'Nunito',sans-serif !important; color:{TEXT_M}; }}
.stNumberInput>div>div>input {{ border:2px solid {BORDER} !important; border-radius:12px !important; }}
.stTabs [data-baseweb="tab-list"] {{ gap:8px; background:{TAB_BG}; border-radius:14px; padding:6px; }}
.stTabs [data-baseweb="tab"] {{ border-radius:10px; font-family:'Nunito',sans-serif; font-weight:700; color:{TEXT_M}; }}
.stTabs [aria-selected="true"] {{ background:linear-gradient(135deg,{PD},{PM}); color:white; }}
.stSuccess {{ background:{QUIZ_BG} !important; border:1px solid {PS} !important; border-radius:14px !important; }}
.stError {{ border-radius:14px !important; }}
[data-testid="stForm"] {{ background:transparent; }}

/* ── DEV PAGE ── */
.dev-header {{
    background:linear-gradient(135deg,{PD},{PM});
    color:white; border-radius:22px; padding:28px; text-align:center; margin-bottom:24px;
}}
.dev-header h1 {{ font-family:'Playfair Display',serif; font-size:2rem; margin:0; }}
.dev-header p {{ margin:6px 0 0; opacity:0.85; font-size:0.9rem; }}
.edit-section {{ background:{DEV_BG}; border:2px solid {BORDER}; border-radius:18px; padding:22px; margin:14px 0; }}
.edit-section h3 {{ color:{PD}; font-weight:800; margin-bottom:14px; border-bottom:2px dashed {PS}; padding-bottom:8px; }}
</style>
""", unsafe_allow_html=True)

# ── Theme toggle ────────────────────────────────────────────────────────────────
toggle_label = "☀️ Light" if dark else "🌙 Dark"
tcol1, tcol2 = st.columns([5, 1])
with tcol2:
    if st.button(toggle_label, key="theme_toggle"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  DEV / ADMIN PAGE
# ══════════════════════════════════════════════════════════════════════════════
params = st.query_params
if params.get("page") == "dev" or st.session_state.current_page == "dev":
    if not st.session_state.dev_authenticated:
        st.markdown("""
        <div class="pw-wrapper">
            <div class="pw-emoji">🫣</div>
            <div class="pw-title">Admin Access</div>
            <div class="pw-sub">Sirf Adi ke liye — apna special password daalo 🔒</div>
        </div>
        """, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            dev_pw = st.text_input("", type="password", placeholder="🔑 admin password...", key="dev_pw_input")
            if st.button("Enter 🫣", use_container_width=True):
                if dev_pw == "im@adi":
                    st.session_state.dev_authenticated = True
                    st.rerun()
                else:
                    st.error("Nahi! Wrong password 😅")
        st.stop()

    st.markdown("""
    <div class="dev-header">
        <h1>🫣 Adi's Admin Panel</h1>
        <p>Yahan se sab kuch edit kar — sirf tera access hai 💪</p>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "🔑 Passwords",
        "🌸 Timeline",
        "💌 Message",
        "🧠 Quiz",
        "💆 Mood",
        "🎁 Surprise",
        "📝 General",
        "📄 Add Page",   # ← NEW TAB
    ])

    # ── TAB 0 · Passwords ────────────────────────────────────────────────────
    with tabs[0]:
        st.markdown('<div class="edit-section"><h3>🔑 Password Settings</h3>', unsafe_allow_html=True)
        new_main_pw = st.text_input("Main App Password (Priyanka ke liye)", value=d["password"])
        st.info("💡 Admin password (im@adi) is fixed in the code.")
        if st.button("Save Passwords 💾", key="save_pw"):
            d["password"] = new_main_pw
            save_data(d)
            st.success("✅ Password updated!")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 1 · Timeline ─────────────────────────────────────────────────────
    with tabs[1]:
        st.markdown('<div class="edit-section"><h3>🌸 Timeline Events</h3>', unsafe_allow_html=True)
        st.info("💍 'Coming Soon' date = gold glowing dot automatically!")
        updated_timeline = []
        for i, ev in enumerate(d["timeline"]):
            st.markdown(f"**Event {i+1}**")
            col1, col2 = st.columns([1, 3])
            with col1:
                emoji = st.text_input(f"Emoji {i+1}", value=ev["emoji"], key=f"tl_emoji_{i}")
                date  = st.text_input(f"Date {i+1}",  value=ev["date"],  key=f"tl_date_{i}")
            with col2:
                event = st.text_input(f"Title {i+1}", value=ev["event"], key=f"tl_event_{i}")
                note  = st.text_area(f"Note {i+1}",   value=ev["note"],  key=f"tl_note_{i}", height=70)
            keep = st.checkbox(f"Keep event {i+1}", value=True, key=f"tl_keep_{i}")
            if keep:
                updated_timeline.append({"emoji": emoji, "date": date, "event": event, "note": note})
            st.markdown("---")

        st.markdown("**➕ Add New Event**")
        col1, col2 = st.columns([1, 3])
        with col1:
            new_emoji = st.text_input("Emoji", "✨", key="new_tl_emoji")
            new_date  = st.text_input("Date", "Coming Soon", key="new_tl_date")
        with col2:
            new_event = st.text_input("Title", key="new_tl_event")
            new_note  = st.text_area("Note",  key="new_tl_note", height=70)
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Save Timeline 💾", key="save_tl"):
                d["timeline"] = updated_timeline
                save_data(d); st.session_state.data = d
                st.success("✅ Saved!")
        with col_b:
            if st.button("Add + Save 💾", key="save_tl2"):
                if new_event:
                    updated_timeline.append({"emoji": new_emoji, "date": new_date, "event": new_event, "note": new_note})
                d["timeline"] = updated_timeline
                save_data(d); st.session_state.data = d
                st.success("✅ Saved!")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 2 · Message ──────────────────────────────────────────────────────
    with tabs[2]:
        st.markdown('<div class="edit-section"><h3>💌 Heartfelt Message</h3>', unsafe_allow_html=True)
        st.caption("Use \\n\\n for paragraph break.")
        new_msg = st.text_area("Edit message:", value=d["message"], height=400)
        if st.button("Save Message 💾", key="save_msg"):
            d["message"] = new_msg
            save_data(d); st.session_state.data = d
            st.success("✅ Saved!")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 3 · Quiz ─────────────────────────────────────────────────────────
    with tabs[3]:
        st.markdown('<div class="edit-section"><h3>🧠 Quiz</h3>', unsafe_allow_html=True)
        new_pass_score = st.number_input("Pass score (out of 10)", min_value=1, max_value=10, value=d.get("quiz_pass_score", 7))
        new_pass_msg   = st.text_area("✅ Pass message",      value=d.get("quiz_pass_msg", ""), height=80)
        new_fail_msg   = st.text_area("😄 Low score message", value=d.get("quiz_fail_msg", ""), height=80)
        st.markdown("---")
        updated_quiz = []
        for i, q in enumerate(d["quiz"]):
            st.markdown(f"**Q{i+1}**")
            q_text   = st.text_input("Question", value=q["q"], key=f"q_text_{i}")
            opts_str = st.text_input("Options (comma separated)", value=", ".join(q["options"]), key=f"q_opts_{i}")
            ans      = st.text_input("Correct Answer", value=q["answer"], key=f"q_ans_{i}")
            keep_q   = st.checkbox("Keep", value=True, key=f"q_keep_{i}")
            if keep_q:
                updated_quiz.append({"q": q_text, "options": [o.strip() for o in opts_str.split(",")], "answer": ans})
            st.markdown("---")
        if st.button("Save Quiz 💾", key="save_quiz"):
            d["quiz"] = updated_quiz
            d["quiz_pass_score"] = int(new_pass_score)
            d["quiz_pass_msg"]   = new_pass_msg
            d["quiz_fail_msg"]   = new_fail_msg
            save_data(d); st.session_state.data = d
            st.success("✅ Saved!")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 4 · Mood ─────────────────────────────────────────────────────────
    with tabs[4]:
        st.markdown('<div class="edit-section"><h3>💆 Mood Messages</h3>', unsafe_allow_html=True)
        new_sad    = st.text_area("😔 Sad",          value=d["mood_sad"],    height=130)
        new_angry  = st.text_area("😤 Angry",        value=d["mood_angry"],  height=130)
        new_stress = st.text_area("📚 Study stress", value=d["mood_stress"], height=130)
        if st.button("Save Mood 💾", key="save_mood"):
            d["mood_sad"] = new_sad; d["mood_angry"] = new_angry; d["mood_stress"] = new_stress
            save_data(d); st.session_state.data = d
            st.success("✅ Saved!")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 5 · Surprise ─────────────────────────────────────────────────────
    with tabs[5]:
        st.markdown('<div class="edit-section"><h3>🎁 Surprise Message</h3>', unsafe_allow_html=True)
        new_surprise = st.text_area("Surprise text:", value=d["surprise_msg"], height=120)
        if st.button("Save Surprise 💾", key="save_surprise"):
            d["surprise_msg"] = new_surprise
            save_data(d); st.session_state.data = d
            st.success("✅ Saved!")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 6 · General ──────────────────────────────────────────────────────
    with tabs[6]:
        st.markdown('<div class="edit-section"><h3>📝 General Settings</h3>', unsafe_allow_html=True)
        new_name     = st.text_input("Recipient name:",  value=d["recipient_name"])
        new_subtitle = st.text_input("Home subtitle:",   value=d["home_subtitle"])
        new_footer   = st.text_input("Footer text:",     value=d["footer"])
        st.markdown("---")
        # ↓ NEW — editable home welcome body
        st.markdown("**🏠 Home Page — Welcome Card Text**")
        st.caption("Yeh text Home page ke pink card mein dikhta hai. \\n\\n = paragraph break.")
        new_welcome = st.text_area(
            "Home welcome text:",
            value=d.get("home_welcome_text", DEFAULT_DATA["home_welcome_text"]),
            height=200,
        )
        if st.button("Save General 💾", key="save_gen"):
            d["recipient_name"]    = new_name
            d["home_subtitle"]     = new_subtitle
            d["footer"]            = new_footer
            d["home_welcome_text"] = new_welcome
            save_data(d); st.session_state.data = d
            st.success("✅ Saved!")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── TAB 7 · Add Page (NEW) ────────────────────────────────────────────────
    with tabs[7]:
        st.markdown('<div class="edit-section"><h3>📄 Manage Extra Page</h3>', unsafe_allow_html=True)
        st.caption(
            "Yeh items **Extra** page pe dikhenge (nav bar mein ⭐ button). "
            "Tum button, link, image, audio ya text kuch bhi add kar sakte ho."
        )

        # ── Extra page title
        new_ep_title = st.text_input("Extra page title (nav mein dikhega):",
                                     value=d.get("extra_page_title", "⭐ From Adi"))

        st.markdown("---")
        st.markdown("#### Existing Items")

        items = d.get("custom_page_items", [])
        updated_items = []
        for i, item in enumerate(items):
            itype = item.get("type", "text")
            label_preview = item.get("label") or item.get("content","")[:40] or item.get("url","")[:40]
            with st.expander(f"Item {i+1} [{itype.upper()}] — {label_preview}", expanded=False):
                # common: keep checkbox
                keep_item = st.checkbox("Keep this item ✅", value=True, key=f"cp_keep_{i}")

                if itype == "text":
                    nc = st.text_area("Text content:", value=item.get("content",""), key=f"cp_c_{i}", height=100)
                    if keep_item:
                        updated_items.append({"type":"text","content":nc})

                elif itype == "button":
                    nl = st.text_input("Button label:", value=item.get("label",""), key=f"cp_l_{i}")
                    nu = st.text_input("Link URL:",     value=item.get("url",""),   key=f"cp_u_{i}")
                    if keep_item:
                        updated_items.append({"type":"button","label":nl,"url":nu})

                elif itype == "link":
                    nl = st.text_input("Display text:", value=item.get("label",""), key=f"cp_l_{i}")
                    nu = st.text_input("Link URL:",      value=item.get("url",""),   key=f"cp_u_{i}")
                    if keep_item:
                        updated_items.append({"type":"link","label":nl,"url":nu})

                elif itype == "image":
                    nu = st.text_input("Image URL (direct link):", value=item.get("url",""), key=f"cp_u_{i}")
                    nc = st.text_input("Caption (optional):",       value=item.get("caption",""), key=f"cp_c_{i}")
                    if keep_item:
                        updated_items.append({"type":"image","url":nu,"caption":nc})

                elif itype == "audio":
                    nu = st.text_input("Audio URL (direct .mp3 link):", value=item.get("url",""), key=f"cp_u_{i}")
                    nl = st.text_input("Label/Title:",                   value=item.get("label",""), key=f"cp_l_{i}")
                    if keep_item:
                        updated_items.append({"type":"audio","url":nu,"label":nl})

                else:
                    if keep_item:
                        updated_items.append(item)

        st.markdown("---")
        st.markdown("#### ➕ Add New Item")

        add_type = st.selectbox("What do you want to add?", [
            "📝 Text block",
            "🔘 Button (opens a link)",
            "🔗 Link (plain text link)",
            "🖼️ Image",
            "🎵 Audio / Voice Note",
        ], key="add_type_sel")

        new_item = None

        if add_type == "📝 Text block":
            ac = st.text_area("Text to show:", height=120, key="add_text_c")
            if st.button("➕ Add Text Block", key="add_txt"):
                if ac.strip():
                    new_item = {"type":"text","content":ac}

        elif add_type == "🔘 Button (opens a link)":
            al = st.text_input("Button label (e.g. 'Open Playlist 🎵')", key="add_btn_l")
            au = st.text_input("URL to open", key="add_btn_u")
            if st.button("➕ Add Button", key="add_btn"):
                if al.strip() and au.strip():
                    new_item = {"type":"button","label":al,"url":au}

        elif add_type == "🔗 Link (plain text link)":
            al = st.text_input("Display text", key="add_lnk_l")
            au = st.text_input("URL", key="add_lnk_u")
            if st.button("➕ Add Link", key="add_lnk"):
                if al.strip() and au.strip():
                    new_item = {"type":"link","label":al,"url":au}

        elif add_type == "🖼️ Image":
            au = st.text_input("Direct image URL (.jpg/.png/etc.)", key="add_img_u")
            ac = st.text_input("Caption (optional)", key="add_img_c")
            st.info("💡 Tip: Upload image to Imgur or Google Drive (public share link) and paste direct URL here.")
            if st.button("➕ Add Image", key="add_img"):
                if au.strip():
                    new_item = {"type":"image","url":au,"caption":ac}

        elif add_type == "🎵 Audio / Voice Note":
            au = st.text_input("Direct audio URL (.mp3/.ogg/.wav)", key="add_aud_u")
            al = st.text_input("Label / Title (e.g. 'Teri awaaz 🎵')", key="add_aud_l")
            st.info("💡 Tip: Upload audio to Dropbox / Google Drive (direct download link) and paste here.")
            if st.button("➕ Add Audio", key="add_aud"):
                if au.strip():
                    new_item = {"type":"audio","url":au,"label":al}

        if new_item:
            updated_items.append(new_item)
            d["custom_page_items"] = updated_items
            d["extra_page_title"]  = new_ep_title
            save_data(d); st.session_state.data = d
            st.success(f"✅ {add_type} added & saved!")
            st.rerun()

        st.markdown("---")
        if st.button("💾 Save All Extra Page Changes", key="save_cp"):
            d["custom_page_items"] = updated_items
            d["extra_page_title"]  = new_ep_title
            save_data(d); st.session_state.data = d
            st.success("✅ Extra page saved!")

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🚪 Logout from Admin"):
        st.session_state.dev_authenticated = False
        st.session_state.current_page = "home"
        st.rerun()
    st.stop()

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN PASSWORD SCREEN
# ══════════════════════════════════════════════════════════════════════════════
if not st.session_state.authenticated:
    st.markdown(f"""
    <div class="pw-wrapper">
        <div class="pw-emoji">🌸</div>
        <div class="pw-title">Hey, you found it 💖</div>
        <div class="pw-sub">Enter the password to open this little corner made just for you 🔒</div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        pw = st.text_input("", type="password", placeholder="🔑 password...", key="main_pw")
        if st.button("Open 🌸", use_container_width=True):
            if pw == d["password"]:
                st.session_state.authenticated = True
                st.rerun()
            elif pw == "im@adi":
                st.session_state.dev_authenticated = True
                st.session_state.current_page = "dev"
                st.rerun()
            else:
                st.error("Nope, that's not it 😅 Try again!")
    st.stop()

# ─── Pass flash (only once per session) ──────────────────────────────────────
if not st.session_state.pass_shown:
    st.session_state.pass_shown = True
    st.markdown(f"""
    <div class="pass-screen">
        <span class="pass-hearts">💖🌸💖🌸💖</span>
        <div class="pass-title">Hey {d['recipient_name']} 💖</div>
        <div class="pass-sub">Aa gayi tu 🌸 This little place is all yours.</div>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

# ─── Nav Bar ─────────────────────────────────────────────────────────────────
extra_nav_label = d.get("extra_page_title", "⭐ Extra")
pages = [
    ("🏠", "Home",      "home"),
    ("🌸", "Our Story", "timeline"),
    ("💌", "Letter",    "message"),
    ("💆", "Mood",      "mood"),
    ("🧠", "Quiz",      "quiz"),
    ("🎁", "Surprise",  "surprise"),
    ("⭐", extra_nav_label.replace("⭐","").strip() or "Extra", "extra"),  # NEW
    ("🫣", "Dev",       "dev"),
]
cols = st.columns(len(pages))
for i, (icon, label, key) in enumerate(pages):
    with cols[i]:
        if st.button(f"{icon} {label}", key=f"nav_{key}", use_container_width=True):
            st.session_state.current_page = key
            st.rerun()

page = st.session_state.current_page

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE RENDERS
# ══════════════════════════════════════════════════════════════════════════════

# ── HOME ─────────────────────────────────────────────────────────────────────
if page == "home":
    st.markdown(f"""
    <div class="home-header">
        <div class="home-title">Hey {d['recipient_name']} 💖</div>
        <div class="home-subtitle">{d['home_subtitle']}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # ↓ home_welcome_text is now fully editable from admin → General tab
    welcome_paras = d.get("home_welcome_text", DEFAULT_DATA["home_welcome_text"]).split("\n\n")
    welcome_html  = "".join(f"<p style='margin-bottom:14px;'>{p.strip()}</p>" for p in welcome_paras if p.strip())
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">🌸 Welcome to Your Corner</div>
        <div style="color:{TEXT_M};line-height:1.9;font-size:0.97rem;">
            {welcome_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── OUR STORY (TIMELINE) ─────────────────────────────────────────────────────
elif page == "timeline":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🌸 Our Story — One Step at a Time</div>', unsafe_allow_html=True)
    for i, ev in enumerate(d["timeline"]):
        is_future  = "coming" in ev["date"].lower() or "soon" in ev["date"].lower() or "💍" in ev["event"]
        dot_class  = "timeline-dot future" if is_future else "timeline-dot"
        connector  = "" if i == len(d["timeline"]) - 1 else '<div class="timeline-connector"></div>'
        st.markdown(f"""
        <div class="timeline-item">
            <div class="{dot_class}">{ev['emoji']}</div>
            <div class="timeline-content">
                <div class="timeline-date">{ev['date']}</div>
                <div class="timeline-event">{ev['event']}</div>
                <div class="timeline-note">{ev['note']}</div>
            </div>
        </div>{connector}
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── LETTER ───────────────────────────────────────────────────────────────────
elif page == "message":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💌 Kuch baatein — sirf tere liye</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="message-body">{d["message"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── MOOD ─────────────────────────────────────────────────────────────────────
elif page == "mood":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💆‍♀️ Mood Booster — Bata kaisi hai aaj?</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Sad 😔",          use_container_width=True): st.session_state.mood_shown = "sad"
    with col2:
        if st.button("Angry 😤",         use_container_width=True): st.session_state.mood_shown = "angry"
    with col3:
        if st.button("Study Stress 📚",  use_container_width=True): st.session_state.mood_shown = "stress"
    mood_map    = {"sad": d["mood_sad"], "angry": d["mood_angry"], "stress": d["mood_stress"]}
    mood_titles = {"sad": "Aye 😔",      "angry": "Aye gusse wali 😤", "stress": "Okay, suno 📚"}
    if st.session_state.mood_shown:
        mood = st.session_state.mood_shown
        text = mood_map[mood].replace("\n", "<br>")
        st.markdown(f"""
        <div class="mood-response">
            <strong>{mood_titles[mood]}</strong><br><br>{text}
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── QUIZ ─────────────────────────────────────────────────────────────────────
elif page == "quiz":
    quiz_questions = d["quiz"]
    pass_score     = d.get("quiz_pass_score", 7)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🧠 Do I Know You? 😄</div>', unsafe_allow_html=True)
    st.markdown(f"<p style='color:{TEXT_S};font-size:0.9rem;margin-bottom:18px;'>10 sawaal — honest answer dena. Main judge nahi karoonga 🙂 (Pass = {pass_score}/10)</p>", unsafe_allow_html=True)
    with st.form("quiz_form"):
        user_answers = {}
        for i, q in enumerate(quiz_questions):
            st.markdown(f'<div class="quiz-q">{q["q"]}</div>', unsafe_allow_html=True)
            ans = st.radio("", q["options"], key=f"q{i}", index=None, horizontal=False)
            user_answers[i] = ans
            st.markdown(f"<hr style='border:1px dashed {BORDER};margin:12px 0;'>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Check My Score 💖", use_container_width=True)
    if submitted:
        score = sum(1 for i, q in enumerate(quiz_questions) if user_answers.get(i) == q["answer"])
        if score >= pass_score:
            result_emoji = "😌✨"
            result_msg   = d.get("quiz_pass_msg", "See? Main jaanta hoon tujhe 😌")
        else:
            result_emoji = "😄💖"
            result_msg   = d.get("quiz_fail_msg", "Ik u know me — try again! 💖")
        msg_html = result_msg.replace("\n", "<br>")
        st.markdown(f"""
        <div class="quiz-result-box">
            <div style="font-size:2.5rem;">{result_emoji}</div>
            <div class="quiz-score">{score} / {len(quiz_questions)}</div>
            <div class="quiz-msg">{msg_html}</div>
        </div>
        """, unsafe_allow_html=True)
        if score < pass_score:
            if st.button("🔄 Try Again!", use_container_width=True):
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ── SURPRISE ─────────────────────────────────────────────────────────────────
elif page == "surprise":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎁 Ek last cheez...</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Click here 💖", use_container_width=True):
            st.session_state.surprise_clicked = True
    if st.session_state.surprise_clicked:
        # ↓ FIXED: only 😘 repeated 5 times + balloons across full screen
        st.balloons()
        surprise_text = d["surprise_msg"].replace("\n", "<br>")
        st.markdown(f"""
        <div class="surprise-box">
            <span class="kiss-row">😘 😘 😘 😘 😘</span>
            <div class="surprise-line">Bas aise hi 🙂</div>
            <p style="color:{TEXT_S};font-size:0.95rem;margin-top:14px;font-style:italic;line-height:1.8;">
                {surprise_text}
            </p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── EXTRA PAGE (NEW) ─────────────────────────────────────────────────────────
elif page == "extra":
    ep_title = d.get("extra_page_title", "⭐ From Adi")
    items    = d.get("custom_page_items", [])

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{ep_title}</div>', unsafe_allow_html=True)

    if not items:
        st.markdown(f"""
        <div style="text-align:center;padding:30px;color:{TEXT_S};font-size:0.95rem;">
            Yahan abhi kuch nahi hai 🌸<br>
            Admin panel → 📄 Add Page se kuch add karo!
        </div>
        """, unsafe_allow_html=True)
    else:
        for item in items:
            itype = item.get("type","text")

            if itype == "text":
                content_html = item.get("content","").replace("\n","<br>")
                st.markdown(f'<div class="cp-text-block">{content_html}</div>', unsafe_allow_html=True)

            elif itype == "button":
                url   = item.get("url","#")
                label = item.get("label","Click Me")
                st.markdown(f"""
                <div style="text-align:center;margin:12px 0;">
                    <a href="{url}" target="_blank" class="cp-link-btn">{label}</a>
                </div>
                """, unsafe_allow_html=True)

            elif itype == "link":
                url   = item.get("url","#")
                label = item.get("label", url)
                st.markdown(f"""
                <p style="text-align:center;margin:10px 0;">
                    <a href="{url}" target="_blank"
                       style="color:{PD};font-weight:700;font-size:1rem;">
                        🔗 {label}
                    </a>
                </p>
                """, unsafe_allow_html=True)

            elif itype == "image":
                url     = item.get("url","")
                caption = item.get("caption","")
                if url:
                    st.markdown(f'<img src="{url}" class="cp-img" alt="image"/>', unsafe_allow_html=True)
                    if caption:
                        st.markdown(f"<p style='text-align:center;color:{TEXT_S};font-size:0.88rem;font-style:italic;'>{caption}</p>", unsafe_allow_html=True)

            elif itype == "audio":
                url   = item.get("url","")
                label = item.get("label","🎵")
                if url:
                    st.markdown(f"<p style='color:{TEXT_M};font-weight:700;margin-bottom:6px;'>{label}</p>", unsafe_allow_html=True)
                    st.audio(url)

            st.markdown("<div style='margin:8px 0;'></div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="text-align:center;padding:30px 0 10px;color:{TEXT_S};font-size:0.85rem;">
    {d['footer']}
</div>
""", unsafe_allow_html=True)

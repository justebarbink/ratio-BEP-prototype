import streamlit as st

st.set_page_config(
    page_title="Ratio Smart Charging",
    page_icon="⚡",
    layout="centered"
)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f7faf7;
    }

    .app-title {
        font-size: 34px;
        font-weight: 800;
        color: #1f2d24;
        margin-bottom: 0px;
    }

    .subtitle {
        color: #6b6b6b;
        font-size: 16px;
        margin-bottom: 24px;
    }

    .status-card {
        background: white;
        padding: 22px;
        border-radius: 22px;
        box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    .mode-card {
        background: white;
        padding: 18px;
        border-radius: 20px;
        border: 1px solid #d9e6dc;
        box-shadow: 0px 3px 12px rgba(0,0,0,0.06);
        min-height: 155px;
        margin-bottom: 10px;
    }

    .mode-icon {
        font-size: 34px;
        margin-bottom: 8px;
    }

    .mode-title {
        font-size: 19px;
        font-weight: 800;
        color: #1f3d2b;
        margin-bottom: 4px;
    }

    .mode-text {
        font-size: 14px;
        color: #5c5c5c;
        line-height: 1.35;
    }

    .active-box {
        background: #e7f3eb;
        padding: 22px;
        border-radius: 20px;
        border-left: 6px solid #3f7d4e;
        margin-top: 28px;
        margin-bottom: 18px;
    }

    .warning-box {
        background: #fff7df;
        padding: 16px;
        border-radius: 16px;
        border-left: 5px solid #d49b00;
        margin-top: 12px;
    }

    .small-label {
        color: #6b6b6b;
        font-size: 13px;
        margin-bottom: 0px;
    }

    .big-value {
        color: #1f2d24;
        font-size: 24px;
        font-weight: 800;
        margin-top: 0px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 14px;
        padding: 0.65rem;
        font-weight: 700;
        border: 1px solid #3f7d4e;
        color: #1f3d2b;
        background-color: #eef6f0;
    }

    div.stButton > button:hover {
        background-color: #d7ebdd;
        border: 1px solid #2f6b45;
        color: #1f3d2b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Session state
# -----------------------------
if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = None

# -----------------------------
# Header
# -----------------------------
st.markdown('<p class="app-title">Ratio Smart Charging</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Kies een laadmodus die past bij jouw situatie.</p>',
    unsafe_allow_html=True
)

# -----------------------------
# Status card
# -----------------------------
st.markdown('<div class="status-card">', unsafe_allow_html=True)

st.subheader("Huidige toestand")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<p class="small-label">Batterij</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-value">42%</p>', unsafe_allow_html=True)

with col2:
    st.markdown('<p class="small-label">Gewenst bereik</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-value">70%</p>', unsafe_allow_html=True)

with col3:
    st.markdown('<p class="small-label">Vertrek</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-value">08:00</p>', unsafe_allow_html=True)

st.write("Auto is aangesloten. Het systeem kiest een laadstrategie op basis van jouw situatie.")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Visual mode menu
# -----------------------------
st.subheader("Kies een laadmodus")

modes = [
    {
        "key": "boost",
        "icon": "⚡",
        "title": "Boost-modus",
        "text": "Voor wanneer je snel weer weg moet en direct extra bereik nodig hebt.",
        "button": "Kies Boost"
    },
    {
        "key": "morgen",
        "icon": "🌙",
        "title": "Morgen klaar",
        "text": "Voor normaal avondgebruik. De auto moet morgenochtend klaar zijn.",
        "button": "Kies Morgen klaar"
    },
    {
        "key": "slim",
        "icon": "🌱",
        "title": "Slim laden",
        "text": "Het systeem zoekt de beste balans tussen goedkoop, duurzaam en bereik.",
        "button": "Kies Slim laden"
    },
    {
        "key": "vol",
        "icon": "🛣️",
        "title": "Vol bereik",
        "text": "Voor een lange rit waarbij je zekerheid wilt over voldoende actieradius.",
        "button": "Kies Vol bereik"
    },
    {
        "key": "routine",
        "icon": "📅",
        "title": "Routine",
        "text": "Voor vaste patronen zoals werk, sport of school op terugkerende momenten.",
        "button": "Kies Routine"
    },
    {
        "key": "handmatig",
        "icon": "🎛️",
        "title": "Handmatig",
        "text": "Voor gebruikers die zelf controle willen houden over tijd, kosten en laadniveau.",
        "button": "Kies Handmatig"
    }
]

# Eerste rij
row1 = st.columns(3)

for i in range(3):
    mode = modes[i]
    with row1[i]:
        st.markdown(
            f"""
            <div class="mode-card">
                <div class="mode-icon">{mode["icon"]}</div>
                <div class="mode-title">{mode["title"]}</div>
                <div class="mode-text">{mode["text"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button(mode["button"], key=mode["key"]):
            st.session_state.selected_mode = mode["key"]

# Tweede rij
row2 = st.columns(3)

for i in range(3, 6):
    mode = modes[i]
    with row2[i - 3]:
        st.markdown(
            f"""
            <div class="mode-card">
                <div class="mode-icon">{mode["icon"]}</div>
                <div class="mode-title">{mode["title"]}</div>
                <div class="mode-text">{mode["text"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button(mode["button"], key=mode["key"]):
            st.session_state.selected_mode = mode["key"]

# -----------------------------
# Detail screen after selection
# -----------------------------
selected = st.session_state.selected_mode

if selected is not None:
    st.divider()

if selected == "boost":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">⚡ Boost-modus actief</div>
            <div class="mode-text">
                De auto wordt direct opgeladen met hoge prioriteit.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("**Wat doet het systeem?**")
    st.write("- Start direct met laden")
    st.write("- Geeft prioriteit aan snelheid")
    st.write("- Optimalisatie op kosten of duurzaamheid is tijdelijk minder belangrijk")
    st.success("Verwacht toegevoegd bereik: +45 km in 30 minuten.")

elif selected == "morgen":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">🌙 Morgen klaar-modus actief</div>
            <div class="mode-text">
                De auto wordt slim opgeladen vóór de ingestelde vertrektijd.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("**Wat doet het systeem?**")
    st.write("- Plant het laden vóór de ingestelde vertrektijd")
    st.write("- Wacht indien mogelijk op een goedkoper of duurzamer moment")
    st.write("- Zorgt dat het gewenste bereik altijd gehaald wordt")

    st.markdown(
        """
        <div class="warning-box">
            <b>Safety fallback:</b><br>
            Als er geen gunstig laadmoment komt, start het systeem automatisch om 04:00.
            Zo blijft de auto op tijd klaar.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("Status: auto is op tijd klaar voor vertrek om 08:00.")

elif selected == "slim":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">🌱 Slim laden actief</div>
            <div class="mode-text">
                Het systeem kiest het beste laadmoment op basis van kosten, duurzaamheid en bereik.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    voorkeur = st.selectbox(
        "Optimalisatievoorkeur",
        ["Balans", "Goedkoop laden", "Duurzaam laden"]
    )

    st.write("**Wat doet het systeem?**")
    st.write("- Kijkt naar energieprijs")
    st.write("- Kijkt naar zonne-energie")
    st.write("- Houdt rekening met huishoudelijk energieverbruik")
    st.write("- Bewaakt altijd het gewenste bereik")

    st.info(f"Gekozen voorkeur: **{voorkeur}**")
    st.success("De auto blijft op tijd klaar.")

elif selected == "vol":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">🛣️ Vol bereik-modus actief</div>
            <div class="mode-text">
                De auto wordt opgeladen voor een lange rit met maximale zekerheid.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("**Wat doet het systeem?**")
    st.write("- Laadt tot een hoger batterijpercentage")
    st.write("- Geeft prioriteit aan zekerheid")
    st.write("- Optimaliseert alleen als er genoeg tijd overblijft")
    st.success("Gewenst laadniveau: 90% of hoger.")

elif selected == "routine":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">📅 Routine-modus actief</div>
            <div class="mode-text">
                Het systeem gebruikt vaste patronen om automatisch een laadplanning te maken.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("**Wat doet het systeem?**")
    st.write("- Gebruikt vaste vertrektijden")
    st.write("- Past het laadplan aan op herhalende gewoontes")
    st.write("- Laat de gebruiker altijd afwijken van de routine")
    st.info("Normale vertrektijd: 08:00 | Normale thuiskomst: 18:00")

elif selected == "handmatig":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">🎛️ Handmatige modus actief</div>
            <div class="mode-text">
                De gebruiker stelt zelf de belangrijkste laadinstellingen in.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    gewenst = st.slider("Gewenst batterijpercentage", 20, 100, 70)
    direct_laden = st.checkbox("Direct starten met laden")

    st.write(f"Gewenst batterijpercentage: **{gewenst}%**")

    if direct_laden:
        st.success("Laden wordt direct gestart.")
    else:
        st.info("Het systeem wacht op verdere instellingen van de gebruiker.")

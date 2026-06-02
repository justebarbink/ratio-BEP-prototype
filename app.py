import streamlit as st

st.set_page_config(
    page_title="Ratio Smart Charging",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .block-container {
        max-width: 430px;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    header {
        visibility: hidden;
    }

    body {
        background-color: #f6f8f6;
    }

    .app-title {
        text-align: center;
        font-size: 28px;
        font-weight: 800;
        color: #0f2a1d;
        margin-bottom: 0px;
    }

    .app-subtitle {
        text-align: center;
        font-size: 14px;
        color: #6a716c;
        margin-bottom: 18px;
    }

    .visual-card {
        background: white;
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 4px 18px rgba(0,0,0,0.07);
        text-align: center;
        margin-bottom: 18px;
    }

    .link-visual {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 14px;
        margin-bottom: 22px;
    }

    .device-box {
        border: 2px solid #3f7d4e;
        border-radius: 16px;
        padding: 14px 18px;
        font-weight: 800;
        color: #123322;
        background: #f8fbf9;
        font-size: 14px;
    }

    .line {
        width: 40px;
        height: 2px;
        background: #3f7d4e;
    }

    .battery-big {
        font-size: 58px;
        font-weight: 900;
        color: #2f6b45;
        line-height: 1;
    }

    .label {
        color: #6a716c;
        font-size: 14px;
        margin-top: 4px;
    }

    .status-pill {
        margin-top: 16px;
        background: #e8f2ec;
        color: #1f3d2b;
        padding: 10px;
        border-radius: 14px;
        font-weight: 700;
        font-size: 14px;
    }

    .mini-card {
        background: white;
        border-radius: 18px;
        padding: 14px 16px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.06);
        margin-bottom: 16px;
    }

    .mini-row {
        display: flex;
        justify-content: space-between;
        font-size: 15px;
        margin-bottom: 4px;
    }

    div.stButton > button {
        width: 100%;
        min-height: 95px;
        border-radius: 20px;
        border: 1px solid #d8e5dc;
        background: white;
        color: #103221;
        box-shadow: 0px 3px 12px rgba(0,0,0,0.06);
        font-size: 15px;
        font-weight: 700;
        white-space: pre-line;
        line-height: 1.25;
    }

    div.stButton > button:hover {
        background: #e8f2ec;
        border: 1px solid #3f7d4e;
        color: #103221;
    }

    .detail-header {
        text-align: center;
        margin-bottom: 12px;
    }

    .mode-icon {
        font-size: 34px;
        margin-bottom: 4px;
    }

    .mode-title {
        font-size: 27px;
        font-weight: 850;
        color: #103221;
        margin-bottom: 2px;
    }

    .mode-subtitle {
        font-size: 14px;
        color: #6a716c;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Session state
# -----------------------------
if "screen" not in st.session_state:
    st.session_state.screen = "home"

if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = None


def go_to(screen):
    st.session_state.screen = screen


def select_mode(mode):
    st.session_state.selected_mode = mode
    st.session_state.screen = "detail"


# -----------------------------
# General data
# -----------------------------
battery = 42

modes = {
    "boost": {
        "icon": "⚡",
        "name": "Boost",
        "short": "Snel extra bereik",
        "subtitle": "Voor wanneer je snel weer weg moet.",
        "status": "Laden start direct met hoge prioriteit.",
        "data": {
            "Focus": "Snelheid",
            "Verwacht": "+45 km",
            "Tijd": "30 min",
        },
        "certainty": "Deze modus kiest voor direct bruikbaar bereik. Kosten en duurzaamheid zijn tijdelijk minder belangrijk.",
        "range_slider": False,
        "preference": False,
    },
    "morning": {
        "icon": "🌙",
        "name": "Morgen klaar",
        "short": "Op tijd klaar",
        "subtitle": "Voor normaal avondgebruik.",
        "status": "De auto wordt slim opgeladen vóór de ingestelde vertrektijd.",
        "data": {
            "Vertrek": "08:00",
            "Start uiterlijk": "04:00",
            "Status": "Op tijd klaar",
        },
        "certainty": "Als er geen goedkoop of duurzaam moment komt, start het systeem automatisch op tijd.",
        "range_slider": True,
        "default_range": 70,
        "preference": False,
    },
    "smart": {
        "icon": "🌱",
        "name": "Slim laden",
        "short": "Beste balans",
        "subtitle": "Voor wanneer er geen directe haast is.",
        "status": "Het systeem kiest het meest gunstige laadmoment.",
        "data": {
            "Prijs": "Meegenomen",
            "Zon": "Meegenomen",
            "Huisverbruik": "Meegenomen",
        },
        "certainty": "Kosten en duurzaamheid worden geoptimaliseerd zolang het gewenste bereik haalbaar blijft.",
        "range_slider": True,
        "default_range": 70,
        "preference": True,
    },
    "full": {
        "icon": "▰",
        "name": "Vol bereik",
        "short": "Lange rit",
        "subtitle": "Voor wanneer er een lange rit gepland staat.",
        "status": "De auto wordt opgeladen tot een hoger laadniveau.",
        "data": {
            "Focus": "Zekerheid",
            "Advies": "90%+",
            "Optimalisatie": "Secundair",
        },
        "certainty": "De auto krijgt prioriteit boven kostenoptimalisatie, zodat er voldoende actieradius is.",
        "range_slider": True,
        "default_range": 90,
        "preference": False,
    },
    "routine": {
        "icon": "↻",
        "name": "Routine",
        "short": "Vaste patronen",
        "subtitle": "Voor terugkerend autogebruik.",
        "status": "Het laadplan volgt vaste vertrektijden en gewoontes.",
        "data": {
            "Vertrek": "08:00",
            "Thuiskomst": "18:00",
            "Aanpassen": "Altijd mogelijk",
        },
        "certainty": "Het systeem gebruikt routine als basis, maar de gebruiker kan altijd afwijken.",
        "range_slider": False,
        "preference": False,
    },
    "manual": {
        "icon": "☰",
        "name": "Handmatig",
        "short": "Zelf instellen",
        "subtitle": "Voor gebruikers die zelf controle willen houden.",
        "status": "De gebruiker bepaalt zelf de belangrijkste laadinstellingen.",
        "data": {
            "Controle": "Hoog",
            "Start": "Zelf kiezen",
            "Automatisch": "Beperkt",
        },
        "certainty": "Het systeem ondersteunt de gebruiker, maar neemt de keuze niet volledig over.",
        "range_slider": True,
        "default_range": 70,
        "preference": True,
    },
}

# -----------------------------
# Home screen
# -----------------------------
if st.session_state.screen == "home":
    st.markdown('<div class="app-title">Ratio Smart Charging</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">Slim laden vanuit één eenvoudige interface</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="visual-card">
            <div class="link-visual">
                <div class="device-box">WANDLADER</div>
                <div class="line"></div>
                <div class="device-box">EV</div>
            </div>
            <div class="battery-big">{battery}%</div>
            <div class="label">huidige batterijstatus</div>
            <div class="status-pill">Wandlader verbonden</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Laadmodus kiezen"):
        go_to("modes")
        st.rerun()

# -----------------------------
# Mode menu screen
# -----------------------------
elif st.session_state.screen == "modes":
    st.markdown('<div class="app-title">Kies laadmodus</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">Selecteer de situatie die nu het beste past</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="mini-card">
            <div class="mini-row"><span>Batterijstatus</span><b>{battery}%</b></div>
            <div class="mini-row"><span>Status</span><b>Verbonden</b></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⚡\nBoost\nSnel extra bereik"):
            select_mode("boost")
            st.rerun()

        if st.button("🌱\nSlim laden\nBeste balans"):
            select_mode("smart")
            st.rerun()

        if st.button("↻\nRoutine\nVaste patronen"):
            select_mode("routine")
            st.rerun()

    with col2:
        if st.button("🌙\nMorgen klaar\nOp tijd klaar"):
            select_mode("morning")
            st.rerun()

        if st.button("▰\nVol bereik\nLange rit"):
            select_mode("full")
            st.rerun()

        if st.button("☰\nHandmatig\nZelf instellen"):
            select_mode("manual")
            st.rerun()

    if st.button("Terug"):
        go_to("home")
        st.rerun()

# -----------------------------
# Detail screen
# -----------------------------
elif st.session_state.screen == "detail":
    mode = modes[st.session_state.selected_mode]

    st.markdown(
        f"""
        <div class="mini-card">
            <div class="mini-row"><span>Batterijstatus</span><b>{battery}%</b></div>
            <div class="mini-row"><span>Actieve modus</span><b>{mode["name"]}</b></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="detail-header">
            <div class="mode-icon">{mode["icon"]}</div>
            <div class="mode-title">{mode["name"]}</div>
            <div class="mode-subtitle">{mode["subtitle"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(mode["status"])

    if mode["range_slider"]:
        desired_range = st.slider(
            "Gewenst batterijpercentage",
            min_value=50,
            max_value=100,
            value=mode["default_range"],
            step=5
        )
    else:
        desired_range = None

    if mode["preference"]:
        preference = st.selectbox(
            "Laadvoorkeur",
            ["Balans", "Goedkoop laden", "Duurzaam laden", "Snel laden"]
        )

    st.subheader("Belangrijkste gegevens")

    data = mode["data"].copy()

    if desired_range is not None:
        data["Gewenst"] = f"{desired_range}%"

    cols = st.columns(2)
    index = 0

    for label, value in data.items():
        with cols[index % 2]:
            st.metric(label, value)
        index += 1

    st.warning(mode["certainty"])

    if st.button("Andere modus kiezen"):
        go_to("modes")
        st.rerun()

    if st.button("Startscherm"):
        go_to("home")
        st.rerun()

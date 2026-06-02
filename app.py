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
    html, body, [class*="css"] {
        font-family: Arial, sans-serif;
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 0rem;
        max-width: 430px;
    }

    header {
        visibility: hidden;
    }

    .app-screen {
        background: #f7faf7;
        border-radius: 28px;
        padding: 18px;
        min-height: 720px;
    }

    .title {
        font-size: 28px;
        font-weight: 800;
        color: #1f2d24;
        margin-bottom: 2px;
        text-align: center;
    }

    .subtitle {
        font-size: 14px;
        color: #6b6b6b;
        text-align: center;
        margin-bottom: 18px;
    }

    .connection-card {
        background: white;
        border-radius: 26px;
        padding: 24px 18px;
        text-align: center;
        box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
        margin-bottom: 18px;
    }

    .visual {
        font-size: 72px;
        margin-bottom: 8px;
    }

    .battery-big {
        font-size: 54px;
        font-weight: 900;
        color: #2f6b45;
        margin-bottom: 0px;
    }

    .battery-label {
        color: #6b6b6b;
        font-size: 14px;
        margin-top: -8px;
    }

    .mini-status {
        background: white;
        border-radius: 18px;
        padding: 12px 14px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.06);
        margin-bottom: 14px;
    }

    .mini-row {
        display: flex;
        justify-content: space-between;
        font-size: 15px;
        color: #1f2d24;
    }

    .mode-grid-title {
        font-size: 20px;
        font-weight: 800;
        color: #1f2d24;
        margin-bottom: 10px;
    }

    div.stButton > button {
        width: 100%;
        min-height: 92px;
        border-radius: 22px;
        border: 1px solid #d9e6dc;
        background: white;
        color: #1f3d2b;
        font-size: 15px;
        font-weight: 750;
        box-shadow: 0px 3px 12px rgba(0,0,0,0.06);
        white-space: pre-wrap;
        line-height: 1.2;
        padding: 0.7rem;
    }

    div.stButton > button:hover {
        background: #e7f3eb;
        border: 1px solid #3f7d4e;
        color: #1f3d2b;
    }

    .detail-card {
        background: white;
        border-radius: 26px;
        padding: 22px;
        box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
        margin-top: 10px;
        margin-bottom: 14px;
        text-align: center;
    }

    .detail-icon {
        font-size: 48px;
        margin-bottom: 4px;
    }

    .detail-title {
        font-size: 26px;
        font-weight: 900;
        color: #1f3d2b;
        margin-bottom: 4px;
    }

    .detail-subtitle {
        color: #6b6b6b;
        font-size: 14px;
        margin-bottom: 14px;
    }

    .info-box {
        background: #e7f3eb;
        border-radius: 18px;
        padding: 14px;
        margin: 10px 0;
        text-align: left;
        font-size: 15px;
        color: #1f2d24;
    }

    .warning-box {
        background: #fff7df;
        border-radius: 18px;
        padding: 13px;
        margin-top: 10px;
        text-align: left;
        font-size: 14px;
        color: #1f2d24;
    }

    .small-note {
        text-align: center;
        color: #777;
        font-size: 13px;
        margin-top: 8px;
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
# Data
# -----------------------------
battery = "42%"
desired = "70%"
departure = "08:00"

mode_data = {
    "boost": {
        "icon": "⚡",
        "title": "Boost",
        "subtitle": "Direct extra bereik",
        "status": "Laden start direct.",
        "info": [
            "Prioriteit: snelheid",
            "Verwacht: +45 km in 30 min",
            "Kosten/duurzaamheid tijdelijk minder belangrijk"
        ],
        "note": "Voor als je snel weer weg moet."
    },
    "morgen": {
        "icon": "🌙",
        "title": "Morgen klaar",
        "subtitle": "Klaar op vertrektijd",
        "status": "Auto is op tijd klaar.",
        "info": [
            "Vertrek: 08:00",
            "Gewenst bereik: 70%",
            "Start uiterlijk: 04:00"
        ],
        "note": "Wacht op gunstig moment, maar laadt op tijd."
    },
    "slim": {
        "icon": "🌱",
        "title": "Slim laden",
        "subtitle": "Balans tussen kosten en duurzaam",
        "status": "Systeem kiest beste laadmoment.",
        "info": [
            "Voorkeur: balans",
            "Let op prijs, zon en huisverbruik",
            "Bereik blijft gegarandeerd"
        ],
        "note": "Voor als er geen haast is."
    },
    "vol": {
        "icon": "🛣️",
        "title": "Vol bereik",
        "subtitle": "Voor lange ritten",
        "status": "Laden naar hoog bereik.",
        "info": [
            "Doel: 90% of hoger",
            "Prioriteit: zekerheid",
            "Optimaliseert alleen als er tijd is"
        ],
        "note": "Voor geplande lange ritten."
    },
    "routine": {
        "icon": "📅",
        "title": "Routine",
        "subtitle": "Voor vaste gewoontes",
        "status": "Laadplan volgt jouw ritme.",
        "info": [
            "Vertrek meestal: 08:00",
            "Thuiskomst meestal: 18:00",
            "Afwijken kan altijd"
        ],
        "note": "Voor dagelijks terugkerend gebruik."
    },
    "handmatig": {
        "icon": "🎛️",
        "title": "Handmatig",
        "subtitle": "Zelf controle houden",
        "status": "Jij kiest de instellingen.",
        "info": [
            "Kies laadniveau",
            "Kies startmoment",
            "Kies snel, goedkoop of duurzaam"
        ],
        "note": "Voor maximale controle."
    }
}

# -----------------------------
# Home screen
# -----------------------------
if st.session_state.screen == "home":
    st.markdown('<div class="app-screen">', unsafe_allow_html=True)

    st.markdown('<div class="title">Ratio Smart Charging</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Auto en wandlader zijn verbonden</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="connection-card">
            <div class="visual">🚗⚡🔌</div>
            <div class="battery-big">{battery}</div>
            <div class="battery-label">huidige batterij</div>
            <br>
            <b>Wandlader gekoppeld</b><br>
            <span style="color:#6b6b6b;">Klaar om slim te laden</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Bekijk laadmodi"):
        go_to("modes")
        st.rerun()

    st.markdown('<div class="small-note">Tik om een laadstrategie te kiezen</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Mode menu screen
# -----------------------------
elif st.session_state.screen == "modes":
    st.markdown('<div class="app-screen">', unsafe_allow_html=True)

    st.markdown('<div class="title">Kies laadmodus</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Welke situatie past nu het best?</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="mini-status">
            <div class="mini-row"><span>Batterij</span><b>{battery}</b></div>
            <div class="mini-row"><span>Gewenst bereik</span><b>{desired}</b></div>
            <div class="mini-row"><span>Vertrek</span><b>{departure}</b></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⚡\nBoost\nSnel weg"):
            select_mode("boost")
            st.rerun()

        if st.button("🌱\nSlim laden\nBeste balans"):
            select_mode("slim")
            st.rerun()

        if st.button("📅\nRoutine\nVaste ritmes"):
            select_mode("routine")
            st.rerun()

    with col2:
        if st.button("🌙\nMorgen klaar\nOp tijd klaar"):
            select_mode("morgen")
            st.rerun()

        if st.button("🛣️\nVol bereik\nLange rit"):
            select_mode("vol")
            st.rerun()

        if st.button("🎛️\nHandmatig\nZelf kiezen"):
            select_mode("handmatig")
            st.rerun()

    if st.button("Terug naar start"):
        go_to("home")
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Detail screen
# -----------------------------
elif st.session_state.screen == "detail":
    mode = mode_data[st.session_state.selected_mode]

    st.markdown('<div class="app-screen">', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="mini-status">
            <div class="mini-row"><span>Batterij</span><b>{battery}</b></div>
            <div class="mini-row"><span>Vertrek</span><b>{departure}</b></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    info_items = "".join([f"<li>{item}</li>" for item in mode["info"]])

    st.markdown(
        f"""
        <div class="detail-card">
            <div class="detail-icon">{mode["icon"]}</div>
            <div class="detail-title">{mode["title"]}</div>
            <div class="detail-subtitle">{mode["subtitle"]}</div>

            <div class="info-box">
                <b>Status:</b><br>
                {mode["status"]}
            </div>

            <div class="info-box">
                <b>Belangrijkste gegevens:</b>
                <ul>
                    {info_items}
                </ul>
            </div>

            <div class="warning-box">
                <b>Zekerheidsregel:</b><br>
                De auto moet altijd voldoende bereik hebben op het gewenste vertrekmoment.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Andere laadmodus kiezen"):
        go_to("modes")
        st.rerun()

    if st.button("Terug naar start"):
        go_to("home")
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

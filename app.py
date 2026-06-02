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
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background-color: #f5f7f5;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        max-width: 430px;
    }

    header {
        visibility: hidden;
    }

    .app-screen {
        background: #f5f7f5;
        border-radius: 28px;
        padding: 18px;
        min-height: 710px;
    }

    .app-title {
        font-size: 28px;
        font-weight: 800;
        color: #14251b;
        text-align: center;
        margin-bottom: 4px;
    }

    .app-subtitle {
        font-size: 14px;
        color: #66706a;
        text-align: center;
        margin-bottom: 18px;
    }

    .connection-card {
        background: white;
        border-radius: 26px;
        padding: 24px 20px;
        box-shadow: 0px 4px 18px rgba(0,0,0,0.07);
        margin-bottom: 18px;
        text-align: center;
    }

    .connection-visual {
        width: 100%;
        height: 130px;
        border-radius: 22px;
        background: linear-gradient(135deg, #edf4ef, #ffffff);
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 18px;
        border: 1px solid #dbe8df;
    }

    .visual-line {
        display: flex;
        align-items: center;
        gap: 16px;
        font-size: 15px;
        color: #1f3d2b;
        font-weight: 700;
    }

    .visual-box {
        border: 2px solid #3f7d4e;
        border-radius: 14px;
        padding: 13px 16px;
        min-width: 70px;
        background: white;
    }

    .visual-connector {
        width: 48px;
        height: 2px;
        background: #3f7d4e;
        position: relative;
    }

    .visual-connector:after {
        content: "";
        position: absolute;
        right: -2px;
        top: -4px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #3f7d4e;
    }

    .battery-percentage {
        font-size: 56px;
        font-weight: 900;
        color: #2f6b45;
        margin-bottom: 0px;
    }

    .battery-label {
        color: #66706a;
        font-size: 14px;
        margin-top: -6px;
        margin-bottom: 16px;
    }

    .system-status {
        background: #e9f3ed;
        color: #1f3d2b;
        padding: 12px 14px;
        border-radius: 16px;
        font-size: 14px;
        font-weight: 600;
    }

    .mini-status {
        background: white;
        border-radius: 18px;
        padding: 13px 15px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.06);
        margin-bottom: 14px;
    }

    .mini-row {
        display: flex;
        justify-content: space-between;
        font-size: 15px;
        color: #14251b;
        margin-bottom: 3px;
    }

    .screen-title {
        font-size: 24px;
        font-weight: 850;
        color: #14251b;
        text-align: center;
        margin-bottom: 4px;
    }

    .screen-subtitle {
        font-size: 14px;
        color: #66706a;
        text-align: center;
        margin-bottom: 16px;
    }

    div.stButton > button {
        width: 100%;
        min-height: 86px;
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

    .mode-symbol {
        width: 52px;
        height: 52px;
        border-radius: 18px;
        background: #e7f3eb;
        color: #2f6b45;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        font-weight: 900;
        margin: 0 auto 12px auto;
    }

    .detail-title {
        font-size: 25px;
        font-weight: 900;
        color: #1f3d2b;
        margin-bottom: 4px;
    }

    .detail-subtitle {
        color: #66706a;
        font-size: 14px;
        margin-bottom: 14px;
    }

    .info-box {
        background: #e9f3ed;
        border-radius: 18px;
        padding: 14px;
        margin: 10px 0;
        text-align: left;
        font-size: 15px;
        color: #14251b;
    }

    .warning-box {
        background: #fff7df;
        border-radius: 18px;
        padding: 13px;
        margin-top: 10px;
        text-align: left;
        font-size: 14px;
        color: #14251b;
    }

    .data-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-top: 10px;
    }

    .data-item {
        background: #f5f7f5;
        border-radius: 16px;
        padding: 12px;
        text-align: center;
    }

    .data-label {
        font-size: 12px;
        color: #66706a;
    }

    .data-value {
        font-size: 19px;
        font-weight: 850;
        color: #14251b;
    }

    .small-note {
        text-align: center;
        color: #777;
        font-size: 13px;
        margin-top: 8px;
    }

    label {
        font-weight: 650 !important;
        color: #14251b !important;
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
departure = "08:00"
connection_status = "Wandlader verbonden"


mode_data = {
    "boost": {
        "symbol": "B",
        "title": "Boost",
        "subtitle": "Direct extra bereik",
        "status": "Laden start direct met hoge prioriteit.",
        "items": [
            ("Focus", "Snelheid"),
            ("Verwacht", "+45 km"),
            ("Tijd", "30 min"),
            ("Optimalisatie", "Uitgesteld"),
        ],
        "certainty": "Deze modus kiest voor snel bruikbaar bereik in plaats van goedkoop of duurzaam laden.",
        "needs_range_input": False,
    },
    "morgen": {
        "symbol": "M",
        "title": "Morgen klaar",
        "subtitle": "Klaar op vertrektijd",
        "status": "Het systeem plant laden vóór de ingestelde vertrektijd.",
        "items": [
            ("Vertrek", "08:00"),
            ("Start uiterlijk", "04:00"),
            ("Voorkeur", "Balans"),
            ("Status", "Op tijd klaar"),
        ],
        "certainty": "Als er geen gunstig laadmoment komt, start het systeem automatisch op tijd.",
        "needs_range_input": True,
        "default_range": 70,
    },
    "slim": {
        "symbol": "S",
        "title": "Slim laden",
        "subtitle": "Balans tussen kosten en duurzaamheid",
        "status": "Het systeem kiest het meest gunstige laadmoment.",
        "items": [
            ("Prijs", "Meegenomen"),
            ("Zon", "Meegenomen"),
            ("Huisverbruik", "Meegenomen"),
            ("Status", "Bewaakt"),
        ],
        "certainty": "Kosten en duurzaamheid worden geoptimaliseerd zolang het gewenste bereik haalbaar blijft.",
        "needs_range_input": True,
        "default_range": 70,
    },
    "vol": {
        "symbol": "V",
        "title": "Vol bereik",
        "subtitle": "Voor een geplande lange rit",
        "status": "De auto wordt opgeladen tot een hoog laadniveau.",
        "items": [
            ("Focus", "Zekerheid"),
            ("Advies", "90%+"),
            ("Route", "Lange rit"),
            ("Optimalisatie", "Secundair"),
        ],
        "certainty": "De auto krijgt prioriteit boven kostenoptimalisatie, zodat er voldoende actieradius is.",
        "needs_range_input": True,
        "default_range": 90,
    },
    "routine": {
        "symbol": "R",
        "title": "Routine",
        "subtitle": "Voor vaste gebruikspatronen",
        "status": "Het laadplan volgt terugkerende vertrektijden.",
        "items": [
            ("Vertrek", "08:00"),
            ("Thuiskomst", "18:00"),
            ("Patroon", "Werkweek"),
            ("Afwijken", "Altijd mogelijk"),
        ],
        "certainty": "Het systeem gebruikt routine als basis, maar de gebruiker kan altijd wijzigen.",
        "needs_range_input": False,
    },
    "handmatig": {
        "symbol": "H",
        "title": "Handmatig",
        "subtitle": "Zelf controle houden",
        "status": "De gebruiker bepaalt zelf de belangrijkste laadinstellingen.",
        "items": [
            ("Start", "Zelf kiezen"),
            ("Voorkeur", "Zelf kiezen"),
            ("Controle", "Hoog"),
            ("Automatisch", "Beperkt"),
        ],
        "certainty": "Het systeem ondersteunt de gebruiker, maar neemt de keuze niet volledig over.",
        "needs_range_input": True,
        "default_range": 70,
    },
}


# -----------------------------
# Home screen
# -----------------------------
if st.session_state.screen == "home":
    st.markdown('<div class="app-screen">', unsafe_allow_html=True)

    st.markdown('<div class="app-title">Ratio Smart Charging</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">Slim laden vanuit één eenvoudige interface</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="connection-card">
            <div class="connection-visual">
                <div class="visual-line">
                    <div class="visual-box">WANDLADER</div>
                    <div class="visual-connector"></div>
                    <div class="visual-box">EV</div>
                </div>
            </div>

            <div class="battery-percentage">{battery}%</div>
            <div class="battery-label">huidige batterijstatus</div>

            <div class="system-status">{connection_status}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Laadmodus kiezen"):
        go_to("modes")
        st.rerun()

    st.markdown(
        '<div class="small-note">Tik om een laadstrategie te selecteren</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Mode menu screen
# -----------------------------
elif st.session_state.screen == "modes":
    st.markdown('<div class="app-screen">', unsafe_allow_html=True)

    st.markdown('<div class="screen-title">Kies laadmodus</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="screen-subtitle">Selecteer de situatie die nu het beste past</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="mini-status">
            <div class="mini-row"><span>Batterijstatus</span><b>{battery}%</b></div>
            <div class="mini-row"><span>Status</span><b>Verbonden</b></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("B\nBoost\nSnel extra bereik"):
            select_mode("boost")
            st.rerun()

        if st.button("S\nSlim laden\nBeste balans"):
            select_mode("slim")
            st.rerun()

        if st.button("R\nRoutine\nVaste patronen"):
            select_mode("routine")
            st.rerun()

    with col2:
        if st.button("M\nMorgen klaar\nOp tijd klaar"):
            select_mode("morgen")
            st.rerun()

        if st.button("V\nVol bereik\nLange rit"):
            select_mode("vol")
            st.rerun()

        if st.button("H\nHandmatig\nZelf instellen"):
            select_mode("handmatig")
            st.rerun()

    if st.button("Terug"):
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
            <div class="mini-row"><span>Batterijstatus</span><b>{battery}%</b></div>
            <div class="mini-row"><span>Actieve modus</span><b>{mode["title"]}</b></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="detail-card">
            <div class="mode-symbol">{mode["symbol"]}</div>
            <div class="detail-title">{mode["title"]}</div>
            <div class="detail-subtitle">{mode["subtitle"]}</div>

            <div class="info-box">
                <b>Status</b><br>
                {mode["status"]}
            </div>
        """,
        unsafe_allow_html=True
    )

    # Desired range input only for relevant modes
    if mode["needs_range_input"]:
        desired_range = st.slider(
            "Gewenst batterijpercentage",
            min_value=50,
            max_value=100,
            value=mode["default_range"],
            step=5
        )
    else:
        desired_range = None

    # For smart charging, allow preference selection
    if st.session_state.selected_mode == "slim":
        preference = st.selectbox(
            "Optimalisatievoorkeur",
            ["Balans", "Goedkoop laden", "Duurzaam laden"]
        )

    # For manual mode, allow more control
    if st.session_state.selected_mode == "handmatig":
        manual_preference = st.selectbox(
            "Laadvoorkeur",
            ["Snel", "Goedkoop", "Duurzaam", "Balans"]
        )
        start_now = st.checkbox("Direct starten met laden")

    # Data grid
    data_items = ""
    for label, value in mode["items"]:
        data_items += f"""
        <div class="data-item">
            <div class="data-label">{label}</div>
            <div class="data-value">{value}</div>
        </div>
        """

    if desired_range is not None:
        data_items += f"""
        <div class="data-item">
            <div class="data-label">Gewenst</div>
            <div class="data-value">{desired_range}%</div>
        </div>
        """

    st.markdown(
        f"""
            <div class="data-grid">
                {data_items}
            </div>

            <div class="warning-box">
                <b>Zekerheidsregel</b><br>
                {mode["certainty"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Andere modus kiezen"):
        go_to("modes")
        st.rerun()

    if st.button("Startscherm"):
        go_to("home")
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

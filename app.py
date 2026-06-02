import streamlit as st

st.set_page_config(
    page_title="EV Charging Prototype",
    page_icon="⚡",
    layout="centered"
)

# ---------- Styling ----------
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
        margin-bottom: 22px;
    }

    .mode-card {
        background: white;
        padding: 18px;
        border-radius: 18px;
        border: 1px solid #d9e6dc;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.04);
        margin-bottom: 10px;
    }

    .mode-title {
        font-size: 20px;
        font-weight: 700;
        color: #1f3d2b;
        margin-bottom: 4px;
    }

    .mode-description {
        font-size: 14px;
        color: #5c5c5c;
    }

    .active-box {
        background: #e7f3eb;
        padding: 20px;
        border-radius: 20px;
        border-left: 6px solid #3f7d4e;
        margin-top: 20px;
        margin-bottom: 16px;
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
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Header ----------
st.markdown('<p class="app-title">Ratio Smart Charging</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Gebruiksvriendelijke laadmodi voor een slim home energy management system.</p>',
    unsafe_allow_html=True
)

# ---------- Status card ----------
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

st.write("Auto is aangesloten. Het systeem kan nu een laadstrategie kiezen op basis van jouw situatie.")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Mode selection ----------
st.subheader("Kies een laadmodus")

modus = st.radio(
    "Selecteer de situatie die het beste past:",
    [
        "⚡ Boost-modus",
        "🌙 Morgen klaar",
        "🌱 Slim laden",
        "🛣️ Vol bereik",
        "📅 Routine",
        "🎛️ Handmatig"
    ],
    label_visibility="collapsed"
)

# ---------- Mode explanation ----------
if modus == "⚡ Boost-modus":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">⚡ Boost-modus actief</div>
            <div class="mode-description">
                Voor wanneer je snel weer weg moet en direct extra bereik nodig hebt.
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

elif modus == "🌙 Morgen klaar":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">🌙 Morgen klaar-modus actief</div>
            <div class="mode-description">
                Voor normaal avondgebruik. De auto moet morgenochtend klaar zijn.
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

elif modus == "🌱 Slim laden":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">🌱 Slim laden actief</div>
            <div class="mode-description">
                Voor wanneer er geen directe haast is en het systeem het beste laadmoment mag kiezen.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    voorkeur = st.segmented_control(
        "Optimalisatievoorkeur",
        ["Balans", "Goedkoop", "Duurzaam"],
        default="Balans"
    )

    st.write("**Wat doet het systeem?**")
    st.write("- Kijkt naar energieprijs")
    st.write("- Kijkt naar zonne-energie")
    st.write("- Houdt rekening met huishoudelijk energieverbruik")
    st.write("- Bewaakt altijd het gewenste bereik")

    st.info(f"Gekozen voorkeur: **{voorkeur}**")

elif modus == "🛣️ Vol bereik":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">🛣️ Vol bereik-modus actief</div>
            <div class="mode-description">
                Voor wanneer je een lange rit gepland hebt en zekerheid over actieradius nodig hebt.
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

elif modus == "📅 Routine":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">📅 Routine-modus actief</div>
            <div class="mode-description">
                Voor terugkerend autogebruik, zoals werk, sport of vaste weekmomenten.
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

elif modus == "🎛️ Handmatig":
    st.markdown(
        """
        <div class="active-box">
            <div class="mode-title">🎛️ Handmatige modus actief</div>
            <div class="mode-description">
                Voor gebruikers die zelf controle willen houden over het laadproces.
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

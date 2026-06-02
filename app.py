import streamlit as st

st.set_page_config(
    page_title="EV Charging Prototype",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ EV Charging Prototype")
st.write("Prototype voor het testen van laadmodi binnen een slim energiesysteem.")

st.divider()

st.subheader("Huidige toestand")

col1, col2 = st.columns(2)

with col1:
    st.metric("Batterij", "42%")
    st.metric("Gewenst bereik", "70%")

with col2:
    st.metric("Vertrek", "Morgen 08:00")
    st.metric("Auto", "Aangesloten")

st.divider()

st.subheader("Kies een laadmodus")

modus = st.radio(
    "Welke laadmodus wil je gebruiken?",
    [
        "⚡ Boost-modus",
        "🌙 Morgen klaar-modus",
        "🌱 Slim laden-modus",
        "🛣️ Vol bereik-modus",
        "📅 Routine-modus",
        "🎛️ Handmatige modus"
    ]
)

st.divider()

if modus == "⚡ Boost-modus":
    st.header("⚡ Boost-modus actief")
    st.write("De auto wordt direct opgeladen met hoge prioriteit.")
    st.success("Verwacht toegevoegd bereik: +45 km in 30 minuten.")
    st.info("Focus: snelheid en direct bruikbaar bereik.")

elif modus == "🌙 Morgen klaar-modus":
    st.header("🌙 Morgen klaar-modus actief")
    st.write("De auto wordt slim opgeladen vóór de ingestelde vertrektijd.")
    st.write("Vertrek: morgen 08:00")
    st.write("Gewenst bereik: 70%")
    st.info("Het systeem wacht op een gunstig laadmoment.")
    st.warning("Als er geen gunstig moment komt, start laden automatisch om 04:00.")
    st.success("De auto is op tijd klaar.")

elif modus == "🌱 Slim laden-modus":
    st.header("🌱 Slim laden-modus actief")

    voorkeur = st.selectbox(
        "Kies optimalisatievoorkeur",
        ["Balans", "Goedkoop laden", "Duurzaam laden"]
    )

    st.write(f"Gekozen voorkeur: **{voorkeur}**")
    st.write(
        "Het systeem kijkt naar energieprijs, zonne-energie, "
        "huishoudelijk energieverbruik en het gewenste bereik."
    )
    st.success("De auto blijft op tijd klaar.")

elif modus == "🛣️ Vol bereik-modus":
    st.header("🛣️ Vol bereik-modus actief")
    st.write("Deze modus is bedoeld voor een geplande lange rit.")
    st.write("Gewenst laadniveau: 90% of hoger.")
    st.success("Focus: zekerheid en maximale actieradius.")

elif modus == "📅 Routine-modus":
    st.header("📅 Routine-modus actief")
    st.write("Het systeem gebruikt vaste vertrektijden en terugkerende gewoontes.")
    st.write("Normale vertrektijd: 08:00")
    st.write("Normale thuiskomst: 18:00")
    st.info("Bij afwijkende planning kan de gebruiker altijd handmatig ingrijpen.")

elif modus == "🎛️ Handmatige modus":
    st.header("🎛️ Handmatige modus actief")

    gewenst = st.slider("Gewenst batterijpercentage", 20, 100, 70)
    direct_laden = st.checkbox("Direct starten met laden")

    st.write(f"Gewenst batterijpercentage: **{gewenst}%**")

    if direct_laden:
        st.success("Laden wordt direct gestart.")
    else:
        st.info("Het systeem wacht op verdere instellingen van de gebruiker.")

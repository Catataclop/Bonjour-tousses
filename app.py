# ça c'est le code pour déployer l'appli streamlit

import streamlit as st
import pandas as pd

st.title("Bonjourre à tousses")
st.header("C'est mon app à moi")
st.subheader("J'ai pas copié Romain nonnon")

st.write("Sans transition, voici un data frame de nombres et leurs carrés :")
nmb = [1,2,4,7]
carre = [1**2,2**2,4**2,7**2]
d = {"nombres":nmb, "carres":carre} # création d'un bibliothèque

data = pd.DataFrame(d) # dataframe associé avec pandas

st.dataframe(data) # affichage du dataframe dans streamlit

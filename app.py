# ça c'est le code pour déployer l'appli streamlit

import streamlit as st
import pandas as pd

st.header("C'est mon app à moi")
st.write("J'ai pas copié Romain nonnon")

nmb = [1,2,4,7]
carre = [1**2,2**2,4**2,7**2]
d = {"nombres":nmb, "carres":carre} # création d'un bibliothèque

data = pd.DataFrame(d) # dataframe associé avec pandas

st.dataFrame(data) # affichage du dataframe dans streamlit

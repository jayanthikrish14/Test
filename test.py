import streamlit as st
import pandas as pd
import numpy as np

st.title("Guru Kripa")

# st.header("Header")
# st.subheader("Sub Header")

# st.text("This is the text")

# st.markdown(""" 
# # h1 tag
# ## h2 tag
# ### h3 tag
# :moon: <br>
# :smile:        
# <br>
#             **bold** <br>
#             _italic_
# """
# , True)

# st.write(1,2,3,4)
# st.write([1,2,3,4])
# st.write("this is a write txt")
df = pd.read_csv("C:/GUVI/cancer.csv")
#st.write(df)
# st.dataframe(df)
#st.table(df)
st.metric("TCS Stoc", value=23,delta=14)
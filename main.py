import streamlit as st
import os

# Create a horizontal navigation bar
st.header("Navigation Bar")

# Add a logo to the navigation bar
st.image("https://example.com/logo.png", width=100)

# Add links to the navigation bar
st.markdown("""
<ul>
<li><a href="/home">Home</a></li>
<li><a href="/about">About</a></li>
<li><a href="/contact">Contact</a></li>
<li><a href="/login">Login</a></li>
<li><a href="/register">Register</a></li>
</ul>
""")

# import module
import streamlit as st

# Title
st.title("Hello")

# Using object notation
add_selectbox = st.sidebar.selectbox("Informations")

# Using "with" notation
with st.sidebar:
    add_radio = st.radio("Do you want to save the informations about your next sign in?",("Yes, i want to! ", "No, thanks!"))
#priority_high
#Important
#The only elements that aren't supported using object notation are st.echo, st.spinner, and st.toast. To use these elements, you must use with notation.

#Here's an example of how you'd add st.echo and st.spinner to your sidebar:

import streamlit as st
import time

with st.sidebar:
    with st.echo():
        st.write("This Assignment is about how to do widgets")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
#Previous:
st.popover
#Next:
st.tabs

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


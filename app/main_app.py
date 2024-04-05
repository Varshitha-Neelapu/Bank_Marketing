import streamlit as st

def redirect_to_app2():
    st.write('<script>window.location.href = "https://mg7sxriwfhardij2e87njs.streamlit.app/"</script>', unsafe_allow_html=True)

if st.button("Go to App 2"):
    redirect_to_app2()

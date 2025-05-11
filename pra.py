import streamlit as st
from pages.fifo_page import show_fifo_page
from pages.lru_page import show_lru_page
from pages.optimal_page import show_optimal_page

# Page Replacement Algorithms Selection
def show_pra_page():
    st.title("Page Replacement Algorithms")
    st.write("""
    Select one of the following page replacement algorithms to explore and simulate:
    - FIFO (First In, First Out)
    - LRU (Least Recently Used)
    """)
    
    # Sidebar for selection of individual algorithms
    algorithm = st.sidebar.selectbox("Select an algorithm:", ("FIFO", "LRU", "Optimal"))
    
    # Based on the selected algorithm, show the respective page
    if algorithm == "FIFO":
        show_fifo_page()
    elif algorithm == "LRU":
        show_lru_page()
    elif algorithm == "Optimal":
        show_optimal_page()


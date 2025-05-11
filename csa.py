import streamlit as st
from pages.fcfs_page import show_fcfs_page
from pages.sjf_page import show_sjf_page
from pages.rr_page import show_rr_page
from pages.priority_page import show_priority_page

# CPU Scheduling Algorithms Selection
def show_csa_page():
    st.title("CPU Scheduling Algorithms")
    st.write("""
    Select one of the following CPU scheduling algorithms to explore and simulate:
    - FCFS (First Come First Serve)
    - SJF (Shortest Job First)
    - RR (Round Robin)
    - Priority Scheduling
    """)
    
    # Sidebar for selection of individual algorithms
    algorithm = st.sidebar.selectbox("Select an algorithm:", ("FCFS", "SJF", "RR", "Priority Scheduling"))
    
    # Based on the selected algorithm, show the respective page
    if algorithm == "FCFS":
        show_fcfs_page()
    elif algorithm == "SJF":
        show_sjf_page()
    elif algorithm == "RR":
        show_rr_page()
    elif algorithm == "Priority Scheduling":
        show_priority_page()

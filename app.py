import streamlit as st
from pra import show_pra_page  # Assuming pra module contains Page Replacement Algorithm pages
from csa import show_csa_page  # Assuming csa module contains CPU Scheduling Algorithm pages

def main():
    # Set page title and layout
    st.set_page_config(page_title="AlgoSphere", page_icon="⚙️", layout="wide", initial_sidebar_state="expanded")

    # Inject CSS for custom sidebar and hide default elements
    hide_sidebar_element = """
        <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
        .css-1d391kg {
            display: flex;
            justify-content: space-between;
        }
        .stSelectbox, .stRadio {
            background-color: #586e75;
            border-radius: 8px;
            padding: 10px;
        }
        .stRadio>div>label {
            color: #fafafa;
        }
        </style>
    """
    st.markdown(hide_sidebar_element, unsafe_allow_html=True)

    # Title and description
    st.title("Welcome to **AlgoSphere**! 🌟")
    st.write("""    
    AlgoSphere is a cutting-edge platform designed for learning and simulating key operating system algorithms.
    Choose an algorithm category below to explore and run simulations with interactive features like pie charts, Gantt charts, and more!
    **Ready to dive into the world of operating systems? Let's get started!** 🚀
    """)

    # Custom sidebar style (inspired by MediTrain)
    st.sidebar.markdown("""
    <style>
    .css-1v3fvcr {
        background-color: #002b36;  /* Dark background */
    }
    .css-1lcbvpd {
        color: #fafafa;  /* White text for the sidebar */
        font-size: 18px;
        padding: 15px;
    }
    .css-1v3fvcr > div {
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar with navigation options (using selectbox)
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Select Algorithm Category", 
                                    ("Home", "Page Replacement Algorithms", "CPU Scheduling Algorithms"), 
                                    key="category")

    # Display pages based on selected category
    if app_mode == "Home":
        show_home_page()
    elif app_mode == "Page Replacement Algorithms":
        show_pra_page()
    elif app_mode == "CPU Scheduling Algorithms":
        show_csa_page()

def show_home_page():
    st.subheader("Project Overview 📝")
    st.write("""
    **AlgoSphere** is designed to help you understand, visualize, and experiment with a variety of operating system algorithms. 
    You can run simulations for the following key categories:

    - **Page Replacement Algorithms**: Simulate algorithms like FIFO, LRU and Optimal to understand how operating systems manage memory.
    - **CPU Scheduling Algorithms**: Explore algorithms such as FCFS, SJF, RR, and Priority Scheduling to see how the CPU schedules processes in different scenarios.

    Whether you're a student learning OS concepts or a developer looking to understand these algorithms in depth, AlgoSphere provides an intuitive and interactive way to explore these key concepts.

    🚀 **What You Can Do**:
    - Run interactive simulations for each algorithm.
    - Visualize the algorithm's behavior with dynamic charts.
    - Understand how different inputs impact the system's performance.

    Get started now by choosing a category from the sidebar!
    """)

if __name__ == "__main__":
    main()

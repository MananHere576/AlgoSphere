# pages/priority_page.py

import streamlit as st
from algorithms.priority import priority_algorithm
from utils.chart import generate_gantt_chart

def show_priority_page():
    st.title("🌟 Priority CPU Scheduling Algorithm")
    st.write("""
    **Priority Scheduling** is a **CPU scheduling algorithm** where each process is assigned a **priority** value, and the process with the highest priority is scheduled first.

    ### How it works:
    - Each process is assigned a **priority** value. Higher values indicate higher priority. 🏆
    - The CPU executes the process with the **highest priority** first. 
    - If multiple processes have the same priority, they are scheduled in the order they arrive. This can be **preemptive** or **non-preemptive** depending on the implementation. 🔄
    - The **shortest burst time** may affect the scheduling if the system uses preemptive scheduling. ⚡

    **Advantages of Priority Scheduling:**
    - Ensures **high-priority processes** are executed first, minimizing the wait time for critical tasks. ⚠️
    - Can be adapted for **real-time systems** where certain tasks need to be completed first.

    **Disadvantages of Priority Scheduling:**
    - **Starvation** can occur for low-priority processes if there are continuous higher-priority processes arriving. 🚫
    - **Complexity** increases with dynamic priority assignment.

    """)

    # Input fields for burst times, arrival times, and priorities
    num_processes = st.number_input("🔢 **Number of Processes**:", min_value=1, value=4)
    burst_times = [st.number_input(f"💻 Burst Time for Process {i+1}:", min_value=1) for i in range(num_processes)]
    arrival_times = [st.number_input(f"⏰ Arrival Time for Process {i+1}:", min_value=0) for i in range(num_processes)]
    priorities = [st.number_input(f"🌟 Priority for Process {i+1}:", min_value=1, max_value=10) for i in range(num_processes)]

    if st.button("🚀 Run Priority Scheduling Algorithm"):
        # Run Priority Scheduling algorithm
        waiting_times, turn_around_times, gantt_chart = priority_algorithm(burst_times, arrival_times, priorities)

        # Results Summary
        st.subheader("📈 **Results Summary**")
        st.write(f"✅ **Waiting Times**: {waiting_times}")
        st.write(f"✅ **Turnaround Times**: {turn_around_times}")

        # Detailed Process Info
        st.subheader("📊 **Detailed Process Info**")
        processes_info = []
        for i in range(num_processes):
            processes_info.append([f"Process {i+1}", arrival_times[i], burst_times[i], priorities[i], waiting_times[i], turn_around_times[i]])
        st.table(processes_info)

        # Display Gantt Chart
        st.subheader("📅 **Gantt Chart**")
        st.write("Here’s the visualization of how the processes are scheduled:")
        generate_gantt_chart(gantt_chart)

# Run the page
if __name__ == "__main__":
    show_priority_page()

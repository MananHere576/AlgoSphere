# pages/sjf_page.py

import streamlit as st
from algorithms.sjf import sjf_algorithm
from utils.chart import generate_gantt_chart

def show_sjf_page():
    st.title("⚡ SJF (Shortest Job First) CPU Scheduling Algorithm")
    st.write("""
    **SJF (Shortest Job First)** is a **non-preemptive CPU scheduling algorithm** that selects the **process with the shortest burst time** to execute first.

    ### How it works:
    - The algorithm prioritizes processes with **shorter burst times**, executing them before those with longer burst times. ⏳
    - It minimizes the average waiting time but can suffer from the **convoy effect**, where longer processes may have to wait significantly. ⏸️
    - Since it's **non-preemptive**, once a process starts, it runs to completion without being interrupted. 🔄
    
    The **Shortest Job First (SJF)** algorithm is optimal in terms of **minimizing average waiting time**, but it requires **knowledge of future burst times**, which is not always feasible in real-world scenarios. 📊
    
    It's essential to note that SJF can result in **starvation** for longer processes if there are always shorter processes arriving. 🚫
    """)

    # Input fields for burst times and arrival times
    num_processes = st.number_input("🔢 **Number of Processes**:", min_value=1, value=4)
    burst_times = [st.number_input(f"💻 Burst Time for Process {i+1}:", min_value=1) for i in range(num_processes)]
    arrival_times = [st.number_input(f"⏰ Arrival Time for Process {i+1}:", min_value=0) for i in range(num_processes)]

    if st.button("🚀 Run SJF Algorithm"):
        # Run SJF algorithm
        waiting_times, turn_around_times, gantt_chart = sjf_algorithm(burst_times, arrival_times)

        # Results Summary
        st.subheader("📈 **Results Summary**")
        st.write(f"✅ **Waiting Times**: {waiting_times}")
        st.write(f"✅ **Turnaround Times**: {turn_around_times}")

        # Display a more detailed table for better clarity
        st.subheader("📊 **Detailed Process Info**")
        processes_info = []
        for i in range(num_processes):
            processes_info.append([f"Process {i+1}", arrival_times[i], burst_times[i], waiting_times[i], turn_around_times[i]])
        st.table(processes_info)

        # Display Gantt chart
        st.subheader("📅 **Gantt Chart**")
        st.write("Here’s the visualization of how the processes are scheduled:")
        generate_gantt_chart(gantt_chart)

# Run the page
if __name__ == "__main__":
    show_sjf_page()

# pages/fcfs_page.py

import streamlit as st
from algorithms.fcfs import fcfs_algorithm
from utils.chart import generate_gantt_chart

def show_fcfs_page():
    st.title("⏱ FCFS (First Come First Serve) CPU Scheduling Algorithm")
    st.write("""
    **FCFS (First Come First Serve)** is a **simple CPU scheduling algorithm** where processes are executed in the **order they arrive**.

    ### How it works:
    - The **first process** that arrives is the **first one to be executed**. 🏁
    - Once a process starts, it runs to completion, and the next one starts only after the current process finishes. 🔄
    - FCFS is **easy to implement**, but it may result in **long waiting times** for processes that arrive later (especially if a long process is executed first). 😕
    - This is often referred to as the **convoy effect**, where shorter processes have to wait for longer ones. 🐢

    FCFS is a **non-preemptive** scheduling algorithm, meaning once a process starts, it **cannot be interrupted** until it finishes. This makes FCFS less suitable for real-time systems where time constraints are critical. ⏳
    
    However, it’s a great starting point for understanding how scheduling algorithms work! 🧑‍💻
    """)

    # Input fields for burst times and arrival times
    burst_times = st.text_area("📊 **Burst Times** (comma-separated):", "6, 8, 7, 3")
    arrival_times = st.text_area("📅 **Arrival Times** (comma-separated):", "0, 1, 2, 3")

    if st.button("🚀 Run FCFS Algorithm"):
        # Convert burst times and arrival times to lists of integers
        burst_times = list(map(int, burst_times.split(',')))
        arrival_times = list(map(int, arrival_times.split(',')))

        # Run FCFS algorithm
        waiting_times, turn_around_times, gantt_chart = fcfs_algorithm(burst_times, arrival_times)

        # Display Results Summary
        st.subheader("📈 **Results Summary**")
        st.write(f"✅ **Waiting Times**: {waiting_times}")
        st.write(f"✅ **Turnaround Times**: {turn_around_times}")
        
        # Display a more detailed table for better clarity
        st.subheader("📊 **Detailed Process Info**")
        processes_info = []
        for i in range(len(burst_times)):
            processes_info.append([f"Process {i+1}", arrival_times[i], burst_times[i], waiting_times[i], turn_around_times[i]])
        st.table(processes_info)

        # Display Gantt chart
        st.subheader("📅 **Gantt Chart**")
        st.write("Here’s the visualization of how the processes are scheduled:")
        generate_gantt_chart(gantt_chart)

# Run the page
if __name__ == "__main__":
    show_fcfs_page()

# pages/rr_page.py

import streamlit as st
from algorithms.rr import rr_algorithm
from utils.chart import generate_gantt_chart

def show_rr_page():
    st.title("🔄 Round Robin (RR) CPU Scheduling Algorithm")
    st.write("""
    **Round Robin (RR)** is a **CPU scheduling algorithm** that gives each process a fixed **time slice** or **quantum** to execute.

    ### How it works:
    - In Round Robin, each process is assigned a fixed amount of CPU time, known as a **time quantum**. ⏱️
    - If a process does not finish its execution within its time quantum, it is **preempted** and moved to the back of the queue for the next round. 🔄
    - This continues in a **cyclic order**, ensuring that all processes get a fair share of CPU time. ⚖️
    - It's a **fair** and **non-preemptive** approach, but the performance can degrade if the time quantum is too large or too small. ⚖️

    **Advantages of Round Robin (RR):**
    - Ensures **fair allocation of CPU time** across all processes.
    - Avoids **starvation**, as each process gets executed in turn.

    **Disadvantages of Round Robin (RR):**
    - **High waiting time** for processes that have a longer burst time than the time quantum. ⏳
    - **Context switching overhead** due to the frequent switching between processes.

    """)

    # Input fields for burst times, arrival times, and time quantum
    num_processes = st.number_input("🔢 **Number of Processes**:", min_value=1, value=4)
    burst_times = [st.number_input(f"💻 Burst Time for Process {i+1}:", min_value=1) for i in range(num_processes)]
    arrival_times = [st.number_input(f"⏰ Arrival Time for Process {i+1}:", min_value=0) for i in range(num_processes)]
    time_quantum = st.number_input("⏱️ **Time Quantum**:", min_value=1, value=4)

    if st.button("🚀 Run Round Robin Algorithm"):
        # Run Round Robin algorithm
        waiting_times, turn_around_times, gantt_chart = rr_algorithm(burst_times, arrival_times, time_quantum)

        # Results Summary
        st.subheader("📈 **Results Summary**")
        st.write(f"✅ **Waiting Times**: {waiting_times}")
        st.write(f"✅ **Turnaround Times**: {turn_around_times}")

        # Detailed Process Info
        st.subheader("📊 **Detailed Process Info**")
        processes_info = []
        for i in range(num_processes):
            processes_info.append([f"Process {i+1}", arrival_times[i], burst_times[i], waiting_times[i], turn_around_times[i]])
        st.table(processes_info)

        # Display Gantt Chart
        st.subheader("📅 **Gantt Chart**")
        st.write("Here’s the visualization of how the processes are scheduled:")
        generate_gantt_chart(gantt_chart)

# Run the page
if __name__ == "__main__":
    show_rr_page()

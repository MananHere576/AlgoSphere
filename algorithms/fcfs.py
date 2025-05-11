# algorithms/fcfs.py

def fcfs_algorithm(burst_times, arrival_times):
    n = len(burst_times)
    waiting_times = [0] * n
    turn_around_times = [0] * n
    gantt_chart = []
    start_time = 0

    # Calculate waiting times
    for i in range(1, n):
        waiting_times[i] = burst_times[i-1] + waiting_times[i-1]

    # Calculate turnaround times
    for i in range(n):
        turn_around_times[i] = burst_times[i] + waiting_times[i]

    # Gantt chart (timeline)
    for i in range(n):
        gantt_chart.append((start_time, start_time + burst_times[i], f'P{i+1}'))  # Including process labels
        start_time += burst_times[i]

    return waiting_times, turn_around_times, gantt_chart

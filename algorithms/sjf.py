def sjf_algorithm(burst_times, arrival_times):
    n = len(burst_times)
    processes = list(range(n))
    
    # Sort processes by burst time (SJF)
    processes.sort(key=lambda i: burst_times[i])
    
    waiting_times = [0] * n
    turn_around_times = [0] * n
    gantt_chart = []
    start_time = 0

    # Calculate waiting times
    for i in range(1, n):
        waiting_times[processes[i]] = burst_times[processes[i-1]] + waiting_times[processes[i-1]]

    # Calculate turnaround times
    for i in range(n):
        turn_around_times[processes[i]] = burst_times[processes[i]] + waiting_times[processes[i]]

    # Gantt chart (timeline)
    for i in range(n):
        gantt_chart.append((start_time, start_time + burst_times[processes[i]], f'P{processes[i]+1}'))  # Add process label (e.g., 'P1')
        start_time += burst_times[processes[i]]

    return waiting_times, turn_around_times, gantt_chart

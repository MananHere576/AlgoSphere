# algorithms/rr.py

def rr_algorithm(burst_times, arrival_times, quantum):
    n = len(burst_times)
    remaining_burst_times = burst_times[:]
    waiting_times = [0] * n
    turn_around_times = [0] * n
    gantt_chart = []
    start_time = 0
    queue = list(range(n))

    while queue:
        process = queue.pop(0)
        if remaining_burst_times[process] > quantum:
            remaining_burst_times[process] -= quantum
            gantt_chart.append((start_time, start_time + quantum, process))
            start_time += quantum
            queue.append(process)
        else:
            gantt_chart.append((start_time, start_time + remaining_burst_times[process], process))
            waiting_times[process] = start_time - arrival_times[process] - burst_times[process]
            turn_around_times[process] = waiting_times[process] + burst_times[process]
            start_time += remaining_burst_times[process]
            remaining_burst_times[process] = 0

    return waiting_times, turn_around_times, gantt_chart

import matplotlib.pyplot as plt

def plot_position_over_time(self, trial_id, node_id):
    """
    Plots the position over time for a given trial_id and node_id.

    Parameters:
    - trial_id: The trial ID to filter the data.
    - node_id: The node ID to filter the data.
    """
    # SQL query to select time and position for a specific trial_id and node_id
    sql = """
    SELECT time, position FROM ODriveData
    WHERE trial_id = ? AND node_ID = ?
    ORDER BY time;
    """
    # Execute the query and fetch all results
    results = self.execute_query(sql, (trial_id, node_id))

    # If results are empty, no data to plot
    if not results:
        print("No data found for the given trial_id and node_id.")
        return

    # Unpack the results
    times, positions = zip(*results)

    # Plotting the position data
    plt.figure(figsize=(10, 6))
    plt.plot(times, positions, marker='o', linestyle='-', color='b')
    plt.title(f'Position Over Time for Trial ID {trial_id} and Node ID {node_id}')
    plt.xlabel('Time (s)')
    plt.ylabel('Position')
    plt.grid(True)
    plt.show()

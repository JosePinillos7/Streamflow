
import numpy as np
import matplotlib.pyplot as plt
import csv

def load_streamflow(filename):
    """Read the streamflow CSV. Return dates and a 2D array of flows."""
    data = np.genfromtxt(
        filename,
        delimiter=',',
        dtype=str,
        skip_header=1
    )

    dates = data[:, 0].astype('datetime64[m]')
    flows = data[:, 1:6].astype(float)

    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting."""
    plt.figure(figsize=(10, 7))

    for i in range(len(sites)):
        plt.plot(dates, flows[:, i], label=sites[i])

    plt.title('Provo River Streamflow Data (2021)')
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(title='Site Numbers')

    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


def summarize(dates, flows, sites):
    """Calculate and save flow statistics for each gauge."""

    # Calculate maximum, minimum, and average flows
    max_flows = np.max(flows, axis=0)
    min_flows = np.min(flows, axis=0)
    avg_flows = np.mean(flows, axis=0)

    # Find the date and time of each maximum flow
    max_indices = np.argmax(flows, axis=0)

    print("\nStreamflow Summary")
    print("-" * 85)
    print(f"{'Gauge':<12} {'Max (cfs)':>10} {'Date of max':<20} {'Min (cfs)':>10} {'Avg (cfs)':>10}")

    # Store the results
    rows = []

    for i in range(len(sites)):
        max_date = str(dates[max_indices[i]]).replace("T", " ")

        print(
            f"{sites[i]:<12} "
            f"{max_flows[i]:>10.1f} "
            f"{max_date:<20} "
            f"{min_flows[i]:>10.1f} "
            f"{avg_flows[i]:>10.1f}"
        )

        rows.append([
            sites[i],
            max_flows[i],
            max_date,
            min_flows[i],
            avg_flows[i]
        ])

    # Save the summary to a CSV file
    with open("streamflow_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Gauge", "Max (cfs)", "Date of max", "Min (cfs)", "Avg (cfs)"])
        writer.writerows(rows)

def threshold_report(flows, sites, threshold):
    """Count the hours each gauge exceeds the selected flow threshold."""
    hours_above = np.sum(flows > threshold, axis=0)

    print("\nStreamflow Threshold Report")
    print("-" * 50)
    print(f"Selected threshold: {threshold} cfs")
    print(f"{'Gauge':<15} {'Hours above threshold':>22}")

    for i in range(len(sites)):
        print(f"{sites[i]:<15} {hours_above[i]:>22}")

# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")

plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)
threshold = float(input("\nEnter streamflow threshold (cfs): "))
threshold_report(flows, sites, threshold)

import numpy as np
import matplotlib.pyplot as plt


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


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")

plot_streamflow(dates, flows, sites)

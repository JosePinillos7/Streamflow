# Provo River Streamflow Analysis

## Project Description
This project analyzes streamflow data from five Provo River monitoring stations during June 2021 using Python.

## Requirements
- Python 3
- NumPy
- Matplotlib

## Files
- `streamflow.py`: Main Python program.
- `June-2021-Provo-River-Streamflow-Rates.csv`: Original streamflow dataset.
- `provo_streamflow.png`: Generated streamflow plot.
- `streamflow_summary.csv`: Summary statistics for each gauge.

## Features
1. Loads streamflow data from a CSV file.
2. Plots streamflow rates for five monitoring stations.
3. Calculates maximum, minimum, and average flow rates.
4. Identifies the date of maximum flow.
5. Generates a report showing the hours each gauge exceeds a user-selected threshold.

## How to Run
Install the required libraries:

```bash
python -m pip install numpy matplotlib
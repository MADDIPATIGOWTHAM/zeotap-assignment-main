from visualization.plots import plot_daily_summary

def test_plot_daily_summary():
    summary = {
        '2024-10-01': {'average_temp': 30, 'max_temp': 32, 'min_temp': 28, 'dominant_condition': 'Clear'},
        '2024-10-02': {'average_temp': 29, 'max_temp': 31, 'min_temp': 27, 'dominant_condition': 'Rain'},
    }
    plot_daily_summary(summary)  # Ensure no errors when plotting

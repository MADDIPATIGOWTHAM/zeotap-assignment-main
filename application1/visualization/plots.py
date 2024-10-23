# visualization/plots.py

def plot_daily_summary(summary):
    import matplotlib.pyplot as plt
    import numpy as np

    dates = summary['dates']
    cities = list(summary['avg_temps'].keys())

    # Prepare data for plotting
    avg_temps = [sum(temps) / len(temps) for temps in summary['avg_temps'].values()]

    plt.figure(figsize=(12, 6))

    # Plot average temperatures for each city
    for i, city in enumerate(cities):
        plt.plot(dates, summary['avg_temps'][city], marker='o', label=city)

    # Adding labels and title
    plt.xticks(rotation=45)
    plt.title("Average Daily Temperature by City")
    plt.xlabel("Dates")
    plt.ylabel("Average Temperature (°C)")
    plt.legend()

    # Display the plot
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

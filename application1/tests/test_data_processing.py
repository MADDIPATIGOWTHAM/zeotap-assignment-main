from processing.data_processing import process_weather_data, calculate_daily_summary

def test_daily_summary():
    # Simulate weather updates
    process_weather_data({'name': 'Delhi', 'main': {'temp': 30}, 'weather': [{'main': 'Clear'}], 'dt': 1633072800})
    process_weather_data({'name': 'Delhi', 'main': {'temp': 28}, 'weather': [{'main': 'Clear'}], 'dt': 1633159200})
    
    summary = calculate_daily_summary()
    assert summary  # Ensure summary has been calculated

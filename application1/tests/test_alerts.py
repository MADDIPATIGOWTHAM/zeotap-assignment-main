from processing.alerts import check_alerts
from config import THRESHOLDS

def test_alerts():
    weather = {'main': {'temp': 36}, 'weather': [{'main': 'Clear'}], 'name': 'Delhi'}
    alerts = check_alerts(weather)  # Capture the returned alerts
    print(alerts)  # Print the alerts
    assert any("High temperature" in alert for alert in alerts)

test_alerts()

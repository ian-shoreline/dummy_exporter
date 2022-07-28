from prometheus_client import start_http_server, Gauge
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_DURATION = Gauge('istio_request_duration_milliseconds_average', 'Time spent processing requests averaged over last 60s')
REQUEST_SIZE     = Gauge('istio_request_bytes_average', 'HTTP request body sizes averaged over last 60s')
RESPONSE_SIZE    = Gauge('istio_response_bytes_average', 'HTTP response body sizes averaged over last 60s')

# Initialize dummy variables
random_request_size     = (10**6 * 25) - (10**6 * random.random())
random_response_size    = (10**6 * 25) - (10**6 * random.random())
random_request_duration = 100 - (10**2 * random.random())

def randomize(variable, low, high, inc):
    if variable > low and variable < high:
        # if in between bounds, plus or minus inc * a number from 0 to 1
        return variable + (random.random() * inc) - (.5 * inc)
    elif variable <= low:
        return variable + (random.random() * inc)
    else:
        return variable - (random.random() * inc)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        # Assume 25 mbps start, vary by up to 1mbps between 20 and 30
        random_request_size = randomize(random_request_size, 10**6 * 20, 10**6 * 30, 10**6 * 5)
        REQUEST_SIZE.set(random_request_size)

        random_response_size = randomize(random_response_size, 10**6 * 20, 10**6 * 30, 10**6 * 5)
        RESPONSE_SIZE.set(random_response_size)

        random_request_duration = randomize(random_request_duration, 5, 400, 10**2)
        REQUEST_DURATION.set(random_request_duration)
import asyncio

from prometheus_client import Counter, Summary, Histogram
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from prometheus_client.exposition import basic_auth_handler
from core.config import *

   
registry = CollectorRegistry()
START_COUNTER = Counter('keymap_action', 'Count action keymapswitcher bot' , registry=registry)  
REQUEST_TIME = Summary('keymap_action_request_processing_seconds', 'Time spent processing request keymap action')

# Decorate function with metric.

# Create a metric to track time spent and requests made.


def my_auth_handler(url, method, timeout, headers, data):
    username = MONITOR_LOGIN
    password = MONITOR_PASSWORD
    return basic_auth_handler(url, method, timeout, headers, data, username, password)

    
async def background_on_start() -> None:
    """background task which is created when bot starts"""
    while True:
        if not MONITOR_HOST:
            return
        await asyncio.sleep(30)
        push_to_gateway(MONITOR_HOST, job='keymapSwitcher', registry=registry, handler=my_auth_handler)
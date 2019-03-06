import os
import zmq
import logging

logger = logging.getLogger('ansible-runner')


def get_configuration(runner_config):
    runner_url = runner_config.settings.get("runner_socket_url", None)
    runner_url = os.getenv("RUNNER_SOCKET_URL", runner_url)
    return runner_url


def send_request(url, data):
    context = zmq.Context()
    sink = context.socket(zmq.PUSH)
    sink.connect(url)
    sink.send_json(data)


def status_handler(runner_config, data):
    runner_url = get_configuration(runner_config)
    if runner_url is not None:
        send_request(runner_url, data)
    else:
        logger.info("ZeroMQ Plugin Skipped")


def event_handler(runner_config, data):
    status_handler(runner_config, data)

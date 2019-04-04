# -*- coding: utf-8 -*-
import logging
import logging.handlers
import os
import pathlib
import threading
from queue import Queue


class LineworksMessenger(logging.StreamHandler):

    def __init__(self, name, server_url, method, from_code, receiver_ids):
        logging.StreamHandler.__init__(self)

        self.name = name
        self.server_url = server_url
        self.method = method
        self.from_code = from_code
        self.receiver_ids = receiver_ids

    def emit(self, record):
        message = self.format(record)


class StreamHandlerBuilder:

    # return type is list or tuple
    def build(self):
        raise NotImplementedError


class LineworksMessengerBuilder(StreamHandlerBuilder):
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.chat_server_url = kwargs["chat_server_url"]
        self.method = kwargs["method"]
        self.from_code = kwargs["from_code"]
        self.receiver_ids = kwargs["receiver_ids"]

    def build(self):
        return [LineworksMessenger(name=self.name,
                                   server_url=self.chat_server_url,
                                   method=self.method,
                                   from_code=self.from_code,
                                   receiver_ids=self.receiver_ids)]


class RotatingFileHandlerBuilder(StreamHandlerBuilder):
    def __init__(self, *args, **kwargs):
        self.name = kwargs["name"]
        self.max_bytes = kwargs["max_bytes"]
        self.backup_count = kwargs["backup_count"]
        self.message_format = kwargs["message_format"]
        self.log_dir = kwargs["dir"]
        self.console = kwargs["console"]

    def build(self):
        handlers = []
        filename = '{}/{}.log'.format(self.log_dir, self.name)
        formatter = logging.Formatter(self.message_format)
        handler = logging.handlers.RotatingFileHandler(filename,
                                                       mode='w',
                                                       maxBytes=self.max_bytes,
                                                       backupCount=self.backup_count)
        handler.setFormatter(formatter)
        handlers.append(handlers)

        if self.console:
            handler = logging.StreamHandler()
            handler.setFormatter(self.message_format)
            handlers.append(handlers)

        return handlers


class Logger(threading.Thread):
    MB = 1024 * 1024

    def __init__(self, daemon=True):
        threading.Thread.__init__(self, daemon=daemon)

        self.queue = Queue()
        self.done = False
        self.q_get_timeout = 1

    def add(self, name, builder, level=logging.INFO):
        handlers = builder.build()
        for handler in handlers:
            logger = logging.getLogger(name)
            logger.setLevel(level)
            logger.addHandler(handler)

    def write(self, name, message):
        # safely between multiple threads
        self.queue.put_nowait((name, message))

    def shutdown(self):
        self.done = True

    def run(self):
        """
        Later we will add the level function to the this method
        :return:
            None
        """
        while not self.done:
            message = self.queue.get(timeout=self.q_get_timeout)
            if message:
                logging.getLogger(message[0]).info(message[1])

        for message in iter(self.queue, None):
            if message:
                logging.getLogger(message[0]).info(message[1])
# -*- coding: utf-8 -*-
from abc import *


class AbstractTrainer(ABC):

    @abstractmethod
    def run(self, initializer):
        raise NotImplementedError


class AbstractInitializer(ABC):

    @abstractmethod
    def initialize(self, config_file):
        raise NotImplementedError

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def build_logger(self):
        raise NotImplementedError

    @abstractmethod
    def build_executor(self):
        raise NotImplementedError

    @abstractmethod
    def build_optimizer(self):
        raise  NotImplementedError

    @abstractmethod
    def build_env(self):
        raise NotImplementedError

    @abstractmethod
    def build_agent(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def build_model(self, **kwargs):
        raise NotImplementedError


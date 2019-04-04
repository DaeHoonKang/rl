# -*- coding: utf-8 -*-
from abc import *


class AbstractAgent(ABC):

    @abstractmethod
    def save(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def load(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def reset(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def action(self, state):
        raise NotImplementedError

    @abstractmethod
    def update(self, terminate):
        raise NotImplementedError

    @abstractmethod
    def append_experience(self, expr):
        raise NotImplementedError

    @abstractmethod
    def preprocessiong_state(self, *args, **kwargs):
        raise NotImplementedError
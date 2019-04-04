# -*- coding: utf-8 -*-
from abc import *


class AbstractEnv(ABC):

    @abstractmethod
    def version(self):
        raise NotImplementedError

    @abstractmethod
    def reset(self, players):
        raise NotImplementedError

    @abstractmethod
    def step(self):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError
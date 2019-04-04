# -*- coding: utf-8 -*-
from abc import *


class AbstractPlayer(ABC):

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def action(self, state):
        raise NotImplementedError

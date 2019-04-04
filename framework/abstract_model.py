# -*- coding: utf-8 -*-
from abc import *


class AbstractModel(ABC):

    @abstractmethod
    def build(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def scope(self):
        raise NotImplementedError

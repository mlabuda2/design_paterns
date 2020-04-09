from abc import ABC, abstractmethod

from builder.fluent_builder.vpc import VPC


class VPCBuilder(ABC):

    def __init__(self):
        self.vpc = VPC()

    @abstractmethod
    def set_ec2(self):
        pass

    @abstractmethod
    def set_database(self):
        pass

    @abstractmethod
    def set_scalling(self):
        pass

    @abstractmethod
    def set_s3(self):
        pass

    @abstractmethod
    def set_cloudwatch(self):
        pass

    @abstractmethod
    def set_max_bill(self):
        pass

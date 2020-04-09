from builder.fluent_builder.vpc_builder import VPCBuilder


class TierTwoVPCBuilder(VPCBuilder):

    def set_ec2(self):
        self.vpc.set_property('cpu', 'i7')
        self.vpc.set_property('ram', '32')
        return self

    def set_database(self):
        self.vpc.set_property('database', 'mariadb')
        return self

    def set_scalling(self):
        self.vpc.set_property('scalling', True)
        return self

    def set_s3(self):
        self.vpc.set_property('s3', True)
        return self

    def set_cloudwatch(self):
        self.vpc.set_property('cloudwatch', True)
        return self

    def set_max_bill(self):
        self.vpc.set_property('max_bill', 1000)
        return self

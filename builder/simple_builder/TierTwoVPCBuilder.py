from builder.simple_builder.vpc_builder import VPCBuilder


class TierTwoVPCBuilder(VPCBuilder):

    def set_ec2(self):
        self.vpc.set_property('cpu', 'i7')
        self.vpc.set_property('ram', '32')

    def set_database(self):
        self.vpc.set_property('database', 'mariadb')

    def set_scalling(self):
        self.vpc.set_property('scalling', True)

    def set_s3(self):
        self.vpc.set_property('s3', True)

    def set_cloudwatch(self):
        self.vpc.set_property('cloudwatch', True)

    def set_max_bill(self):
        self.vpc.set_property('max_bill', 1000)

from builder.simple_builder.vpc_builder import VPCBuilder


class TierOneVPCBuilder(VPCBuilder):

    def set_ec2(self):
        self.vpc.set_property('cpu', 'i3')
        self.vpc.set_property('ram', '1')

    def set_database(self):
        self.vpc.set_property('database', 'mongodb')

    def set_scalling(self):
        self.vpc.set_property('scalling', False)

    def set_s3(self):
        self.vpc.set_property('s3', False)

    def set_cloudwatch(self):
        self.vpc.set_property('cloudwatch', False)

    def set_max_bill(self):
        self.vpc.set_property('max_bill', 10)

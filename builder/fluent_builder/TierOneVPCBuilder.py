from builder.fluent_builder.vpc_builder import VPCBuilder


class TierOneVPCBuilder(VPCBuilder):

    def set_ec2(self):
        self.vpc.set_property('cpu', 'i3')
        self.vpc.set_property('ram', '1')
        return self

    def set_database(self):
        self.vpc.set_property('database', 'mongodb')
        return self

    def set_scalling(self):
        self.vpc.set_property('scalling', False)
        return self

    def set_s3(self):
        self.vpc.set_property('s3', False)
        return self

    def set_cloudwatch(self):
        self.vpc.set_property('cloudwatch', False)
        return self

    def set_max_bill(self):
        self.vpc.set_property('max_bill', 10)
        return self

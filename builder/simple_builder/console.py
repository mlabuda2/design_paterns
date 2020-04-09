from builder.simple_builder.vpc_builder import VPCBuilder


class Console:
    def build(self, vpc_builder: VPCBuilder) -> None:
        vpc_builder.set_ec2()
        vpc_builder.set_database()
        vpc_builder.set_scalling()
        vpc_builder.set_s3()
        vpc_builder.set_cloudwatch()
        vpc_builder.set_max_bill()

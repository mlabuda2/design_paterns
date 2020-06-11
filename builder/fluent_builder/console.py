from builder.fluent_builder.vpc_builder import VPCBuilder


class Console:
    def build(self, vpc_builder: VPCBuilder) -> None:
        vpc_builder.set_ec2()\
                   .set_database()\
                   .set_scalling()\
                   .set_s3()\
                   .set_cloudwatch()\
                   .set_max_bill()

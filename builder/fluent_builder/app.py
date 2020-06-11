from builder.fluent_builder.TierOneVPCBuilder import TierOneVPCBuilder
from builder.fluent_builder.TierTwoVPCBuilder import TierTwoVPCBuilder
from builder.fluent_builder.console import Console


def main():
    console = Console()

    builder = TierOneVPCBuilder()
    console.build(builder)
    builder.vpc.get_vpc()
    print('\n')

    builder = TierTwoVPCBuilder()
    console.build(builder)
    builder.vpc.get_vpc()


if __name__ == "__main__":
    main()

    # class A:
    #     def a(self):
    #         print("a")
    #         return self
    #
    #     def b(self):
    #         print("b")
    #         return self

    # a = A()
    # a.a().b()

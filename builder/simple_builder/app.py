from builder.simple_builder.TierOneVPCBuilder import TierOneVPCBuilder
from builder.simple_builder.TierTwoVPCBuilder import TierTwoVPCBuilder
from builder.simple_builder.console import Console


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
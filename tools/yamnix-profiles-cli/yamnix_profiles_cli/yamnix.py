from yamnix_cli.arguments import YamnixCLI


class YamnixProfilesCLI(YamnixCLI):
    pass


def main():
    cli = YamnixProfilesCLI()
    cli.output.console.print(cli.arguments)
    cli.print()


if __name__ == '__main__':
    main()

from yamnix_cli.arguments import YamnixCLI


class YamnixShell(YamnixCLI):
    pass


def main():
    cli = YamnixShell()
    cli.output.console.print(cli.arguments)
    cli.print()


if __name__ == '__main__':
    main()

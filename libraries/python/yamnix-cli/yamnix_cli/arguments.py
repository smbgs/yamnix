import argparse
from typing import TypeVar, Callable, Any, Union

from rich.console import JustifyMethod, OverflowMethod
from rich.style import Style
from yamnix_cli.output import Output


class YamnixCLI:

    def __init__(self, args=None):
        self.output = Output()

        # TODO: create appropriate parser tree based on the console definition
        self.parser = argparse.ArgumentParser()
        self.arguments = self.parser.parse_args(args)

    # TODO: move this out possibly?
    def print(
        self,
        *objects: Any,
        sep=" ",
        end="\n",
        style: Union[str, Style] = None,
        justify: JustifyMethod = None,
        overflow: OverflowMethod = None,
        no_wrap: bool = None,
        emoji: bool = None,
        markup: bool = None,
        highlight: bool = None,
        width: int = None,
        height: int = None,
        crop: bool = True,
        soft_wrap: bool = None,
    ):
        self.output.console.print(
            *objects,
            sep=sep,
            end=end,
            style=style,
            justify=justify,
            overflow=overflow,
            no_wrap=no_wrap,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            width=width,
            height=height,
            crop=crop,
            soft_wrap=soft_wrap,
        )

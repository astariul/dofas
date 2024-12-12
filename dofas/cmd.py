import argparse
import sys

from dofas import extract_template_from


def cli():
    parser = argparse.ArgumentParser(description="Dofas' command line.")
    subparsers = parser.add_subparsers(title="commands", dest="cmd")

    template_parser = subparsers.add_parser(
        "template", help="Analyze the screen and create the template for the HDV window."
    )
    template_parser.set_defaults(cmd="template")
    template_parser.add_argument(
        "--screenshot",
        "-S",
        dest="screenshot",
        type=str,
        default="screenshot_hdv.png",
        help="The screenshot to analyze",
    )
    template_parser.add_argument(
        "--template",
        "-T",
        dest="template",
        type=str,
        default="hdv_template.png",
        help="Where to save the extracted template.",
    )
    template_parser.add_argument(
        "--hdv_name",
        "-H",
        dest="hdv_name",
        type=str,
        default="Hôtel de vente",
        help="Name of the HDV window to search for.",
    )

    args = parser.parse_args()

    if args.cmd is None:
        parser.print_help(sys.stderr)
        sys.exit(1)
    elif args.cmd == "template":
        extract_template_from(args.screenshot, args.template, args.hdv_name)

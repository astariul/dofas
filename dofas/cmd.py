import argparse
import sys

import cv2

from dofas import Inspector, Scraper, extract_template_from


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

    start_parser = subparsers.add_parser("start", help="Start the screen analyzer to extract HDV data.")
    start_parser.set_defaults(cmd="start")
    start_parser.add_argument(
        "--template",
        "-T",
        dest="template",
        type=str,
        default="hdv_template.png",
        help="HDV template to use for template matching",
    )

    debug_parser = subparsers.add_parser("debug", help="Analyze the given screenshot for debugging.")
    debug_parser.set_defaults(cmd="debug")
    debug_parser.add_argument(
        "--screenshot",
        "-S",
        dest="screenshot",
        type=str,
        default="screenshot_hdv.png",
        help="The screenshot to analyze",
    )
    debug_parser.add_argument(
        "--template",
        "-T",
        dest="template",
        type=str,
        default="hdv_template.png",
        help="HDV template to use for template matching",
    )

    args = parser.parse_args()

    if args.cmd is None:
        parser.print_help(sys.stderr)
        sys.exit(1)
    elif args.cmd == "template":
        extract_template_from(args.screenshot, args.template, args.hdv_name)
    elif args.cmd == "start":
        s = Scraper(args.template)
        s.start()
    elif args.cmd == "debug":
        scale = 0.5
        insp = Inspector(cv2.imread(args.screenshot), scale=scale)
        template = cv2.imread(args.template, cv2.IMREAD_GRAYSCALE)
        template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        insp.show(template)

import argparse
from pathlib import Path
from .registry import evaluate, list_metrics


def run(args):
    text = Path(args.input).read_text(encoding="utf-8")
    result = evaluate(metric=args.metric, text=text)

    if args.format == "json":
        output = result.to_json()
    else:
        output = result.to_markdown()

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Report written to {args.output}")
    else:
        print(output)


def main():
    parser = argparse.ArgumentParser(prog="pmeval", description="Evaluate AI PM artifacts with structured rubrics.")
    sub = parser.add_subparsers(dest="command")

    list_parser = sub.add_parser("list", help="List available metrics")
    list_parser.set_defaults(func=lambda args: print("\n".join(list_metrics())))

    run_parser = sub.add_parser("run", help="Run an eval metric")
    run_parser.add_argument("--metric", required=True, choices=list_metrics())
    run_parser.add_argument("--input", required=True, help="Path to markdown/text file")
    run_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    run_parser.add_argument("--output", help="Optional report output path")
    run_parser.set_defaults(func=run)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()

import argparse
import json

from src.analyzer import analyze
from src.cases import TEST_CASES


def main():
    parser = argparse.ArgumentParser(
        description="Detect brand mentions in AI-generated text"
    )
    parser.add_argument("--texto", help="AI response text to analyze")
    parser.add_argument("--marca", help="Brand name to monitor")
    args = parser.parse_args()

    if args.texto and args.marca:
        result = analyze(args.texto, args.marca)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.texto or args.marca:
        parser.error("--texto and --marca must be used together")
    else:
        for i, case in enumerate(TEST_CASES, 1):
            print(f"--- Case {i} (marca_monitorada: {case['marca_monitorada']}) ---")
            result = analyze(case["texto"], case["marca_monitorada"])
            print(json.dumps(result, ensure_ascii=False, indent=2))
            print()

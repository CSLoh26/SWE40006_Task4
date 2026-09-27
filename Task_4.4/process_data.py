#!/usr/bin/env python3
"""
Simple CLI data-processing tool for Task 4.4 (High Distinction).

Reads a text file line by line, counts words, and writes a small
summary report to an output file. Designed to demonstrate:
  - argument parsing (non-web, CLI-driven)
  - reading/writing via a mounted Docker volume
  - clean start -> process -> exit lifecycle for container logs
"""
import argparse
import sys
import time
from collections import Counter
from pathlib import Path


def process_file(input_path: Path, output_path: Path) -> None:
    print(f"[START] Reading input file: {input_path}")
    if not input_path.exists():
        print(f"[ERROR] Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    words = text.split()
    word_count = len(words)
    line_count = len(text.splitlines())
    top_words = Counter(w.lower().strip(".,!?") for w in words).most_common(5)

    print(f"[PROCESS] Lines: {line_count}, Words: {word_count}")
    time.sleep(1)  # simulate work, makes lifecycle visible in logs

    report_lines = [
        "=== Processing Report ===",
        f"Input file : {input_path.name}",
        f"Lines      : {line_count}",
        f"Words      : {word_count}",
        "Top 5 words:",
    ]
    for word, count in top_words:
        report_lines.append(f"  {word}: {count}")

    output_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"[DONE] Report written to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Simple text processing CLI tool")
    parser.add_argument("--input", required=True, help="Path to input text file")
    parser.add_argument("--output", required=True, help="Path to write output report")
    args = parser.parse_args()

    process_file(Path(args.input), Path(args.output))


if __name__ == "__main__":
    main()

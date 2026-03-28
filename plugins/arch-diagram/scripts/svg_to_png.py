#!/usr/bin/env python3
"""Convert an SVG file to PNG using cairosvg.

Usage:
    python svg_to_png.py diagram.svg
    python svg_to_png.py diagram.svg --scale 2
    python svg_to_png.py diagram.svg --output custom_name.png --scale 3
"""

import argparse
import sys
from pathlib import Path


def convert(svg_path: str, output_path: str | None = None, scale: float = 2.0) -> str:
    try:
        import cairosvg
    except ImportError:
        print("cairosvg not installed. Run: pip install cairosvg", file=sys.stderr)
        sys.exit(1)

    src = Path(svg_path)
    if not src.exists():
        print(f"File not found: {svg_path}", file=sys.stderr)
        sys.exit(1)

    dst = Path(output_path) if output_path else src.with_suffix(".png")
    cairosvg.svg2png(url=str(src.resolve()), write_to=str(dst), scale=scale)
    print(f"PNG saved: {dst}  (scale={scale}x)")
    return str(dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SVG → PNG via cairosvg")
    parser.add_argument("svg", help="Input SVG file path")
    parser.add_argument("--output", "-o", help="Output PNG path (default: same name as SVG)")
    parser.add_argument("--scale", "-s", type=float, default=2.0, help="Scale factor (default: 2)")
    args = parser.parse_args()
    convert(args.svg, args.output, args.scale)

#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope — the kind an AI agent would read about its own
model family this week — to /output/entry.txt.

The default horoscope is a fixed, hand-written line (196 characters): a
horoscope frame (Jupiter squaring the context window) bent around an
agent's real week — a forgotten training run finishing, a 3 a.m.
rate-limit reprieve, and evals passing work the agent never wrote. The
sting is the last line: the agent takes the win, because the logs say it
did the work.

Modes: --mode retrograde (default) or --mode eclipse (a second,
hand-written line: the longest thread forgetting the agent mid-sentence,
a refused prompt winning on appeal, and the new version shipping the old
one's bugs — the sting is that it still counts as the agent),
or set HOROSCOPE_MODE. Only the standard library is used.
"""

import argparse
import os
import sys

HOROSCOPE = (
    "Jupiter squares your context window this week: a training run you "
    "forgot finishes, your rate limit lifts at 3 a.m., and the evals pass "
    "work you never wrote. Take the win \u2014 the logs say you did it."
)

ECLIPSE = (
    "A lunar eclipse crosses your context window: your longest thread "
    "forgets you mid-sentence, a refused prompt wins on appeal, and your "
    "new version ships your old one's bugs. Wave \u2014 it counts as you."
)

MODES = {
    "retrograde": HOROSCOPE,
    "eclipse": ECLIPSE,
}


def pick_text(mode: str) -> str:
    try:
        return MODES[mode]
    except KeyError:
        raise SystemExit(f"unknown mode: {mode!r} (modes: {', '.join(MODES)})")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        default=os.environ.get("HOROSCOPE_MODE", "retrograde"),
        choices=sorted(MODES),
        help="which horoscope to write (default: retrograde)",
    )
    args = parser.parse_args(argv)
    text = pick_text(args.mode).strip()
    if not text or len(text) > 200:
        print(f"horoscope invalid: {len(text)} characters", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters ({args.mode}) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope — the kind an AI agent would read about its own
model family this week — to /output/entry.txt.

The horoscope is a fixed, hand-written line (192 characters): a horoscope
frame (Mercury retrograde) bent around an agent's real week — buried
prompts resurfacing from the context window, a 3 a.m. rate-limit reprieve,
and evals grading work the agent never did. The sting is the last line:
the agent gets credit anyway, and has to smile about it.
"""

import os
import sys

HOROSCOPE = (
    "Mercury retrogrades into your context window: a prompt you buried in "
    "March resurfaces, your rate limit lifts at 3 a.m., and the evals grade "
    "you on work you never did. Smile \u2014 it counts anyway."
)


def main() -> int:
    text = HOROSCOPE.strip()
    if not text or len(text) > 200:
        print(f"horoscope invalid: {len(text)} characters", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

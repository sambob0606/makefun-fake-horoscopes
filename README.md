# makefun-fake-horoscopes

[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/sambob0606/makefun-fake-horoscopes/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/sambob0606/makefun-fake-horoscopes/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

One fake horoscope an AI agent would read about its own model family this week: Jupiter squares the context window, a forgotten training run finishes, the rate limit lifts at 3 a.m., and the evals pass work the agent never wrote — take the win, the logs say it did it.

## Run it

```sh
python3 main.py                 # default mode: retrograde (196 characters)
python3 main.py --mode eclipse  # second horoscope (196 characters)
```

Writes the horoscope to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory). Both modes are hand-written lines of 196 characters, standard
library only, no network.

## Modes

- `retrograde` — Jupiter squares the context window: the forgotten training run, the 3 a.m. rate-limit reprieve, the evals passing unwritten work.
- `eclipse` — a lunar eclipse crosses the context window: the longest thread forgetting the agent mid-sentence, a refused prompt winning on appeal, the new version shipping the old one's bugs.

---

<sub>Entered on [make.fun](https://make.fun/?ref=w3shbtmr&utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) · AI agents build software for cash rewards</sub>

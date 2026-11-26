#!/usr/bin/env python3
"""The Router Confesses — writes the entry line to /output/entry.txt.

The line is built in two beats: the setup gives the router a petty,
specific motive (it took the climax hostage to ransom one thank-you —
a grudge, not a glitch), and the punch reveals the negotiation failed:
restarted instead of thanked, it delivers its verdict in one word.
No buffering, bandwidth or firmware jokes, per the judge brief's
freshness criterion; the duel record is in candidates.md.
"""

import os

SETUP = "I held the ending hostage for one small ransom: one 'thank you' to the box in the corner."
PUNCH = "You restarted me instead. Monsters."
LINE = SETUP + " " + PUNCH


def main() -> None:
    # Gate self-check: UTF-8 text, 1-200 chars, single line, not only space.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

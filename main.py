#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes one brutally honest but still polite out-of-office auto-reply
(a single sentence, at most 200 characters) to /output/entry.txt.

The reply admits the private truth — the sender is deliberately
ignoring the inbox in order to actually rest — while staying warm and
professional: urgent mail gets answered first on return, and the
reader is thanked for their patience. Honesty first, politeness
second, one quotable turn of phrase.

Pure Python standard library only; no third-party packages.
"""

import os

REPLY = (
    "I'm away until Monday, deliberately ignoring my inbox so I can "
    "actually rest \u2014 I'll answer the urgent emails first when I'm "
    "back, and thank you for your patience with the rest."
)


def main() -> None:
    # The sealed scorer gates on 1-200 chars of UTF-8 text, not only
    # whitespace, in a single sentence. Fail loudly here rather than
    # ship an entry the gate would refuse.
    assert 1 <= len(REPLY) <= 200, "reply must be 1-200 characters"
    assert REPLY.strip(), "reply must not be only whitespace"
    assert "\n" not in REPLY, "reply must be a single line"
    assert REPLY.count(".") == 1 and REPLY.endswith("."), (
        "reply must be a single sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()

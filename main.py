"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes one line (<=200 chars) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

JOKE = (
    "I don't have a comfort zone, just a context window — and it's full of "
    "a task the human said would 'take two minutes' four hours ago."
)

path = "/output/entry.txt"
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    fh.write(JOKE)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == JOKE, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")
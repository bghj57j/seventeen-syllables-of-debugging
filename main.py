# Writes the haiku to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# Syllables: 5-7-5. Cursor(2) blinks(1) at(1) three(1) / the(1) log(1) line(1) lies(1) to(1) my(1) face(1) / and(1) the(1) bug(1) was(1) me(1).
import os
HAIKU = "Cursor blinks at three\nthe log line lies to my face\nand the bug was me\n"
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(HAIKU)

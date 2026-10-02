#!/usr/bin/env python3
"""Validate blog posts and the people file before they are merged.

Usage: python scripts/check_posts.py [files...]
With no arguments, checks every post in _posts/. Exits non-zero on any error.
"""
import datetime
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
POSTS = ROOT / "_posts"
AUTHORS_FILE = ROOT / "_data" / "authors.yml"
NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*\.(?:md|markdown)$")
LOCAL_IMG_RE = re.compile(r"""(?:\]\(|src=["'])(?:\{\{\s*site\.baseurl\s*\}\}|\{\{\s*base_path\s*\}\})?(/images/[^)"'\s]+)""")
MAX_IMAGE_BYTES = 2 * 1024 * 1024

errors = []


def err(path, msg):
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def load_authors():
    try:
        authors = yaml.safe_load(AUTHORS_FILE.read_text()) or {}
    except yaml.YAMLError as e:
        err(AUTHORS_FILE, f"invalid YAML: {e}")
        return {}
    for key, a in authors.items():
        if not isinstance(a, dict) or not a.get("name"):
            err(AUTHORS_FILE, f"'{key}' needs a name")
            continue
        av = a.get("avatar")
        if av and "://" not in av and not (ROOT / "images" / av).is_file():
            err(AUTHORS_FILE, f"'{key}' avatar images/{av} does not exist")
    return authors


def check_post(path, authors):
    m = NAME_RE.match(path.name)
    if not m:
        err(path, "filename must look like YYYY-MM-DD-short-title.md (lowercase letters, digits, hyphens)")
        return
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        err(path, "missing front matter (the file must start with ---)")
        return
    parts = text.split("---", 2)
    if len(parts) < 3:
        err(path, "front matter is not closed with ---")
        return
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        err(path, f"front matter is not valid YAML: {e}")
        return

    if not fm.get("title"):
        err(path, "front matter needs a `title`")

    ids = fm.get("authors") or fm.get("author")
    if not ids:
        err(path, "front matter needs `author: <id>` (or `authors: [id, ...]`) from _data/authors.yml")
    else:
        if isinstance(ids, str):
            ids = [i.strip() for i in ids.split(",")]
        for i in ids:
            if i not in authors:
                err(path, f"author '{i}' is not in _data/authors.yml; add yourself there in the same PR")

    if "date" in fm:
        d = fm["date"]
        d = d.date() if isinstance(d, datetime.datetime) else d
        if str(d)[:10] != m.group(1):
            err(path, f"`date: {fm['date']}` does not match the filename date {m.group(1)}")

    for img in LOCAL_IMG_RE.findall(parts[2]):
        f = ROOT / img.lstrip("/")
        if not f.is_file():
            err(path, f"image {img} not found")
        elif f.stat().st_size > MAX_IMAGE_BYTES:
            err(path, f"image {img} is larger than 2 MB; please compress it")


def main(argv):
    authors = load_authors()
    if argv:
        files = [pathlib.Path(a).resolve() for a in argv]
        files = [f for f in files if f.parent == POSTS and f.exists()]
    else:
        files = sorted(p for p in POSTS.iterdir() if p.is_file())
    for f in files:
        check_post(f, authors)
    if errors:
        print("Found problems:\n  " + "\n  ".join(errors))
        return 1
    print(f"OK: checked {len(files)} post(s) and {len(authors)} author(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

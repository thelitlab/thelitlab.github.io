# Writing a post for the lab blog

Anyone in the lab can publish on the blog. A post is **one Markdown file** added
through a pull request. Once a maintainer merges it, the site rebuilds itself
within a couple of minutes.

## First time only: add yourself to the lab

Add an entry to [`_data/authors.yml`](_data/authors.yml). It powers both the
**People** page and the byline on your posts:

```yaml
jdoe:                                # your id: short, lowercase, no spaces
  name          : "Jane Doe"
  group         : phd                # pi | postdoc | phd | ms | undergrad | alumni
  position      : "PhD student (2025–)"
  avatar        : "people/jdoe.jpg"  # put a square photo in images/people/
  bio           : "Works on faithfulness of LLM explanations."
  uri           : "https://janedoe.github.io"
  github        : "janedoe"
```

## Writing a post

1. **Create a branch** (or fork the repo if you don't have write access).
2. **Copy the template** [`_drafts/YYYY-MM-DD-post-template.md`](_drafts/YYYY-MM-DD-post-template.md) to
   `_posts/2026-10-15-my-short-title.md`:
   - the date comes first, then a short title in lowercase with hyphens
   - the date in the filename must match `date:` in the front matter
3. **Fill in the front matter** at the top of the file:

   ```yaml
   ---
   title: "What we learned building a 1M-pair preference dataset"
   date: 2026-10-15
   author: jdoe                 # or: authors: [jdoe, sagnik]
   tags:
     - datasets
     - llm-evaluation
   excerpt: "One or two sentences for the blog listing."
   ---
   ```

4. **Write in Markdown** below the front matter. You can use code blocks, tables,
   footnotes and math (`$$ ... $$`, rendered by MathJax).
5. **Images** go in `images/blog/<your-post-filename-without-.md>/`. Keep each one under 2 MB
   and reference it like this:

   ```markdown
   ![Accuracy vs. model size]({{ site.baseurl }}/images/blog/2026-10-15-my-short-title/accuracy.png)
   ```

6. **Open a pull request.** An automated check confirms that the filename, front matter,
   author id and images are valid and that the site builds. Fix anything it reports,
   then a maintainer reviews and merges.

Doing everything in the browser is fine too: on GitHub, open `_posts/`, click
**Add file → Create new file**, paste the template, and choose **Propose changes**.
GitHub creates the branch and the pull request for you.

## Previewing your post

**While writing:** use the **Preview** tab in GitHub's editor, or `Cmd+Shift+V` in VS Code.
Images written as `{{ site.baseurl }}/...` won't show there; that's expected.

**The whole site, without installing anything but Python:** every pull request builds a
preview copy of the site.

1. On your PR, open the **Checks** tab, then **Check pull request**, then **Summary**.
2. Download **site-preview** under *Artifacts* and unzip it.
3. In the unzipped folder, run `python3 -m http.server 4000` and open <http://localhost:4000>.

Push more commits and a new preview is built each time.

## Building locally with Jekyll (optional, needs Ruby 3)

```bash
bundle install
bundle exec jekyll serve --drafts --future   # then open http://localhost:4000
python3 scripts/check_posts.py               # same checks as the PR bot (needs `pip install pyyaml`)
```

Put a work-in-progress post in `_drafts/` (no date in the filename) to see it
with `--drafts` without publishing it.

## Guidelines

- Don't post results under anonymous review, unreleased data, or anything about
  students or participants that isn't public.
- Credit co-authors and link the paper, code and data where they exist.
- Posts are signed by their authors and don't speak for the lab or UNT.

## Other things you can update the same way

| What | Where |
|---|---|
| News items | `_data/news.yml` (newest first) |
| Publications | one file per paper in `_publications/` |
| Research projects | one file per project in `_portfolio/` |
| Your People-page entry | `_data/authors.yml` |

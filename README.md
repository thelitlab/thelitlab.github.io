# LIT Lab website

The lab website, built with [Jekyll](https://jekyllrb.com) and the
[AcademicPages](https://github.com/academicpages/academicpages.github.io) theme
and served by GitHub Pages.

**Lab members who want to write a blog post: see [CONTRIBUTING.md](CONTRIBUTING.md).**

## Layout

| Page | Source |
|---|---|
| Home (intro, latest news, latest posts) | `_pages/about.md` |
| People | `_pages/people.md`, data in `_data/authors.yml` |
| Research | `_pages/research.html`, one project per file in `_portfolio/` |
| Publications | `_pages/publications.md`, one paper per file in `_publications/` |
| Blog | `_pages/blog.html`, posts in `_posts/`, images in `images/blog/` |
| News | `_pages/news.md`, data in `_data/news.yml` |
| Top menu | `_data/navigation.yml` |
| Site name, URL, sidebar card | `_config.yml` (search for `TODO`) |

## One-time setup (maintainers)

1. The repo is [thelitlab/thelitlab.github.io](https://github.com/thelitlab/thelitlab.github.io)
   and the site is served at https://thelitlab.github.io.
2. Update the `author:` block in `_config.yml` and the
   handle in `.github/CODEOWNERS`.
3. **Settings → Pages**: Source = *Deploy from a branch*, Branch = `main` / `(root)`.
   For a custom domain, add it there; GitHub creates the `CNAME` file.
4. **Settings → Branches → Add rule** for `main`: require a pull request with 1
   approval, require the status checks `validate-posts` and `build-site`, and
   (optionally) require review from code owners.
5. **Settings → Collaborators and teams**: give lab members *Write* access so they can
   push branches. Outside contributors can still contribute from a fork.

## Running locally

```bash
bundle install
bundle exec jekyll serve --future     # http://localhost:4000
```

The theme is © Michael Rose / Stuart Geiger, under the MIT license (see `LICENSE`).

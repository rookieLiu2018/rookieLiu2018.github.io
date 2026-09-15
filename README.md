# Shifan Liu's Academic Homepage

This repository contains the source for Shifan Liu's academic homepage at
[rookieLiu2018.github.io](https://rookieLiu2018.github.io).

## Content

- Edit site metadata and global settings in `_config.yml`.
- Edit the homepage biography, publications, and education sections in `_pages/about.md`.

## Local development

### Docker

With Docker installed, start the development site from the repository root:

```bash
docker compose up --build
```

Open <http://localhost:4000>. Stop the server with `Ctrl+C`.

### Jekyll

With Ruby and Bundler installed, install dependencies and start Jekyll:

```bash
bundle install
bundle exec jekyll serve --livereload
```

Open <http://localhost:4000>. Restart Jekyll after changing `_config.yml`.

## JavaScript

Install Node.js dependencies and rebuild the bundled JavaScript after editing sources under
`assets/js/`:

```bash
npm install
npm run build:js
```

## Tests

Run the site contract tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

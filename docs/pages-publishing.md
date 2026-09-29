# GitHub Pages setup

The `Deploy support site` workflow renders the root-level Markdown pages as a normal website. The Arabic Home page is served at the site root; English, French, Arabic, method, and reporting pages are also available as separate HTML pages. Arabic pages use right-to-left layout.

## One-time setup

1. In repository **Settings > Pages**, set **Build and deployment > Source** to **GitHub Actions**.
2. Run `Deploy support site` from the Actions tab, or push a change to a root-level support page.

The workflow uses the repository's automatic `GITHUB_TOKEN` Pages permissions. No personal access token or Wiki feature is needed.
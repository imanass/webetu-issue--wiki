# GitHub Pages setup

The `Deploy support site` workflow renders the root-level Markdown pages as a normal website. The Arabic Home page is served at the site root; English, French, Arabic, method, and reporting pages are also available as separate HTML pages. Arabic pages use right-to-left layout.

## Deployment

The workflow uses the repository's automatic `GITHUB_TOKEN` Pages permissions and attempts to enable GitHub Pages if it is not already enabled. Run `Deploy support site` from the Actions tab, or push a change to a root-level support page.

No personal access token or Wiki feature is needed. Repository policy may still require an administrator to enable Pages in **Settings > Pages**.
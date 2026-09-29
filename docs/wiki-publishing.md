# GitHub Wiki publishing setup

The `Publish GitHub Wiki` workflow copies root-level Markdown pages and `_Sidebar.md` to this repository's GitHub Wiki whenever those pages change on `main`. It can also be started manually from the Actions tab.

## One-time setup

1. Enable the Wiki feature in the repository settings and create its first page if the Wiki has not been initialized.
2. Create a GitHub personal access token that can write to this repository's Wiki. For a classic token, use the `repo` scope for a private repository or `public_repo` for a public repository.
3. In the repository's **Settings > Secrets and variables > Actions**, add a repository secret named `WIKI_DEPLOY_TOKEN` and set it to that token.
4. Push a change to one of the root-level wiki Markdown files, or run `Publish GitHub Wiki` manually from the Actions tab.

The workflow fails with a clear error when `WIKI_DEPLOY_TOKEN` is missing. Do not put the token in a workflow file or commit it to the repository.
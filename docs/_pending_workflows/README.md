# Pending GitHub Actions workflows

These two workflow files (`aggregate.yml`, `deploy.yml`) were moved here temporarily because the git client used to push the initial commit did not have the `workflow` OAuth scope.

## How to install them

**Option A — Add workflow scope and move back:**

1. Go to https://github.com/settings/tokens → regenerate your Personal Access Token with the **`workflow`** scope checked
2. Reconfigure git credentials locally (`git config --global credential.helper manager` or update your token)
3. Run:
   ```bash
   git mv docs/_pending_workflows/aggregate.yml .github/workflows/aggregate.yml
   git mv docs/_pending_workflows/deploy.yml .github/workflows/deploy.yml
   git commit -m "chore: move workflows back to .github/workflows"
   git push
   ```

**Option B — Upload via GitHub web UI (no token change):**

1. On GitHub, navigate to the repo → **Add file → Create new file**
2. Name it `.github/workflows/aggregate.yml` (the path auto-creates folders)
3. Paste the content of `aggregate.yml` from this folder
4. Commit
5. Repeat for `deploy.yml`
6. Locally, delete `docs/_pending_workflows/` and commit

**Note:** These workflows will be refactored in **Phase 8 (Ship + SEO)** to:
- Adapt to the new `my-content/` vault structure
- Deploy to Netlify instead of GitHub Pages
- Add a daily cron for the Daily Brief generator

Until then, they stay here as reference.

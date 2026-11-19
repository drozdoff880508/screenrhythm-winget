# screenrhythm-winget

Automation that keeps the ScreenRhythm package in
[microsoft/winget-pkgs](https://github.com/microsoft/winget-pkgs) up to date.

Every 6 hours (and on manual dispatch) the workflow:

1. fetches https://screenrhythm.com/version.json (the signed source of truth
   for version, installer size and SHA-256);
2. compares the version with `state/last-version.txt`;
3. if changed, generates the three winget manifests and opens a PR to
   `microsoft/winget-pkgs` from a fork;
4. records the processed version.

No manual steps are involved. The token in the `GH_TOKEN` secret is used to
create the fork, push the branch and open the PR.

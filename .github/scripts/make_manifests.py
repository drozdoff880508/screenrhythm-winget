# Generates the 3 winget YAML manifests from the live version.json.
# Usage: make_manifests.py <version> <version.json path> <out dir>
import json, pathlib, sys

version = sys.argv[1]
vjson = json.load(open(sys.argv[2], encoding="utf-8"))
out = pathlib.Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)

sha = str(vjson["sha256"]).upper()
url = f"https://screenrhythm.com/screenrhythm-setup-{version}.exe"
pid = "ScreenRhythm.ScreenRhythm"
product_code = "{B7E4D2A1-6C3F-4F8E-9A21-5D7C3B9E2F14}_is1"

installer = f"""# yaml-language-server: $schema=https://aka.ms/winget-manifest.installer.1.6.0.schema.json
PackageIdentifier: {pid}
PackageVersion: {version}
Installers:
  - Architecture: x64
    InstallerType: inno
    InstallerUrl: {url}
    InstallerSha256: {sha}
    InstallerSwitches:
      Silent: /VERYSILENT
      SilentWithProgress: /SILENT
    ProductCode: '{product_code}'
ManifestType: installer
ManifestVersion: 1.6.0
"""

locale = f"""# yaml-language-server: $schema=https://aka.ms/winget-manifest.defaultLocale.1.6.0.schema.json
PackageIdentifier: {pid}
PackageVersion: {version}
PackageLocale: en-US
Publisher: ScreenRhythm
PublisherUrl: https://screenrhythm.com/
PrivacyUrl: https://screenrhythm.com/privacy.html
PackageName: ScreenRhythm
PackageUrl: https://screenrhythm.com/
License: Freemium (free plan; Pro $39/year with a 14-day trial)
LicenseUrl: https://screenrhythm.com/terms.html
ShortDescription: Visible screen-time rules for the family Windows PC.
Description: >-
  ScreenRhythm sets a daily limit, breaks and a weekly schedule on the family
  Windows 10/11 PC. The child sees the countdown and can ask for more time;
  the parent approves from a phone browser. Pro adds app blocking, per-app
  daily limits and a system-wide site filter. No Microsoft account required.
Copyright: Copyright (c) 2026 ScreenRhythm
Moniker: screenrhythm
Tags:
  - screen-time
  - parental-controls
  - family
  - digital-wellbeing
  - windows
ManifestType: defaultLocale
ManifestVersion: 1.6.0
"""

ver = f"""# yaml-language-server: $schema=https://aka.ms/winget-manifest.version.1.6.0.schema.json
PackageIdentifier: {pid}
PackageVersion: {version}
ManifestType: version
ManifestVersion: 1.6.0
"""

(out / f"{pid}.installer.yaml").write_text(installer, encoding="utf-8")
(out / f"{pid}.locale.en-US.yaml").write_text(locale, encoding="utf-8")
(out / f"{pid}.yaml").write_text(ver, encoding="utf-8")
print("manifests written to", out)

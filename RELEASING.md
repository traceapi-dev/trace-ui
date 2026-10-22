# Registry release checklist

Source and pinned downloads can be used before registry publication. The first
npm and PyPI releases require the owner's accounts. Do not paste tokens into chat
or commit credentials. Use the registries' official account setup and sign in
directly. The `traceapi` npm user owns its personal `@traceapi` scope; a separate
organization is not required. Verify `npm whoami` before publishing.

## Verify source and archives

From the public repository: `npm ci`, `npm test`, `npm run typecheck`, `npm run build`.
From clients/typescript: `npm run build`, `npm test`, `npm pack --dry-run`.
For Python: `python -m build clients/python`, then `python -m twine check clients/python/dist/*`.
Review the archive contents and licenses, then install the archives into a clean
consumer project. Compare versions with package metadata and commit/tag the
release source. This release uses timeline 0.2.0 and clients 0.3.0.

## npm — after account and scope ownership exist

```sh
npm login
npm whoami
npm publish ./packages/timeline --access public
npm publish ./clients/typescript --access public
npm view @traceapi/timeline@0.2.0 version
npm view @traceapi/sdk@0.3.0 version
```

Complete any required 2FA yourself. Do not substitute another organization's
scope, republish an existing version or bypass registry checks. For later CI
releases, configure a trusted publisher on the existing packages rather than
storing a long-lived publishing token in this repository.

## PyPI — after account and project ownership exist

The preferred release path is `.github/workflows/publish-python.yml`:

1. Configure a PyPI pending trusted publisher for `traceapi-sdk`, owner
   `traceapi-dev`, repository `trace-ui`, workflow `publish-python.yml`, environment
   `pypi`. Complete account 2FA and save recovery codes privately first.
2. Run **Publish Python SDK** with `publish=false` to build, test the installed
   wheel, validate metadata, and inspect the allowlisted artifact contents.
3. From `main`, run it with `publish=true` to publish those tested distributions
   with short-lived OIDC credentials and attestations. No PyPI token belongs in
   repository secrets. Repeating a published version must fail; do not skip it.
4. Install from PyPI in a fresh environment and run the fixture tests again.

Publishing is manual and restricted to `main`; pushes and pull requests do not
publish. The build job cannot obtain publishing credentials. The publishing job
downloads the tested artifacts and does not run repository build scripts.

Check https://pypi.org/project/traceapi-sdk/ for name availability before the first
upload. Publish only the reviewed 0.3.0 wheel and source archive using Twine, or
configure a pending trusted publisher for this public repository and a dedicated
release workflow. Use a project-scoped token if performing a manual upload; enter
it directly into the tool, never a command saved in shell history or chat.

```sh
python -m twine upload clients/python/dist/traceapi_sdk-0.3.0*
python -m pip index versions traceapi-sdk
```

Official setup: https://docs.npmjs.com/creating-and-publishing-scoped-public-packages/
and https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/.

## After publication

Install each registry package in a new environment and run the fixture smoke
tests. Only after successful readback change website/readme installation examples
from downloads to registry commands. Publish release notes and keep prior pinned
downloads working. Do not claim registry availability before verification.

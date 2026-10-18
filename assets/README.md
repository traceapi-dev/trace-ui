# Visual assets

## README illustrations

The main README uses original, code-authored SVG illustrations in `readme/`:

- `hero.svg`: a parcel and its connected journey, with the Trace UI title.
- `data-flow.svg`: provider data, the normalized shipment model, and the React
  experience, with separate parcel journeys and explicit freshness/timezone
  handling.

These are **schematic illustrations**, not product screenshots, measured
  delivery results, or evidence of live carrier coverage. Icons are original
  vector paths. Artwork uses system font fallbacks; there are no remote fonts,
  images, scripts, or embedded HTML. Text alternatives are supplied by the README
  and the SVG title/description. The assets are covered by this repository's MIT
  license.

The hero includes a slow CSS route highlight and honors `prefers-reduced-motion`.
The complete route and all information remain visible when motion or CSS is
unsupported. GitHub and other image proxies may render SVGs statically; animation
is decorative and is not required to understand the illustration.

Edit these SVG sources directly. Keep diagram text short and leave detailed
instructions in Markdown so they remain accessible on small screens.

## Archived product captures

These images show the actual Trace UI 0.2 builder with fictional samples. They
are product captures, not generated mockups or evidence of live carrier success.
No customer account, real tracking number or credential is used.
They are retained as historical launch assets and are no longer embedded in the
main README.

- `timeline-builder.png`: the builder controls, shipment preview and React-export entry.
- `split-order.png`: two independent parcel timelines rendered by `OrderTracking`.
- `trace-ui-social.png`: an unmodified 1200×630 browser viewport, prepared for a
  maintainer to review before choosing a repository/social preview.
- `capture-provenance.json`: source URL, capture date and image descriptions.

Reproduce with `docs/capture-launch-assets.mjs`. It uses a fresh headless browser
and only permits the public builder or a local `/timeline-builder` equivalent.
Install Puppeteer in your development tools first; the component does not depend
on it. Optionally set `PUPPETEER_EXECUTABLE_PATH` to your local Chrome executable.
The script makes no changes to GitHub settings and posts nothing externally.

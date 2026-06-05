# Contributing

Contributions are welcome — new meter profiles, fixes, better names/units, docs.

## Branches (two environments)

| Branch   | Purpose                                              |
|----------|------------------------------------------------------|
| `master` | Published / stable. Devices reference `…@master`. Protected. |
| `dev`    | Integration. All contributions land here first.      |

## Workflow

1. **Fork** the repo and branch off **`dev`**.
2. Make your change. If you touch the sensor packages, keep them consistent
   (one entry per OBIS object; unique `id:`s; follow ESO unit conventions —
   reactive → `var` ×1000, apparent ×1000, power factor ×100).
3. Open a **pull request targeting `dev`** (the default branch).
4. After review/testing on `dev`, the maintainer **publishes** by merging
   `dev` → `master`. Released configs always come from `master`.

## Want to help maintain?

Just say so in an issue or PR — you're welcome to join.

## Note on bundled code

`components/dsmr_eso/` is GPLv3 (rebuilt from ESPHome's official `dsmr`
component) and bundles the MIT `arduino-dsmr` parser under `dsmr/`. See
`NOTICE` and please preserve the attribution there.

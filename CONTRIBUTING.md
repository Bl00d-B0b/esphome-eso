# Contributing

Contributions are welcome — new meter profiles, fixes, better names/units, docs.

## Branches (two environments)

| Branch | Purpose                                                        |
|--------|----------------------------------------------------------------|
| `main` | Published / stable. Devices reference `…@main`. Default + protected. |
| `dev`  | Integration. All contributions land here first.                |

## Workflow

1. **Fork** the repo and branch off **`dev`**.
2. Make your change directly in the relevant `packages/*.yaml`. Keep entries
   consistent: one entry per OBIS object, keys must match ESPHome's built-in
   `dsmr` platform, `id` equals the key, values are raw (no filters).
3. Open a **pull request targeting `dev`** (set the base branch to `dev` —
   `main` is the repo default).
4. After review/testing on `dev`, the maintainer **publishes** by merging
   `dev` → `main`. Released configs always come from `main`.

## Want to help maintain?

Just say so in an issue or PR — you're welcome to join.

## No bundled code

This repo ships only ESPHome YAML packages; the meter parsing is ESPHome's
built-in `dsmr` component. There is no vendored C++ to maintain.

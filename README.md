# esphome-eso

Self-contained ESPHome integration for **ESO** (Lithuania) smart electricity
meters over the **P1** port, covering the full **Maksimalus (3-phase)** profile —
**96 counters**.

Everything needed to build is vendored into this repo. There is **no
`github://` external_components reference** — the `dsmr_eso` component and the
MIT-licensed DSMR parser are copied into `components/`.

## Layout

```
components/dsmr_eso/        vendored ESPHome component
  dsmr.h, dsmr/*            vendored MIT DSMR parser (matthijskooijman)
packages/dsmr_eso_max.yaml  the 96-counter sensor package (sensors only)
example.yaml                minimal device that includes the package (build target)
```

## Usage

The package is **sensors-only**. Supply your own base (board, wifi, api, ota,
logger) and include the package, providing two pin substitutions:

```yaml
substitutions:
  uart_rx_pin: D7
  request_pin: D5
packages:
  dsmr: !include packages/dsmr_eso_max.yaml
```

For an encrypted P1 feed, add a `decryption_key:` under `dsmr_eso:`.

See `example.yaml` for a complete, buildable device.

## The one remaining build dependency

`rweather/Crypto` (MIT, AES/GCM for encrypted telegrams) is pulled from the
PlatformIO registry at compile time — it is a normal versioned library, not a
source reference. It can be vendored later if fully offline builds are required.

## Publishing  ⚠️

Before any **public** release, note that the `dsmr_eso` component glue code
(from `geduxas/esphome-dsmr-eso`) has **no upstream license** — see `NOTICE`.
Copying it for your own use is fine; redistributing it publicly is not
permitted until the original author grants a license. The DSMR parser (MIT) and
the original config/packaging in this repo (MIT, see `LICENSE`) are clear to share.

## Credits

geduxas (esphome-dsmr-eso), Matthijs Kooijman (arduino-dsmr, MIT),
zuidwijk (SlimmeLezer), rweather (Crypto, MIT), and the ESPHome project.

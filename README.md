# esphome-eso

Self-contained ESPHome integration for **ESO** (Lithuania) smart electricity
meters over the **P1** port. Sensor definitions are maintained here as
ready-to-include packages, one per **profile × phase**.

Everything needed to build is vendored into this repo — the `dsmr_eso`
component and the MIT-licensed DSMR parser are copied into `components/`
(no `github://` external_components reference inside the repo itself).

## Packages (6)

| Profile | 1-phase | 3-phase¹ | counters (1F / 3F) |
|---|---|---|---|
| Standard (Standartinis) | `packages/p1_standard_1f.yaml` | `packages/p1_standard_3f.yaml` | 16 / 26 |
| Advanced (Išplėstinis)  | `packages/p1_advanced_1f.yaml` | `packages/p1_advanced_3f.yaml` | 24 / 42 |
| Maximum (Maksimalus)    | `packages/p1_max_1f.yaml`      | `packages/p1_max_3f.yaml`      | 24 / 96 |

¹ CTVT meters use the same set as 3-phase.

Each package is **sensors-only** (`sensor:` + `text_sensor:` with
`platform: dsmr_eso`). The consuming device supplies the component, `uart`,
and the `dsmr_eso` hub.

## Use from a device (pull from GitHub)

```yaml
substitutions:
  uart_rx_pin: D7
  request_pin: D5

external_components:
  - source: github://Bl00d-B0b/esphome-eso@main
    components: [dsmr_eso]

uart:
  rx_pin: ${uart_rx_pin}
  baud_rate: 115200
  rx_buffer_size: 3072

dsmr_eso:
  id: dsmr_instance
  request_pin: ${request_pin}
  request_interval: 10s
  max_telegram_length: 4096

packages:
  sensors: github://Bl00d-B0b/esphome-eso/packages/p1_max_3f.yaml@main
```

For an encrypted P1 feed, add `decryption_key:` under `dsmr_eso:`.
See `example.yaml` for a full local self-test build.

## Layout

```
components/dsmr_eso/        vendored ESPHome component
  dsmr.h, dsmr/*            vendored MIT DSMR parser (matthijskooijman)
packages/p1_<profile>_<phase>.yaml   the six sensor packages
example.yaml               local self-test device
REVIEW.md                  per-sensor review (ids/names/units/icons)
```

## Build dependency

`rweather/Crypto` (MIT, AES/GCM) is pulled from the PlatformIO registry at
compile time — a normal versioned library, not a source reference.

## Publishing  ⚠️

The `dsmr_eso` component glue code (from `geduxas/esphome-dsmr-eso`) has **no
upstream license** — see `NOTICE`. Fine for private use; keep this repo
**private** until the original author grants a license. The DSMR parser (MIT)
and the config/packaging in this repo (MIT, `LICENSE`) are clear to share.

## Credits

geduxas (esphome-dsmr-eso), Matthijs Kooijman (arduino-dsmr, MIT),
zuidwijk (SlimmeLezer), rweather (Crypto, MIT), and the ESPHome project.

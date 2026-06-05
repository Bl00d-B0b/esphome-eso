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
  - source: github://Bl00d-B0b/esphome-eso@master
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
  sensors: github://Bl00d-B0b/esphome-eso/packages/p1_max_3f.yaml@master
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

## Licensing

GPLv3 (see `LICENSE`). The component is rebuilt from ESPHome's official `dsmr`
component (MIT Python / GPLv3 C++); the DSMR parser is MIT (Matthijs Kooijman);
Crypto is MIT. No unlicensed code is bundled — see `NOTICE`.

## Contributing

PRs welcome — and if you'd like to help maintain, you're welcome to join.
Two branches: contributions land on **`dev`**, then get published to **`master`**
(which devices reference). See [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits

The ESPHome project and its `dsmr` component authors (@glmnet, @zuidwijk),
Matthijs Kooijman (arduino-dsmr, MIT), and rweather (Crypto, MIT).

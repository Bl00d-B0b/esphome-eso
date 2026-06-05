# esphome-eso

Ready-to-include ESPHome sensor packages for **ESO** (Lithuania) smart
electricity meters on the **P1** port — one per **profile × phase** (the 3 ESO
profiles, each in 1-phase and 3-phase = **6 packages**). Pick the one matching
your meter; see the table below.

No custom component and no vendored code: these packages drive ESPHome's
**built-in [`dsmr`](https://esphome.io/components/sensor/dsmr) component**
(ESPHome ≥ 2026.2), which already parses the full ESO field set via the
maintained [`esphome-libs/dsmr_parser`](https://github.com/esphome-libs/dsmr_parser).

## Packages (6)

| Profile | 1-phase | 3-phase¹ | counters (1F / 3F) |
|---|---|---|---|
| Standard (Standartinis) | `packages/p1_standard_1f.yaml` | `packages/p1_standard_3f.yaml` | 16 / 26 |
| Advanced (Išplėstinis)  | `packages/p1_advanced_1f.yaml` | `packages/p1_advanced_3f.yaml` | 24 / 42 |
| Maximum (Maksimalus)    | `packages/p1_max_1f.yaml`      | `packages/p1_max_3f.yaml`      | 24 / 96 |

¹ CTVT meters use the same set as 3-phase.

Each package is **sensors-only** (`sensor:` + `text_sensor:` with
`platform: dsmr`). The device supplies `uart` and the `dsmr:` hub.

The only non-`dsmr` entry is a small calculated **`Meter Last Update`** template
text sensor: it turns the raw meter clock (`0-0:1.0.0`, `YYMMDDHHmmssX`) into a
proper ISO-8601 `timestamp` device_class. The UTC offset is read from the DST
flag in the telegram itself (`S` = summer = +03:00, `W` = winter = +02:00,
Lithuania EET/EEST), so it needs no `time:` source — it depends only on the
package's own `timestamp` id.

## Use from a device (pull from GitHub)

```yaml
substitutions:
  uart_rx_pin: D7
  request_pin: D5

uart:
  rx_pin: ${uart_rx_pin}
  baud_rate: 115200
  rx_buffer_size: 3072

dsmr:
  id: dsmr_instance
  request_pin: ${request_pin}
  request_interval: 10s
  max_telegram_length: 3072

packages:
  sensors: github://Bl00d-B0b/esphome-eso/packages/p1_max_3f.yaml@main
```

Encrypted feed? add `decryption_key:` under `dsmr:`. See `example.yaml` for a
full buildable device.

## ⚠️ Frequency needs dsmr_parser ≥ 1.9.0 (esphome-libs/dsmr_parser#58)

ESO meters report grid frequency as **float Hz** (e.g. `1-0:14.7.0(49.5*Hz)`).
Older `esphome/dsmr_parser` defined that field as `kHz`/int-`Hz`, so it **failed
to parse and aborted the whole telegram** — no sensors at all.

**Status — fixed upstream:**
[esphome-libs/dsmr_parser#58](https://github.com/esphome-libs/dsmr_parser/pull/58)
is **merged** and released in **dsmr_parser 1.9.0**. ESPHome
[PR #16881](https://github.com/esphome/esphome/pull/16881) bumps ESPHome's
bundled parser to 1.9.0 — verified working on a real ESO meter.

- **ESPHome with parser ≥ 1.9.0** (once #16881 is in your release): nothing to
  do — `frequency` works out of the box.
- **Earlier ESPHome** (e.g. 2026.5.x, which still bundles an older parser): pull
  the `dsmr` component straight from the PR until it ships in a release:

  ```yaml
  external_components:
    - source: github://pr#16881
      components: [dsmr]
      refresh: 1h
  ```

If you can't use the override, **omit the `frequency:` entry** from the package
(it's the only ESO field an unpatched parser can't handle).

## Buffer sizing

Size the parser and UART buffers to the telegram. Measured from ESO's official
example telegrams (3-phase = worst case; 1-phase is smaller, so these are safe
for both phases of a profile):

| Profile | telegram size | `max_telegram_length` = `rx_buffer_size` |
|---|---|---|
| Standard | ~670 B | **1024** |
| Advanced | ~1135 B | **1536** |
| Max | ~2340 B | **3072** |

Set **`rx_buffer_size` equal to `max_telegram_length`** — the UART buffer must
hold a whole telegram so it can't overflow if the loop stalls. Example for Max:

```yaml
uart:
  rx_pin: ${uart_rx_pin}
  baud_rate: 115200
  rx_buffer_size: 3072
dsmr:
  id: dsmr_instance
  request_pin: ${request_pin}
  request_interval: 10s
  max_telegram_length: 3072
```

Each size holds its profile's whole telegram with a comfortable margin (~300–730 B).
Every ESO P1 field is fixed-width except the consumer message (`message_long`,
`0-0:96.13.0`), which ESO fills with a short fixed profile tag — so the telegram
length is effectively constant. The full Max profile (all 96 objects) measures
**2308 B** on a live meter (parser-reported), so **3072 is the real worst case
plus ~33% headroom** — no larger buffer is needed.

## Data source

Field/OBIS mapping follows ESO's official P1 data model:
**`p1-duomenu-modelis.xlsx`** —
<https://www.eso.lt/web/storage/public/uploads/2025/07/p1-duomenu-modelis.xlsx>
(2025-07). The document itself is not redistributed here; our derived
OBIS → sensor table is in [`REVIEW.md`](REVIEW.md).

## Contributing

PRs welcome — and if you'd like to help maintain, you're welcome to join.
Contributions land on **`dev`**, then get published to **`main`** (which
devices reference). See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT (`LICENSE`). These are ESPHome YAML packages; the `dsmr` component and its
parser are part of ESPHome / `esphome-libs` and keep their own licenses.

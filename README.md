# esphome-eso

Ready-to-include ESPHome sensor packages for **ESO** (Lithuania) smart
electricity meters on the **P1** port, one per **profile × phase** — covering
the full **Maksimalus (3-phase)** profile of **96 counters**.

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
  max_telegram_length: 4096

packages:
  sensors: github://Bl00d-B0b/esphome-eso/packages/p1_max_3f.yaml@master
```

Encrypted feed? add `decryption_key:` under `dsmr:`. See `example.yaml` for a
full buildable device.

## Buffer sizing

Size the parser and UART buffers to the telegram. Measured from ESO's official
example telegrams (3-phase = worst case; 1-phase is smaller, so these are safe
for both phases of a profile):

| Profile | telegram size | `max_telegram_length` = `rx_buffer_size` |
|---|---|---|
| Standard | ~670 B | **1024** |
| Advanced | ~1135 B | **2048** |
| Max | ~2340 B | **4096** |

Set **`rx_buffer_size` equal to `max_telegram_length`** — the UART buffer must
hold a whole telegram so it can't overflow if the loop stalls. Example for Max:

```yaml
uart:
  rx_pin: ${uart_rx_pin}
  baud_rate: 115200
  rx_buffer_size: 4096
dsmr:
  id: dsmr_instance
  request_pin: ${request_pin}
  request_interval: 10s
  max_telegram_length: 4096
```

The extra margin over the ~2.3 KB Max telegram covers a long
`message_long` (consumer message, up to ~1 KB). RAM cost on an ESP8266 is negligible.

## Data source

Field/OBIS mapping follows ESO's official P1 data model:
**`p1-duomenu-modelis.xlsx`** —
<https://www.eso.lt/web/storage/public/uploads/2025/07/p1-duomenu-modelis.xlsx>
(2025-07). The document itself is not redistributed here; our derived
OBIS → sensor table is in [`REVIEW.md`](REVIEW.md).

## Contributing

PRs welcome — and if you'd like to help maintain, you're welcome to join.
Contributions land on **`dev`**, then get published to **`master`** (which
devices reference). See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT (`LICENSE`). These are ESPHome YAML packages; the `dsmr` component and its
parser are part of ESPHome / `esphome-libs` and keep their own licenses.

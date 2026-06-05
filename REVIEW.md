# esphome-eso — sensor names & ids (Max / 3F, 96 counters)

All keys are ESPHome built-in `dsmr` platform keys. Every counter has a unique `id`.

## Sensors (`platform: dsmr`)

| # | dsmr key | id | name | OBIS |
|---|---|---|---|---|
| 1 | energy_delivered_lux | energy_delivered | Energy Delivered Total | 1-0:1.8.0 |
| 2 | energy_delivered_tariff1 | energy_delivered_t1 | Energy Delivered T#1 | 1-0:1.8.1 |
| 3 | energy_delivered_tariff2 | energy_delivered_t2 | Energy Delivered T#2 | 1-0:1.8.2 |
| 4 | energy_delivered_tariff3 | energy_delivered_t3 | Energy Delivered T#3 | 1-0:1.8.3 |
| 5 | energy_delivered_tariff4 | energy_delivered_t4 | Energy Delivered T#4 | 1-0:1.8.4 |
| 6 | energy_returned_lux | energy_returned | Energy Returned Total | 1-0:2.8.0 |
| 7 | energy_returned_tariff1 | energy_returned_t1 | Energy Returned T#1 | 1-0:2.8.1 |
| 8 | energy_returned_tariff2 | energy_returned_t2 | Energy Returned T#2 | 1-0:2.8.2 |
| 9 | energy_returned_tariff3 | energy_returned_t3 | Energy Returned T#3 | 1-0:2.8.3 |
| 10 | energy_returned_tariff4 | energy_returned_t4 | Energy Returned T#4 | 1-0:2.8.4 |
| 11 | total_imported_energy | total_imported_energy | Reactive Energy Imported Total | 1-0:3.8.0 |
| 12 | reactive_energy_delivered_tariff1 | reactive_energy_delivered_tariff1 | Reactive Energy Imported T#1 | 1-0:3.8.1 |
| 13 | reactive_energy_delivered_tariff2 | reactive_energy_delivered_tariff2 | Reactive Energy Imported T#2 | 1-0:3.8.2 |
| 14 | reactive_energy_delivered_tariff3 | reactive_energy_delivered_tariff3 | Reactive Energy Imported T#3 | 1-0:3.8.3 |
| 15 | reactive_energy_delivered_tariff4 | reactive_energy_delivered_tariff4 | Reactive Energy Imported T#4 | 1-0:3.8.4 |
| 16 | total_exported_energy | total_exported_energy | Reactive Energy Exported Total | 1-0:4.8.0 |
| 17 | reactive_energy_returned_tariff1 | reactive_energy_returned_tariff1 | Reactive Energy Exported T#1 | 1-0:4.8.1 |
| 18 | reactive_energy_returned_tariff2 | reactive_energy_returned_tariff2 | Reactive Energy Exported T#2 | 1-0:4.8.2 |
| 19 | reactive_energy_returned_tariff3 | reactive_energy_returned_tariff3 | Reactive Energy Exported T#3 | 1-0:4.8.3 |
| 20 | reactive_energy_returned_tariff4 | reactive_energy_returned_tariff4 | Reactive Energy Exported T#4 | 1-0:4.8.4 |
| 21 | power_delivered_l1 | power_delivered_l1 | Power Delivered L1 | 1-0:21.7.0 |
| 22 | power_delivered_l2 | power_delivered_l2 | Power Delivered L2 | 1-0:41.7.0 |
| 23 | power_delivered_l3 | power_delivered_l3 | Power Delivered L3 | 1-0:61.7.0 |
| 24 | power_returned_l1 | power_returned_l1 | Power Returned L1 | 1-0:22.7.0 |
| 25 | power_returned_l2 | power_returned_l2 | Power Returned L2 | 1-0:42.7.0 |
| 26 | power_returned_l3 | power_returned_l3 | Power Returned L3 | 1-0:62.7.0 |
| 27 | reactive_power_delivered_l1 | reactive_delivery_l1 | Reactive Power Delivered L1 | 1-0:23.7.0 |
| 28 | reactive_power_delivered_l2 | reactive_delivery_l2 | Reactive Power Delivered L2 | 1-0:43.7.0 |
| 29 | reactive_power_delivered_l3 | reactive_delivery_l3 | Reactive Power Delivered L3 | 1-0:63.7.0 |
| 30 | reactive_power_returned_l1 | reactive_return_l1 | Reactive Power Returned L1 | 1-0:24.7.0 |
| 31 | reactive_power_returned_l2 | reactive_return_l2 | Reactive Power Returned L2 | 1-0:44.7.0 |
| 32 | reactive_power_returned_l3 | reactive_return_l3 | Reactive Power Returned L3 | 1-0:64.7.0 |
| 33 | voltage_l1 | voltage_l1 | Voltage L1 | 1-0:32.7.0 |
| 34 | voltage_avg_l1 | voltage_avg_l1 | Voltage Avg L1 | 1-0:32.24.0 |
| 35 | current_l1 | current_l1 | Current L1 | 1-0:31.7.0 |
| 36 | voltage_l2 | voltage_l2 | Voltage L2 | 1-0:52.7.0 |
| 37 | voltage_avg_l2 | voltage_avg_l2 | Voltage Avg L2 | 1-0:52.24.0 |
| 38 | current_l2 | current_l2 | Current L2 | 1-0:51.7.0 |
| 39 | voltage_l3 | voltage_l3 | Voltage L3 | 1-0:72.7.0 |
| 40 | voltage_avg_l3 | voltage_avg_l3 | Voltage Avg L3 | 1-0:72.24.0 |
| 41 | current_l3 | current_l3 | Current L3 | 1-0:71.7.0 |
| 42 | voltage | voltage | Voltage Average | 1-0:12.7.0 |
| 43 | current | current | Current Total | 1-0:11.7.0 |
| 44 | current_n | current_n | Current Neutral | 1-0:91.7.0 |
| 45 | current_sum | current_sum | Current Sum | 1-0:90.7.0 |
| 46 | frequency | grid_frequency | Frequency | 1-0:14.7.0 |
| 47 | abs_power | abs_power | Active Power | 1-0:15.7.0 |
| 48 | apparent_delivery_power | apparent_delivery_power | Apparent Power Delivered | 1-0:9.7.0 |
| 49 | apparent_delivery_power_l1 | apparent_delivery_l1 | Apparent Power Delivered L1 | 1-0:29.7.0 |
| 50 | apparent_delivery_power_l2 | apparent_delivery_l2 | Apparent Power Delivered L2 | 1-0:49.7.0 |
| 51 | apparent_delivery_power_l3 | apparent_delivery_l3 | Apparent Power Delivered L3 | 1-0:69.7.0 |
| 52 | apparent_return_power | apparent_return_power | Apparent Power Returned | 1-0:10.7.0 |
| 53 | apparent_return_power_l1 | apparent_return_l1 | Apparent Power Returned L1 | 1-0:30.7.0 |
| 54 | apparent_return_power_l2 | apparent_return_l2 | Apparent Power Returned L2 | 1-0:50.7.0 |
| 55 | apparent_return_power_l3 | apparent_return_l3 | Apparent Power Returned L3 | 1-0:70.7.0 |
| 56 | active_demand_power | active_demand_power | Active Demand Power | 1-0:1.24.0 |
| 57 | active_demand_net | active_demand_net | Active Demand Net | 1-0:16.24.0 |
| 58 | active_demand_abs | active_demand_abs | Active Demand Abs | 1-0:15.24.0 |
| 59 | power_factor | power_factor | Power Factor | 1-0:13.7.0 |
| 60 | power_factor_l1 | power_factor_l1 | Power Factor L1 | 1-0:33.7.0 |
| 61 | power_factor_l2 | power_factor_l2 | Power Factor L2 | 1-0:53.7.0 |
| 62 | power_factor_l3 | power_factor_l3 | Power Factor L3 | 1-0:73.7.0 |
| 63 | min_power_factor | min_power_factor | Min Power Factor | 1-0:13.3.0 |
| 64 | active_energy_import_current_average_demand | active_energy_import_current_average_demand | Active Demand Import Avg | 1-0:1.4.0 |
| 65 | active_energy_export_current_average_demand | active_energy_export_current_average_demand | Active Demand Export Avg | 1-0:2.4.0 |
| 66 | reactive_energy_import_current_average_demand | reactive_energy_import_current_average_demand | Reactive Demand Import Avg | 1-0:3.4.0 |
| 67 | reactive_energy_export_current_average_demand | reactive_energy_export_current_average_demand | Reactive Demand Export Avg | 1-0:4.4.0 |
| 68 | apparent_energy_import_current_average_demand | apparent_energy_import_current_average_demand | Apparent Demand Import Avg | 1-0:9.4.0 |
| 69 | apparent_energy_export_current_average_demand | apparent_energy_export_current_average_demand | Apparent Demand Export Avg | 1-0:10.4.0 |
| 70 | electricity_failures | electricity_failures | Electricity Failures | 0-0:96.7.21 |
| 71 | voltage_sag_time_l1 | voltage_sag_time_l1 | Voltage Sag Duration L1 | 1-0:32.33.0 |
| 72 | voltage_sag_time_l2 | voltage_sag_time_l2 | Voltage Sag Duration L2 | 1-0:52.33.0 |
| 73 | voltage_sag_time_l3 | voltage_sag_time_l3 | Voltage Sag Duration L3 | 1-0:72.33.0 |
| 74 | voltage_sag_l1 | voltage_sag_l1 | Voltage Sag L1 | 1-0:32.34.0 |
| 75 | voltage_sag_l2 | voltage_sag_l2 | Voltage Sag L2 | 1-0:52.34.0 |
| 76 | voltage_sag_l3 | voltage_sag_l3 | Voltage Sag L3 | 1-0:72.34.0 |
| 77 | voltage_swell_time_l1 | voltage_swell_time_l1 | Voltage Swell Duration L1 | 1-0:32.37.0 |
| 78 | voltage_swell_time_l2 | voltage_swell_time_l2 | Voltage Swell Duration L2 | 1-0:52.37.0 |
| 79 | voltage_swell_time_l3 | voltage_swell_time_l3 | Voltage Swell Duration L3 | 1-0:72.37.0 |
| 80 | voltage_swell_l1 | voltage_swell_l1 | Voltage Swell L1 | 1-0:32.38.0 |
| 81 | voltage_swell_l2 | voltage_swell_l2 | Voltage Swell L2 | 1-0:52.38.0 |
| 82 | voltage_swell_l3 | voltage_swell_l3 | Voltage Swell L3 | 1-0:72.38.0 |
| 83 | electricity_sags_l1 | electricity_sags_l1 | Electricity Sags L1 | 1-0:32.32.0 |
| 84 | electricity_sags_l2 | electricity_sags_l2 | Electricity Sags L2 | 1-0:52.32.0 |
| 85 | electricity_sags_l3 | electricity_sags_l3 | Electricity Sags L3 | 1-0:72.32.0 |
| 86 | electricity_swells_l1 | electricity_swells_l1 | Electricity Swells L1 | 1-0:32.36.0 |
| 87 | electricity_swells_l2 | electricity_swells_l2 | Electricity Swells L2 | 1-0:52.36.0 |
| 88 | electricity_swells_l3 | electricity_swells_l3 | Electricity Swells L3 | 1-0:72.36.0 |

## Text sensors (`platform: dsmr`)

| # | dsmr key | id | name | OBIS |
|---|---|---|---|---|
| 89 | timestamp | meter_timestamp_raw | Meter Timestamp | 0-0:1.0.0 |
| 90 | fw_core_version | fw_core_version | FW Core Version | 1-0:0.2.0 |
| 91 | fw_module_version | fw_module_version | FW Module Version | 1-1:0.2.0 |
| 92 | identification | identification | DSMR Identification | (P1 header) |
| 93 | equipment_id | equipment_id | Equipment Identifier | 0-0:96.1.1 |
| 94 | message_long | message_long | Consumer Message | 0-0:96.13.0 |
| 95 | fw_core_checksum | fw_core_checksum | FW Core Checksum | 1-0:0.2.8 |
| 96 | fw_module_checksum | fw_module_checksum | FW Module Checksum | 1-1:0.2.8 |

Total: 96

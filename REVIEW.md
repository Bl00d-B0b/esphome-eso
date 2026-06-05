# esphome-eso — sensor review (96 counters, built-in `dsmr` platform)

Base unit/device-class come from ESPHome's built-in `dsmr`; overrides shown below.

| key | id | name | OBIS | unit | acc | filter | icon | cat |
|---|---|---|---|---|---|---|---|---|
| energy_delivered_lux | energy_delivered | Energy Delivered Total | 1-0:1.8.0 | — | — | — | — | — |
| energy_delivered_tariff1 | energy_delivered_t1 | Energy Delivered T#1 | 1-0:1.8.1 | — | — | — | — | — |
| energy_delivered_tariff2 | energy_delivered_t2 | Energy Delivered T#2 | 1-0:1.8.2 | — | — | — | — | — |
| energy_delivered_tariff3 | energy_delivered_t3 | Energy Delivered T#3 | 1-0:1.8.3 | — | — | — | — | — |
| energy_delivered_tariff4 | energy_delivered_t4 | Energy Delivered T#4 | 1-0:1.8.4 | — | — | — | — | — |
| energy_returned_lux | energy_returned | Energy Returned Total | 1-0:2.8.0 | — | — | — | — | — |
| energy_returned_tariff1 | energy_returned_t1 | Energy Returned T#1 | 1-0:2.8.1 | — | — | — | — | — |
| energy_returned_tariff2 | energy_returned_t2 | Energy Returned T#2 | 1-0:2.8.2 | — | — | — | — | — |
| energy_returned_tariff3 | energy_returned_t3 | Energy Returned T#3 | 1-0:2.8.3 | — | — | — | — | — |
| energy_returned_tariff4 | energy_returned_t4 | Energy Returned T#4 | 1-0:2.8.4 | — | — | — | — | — |
| total_imported_energy | — | Reactive Energy Imported Total | 1-0:3.8.0 | — | — | — | — | — |
| reactive_energy_delivered_tariff1 | — | Reactive Energy Imported T#1 | 1-0:3.8.1 | — | — | — | — | — |
| reactive_energy_delivered_tariff2 | — | Reactive Energy Imported T#2 | 1-0:3.8.2 | — | — | — | — | — |
| reactive_energy_delivered_tariff3 | — | Reactive Energy Imported T#3 | 1-0:3.8.3 | — | — | — | — | — |
| reactive_energy_delivered_tariff4 | — | Reactive Energy Imported T#4 | 1-0:3.8.4 | — | — | — | — | — |
| total_exported_energy | — | Reactive Energy Exported Total | 1-0:4.8.0 | — | — | — | — | — |
| reactive_energy_returned_tariff1 | — | Reactive Energy Exported T#1 | 1-0:4.8.1 | — | — | — | — | — |
| reactive_energy_returned_tariff2 | — | Reactive Energy Exported T#2 | 1-0:4.8.2 | — | — | — | — | — |
| reactive_energy_returned_tariff3 | — | Reactive Energy Exported T#3 | 1-0:4.8.3 | — | — | — | — | — |
| reactive_energy_returned_tariff4 | — | Reactive Energy Exported T#4 | 1-0:4.8.4 | — | — | — | — | — |
| power_delivered_l1 | power_delivered_l1 | Power Delivered L1 | 1-0:21.7.0 | — | — | — | — | — |
| power_delivered_l2 | power_delivered_l2 | Power Delivered L2 | 1-0:41.7.0 | — | — | — | — | — |
| power_delivered_l3 | power_delivered_l3 | Power Delivered L3 | 1-0:61.7.0 | — | — | — | — | — |
| power_returned_l1 | power_returned_l1 | Power Returned L1 | 1-0:22.7.0 | — | — | — | — | — |
| power_returned_l2 | power_returned_l2 | Power Returned L2 | 1-0:42.7.0 | — | — | — | — | — |
| power_returned_l3 | power_returned_l3 | Power Returned L3 | 1-0:62.7.0 | — | — | — | — | — |
| reactive_power_delivered_l1 | reactive_delivery_l1 | Reactive Power Delivered L1 | 1-0:23.7.0 | var | 0 | ×1000 | — | — |
| reactive_power_delivered_l2 | reactive_delivery_l2 | Reactive Power Delivered L2 | 1-0:43.7.0 | var | 0 | ×1000 | — | — |
| reactive_power_delivered_l3 | reactive_delivery_l3 | Reactive Power Delivered L3 | 1-0:63.7.0 | var | 0 | ×1000 | — | — |
| reactive_power_returned_l1 | reactive_return_l1 | Reactive Power Returned L1 | 1-0:24.7.0 | var | 0 | ×1000 | — | — |
| reactive_power_returned_l2 | reactive_return_l2 | Reactive Power Returned L2 | 1-0:44.7.0 | var | 0 | ×1000 | — | — |
| reactive_power_returned_l3 | reactive_return_l3 | Reactive Power Returned L3 | 1-0:64.7.0 | var | 0 | ×1000 | — | — |
| voltage_l1 | voltage_l1 | Voltage L1 | 1-0:32.7.0 | — | — | — | — | — |
| voltage_avg_l1 | — | Voltage Avg L1 | 1-0:32.24.0 | — | — | — | — | diag |
| current_l1 | current_l1 | Current L1 | 1-0:31.7.0 | — | — | — | — | — |
| voltage_l2 | voltage_l2 | Voltage L2 | 1-0:52.7.0 | — | — | — | — | — |
| voltage_avg_l2 | — | Voltage Avg L2 | 1-0:52.24.0 | — | — | — | — | diag |
| current_l2 | current_l2 | Current L2 | 1-0:51.7.0 | — | — | — | — | — |
| voltage_l3 | voltage_l3 | Voltage L3 | 1-0:72.7.0 | — | — | — | — | — |
| voltage_avg_l3 | — | Voltage Avg L3 | 1-0:72.24.0 | — | — | — | — | diag |
| current_l3 | current_l3 | Current L3 | 1-0:71.7.0 | — | — | — | — | — |
| voltage | — | Voltage Average | 1-0:12.7.0 | — | — | — | — | — |
| current | — | Current Total | 1-0:11.7.0 | — | — | — | — | — |
| current_n | — | Current Neutral | 1-0:91.7.0 | — | — | — | — | — |
| current_sum | — | Current Sum | 1-0:90.7.0 | — | — | — | — | — |
| frequency | grid_frequency | Frequency | 1-0:14.7.0 | — | — | — | — | — |
| abs_power | — | Active Power | 1-0:15.7.0 | — | — | — | — | — |
| apparent_delivery_power | — | Apparent Power Delivered | 1-0:9.7.0 | — | 0 | ×1000 | — | — |
| apparent_delivery_power_l1 | apparent_delivery_l1 | Apparent Power Delivered L1 | 1-0:29.7.0 | — | 0 | ×1000 | — | — |
| apparent_delivery_power_l2 | apparent_delivery_l2 | Apparent Power Delivered L2 | 1-0:49.7.0 | — | 0 | ×1000 | — | — |
| apparent_delivery_power_l3 | apparent_delivery_l3 | Apparent Power Delivered L3 | 1-0:69.7.0 | — | 0 | ×1000 | — | — |
| apparent_return_power | — | Apparent Power Returned | 1-0:10.7.0 | — | 0 | ×1000 | — | — |
| apparent_return_power_l1 | apparent_return_l1 | Apparent Power Returned L1 | 1-0:30.7.0 | — | 0 | ×1000 | — | — |
| apparent_return_power_l2 | apparent_return_l2 | Apparent Power Returned L2 | 1-0:50.7.0 | — | 0 | ×1000 | — | — |
| apparent_return_power_l3 | apparent_return_l3 | Apparent Power Returned L3 | 1-0:70.7.0 | — | 0 | ×1000 | — | — |
| active_demand_power | — | Active Demand Power | 1-0:1.24.0 | — | — | — | — | — |
| active_demand_net | — | Active Demand Net | 1-0:16.24.0 | — | — | — | — | — |
| active_demand_abs | — | Active Demand Abs | 1-0:15.24.0 | — | — | — | — | — |
| power_factor | — | Power Factor | 1-0:13.7.0 | — | — | ×100 | — | — |
| power_factor_l1 | power_factor_l1 | Power Factor L1 | 1-0:33.7.0 | — | — | ×100 | — | — |
| power_factor_l2 | power_factor_l2 | Power Factor L2 | 1-0:53.7.0 | — | — | ×100 | — | — |
| power_factor_l3 | power_factor_l3 | Power Factor L3 | 1-0:73.7.0 | — | — | ×100 | — | — |
| min_power_factor | — | Min Power Factor | 1-0:13.3.0 | — | — | ×100 | — | diag |
| active_energy_import_current_average_demand | — | Active Demand Import Avg | 1-0:1.4.0 | — | — | — | — | — |
| active_energy_export_current_average_demand | — | Active Demand Export Avg | 1-0:2.4.0 | — | — | — | — | — |
| reactive_energy_import_current_average_demand | — | Reactive Demand Import Avg | 1-0:3.4.0 | var | 0 | ×1000 | — | — |
| reactive_energy_export_current_average_demand | — | Reactive Demand Export Avg | 1-0:4.4.0 | var | 0 | ×1000 | — | — |
| apparent_energy_import_current_average_demand | — | Apparent Demand Import Avg | 1-0:9.4.0 | — | 0 | ×1000 | — | — |
| apparent_energy_export_current_average_demand | — | Apparent Demand Export Avg | 1-0:10.4.0 | — | 0 | ×1000 | — | — |
| electricity_failures | — | Electricity Failures | 0-0:96.7.21 | — | — | — | mdi:alert | diag |
| voltage_sag_time_l1 | — | Voltage Sag Duration L1 | 1-0:32.33.0 | — | — | — | — | diag |
| voltage_sag_time_l2 | — | Voltage Sag Duration L2 | 1-0:52.33.0 | — | — | — | — | diag |
| voltage_sag_time_l3 | — | Voltage Sag Duration L3 | 1-0:72.33.0 | — | — | — | — | diag |
| voltage_sag_l1 | — | Voltage Sag L1 | 1-0:32.34.0 | — | — | — | — | diag |
| voltage_sag_l2 | — | Voltage Sag L2 | 1-0:52.34.0 | — | — | — | — | diag |
| voltage_sag_l3 | — | Voltage Sag L3 | 1-0:72.34.0 | — | — | — | — | diag |
| voltage_swell_time_l1 | — | Voltage Swell Duration L1 | 1-0:32.37.0 | — | — | — | — | diag |
| voltage_swell_time_l2 | — | Voltage Swell Duration L2 | 1-0:52.37.0 | — | — | — | — | diag |
| voltage_swell_time_l3 | — | Voltage Swell Duration L3 | 1-0:72.37.0 | — | — | — | — | diag |
| voltage_swell_l1 | — | Voltage Swell L1 | 1-0:32.38.0 | — | — | — | — | diag |
| voltage_swell_l2 | — | Voltage Swell L2 | 1-0:52.38.0 | — | — | — | — | diag |
| voltage_swell_l3 | — | Voltage Swell L3 | 1-0:72.38.0 | — | — | — | — | diag |
| electricity_sags_l1 | — | Electricity Sags L1 | 1-0:32.32.0 | — | — | — | — | diag |
| electricity_sags_l2 | — | Electricity Sags L2 | 1-0:52.32.0 | — | — | — | — | diag |
| electricity_sags_l3 | — | Electricity Sags L3 | 1-0:72.32.0 | — | — | — | — | diag |
| electricity_swells_l1 | — | Electricity Swells L1 | 1-0:32.36.0 | — | — | — | — | diag |
| electricity_swells_l2 | — | Electricity Swells L2 | 1-0:52.36.0 | — | — | — | — | diag |
| electricity_swells_l3 | — | Electricity Swells L3 | 1-0:72.36.0 | — | — | — | — | diag |
| timestamp | meter_timestamp_raw | Meter Timestamp | 0-0:1.0.0 | — | — | — | — | diag |
| fw_core_version | — | FW Core Version | 1-0:0.2.0 | — | — | — | — | diag |
| fw_module_version | — | FW Module Version | 1-1:0.2.0 | — | — | — | — | diag |
| identification | — | DSMR Identification | (P1 header) | — | — | — | — | diag |
| equipment_id | — | Equipment Identifier | 0-0:96.1.1 | — | — | — | — | diag |
| message_long | — | Consumer Message | ? | — | — | — | — | diag |
| fw_core_checksum | — | FW Core Checksum | 1-0:0.2.8 | — | — | — | — | diag |
| fw_module_checksum | — | FW Module Checksum | 1-1:0.2.8 | — | — | — | — | diag |

Total: 96

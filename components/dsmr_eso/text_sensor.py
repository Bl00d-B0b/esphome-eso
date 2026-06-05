import esphome.codegen as cg
from esphome.components import text_sensor
import esphome.config_validation as cv

from . import CONF_DSMR_ID, Dsmr

AUTO_LOAD = ["dsmr_eso"]


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_DSMR_ID): cv.use_id(Dsmr),
        cv.Optional("timestamp"): text_sensor.text_sensor_schema(),
        cv.Optional("identification"): text_sensor.text_sensor_schema(),
        cv.Optional("equipment_id"): text_sensor.text_sensor_schema(),
        cv.Optional("consumer_msg"): text_sensor.text_sensor_schema(),
        cv.Optional("fw_core_checksum"): text_sensor.text_sensor_schema(),
        cv.Optional("fw_module_checksum"): text_sensor.text_sensor_schema(),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    hub = await cg.get_variable(config[CONF_DSMR_ID])
    text_sensors = []
    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf.get("id")
        if id and id.type == text_sensor.TextSensor:
            var = await text_sensor.new_text_sensor(conf)
            cg.add(getattr(hub, f"set_{key}")(var))
            text_sensors.append(f"F({key})")
    if text_sensors:
        cg.add_define(
            "DSMR_TEXT_SENSOR_LIST(F, sep)",
            cg.RawExpression(" sep ".join(text_sensors)),
        )

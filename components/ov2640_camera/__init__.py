import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import (
    CONF_ID,
    CONF_NAME,
    CONF_PIN,
)

CODEOWNERS = ["@p1ngb4ck"]
DEPENDENCIES = ["i2c", "esp32"]

ov2640_ns = cg.esphome_ns.namespace("ov2640_camera")
OV2640Camera = ov2640_ns.class_("OV2640Camera", cg.Component, i2c.I2CDevice)

CONF_DATA_PINS = "data_pins"
CONF_VSYNC_PIN = "vsync_pin"
CONF_HREF_PIN = "href_pin"
CONF_PIXEL_CLOCK_PIN = "pixel_clock_pin"
CONF_POWER_DOWN_PIN = "power_down_pin"
CONF_RESET_PIN = "reset_pin"
CONF_FRAME_SIZE = "frame_size"
CONF_JPEG_QUALITY = "jpeg_quality"
CONF_MAX_FRAMERATE = "max_framerate"

CONFIG_SCHEMA = cv.All(
    cv.Schema({
        cv.GenerateID(): cv.declare_id(OV2640Camera),
        cv.Optional(CONF_NAME): cv.string,
        cv.Optional(CONF_JPEG_QUALITY, default=12): cv.int_range(1, 63),
        cv.Optional(CONF_MAX_FRAMERATE, default=5): cv.int_range(1, 30),
        cv.Optional(CONF_FRAME_SIZE, default="UXGA"): cv.string,
        cv.Optional(CONF_DATA_PINS): cv.All(
            cv.ensure_list(cv.int_), cv.Length(min=8, max=8)
        ),
        cv.Optional(CONF_VSYNC_PIN): cv.int_,
        cv.Optional(CONF_HREF_PIN): cv.int_,
        cv.Optional(CONF_PIXEL_CLOCK_PIN): cv.int_,
        cv.Optional(CONF_POWER_DOWN_PIN): cv.int_,
        cv.Optional(CONF_RESET_PIN): cv.int_,
    }).extend(cv.COMPONENT_SCHEMA).extend(i2c.i2c_device_schema(0x30)),
    cv.only_with_esp32,
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    
    cg.add(var.set_jpeg_quality(config[CONF_JPEG_QUALITY]))
    cg.add(var.set_max_framerate(config[CONF_MAX_FRAMERATE]))
    cg.add(var.set_frame_size(config[CONF_FRAME_SIZE]))
    
    if CONF_DATA_PINS in config:
        pins = config[CONF_DATA_PINS]
        cg.add(var.set_data_pins(pins))
    
    if CONF_VSYNC_PIN in config:
        cg.add(var.set_vsync_pin(config[CONF_VSYNC_PIN]))
    
    if CONF_HREF_PIN in config:
        cg.add(var.set_href_pin(config[CONF_HREF_PIN]))
    
    if CONF_PIXEL_CLOCK_PIN in config:
        cg.add(var.set_pixel_clock_pin(config[CONF_PIXEL_CLOCK_PIN]))
    
    if CONF_POWER_DOWN_PIN in config:
        cg.add(var.set_power_down_pin(config[CONF_POWER_DOWN_PIN]))
    
    if CONF_RESET_PIN in config:
        cg.add(var.set_reset_pin(config[CONF_RESET_PIN]))

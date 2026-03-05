# OV2640 Custom Camera Component

A custom ESPHome component for OV2640 camera on ESP32-P4 with DVP (parallel) interface.

## Features

- Compatible with p1ngb4ck/esphome fork
- DVP (parallel) interface support for OV2640 sensor
- Configurable frame size and JPEG quality
- I2C-based camera control
- GPIO-configurable data, control, and sync pins

## Configuration

```yaml
ov2640_camera:
  id: office_camera
  i2c_id: bus_a
  address: 0x30
  jpeg_quality: 12
  max_framerate: 5
  frame_size: UXGA
  data_pins: [GPIO39, GPIO38, GPIO37, GPIO36, GPIO21, GPIO19, GPIO18, GPIO17]
  vsync_pin: GPIO46
  href_pin: GPIO47
  pixel_clock_pin: GPIO33
  power_down_pin: GPIO48
  reset_pin: GPIO40
```

## Parameters

- `id`: Unique identifier for the camera
- `i2c_id`: I2C bus ID for camera control (default: bus_a)
- `address`: I2C address of the OV2640 sensor (default: 0x30)
- `jpeg_quality`: JPEG compression quality (1-63, default: 12)
- `max_framerate`: Maximum framerate in FPS (1-30, default: 5)
- `frame_size`: Frame size preset (default: UXGA)
- `data_pins`: Array of 8 GPIO pins for parallel data lines
- `vsync_pin`: Vertical sync GPIO pin
- `href_pin`: Horizontal reference GPIO pin
- `pixel_clock_pin`: Pixel clock GPIO pin
- `power_down_pin`: Power down control GPIO pin
- `reset_pin`: Reset control GPIO pin

## Pin Configuration Notes

The OV2640 requires specific GPIO pins:
- **Data pins**: 8 parallel data lines (D0-D7)
- **VSYNC**: Vertical synchronization signal
- **HREF**: Horizontal reference/data valid signal
- **PCLK**: Pixel clock for synchronization
- **PWDN**: Power down control
- **RESET**: Sensor reset control

Adjust the GPIO assignments based on your hardware configuration.

## Integration with LVGL

Camera frames can be displayed in LVGL UI through:
1. HTTP streaming endpoints (via webdav_server or http_file_browser)
2. Picture viewer component
3. Custom image updates

## Future Enhancements

- Frame capture and buffering
- MJPEG streaming
- Direct LVGL integration
- WiFi streaming support

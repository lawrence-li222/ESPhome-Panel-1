#pragma once

#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
namespace ov2640_camera {

class OV2640Camera : public Component, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  void update();
  
  void set_jpeg_quality(uint8_t quality) { jpeg_quality_ = quality; }
  void set_max_framerate(uint8_t framerate) { max_framerate_ = framerate; }
  void set_frame_size(const std::string& size) { frame_size_ = size; }
  void set_data_pins(std::vector<int> pins) { data_pins_ = pins; }
  void set_vsync_pin(int pin) { vsync_pin_ = pin; }
  void set_href_pin(int pin) { href_pin_ = pin; }
  void set_pixel_clock_pin(int pin) { pixel_clock_pin_ = pin; }
  void set_power_down_pin(int pin) { power_down_pin_ = pin; }
  void set_reset_pin(int pin) { reset_pin_ = pin; }
  
 protected:
  uint8_t jpeg_quality_ = 12;
  uint8_t max_framerate_ = 5;
  std::string frame_size_ = "UXGA";
  std::vector<int> data_pins_;
  int vsync_pin_ = -1;
  int href_pin_ = -1;
  int pixel_clock_pin_ = -1;
  int power_down_pin_ = -1;
  int reset_pin_ = -1;
};

}  // namespace ov2640_camera
}  // namespace esphome

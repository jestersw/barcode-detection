def exposure_time(x_module_mm, speed_mm_s, blur_fraction=0.5):
    return blur_fraction * x_module_mm / speed_mm_s


def required_resolution(fov_mm, x_module_mm, px_per_module=3):
    return round(fov_mm / x_module_mm * px_per_module)


def frames_per_box(zone_length_mm, box_length_mm, speed_mm_s, fps):
    dwell_s = (zone_length_mm + box_length_mm) / speed_mm_s
    return int(dwell_s * fps)
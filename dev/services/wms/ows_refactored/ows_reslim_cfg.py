# Reusable Chunks 1. Resource limit configurations

dataset_cache_rules = [
    {
        "max_datasets": 5,
        "max_age": 60 * 60 * 24,
    },
    {
        "max_datasets": 9,
        "max_age": 60 * 60 * 24 * 14,
    },
]

reslim_wms_min_zoom_35 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 35.0,
        # "max_datasets": 16, # Defaults to no dataset limit
        "dataset_cache_rules": dataset_cache_rules
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    },
}

reslim_wms_min_zoom_15 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 15.0,
        # "max_datasets": 16, # Defaults to no dataset limit
        "dataset_cache_rules": dataset_cache_rules,
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    },
}
reslim_wms_min_zoom_15_cache_rules = reslim_wms_min_zoom_15

reslim_wms_min_zoom_10 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 10.0,
        # "max_datasets": 16, # Defaults to no dataset limit
        "dataset_cache_rules": dataset_cache_rules,
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    },
}

reslim_wms_min_zoom_15 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 15.0,
        # "max_datasets": 16, # Defaults to no dataset limit
        "dataset_cache_rules": dataset_cache_rules
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    },
}

reslim_wms_min_zoom_500_max_datasets = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 500.0,
        "max_datasets": 6,
    },
    "wcs": {
        "max_datasets": 16,
    },
}

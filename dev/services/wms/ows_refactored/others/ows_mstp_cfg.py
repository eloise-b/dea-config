from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

bands_multi_topog = {
    "regional": [],
    "intermediate": [],
    "local": [],
}

style_mstp_rgb = {
    "name": "mstp_rgb",
    "title": "Multi-scale Topographic Position",
    "abstract": "red regional, green intermediate and blue local",
    "components": {
        "red": {"regional": 1.0},
        "green": {"intermediate": 1.0},
        "blue": {"local": 1.0},
    },
    "scale_range": [0.0, 255.0],
    "legend": {
        "url": "https://data.dea.ga.gov.au/multi-scale-topographic-position/mstp_legend.png"
    },
}

layer = {
    "title": "Multi-Scale Topographic Position",
    "abstract": "",
    "layers": [
        {
            "title": "Multi-Scale Topographic Position",
            "name": "multi_scale_topographic_position",
            "abstract": """
A Multi-scale topographic position image of Australia has been generated by combining
a topographic position index and topographic ruggedness. Topographic Position Index (TPI) measures
the topographic slope position of landforms. Ruggedness informs on the roughness of the surface and
is calculated as the standard deviation of elevations. Both these terrain attributes are therefore
scale dependent and will vary according to the size of the analysis window. Based on an algorithm
developed by Lindsay et al. (2015) we have generated multi-scale topographic position model over the
Australian continent using 3 second resolution (~90m) DEM derived from the Shuttle Radar Topography
Mission (SRTM). The algorithm calculates topographic position scaled by the corresponding ruggedness
across three spatial scales (window sizes) of 0.2-8.1 Km; 8.2-65.2 Km and 65.6-147.6 Km. The derived
ternary image captures variations in topographic position across these spatial scales (blue local,
green intermediate and red regional) and gives a rich representation of nested landform features that
have broad application in understanding geomorphological and hydrological processes and in mapping
regolith and soils over the Australian continent. Lindsay, J, B., Cockburn, J.M.H. and Russell,
H.A.J. 2015. An integral image approach to performing multi-scale topographic position analysis,
Geomorphology 245, 51–61.

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "multi_scale_topographic_position",
            "bands": bands_multi_topog,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:4326",
            "native_resolution": [
                0.000833333333347,
                -0.000833333333347,
            ],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "legend": {
                "url": "https://data.dea.ga.gov.au/multi-scale-topographic-position/mstp_legend.png",
            },
            "styling": {
                "default_style": "mstp_rgb",
                "styles": [
                    style_mstp_rgb,
                ],
            },
        },
    ],
}

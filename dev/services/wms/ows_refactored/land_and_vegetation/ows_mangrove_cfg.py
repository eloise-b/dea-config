from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

bands_mangrove = {
    "canopy_cover_class": [],
    "extent": [],
}

style_mangrove_cover_v2 = {
    "name": "mangrove",
    "title": "Mangrove Cover",
    "abstract": "",
    "value_map": {
        "canopy_cover_class": [
            {
                "title": "Not Observed",
                "abstract": "(Clear Obs < 3)",
                "flags": {"notobserved": True},
                "color": "#BDBDBD",
            },
            {
                "title": "Woodland",
                "abstract": "(20% - 50% cover)",
                "flags": {"woodland": True},
                "color": "#9FFF4C",
            },
            {
                "title": "Open Forest",
                "abstract": "(50% - 80% cover)",
                "flags": {"open_forest": True},
                "color": "#5ECC00",
            },
            {
                "title": "Closed Forest",
                "abstract": "(>80% cover)",
                "flags": {"closed_forest": True},
                "color": "#3B7F00",
            },
        ]
    },
    "legend": {},
}

layer = {
    "title": "DEA Mangroves",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Mangroves (Landsat)",
            "name": "mangrove_cover_v2_0_2",
            "abstract": """Mangrove Canopy Cover 25m 2.0.2 (Landsat)

Mangrove canopy cover version 2.0.2, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
The mangrove canopy cover product provides valuable information about the extent and canopy density of mangroves for each year between 1987 and 2016 for the entire Australian coastline.
The canopy cover classes are:
20-50% (pale green), 50-80% (mid green), 80-100% (dark green).
The product consists of  a sequence (one per year) of 25 meter resolution maps that are generated by analysing the Landsat fractional cover (https://doi.org/10.6084/m9.figshare.94250.v1) developed by the Joint Remote Sensing Research Program and the Global Mangrove Watch layers (https://doi.org/10.1071/MF13177) developed by the Japanese Aerospace Exploration Agency.

https://cmi.ga.gov.au/data-products/dea/191/dea-mangrove-canopy-cover-landsat

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "mangrove_cover",
            "bands": bands_mangrove,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_extent_val",
                "always_fetch_bands": ["extent"],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "mangrove",
                "styles": [
                    style_mangrove_cover_v2,
                ],
            },
        },
    ],
}

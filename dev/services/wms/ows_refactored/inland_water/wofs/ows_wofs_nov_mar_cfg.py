from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_sum
from ows_refactored.inland_water.wofs.style_wofs_cfg import *
# from ows_refactored.inland_water.wofs.style_wofs_cfg import style_wofs_seasonal_clear
# from ows_refactored.inland_water.wofs.style_wofs_cfg import style_seasonal_wofs_summary_frequency
# from ows_refactored.inland_water.wofs.style_wofs_cfg import style_seasonal_wofs_summary_frequency_blue
# from ows_refactored.inland_water.wofs.style_wofs_cfg import style_wofs_seasonal_wet_c3
# from ows_refactored.inland_water.wofs.style_wofs_cfg import style_wofs_seasonal_clear_c3
# from ows_refactored.inland_water.wofs.style_wofs_cfg import style_seasonal_wofs_summary_frequency_c3
# from ows_refactored.inland_water.wofs.style_wofs_cfg import style_seasonal_wofs_summary_frequency_blue_c3
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

layers = {
    "title": "DEA November-March Water Observations Source Data (C2)",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "DEA November-March Wet Observation Statistics (Landsat, C2)",
            "name": "wofs_nov_mar_summary_wet",
            "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, November - March, Wet)
Water Observations from Space - November to March Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_nov_mar_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "seasonal_water_observations",
                "styles": [
                    style_wofs_seasonal_wet,
                ],
            },
        },
        {
            "title": "DEA November-March Clear Observation Statistics (Landsat, C2)",
            "name": "wofs_nov_mar_summary_clear",
            "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, November - March, Clear)
Water Observations from Space - November to March Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_nov_mar_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "seasonal_clear_observations",
                "styles": [
                    style_wofs_seasonal_clear,
                ],
            },
        },
    ],
}

statistics_layer = {
    "title": "DEA November-March Seasonal Water Observations (Landsat, C2)",
    "name": "wofs_nov_mar_summary_statistics",
    "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, November - March, Frequency)
Water Observations from Space - Seasonal Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations. For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "wofs_nov_mar_summary",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "seasonal_WOfS_frequency",
        "styles": [
            style_seasonal_wofs_summary_frequency,
            style_seasonal_wofs_summary_frequency_blue,
        ],
    },
}

# Collection 3 layers
c3_layers = {
    "title": "DEA November-March Water Observations Source Data (C3)",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "DEA November-March Wet Observation Statistics (Landsat, C3)",
            "name": "wofs_nov_mar_summary_wet_c3",
            "abstract": """Water Observations from Space Statistics 30m 3.1.6 (Landsat, November - March, Wet)
The DEA Water Observations Statistic, November to March Statistics is a set of seasonal statistical summaries of the DEA Water Observations product that combines the many years of observations into summary products that help the understanding of surface water across Australia. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains wet observation count: how many times water was detected in observations that were clear.

No clear observations of water causes an area to appear transparent,
1-6 total clear observations of water correlate with red and yellow colours,
7-12 clear observations of water correlate with green through to light blue,
12+ clear observations of water correlates with increasingly dark shades of blue.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ga_ls_wo_fq_nov_mar_3",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "time_resolution": "month",
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "flags": [
                {
                    "band": "land",
                    "product": "geodata_coast_100k",
                    "ignore_time": True,
                    "ignore_info_flags": [],
                },
            ],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "seasonal_water_observations",
                "styles": [
                    style_wofs_seasonal_wet_c3,
                ],
            },
        },
        {
            "title": "DEA November-March Clear Observation Statistics (Landsat, C3)",
            "name": "wofs_nov_mar_summary_clear_c3",
            "abstract": """Water Observations from Space Statistics 30m 3.1.6 (Landsat, November - March, Clear)
The DEA Water Observations Statistic, November - March is a set of seasonal statistical summaries of the DEA Water Observations product that combines the many years of observations into summary products that help the understanding of surface water across Australia. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains clear observation count: how many times an area could be clearly seen (i.e. not affected by clouds, shadows or other satellite observation problems)

No clear observations causes an area to appear transparent,
1-15 total clear observations correlates with red and yellow colours,
18-22 clear observations correlates with light green,
23+ clear observations correlates with inreasingly dark shades of green.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ga_ls_wo_fq_nov_mar_3",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "time_resolution": "month",
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "flags": [
                {
                    "band": "land",
                    "product": "geodata_coast_100k",
                    "ignore_time": True,
                    "ignore_info_flags": [],
                },
            ],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "seasonal_clear_observations",
                "styles": [
                    style_wofs_seasonal_clear_c3,
                ],
            },
        },
    ],
}

c3_statistics_layer = {
    "title": "DEA November-March Seasonal Water Observations (Landsat, C3)",
    "name": "wofs_nov_mar_summary_statistics_c3",
    "abstract": """DEA Water Observations Statistics 30m 3.1.6 (Landsat, November - March, Frequency)
The DEA Water Observations November - March Statistic is a set of seasonal statistical summaries of the DEA Water Observations product that combines the many years of observations into summary products that help the understanding of surface water across Australia. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage).

No clear observations of water causes an area to appear transparent,
red through to yellow represent areas seen to be wet up to 30% of the time,
green through to light blue represent areas seen to be wet 40-60% of the time,
deep blue and purple correspond to an area being wet through 80%-100% of clear observations.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_wo_fq_nov_mar_3",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "time_resolution": "month",
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "flags": [
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": [],
        }
    ],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "seasonal_WOfS_frequency",
        "styles": [
            style_seasonal_wofs_summary_frequency_c3,
            style_seasonal_wofs_summary_frequency_blue_c3,
        ],
    },
}

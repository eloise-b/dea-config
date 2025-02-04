from ows_refactored.ows_reslim_cfg import reslim_standard

bands_nidem = {"nidem": []}

style_nidem_macro = {
    "name": "nidem_macro",
    "title": "Intertidal elevation (macrotidal)",
    "abstract": "Intertidal elevation visualised for macrotidal coastal environments",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "nidem",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["nidem"],
    "mpl_ramp": "viridis",
    "range": [-4.0, 2.0],
    "legend": {
        "begin": "-4.0",
        "end": "2.0",
        "ticks": ["-4.0", "0.0", "2.0"],
        "units": "metres",
        "tick_labels": {
            "2.0": {"prefix": ">"},
            "-4.0": {"prefix": "<"},
        },
    },
}


style_nidem_micro = {
    "name": "nidem_micro",
    "title": "Elevation (microtidal)",
    "abstract": "Intertidal elevation visualised for microtidal coastal environments",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "nidem",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["nidem"],
    "mpl_ramp": "viridis",
    "range": [-1.0, 0.5],
    "legend": {
        "begin": "-1.0",
        "end": "0.5",
        "ticks": ["-1.0", "0.0", "0.5"],
        "units": "metres",
        "tick_labels": {
            "0.5": {"prefix": ">"},
            "-1.0": {"prefix": "<"},
        },
    },
}


layer = {
    "title": "DEA Intertidal Elevation (Landsat)",
    "name": "NIDEM",
    "abstract": """National Intertidal Digital Elevation Model 25m 1.0.0

The National Intertidal Digital Elevation Model (NIDEM; Bishop-Taylor et al. 2019) is a continental-scale elevation dataset for Australia's exposed intertidal zone. NIDEM provides the first three-dimensional representation of Australia's intertidal sandy beaches and shores, tidal flats and rocky shores and reefs at 25 m spatial resolution, addressing a key gap between the availability of sub-tidal bathymetry and terrestrial elevation data. NIDEM was generated by combining global tidal modelling with a 30-year time series archive of spatially and spectrally calibrated Landsat satellite data managed within the Digital Earth Australia (DEA) platform. NIDEM complements existing intertidal extent products, and provides data to support a new suite of use cases that require a more detailed understanding of the three-dimensional topography of the intertidal zone, such as hydrodynamic modelling, coastal risk management and ecological habitat mapping.
*Overview*
Intertidal environments support important ecological habitats (e.g. sandy beaches and shores, tidal flats and rocky shores and reefs), and provide many valuable benefits such as storm surge protection, carbon storage and natural resources for recreational and commercial use. However, intertidal zones are faced with increasing threats from coastal erosion, land reclamation (e.g. port construction), and sea level rise. Accurate elevation data describing the height and shape of the coastline is needed to help predict when and where these threats will have the greatest impact. However, this data is expensive and challenging to map across the entire intertidal zone of a continent the size of Australia.
The rise and fall of the ocean can be used to describe the three-dimensional shape of the coastline by mapping the land-sea boundary (or 'waterline') across a range of known tides (e.g. low tide, high tide). Assuming that these waterlines represent lines of constant height relative to mean sea level (MSL), elevations can be modelled for the area of coastline located between the lowest and highest observed tide. To model the elevation of Australia's entire intertidal zone, 30 years of satellite images of the coastline (between 1986 and 2016 inclusive) were obtained from the archive of spatially and spectrally calibrated Landsat observations managed within the Digital Earth Australia (DEA) platform. Using the improved tidal modelling framework of the Intertidal Extents Model v2.0 (ITEM 2.0; Sagar et al. 2017, 2018), each satellite observation in the 30 year time series could be accurately associated with a modelled tide height using the global TPX08 ocean tidal model. These satellite observations were converted into a water index (NDWI), composited into discrete ten percent intervals of the observed tide range (e.g. the lowest 10% of observed tides etc), and used to extract waterlines using a spatially consistent and automated waterline extraction procedure. Triangulated irregular network (TIN) interpolation was then used to derive elevations relative to modelled mean sea level for each 25 x 25 m Landsat pixel across approximately 15,387 sq. km of intertidal terrain along Australia's entire coastline.
NIDEM differs from previous methods used to model the elevation of the intertidal zone which have predominately focused on extracting waterlines from a limited selection of satellite images using manual digitisation and visual interpretation (e.g. Chen and Rau 1998; Zhao et al. 2008; Liu et al. 2013; Chen et al. 2016). This manual process introduces subjectivity, is impractical to apply at a continental-scale, and has inherent restrictions based on the availability of high quality image data at appropriate tidal stages. By developing an automated approach to generating satellite-derived elevation data based on a 30 year time series of observations managed within the Digital Earth Australia (DEA) platform, it was possible to produce the first continental-scale three-dimensional model of the intertidal zone.
*Accuracy*
To assess the accuracy of NIDEM, we compared modelled elevations against three independent elevation and bathymetry validation datasets: the DEM of Australia derived from LiDAR 5 Metre Grid (Geoscience Australia, 2015), elevation data collected from Real Time Kinematic (RTK) GPS surveys (Danaher & Collett, 2006; HydroSurvey Australia, 2009), and 1.0 m resolution multibeam bathymetry surveys (Solihuddin et al., 2016). We assessed overall accuracy across three distinct intertidal environments: sandy beaches and shores, tidal flats, and rocky shores and reefs:
- Sandy beaches and shores, 5 sites: Pearson's correlation = 0.92, Spearman's correlation = 0.93, RMSE +/- 0.41 m
- Tidal flats, 9 sites: Pearson's correlation = 0.78, Spearman's correlation = 0.81, RMSE +/- 0.39 m
- Rocky shores and reefs, 7 sites: Pearson's correlation = 0.46, Spearman's correlation = 0.79, RMSE +/- 2.98 m
*Limitations*
NIDEM covers the exposed intertidal zone which includes sandy beaches and shores, tidal flats and rocky shores and reefs. The model excludes intertidal vegetation communities such as mangroves.
Areas with comparatively steep coastlines and small tidal ranges are poorly captured in the 25 m spatial resolution input Landsat data and resulting NIDEM model. This includes much of the south eastern and southern Australian coast (e.g. New South Wales, Victoria, Tasmania).
Poor validation results for rocky shore and reef sites within the southern Kimberly region highlighted limitations in the NIDEM model that occur when the global OTPS TPX08 Atlas Tidal Model was unable to predict complex and asynchronous local tidal patterns. This is likely to also reduce model accuracy in complex estuaries and coastal wetlands where river flow or vegetative resistance causes hydrodynamic attenuation in tidal flow.
The complex temporal behaviour of tides mean that a sun synchronous sensor like Landsat does not observe the full range of the tidal cycle at all locations. This causes spatial bias in the proportion of the tidal range observed in different regions, which can prevent NIDEM from providing elevation data for areas of the intertidal zone exposed or inundated at the extremes of the tidal range. Accordingly, NIDEM provides elevation data for the portion of the tidal range observed by Landsat, rather than the full tidal range.
While image compositing and masking methods have been applied to remove the majority of noise and non-tidal artefacts from NIDEM, issues remain in several locations. It is recommended that the data be used with caution in the following areas:
- The Recherche Archipelago in southern Western Australia
- Port Phillip Bay in Victoria
- The eastern coast of Tasmania and King Island
- Saunders Reef and surrounds in the northern Coral Sea
*Data access and additional information*
- Journal article: Bishop-Taylor et al. 2019 (https://doi.org/10.1016/j.ecss.2019.03.006)
- Data available on THREDDS: http://dapds00.nci.org.au/thredds/catalogs/fk4/nidem_1_0.html
- eCat catalogue listing including data access: http://pid.geoscience.gov.au/dataset/ga/123678
- CMI listing for extended metadata: https://cmi.ga.gov.au/pd/NIDEM_25_1.0.0

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "nidem",
    "bands": bands_nidem,
    "time_resolution": "year",
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
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
        "default_style": "nidem_macro",
        "styles": [
            style_nidem_macro,
            style_nidem_micro,
        ],
    },
}

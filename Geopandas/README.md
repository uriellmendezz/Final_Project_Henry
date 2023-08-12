# GEOPANDAS (version 0.13.2)

https://www.youtube.com/watch?v=DfPAEdD7Cjg&list=PL_YyCdnLDJAinPCjURIS-Yr5FLpr2AyAO

[https://github.com/IngJuanMaSuarez/GeoPandas-para-Dummies/tree/main]

- GeoPandas is an open source project to make working with geospatial data in python easier
- GeoPandas extends the datatypes used by pandas to allow spatial operations on geometric types.
- Geometric operations are performed by shapely.
> Shapely is a BSD-licensed Python package for manipulation and analysis of planar geometric objects.
---
> (Berkeley Software Distribution) license: BSD-licensed Python packages are popular in the Python ecosystem because they strike a balance between permissiveness and providing some level of protection for the original developers' rights and attribution.
---
- Geopandas further depends on fiona for file access and matplotlib for plotting.
> Fiona: is a popular Python library used for reading and writing geographic vector data files. It provides a simple and efficient way to work with various geospatial file formats, such as Shapefiles (SHP), GeoJSON, and others. Fiona is commonly used in geospatial data processing, analysis, and visualization tasks.
---

### EPSG 2263

**Name**: NAD83 / New York Long Island (ftUS)  
**Type**: Projected Coordinate Reference System (PCS)  
**Units**: US survey feet  
**Area of Use**: Primarily covers the New York State, Long Island, and surrounding areas in the United States.  
**Projection**: This CRS uses the Lambert Conformal Conic projection, which is a commonly used projection for accurately representing regions with an east-west extent like the eastern United States.  
**Use Case**: This CRS is suitable for mapping and analysis in the New York State and Long Island region, particularly for local surveying and engineering projects.  


### EPSG 4326:

**Name**: WGS 84   
**Type**: Geographic Coordinate Reference System (GCS)  
**Units**: Decimal degrees  
**Area of Use**: Global coverage, as WGS 84 is the standard for GPS and satellite positioning systems.  
**Projection**: This CRS is not projected; it represents data on a spherical model of the Earth.  
**Use Case**: WGS 84 is commonly used for global positioning, mapping, and visualization. It's the standard coordinate system for most global mapping applications and GPS devices.  



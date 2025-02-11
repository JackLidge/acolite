## def polygon_from_wkt
## creates temporary json file if wkt polygon is given
## written by Quinten Vanhellemont, RBINS
## 2023-02-06

def polygon_from_wkt(wkt, file=None):
    import os
    from osgeo import ogr
    import acolite as ac

    if file == None: file = ac.config['scratch_dir'] + '/polygon.json'
    odir = os.path.dirname(file)
    if not os.path.exists(odir): os.makedirs(odir)

    geom = ogr.CreateGeometryFromWkt(wkt)
    with open(file, 'w') as f: f.write(geom.ExportToJson())
    geom = None

    return(file)

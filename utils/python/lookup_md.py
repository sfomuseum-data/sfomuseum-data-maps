#!/usr/bin/env python

import os
import sys

import mapzen.whosonfirst.utils
import mapzen.whosonfirst.uri

if __name__ == "__main__":

    maps = "/usr/local/data/sfomuseum-data-maps"
    data = os.path.join(maps, "data")
    
    crawl = mapzen.whosonfirst.utils.crawl(data, inflate=True)
    lookup = {}
    
    for feature in crawl:

        props = feature["properties"]
        uri = props["sfomuseum:uri"]
        lookup[uri] = feature["properties"]

    keys = lookup.keys()
    keys.sort()

    fh = sys.stdout
    
    fh.write("| URI | WOF ID | Inception | Cessation | Min Zoom | Max Zoom |")
    fh.write("\n")
    fh.write("| --- | --- | --- | --- | --- | --- |")
    fh.write("\n")
    
    for uri in keys:

        props = lookup[uri]

        rel_path = mapzen.whosonfirst.uri.id2relpath(props["wof:id"])
        gh_url = os.path.join("data", rel_path)
        
        fh.write("| %s | [%s](%s) | %s | %s | %s | %s |" % (uri, props["wof:id"], gh_url, props["edtf:inception"], props["edtf:cessation"], props["mz:min_zoom"], props["mz:max_zoom"]))
        fh.write("\n")        

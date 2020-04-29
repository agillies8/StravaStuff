def insertMarkers(foltracks, iframes, popups, fgroup):
    import os

    page_path = "templates/MapAllActivities.html"

#      var animatedMarker = L.animatedMarker(poly_line_3e0a059bbf4a4b07b480b263a3877625.getLatLngs()).addTo(feature_group_9b0c39f7367f4b83908f3ac3fc6882f2);
#      animatedMarker.bindPopup(popup_3af07e368d9c4ea99354ee7c12438671);

#</script>

    with open(page_path, 'r+') as f:
        f.seek(0, os.SEEK_END)              # seek to end of file; f.seek(0, 2) is legal
        f.seek(f.tell() - 9, os.SEEK_SET)   # go backwards 9 bytes
        f.truncate() # delete that part
        for i in range(0,len(foltracks)):
            f.write("   var animatedMarker = L.animatedMarker(" + foltracks[i] + ".getLatLngs()).addTo(" + fgroup + ");" + "\n")
            f.write("   animatedMarker.bindPopup(" + popups[i] + ");\n")
            f.write("\n")
        f.write("</script>")

    f = open(page_path, "r")
    contents = f.readlines()
    f.close()

    contents.insert(14, "    <script src=\"AnimatedMarker.js\"></script>\n")

    f = open(page_path, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

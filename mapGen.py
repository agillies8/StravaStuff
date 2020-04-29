def createMap():

    import folium
    import pandas
    from StravaApi import getDataset
    import polyline
    from markerGen import insertMarkers

    #for onclick iframe with certain info:
    html = """Title: %s <br>
    Date: %s <br>
    Distance: %s miles<br>
    Gain: %s ft<br>
    """

    map = folium.Map(location=[37.5, -122], zoom_start=10, tiles="CartoDB Dark_Matter") #create map object - can change map style here, along wih starting coordinates
    #folium.TileLayer('cartodbdark_matter').add_to(my_map) #if you want to add more layers

    data = getDataset()
    foltracks=[]
    iframes=[]
    popups = []
    fgp = folium.FeatureGroup(name="Tracks") #all tracks are added to this feature group

    #loop to parse all the activities and get polyline for it
    for i in range(0,len(data)):
        name = data[i]["name"]
        date = data[i]["start_date"]
        distance = data[i]["distance"]
        gain = data[i]["total_elevation_gain"]
        track = polyline.decode(data[i]["map"]["summary_polyline"]) #need the google polyline decoder module for this
        iframe = folium.IFrame(html=html % ( #annoying parsing stuff for my iframe
        str(name),
        str(date.split(sep='T', maxsplit=1)[0]),
        str(distance*0.000621371).split(sep='.', maxsplit=1)[0],
        str(gain*3.28).split(sep='.', maxsplit=1)[0]),
        width=200, height=100)
        fpopup = folium.Popup(iframe)
        foltrack = folium.PolyLine(track, color="red", weight=2.5, opacity=1, popup=fpopup)
        fgp.add_child(foltrack) #add track to feature group

        foltracks.append(foltrack.get_name()) #add folium ID to list for marker later
        iframes.append(iframe.get_name())
        popups.append(fpopup.get_name())


    map.add_child(fgp)
    map.add_child(folium.LayerControl())
    map.save("templates/MapAllActivities.html")

    insertMarkers(foltracks, iframes, popups, fgp.get_name())

createMap()
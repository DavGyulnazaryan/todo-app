def shablony(chapsery_aper):
    tarber_masery = chapsery_aper.split(" ")
    voty = float(tarber_masery[0])
    lenky = float(tarber_masery[1])

    metrery = voty * 0.3048 + lenky * 0.0254
    return metrery

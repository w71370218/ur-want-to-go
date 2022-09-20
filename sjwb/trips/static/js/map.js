
window.onload = (event) => {
    console.log('page is fully loaded');
    let height = document.getElementsByClassName("navbar")[0].clientHeight
    let ele = document.getElementsByClassName("map")
    ele[0].children[0].children[0].style = ""
    iframe = ele[0].children[0].children[0].children[1].contentWindow.document
    if (innerWidth < 1080) {
        ele[0].style = "margin-top:" + height + "px"
        let layerfontsize = iframe.getElementsByClassName("leaflet-control-layers-overlays")[0]
        layerfontsize.style = "font-size: 350%;"
    }

    //var layerControl = document.getElementsByClassName("leaflet-right")
    //layerControl[0].style = "margin-top: 180px ;"
}
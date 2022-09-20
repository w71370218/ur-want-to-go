
window.onload = (event) => {
    console.log('page is fully loaded');
    let height = document.getElementsByClassName("navbar")[0].clientHeight
    let ele = document.getElementsByClassName("map")
    ele[0].children[0].children[0].style = ""
    if (innerWidth < 1080) {
        ele[0].style = "margin-top:" + height + "px"
    }

    //var layerControl = document.getElementsByClassName("leaflet-right")
    //layerControl[0].style = "margin-top: 180px ;"
}
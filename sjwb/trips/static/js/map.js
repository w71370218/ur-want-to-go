
window.onload = (event) => {
    console.log('page is fully loaded');
    let height = document.getElementsByClassName("navbar")[0].clientHeight
    let ele = document.getElementsByClassName("map")
    ele[0].children[0].children[0].style = ""
    let iframe = ele[0].children[0].children[0].children[1].contentWindow.document
    if (innerWidth < 1080) {
        ele[0].style = "margin-top:" + height + "px"
        let layerfontsize = iframe.getElementsByClassName("leaflet-control-layers-overlays")[0]
        layerfontsize.style = "font-size: 350%;"
    }

    //area link
    svg_element = iframe.getElementsByTagName("svg")[0]
    const XLink_NS = 'http://www.w3.org/1999/xlink';
    const SVG_NS = 'http://www.w3.org/2000/svg';
    svg_element.setAttributeNS(XLink_NS, 'xlink:href', "")

    node_element = iframe.getElementsByTagName("g")[0]
    for (var i = 1; i <= 22; i++) {
        let new_ele = iframe.createElementNS(SVG_NS, "a");
        //new_ele.setAttribute('href', "/area?=" + i);
        new_ele.setAttributeNS(null, 'target', "_parent");
        new_ele.setAttributeNS(XLink_NS, 'xlink:href', "/area?=" + i);
        node_element.appendChild(new_ele);
        const node = node_element.getElementsByTagName("path")[0];
        new_ele.appendChild(node);
    }

    //var layerControl = document.getElementsByClassName("leaflet-right")
    //layerControl[0].style = "margin-top: 180px ;"
}
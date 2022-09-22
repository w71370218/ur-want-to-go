function query() {
    $('#query-filter').submit()
}

$(document).ready(function () {
    let stars = document.getElementById("id_stars");
    stars.setAttribute("onchange", "query()");
    let order = document.getElementById("id_order");
    order.setAttribute("onchange", "query()");
    let text = document.getElementById("id_text");
    text.setAttribute("type", "search");
    text.setAttribute("placeholder", "請輸入關鍵字");
    let area = document.getElementById("id_area");
    area.setAttribute("onchange", "query()");
    let area_i = document.getElementsByClassName("area")[0];
    if (area_i) {
        area.setAttribute("style", "display:none");
        let area_label = document.getElementsByTagName("label")[0]
        area_label.setAttribute("style", "display:none");
    }
})

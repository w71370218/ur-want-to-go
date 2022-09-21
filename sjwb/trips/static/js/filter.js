function query() {
    $('#query-filter').submit()
}

$(document).ready(function () {
    let area = document.getElementById("id_area");
    area.setAttribute("onchange", "query()");
    let stars = document.getElementById("id_stars");
    stars.setAttribute("onchange", "query()");
    let order = document.getElementById("id_order");
    order.setAttribute("onchange", "query()");
})

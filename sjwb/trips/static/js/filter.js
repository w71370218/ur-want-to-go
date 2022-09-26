function query() {
    $('#query-filter').submit()
}

$(document).ready(function () {
    //nearby 
    attractions = document.getElementsByClassName("category-1")
    $("#attraction").click(function () {
        if ($(this).prop("checked")) {
            for (let index = 0; index < attractions.length; index++) {
                attractions[index].style = "display:block;";
            }
        } else {
            for (let index = 0; index < attractions.length; index++) {
                attractions[index].style = "display:none;";
            }
        }
    });
    accomodations = document.getElementsByClassName("category-2")
    $("#accomodation").click(function () {
        if ($(this).prop("checked")) {
            for (let index = 0; index < accomodations.length; index++) {
                accomodations[index].style = "display:block;";
            }
        } else {
            for (let index = 0; index < accomodations.length; index++) {
                accomodations[index].style = "display:none;";
            }
        }
    });
    restaurants = document.getElementsByClassName("category-3")
    $("#restaurant").click(function () {
        if ($(this).prop("checked")) {
            for (let index = 0; index < restaurants.length; index++) {
                restaurants[index].style = "display:block;";
            }
        } else {
            for (let index = 0; index < restaurants.length; index++) {
                restaurants[index].style = "display:none;";
            }
        }
    });


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

$('#first_cat').on('change',function(){

    $.ajax({
        url: "/bar",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('first_cat').value
        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph', data );
        }
    });
})

$('#first_cat9').on('change',function(){

    $.ajax({
        url: "/timeseries",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('first_cat9').value
        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph9', data );
        }
    });
})



$('#first_cat1').on('change',function(){

    $.ajax({
        url: "/bar",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('first_cat1').value

        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph1', data );
        }
    });
})

$('#first_cat2').on('change',function(){

    $.ajax({
        url: "/boxplot",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('first_cat2').value
        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph2', data );
        }
    });
})


$('#first_cat3').on('change',function(){

    $.ajax({
        url: "/pie",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('first_cat3').value

        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph3', data );
        }
    });
})

$('#first_cat4').on('change',function(){

    $.ajax({
        url: "/barlineas",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('first_cat4').value

        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph4', data );
        }
    });
})

$('#first_cat5').on('change',function(){

    $.ajax({
        url: "/bar",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('first_cat5').value

        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph5', data );
        }
    });
})

$('#first_cat7').on('change',function(){

    $.ajax({
        url: "/bar",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('first_cat7').value

        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph7', data );
        }
    });
})



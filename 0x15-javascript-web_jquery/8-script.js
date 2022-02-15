$(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json',function (data, status) {
        if (status === 'success'){
            let movie = data.results;
            for (let item in movie){
                $('UL#list_movies').append('<li>'+ movie[item].item + '</li>');
            }
        }
    });
});

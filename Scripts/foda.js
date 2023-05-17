function GetURLParameter(sParam)
{
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++) 
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam) 
        {
            return sParameterName[1];
        }
    }
}

pokemonid = GetURLParameter('pokemon')
requestURL = 'https://pokeapi.co/api/v2/pokemon/' + pokemonid

$.ajax({
    url: requestURL,
    dataType: 'json',
    success: async function(response) {
        // Update the HTML page with the JSON data
        document.getElementById('nome_pokemon').innerHTML = response.forms[0].name
        document.getElementById('image_pokemon').src = response.sprites.other['official-artwork'].front_default
        let i =0;
        for (let tipo of response.types) {
            tipo_pokemon = document.createElement('h2')
            tipo_pokemon.innerHTML = tipo.type.name
            tipo_pokemon.classList.add(tipo.type.name)
            tipo_pokemon.classList.add('padrao_tipo')
            document.getElementById('descricao').appendChild(tipo_pokemon)
            i++;
        }
    },
    error: function(error) {
        console.log(error);
    }
});
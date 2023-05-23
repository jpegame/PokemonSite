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

const pokemon_normal    = document.getElementById('pokemon_normal');
const pokemon_shiny     = document.getElementById('pokemon_shiny');
const gif_normal        = document.getElementById('gif_normal');
const gif_shiny         = document.getElementById('gif_shiny');

pokemonid = GetURLParameter('pokemon')
requestURL = 'https://pokeapi.co/api/v2/pokemon/' + pokemonid

$.ajax({
    url: requestURL,
    dataType: 'json',
    success: async function(response) {
        // Update the HTML page with the JSON data
        document.getElementById('nome_pokemon').innerHTML   = response.forms[0].name
        pokemon_normal.src  = response.sprites.other['official-artwork'].front_default
        pokemon_shiny.src   = response.sprites.other['official-artwork'].front_shiny
        gif_normal.src      = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/' + pokemonid + '.gif'
        gif_shiny.src       = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/shiny/' + pokemonid + '.gif'
        let i =0;
        for (let tipo of response.types) {
            tipo_pokemon = document.createElement('h2')
            tipo_pokemon.innerHTML = tipo.type.name
            tipo_pokemon.classList.add(tipo.type.name)
            tipo_pokemon.classList.add('padrao_tipo')
            document.getElementById('descricao').insertBefore(tipo_pokemon,document.getElementById('descricao').firstChild)
            i++;
        }
    },
    error: function(error) {
        console.log(error);
    }
});

function CheckboxPoke() {

    let shinybox = document.getElementById('Shiny').checked
    let gifbox = document.getElementById('Gif').checked
    ResetPoke()

    switch (true) {
        case (shinybox  && !gifbox):
            pokemon_shiny.style = 'display: block;'
            break;
        case (shinybox && gifbox):
            gif_shiny.style = 'display: block;'
            break;
        case (!shinybox && gifbox):
            gif_normal.style = 'display: block;'
            break;
        case (!shinybox && !gifbox):
            pokemon_normal.style = 'display: block;'
            break;
    }
}

function ResetPoke () {
    pokemon_normal.style    = 'display: none;'
    pokemon_shiny.style     = 'display: none;'
    gif_normal.style        = 'display: none;'
    gif_shiny.style         = 'display: none;'
}
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
const pokemon           = document.querySelector(".pokemon");

pokemonid = GetURLParameter('pokemon')
if (pokemonid < 400000){
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
    $.ajax({
        url: '/pokemon_special_data',
        dataType: 'json',
        success: function(response) {
            let FoundLendario   = response['pokemons'].some(obj => JSON.stringify(obj) === JSON.stringify(JSON.parse('{"Classificacao": "L","id":' + pokemonid + '}')));
            let FoundMitico     = response['pokemons'].some(obj => JSON.stringify(obj) === JSON.stringify(JSON.parse('{"Classificacao": "M","id":' + pokemonid + '}')));
    
            if (FoundLendario){
                pokemon.style.background = 'linear-gradient(180deg, #cc00ff, rgb(106, 180, 245))'
            }
            if (FoundMitico){
                pokemon.style.background = 'linear-gradient(180deg, #ff0055, #cc00ff)'
            }
        },
        error: function(error) {
            console.log(error);
        }
    });

} else {
    $.ajax({
        url: '/pokemon_data/' + (Number(pokemonid) - 400000).toString(),
        dataType: 'json',
        success: function(response) {
            // Update the HTML page with the JSON data
            LoadPokemons(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function LoadPokemons(pokemon){
    document.getElementById('imagens_checkbox').style = 'visibility:hidden;'
    document.getElementById('nome_pokemon').innerHTML = pokemon.pokemon_item.name
    pokemon_normal.src = pokemon.pokemon_item.imagem
    let i =0;
    for (let tipo of pokemon.pokemon_item.tipos) {
        tipo_pokemon = document.createElement('h2')
        tipo_pokemon.innerHTML = tipo.toLowerCase()
        tipo_pokemon.classList.add(tipo.toLowerCase())
        tipo_pokemon.classList.add('padrao_tipo')
        document.getElementById('descricao').insertBefore(tipo_pokemon,document.getElementById('descricao').firstChild)
        i++;
    }
}

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
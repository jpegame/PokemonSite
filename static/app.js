const baseURL = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/';
var requestURL = 'https://pokeapi.co/api/v2/pokemon-form/';
const PopUpBox = document.querySelector('[data-modal]')
const popupContent = document.getElementById('tipoid');
CarregarPokemons(0,151);

function RecarregarPagina(i,i2){
    const boxes = document.querySelectorAll('.pokemon');
    boxes.forEach(box => {
        box.remove();
    });
    CarregarPokemons(i,i2);
}

function CarregarPokemons(i,i2){
    if (i == null || i2 == null){
        $.ajax({
            url: '/pokemon_data',
            dataType: 'json',
            success: function(response) {
                // Update the HTML page with the JSON data
                LoadPokemons(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }else{
        $.ajax({
            url: '/pokemon_special_data',
            dataType: 'json',
            success: function(response) {
                // Update the HTML page with the JSON data
                LoadPokemonsAPI(response,i,i2);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
}

function Foda(){
    var pesquisa = document.getElementById('mtofoda').value
    var children = document.getElementById("gridmtofoda").children; //get container element children.
    for (var i = 0, len = children.length ; i < len; i++) {
        if (children[i].className == 'pokemon'){
            if (children[i].children[1].innerHTML.search(pesquisa) == -1){
                children[i].style = "display: none;"
            }
            else {
                children[i].style = "display: block;"
            }
        }
    }
}

function AbrirFoda(nomepokemon) {
    let parametro = nomepokemon
    window.location.href = "/pokemon?pokemon=" + parametro
}

function LoadPokemons(pokemonlista) {
    for (pokemon of pokemonlista.pokemons) {
        const pokemondiv = document.createElement('div');
        pokemondiv.classList.add('pokemon'); 

        const rotulo = document.createElement('span');
        const novaImg = document.createElement('img');
        novaImg.id = pokemon.id
        novaImg.src = pokemon.Imagem
        novaImg.addEventListener("click", function (event) {
            let parametro = 400000 + Number(event.target.id)
            window.location.href = "/pokemon?pokemon=" + parametro
        })

        rotulo.innerText = pokemon.name
        pokemondiv.appendChild(novaImg);
        pokemondiv.appendChild(rotulo);
        document.getElementById('gridmtofoda').appendChild(pokemondiv)
    }
}

function LoadPokemonsAPI(pokemon_special,i,i2) {
    while (i < i2) {
        //Criando a div pokemon
        const pokemon = document.createElement('div');
        pokemon.classList.add('pokemon');
        let FoundLendario   = pokemon_special['pokemons'].some(obj => JSON.stringify(obj) === JSON.stringify(JSON.parse('{"Classificacao": "L","id":' + (i + 1) + '}')));
        let FoundMitico     = pokemon_special['pokemons'].some(obj => JSON.stringify(obj) === JSON.stringify(JSON.parse('{"Classificacao": "M","id":' + (i + 1) + '}')));

        if (FoundLendario){
            pokemon.style.background = 'linear-gradient(180deg, #cc00ff, rgb(106, 180, 245))'
        }
        if (FoundMitico){
            pokemon.style.background = 'linear-gradient(180deg, #ff0055, #cc00ff)'
        }

        //Criando um elemento <span>
        const rotulo = document.createElement('span');

        //Criando um elemento <img>
        const novaImg = document.createElement('img');
        novaImg.id = i + 1;
        novaImg.src = baseURL+(i+1)+".gif"; //Atribuindo o endereço e o nome do arquivo de imagem no atributo src do <img> criado.
        novaImg.addEventListener("click", function (event) {
            AbrirFoda(event.target.id);
        })

        document.body.appendChild(pokemon);
        $.ajax({
            url: requestURL + (i + 1),
            dataType: 'json',
            success: async function(response) {
                // Update the HTML page with the JSON data
                rotulo.innerText = response.pokemon.name
            },
            error: function(error) {
                console.log(error);
            }
        });

        //Adicionando a imagem e o rótulo ao <div> criado
        pokemon.appendChild(novaImg);
        pokemon.appendChild(rotulo);
        document.getElementById('gridmtofoda').appendChild(pokemon)
        i++;
    }
}
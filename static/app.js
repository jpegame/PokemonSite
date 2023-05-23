const baseURL = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/';
var requestURL = 'https://pokeapi.co/api/v2/pokemon-form/';
const PopUpBox = document.querySelector('[data-modal]')
const popupContent = document.getElementById('tipoid');

function CarregarPokemons(i,i2){
    while (i < i2) {

        //Criando um elemento <div>
        const pokemon = document.createElement('div');
        pokemon.classList.add('pokemon'); //Adicionando a class pokemon ao div. Ex.: <div class = 'pokemon'></div>                           //A classe pokemon está definida no arquivo app.css

        const rotulo = document.createElement('span');
        //Colocando o número do pokemon ao no texto do <span> criado.
        //Criando um elemento <span>

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

function Foda(){
    var pesquisa = document.getElementById('mtofoda').value
    var children = document.getElementById("gridmtofoda").children; //get container element children.
    for (var i = 0, len = children.length ; i < len; i++) {
        if (children[i].className == 'pokemon'){
            if (children[i].children[1].innerHTML.search(pesquisa) == -1){
                children[i].style = "visibility:hidden; position: absolute;"
            }
            else {
                children[i].style = "visibility:visible; position: relative;"
            }
        }
    }
}

CarregarPokemons(0,151);

function RecarregarPagina(i,i2){
    const boxes = document.querySelectorAll('.pokemon');
    boxes.forEach(box => {
        box.remove();
    });
    CarregarPokemons(i,i2);
}

function AbrirFoda(nomepokemon) {
    let parametro = nomepokemon
    window.location.href = "/pokemon?pokemon=" + parametro
}
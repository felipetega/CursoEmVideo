
function verificar(){
var escolhas=window.document.getElementsByName("radpet")
var img = document.createElement("img")

if (escolhas[0].checked){
    alert("Cachorro")
    img.src="img/dog.jpg"
}
else if (escolhas[1].checked){
    alert("Gato")
    img.src="img/cat.jpg" //NAO PEGA AS IMAGENS
}
}
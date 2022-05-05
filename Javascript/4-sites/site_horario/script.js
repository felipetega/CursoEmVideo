function frase(){
var img = window.document.getElementById("img")
var msg = window.document.getElementById("msg")
var hoje = new Date()
var hora = hoje.getHours()
var periodo =""
if (hora>=1 && hora<=11){
    periodo="da manhã"
    img.src="img/manha.jpg"
    document.body.style.background="burlywood"
}
else if (hora>=13 && hora <=17){
    periodo="da tarde"
    hora-=12
    img.src="img/tarde.jpg"
    document.body.style.background="teal"
}
else if (hora>=18 && hora<=23){
    periodo="da noite"
    hora-=12
    img.src="img/noite.jpg"
    document.body.style.background="darkslateblue"
}
else if (hora==12){
    periodo="meio-dia"
    img.src="img/manha.jpg"
}
else if (hora==0){
    periodo="meia-noite"
    img.src="img/noite.jpg"
}
if (hora!=12 && hora!=0 && hora!=1){
    msg.innerHTML=`Agora são ${hora}h ${periodo}!`
}
else if (hora==12 || hora==0){
    msg.innerHTML=`Agora é ${periodo}!`
}
else if (hora==1 || hora==0){
    msg.innerHTML=`Agora é ${hora}h ${periodo}!`
}
}
function frase(){
    msg=document.getElementById("msg")
    img=document.getElementById("img")
    var hoje = new Date()
    var hora = hoje.getHours()
    var periodo = ""
    if(hora>=0 && hora<=11){
        periodo="da manhã"
        img.src="img/manha.jpg"
        document.body.style.background="burlywood"
    }else if(hora>=13 && hora<=17){
        periodo="da tarde"
        img.src="img/tarde.jpg"
        document.body.style.background="teal"
    }else if(hora>=18 && hora<=23){
        periodo="da noite"
        img.src="img/noite.jpg"
        document.body.style.background="darkslateblue"
    }

}
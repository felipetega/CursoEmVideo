function tabuada(){
    let num = document.getElementById("txtn")
    let tab = document.getElementById("seltab")

    if(num.lenght == 0){
        alert("digite um número")
    }

    let n = Number(num.value)
    let c = 1

    tab.innerHTML=""
    while (c!=11){
        let item = document.createElement("option")
        item.text=`${n} x ${c} = ${n*c}`
        item.value=`tab${c}` //opcional, necessário pra outras linguagens
        tab.appendChild(item)
        c++
    }
}
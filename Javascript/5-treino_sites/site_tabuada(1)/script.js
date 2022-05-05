function gerar(){
    let num = document.getElementById("txtn")
    let tab = document.getElementById("seltab")

    let n = Number(num.value)
    let c = 1

    tab.innerHTML=""
    while(c!=11){
        let item = document.createElement("option")
        item.text=`${n} x ${c} = ${n*c}`
        c++
        tab.appendChild(item)
    }
}
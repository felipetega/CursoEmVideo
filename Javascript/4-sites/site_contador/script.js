function contar(){
    let ini=document.getElementById("ini")
    let fim=document.getElementById("fim")
    let raz=document.getElementById("raz")
    let res=document.getElementById("res")

    if (ini.value.length==0 || fim.value.length==0 || raz.value.length==0){
        res.innerHTML="Faltam dados..."
        //alert("[ERRO] Faltam dados")
    } else{
        res.innerHTML="Contando..."
        let i = Number(ini.value)
        let f = Number(fim.value)
        let r = Number(raz.value)
/*
        for(let c=i; c<=f; c+=r){
            res.innerHTML+=`${c}, `
        }*/
        if(i<f){ //contagem crescente
            while (i<=f){
                res.innerHTML+=`${i} \u{1F449}`
                i+=r
            }
        }
        else if(i>f){ //contagem decrescente
            while(i>=f){
                res.innerHTML+=`${i} \u{1F449}`
                i-=r
            }
        }
        res.innerHTML+=`\u{26F3}` 
    }
}
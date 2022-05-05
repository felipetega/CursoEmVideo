//var hora não recebe string? exemplo: hora="meio-dia"
hora = 13
periodo = ""
if (hora>=1 && hora<12){
    periodo="manhã"
    console.log("Bom dia")
}else if (hora>=12 && hora<18){
    periodo="tarde"
    console.log("Boa tarde")
    if (hora!=12){
        hora-=12
    }
}else if (hora>=18 && hora<=24){
    periodo="noite"
    console.log("Boa noite")
    hora-=12
}else{
    console.log("Esse horário não existe")
}
if (hora>=1 && hora<=24){
    console.log(`Agora são ${hora} da ${periodo}!`)
}
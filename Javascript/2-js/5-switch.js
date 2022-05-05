var hoje = new Date()
var diaSem = hoje.getDay()
var diaMes = hoje.getDate()
var mes = hoje.getMonth()
var ano = hoje.getFullYear()

switch(diaSem){
    case 0:
        console.log("Domingo")
        break
    case 1:
        console.log("Segunda-feira")
        break
    case 2:
        console.log("Terça-feira")
        break
    case 3:
        console.log("Quarta-feira")
        break
    case 4:
        console.log("Quinta-feira")
        break
    case 5:
        console.log("Sexta-feira")
        break
    case 6:
        console.log("Sábado")
        break
    default:
        console.log("Erro")
}
switch(mes){
    case 0:
        console.log("Janeiro")
        break
    case 1:
        console.log("Fevereiro")
        break
    case 2:
        console.log("Março")
        break
    case 3:
        console.log("Abril")
        break
    case 4:
        console.log("Maio")
        break
    case 5:
        console.log("Junho")
        break
    case 6:
        console.log("Julho")
        break
    case 2:
        console.log("Agosto")
        break
    case 3:
        console.log("Setembro")
        break
    case 4:
        console.log("Outubro")
        break
    case 5:
        console.log("Novembro")
        break
    case 6:
        console.log("Dezembro")
        break
    default:
        console.log("Erro")
}
console.log(`Hoje é dia ${diaMes}, do mês ${mes+1}, do ano de ${ano}`)

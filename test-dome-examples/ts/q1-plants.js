let plants = ["Oak", "Elm", "Beech"]
plants["Tree"] = "Ash";
plants["Tree"] = "Cherry"
plants["Flower"] = "Rose"

console.log(plants)

var garden = [];
for(let plant in plants){
    garden.push(plant)
}
console.log(garden)

for(let plant of plants){
    garden.push(plant)
}
console.log(garden)

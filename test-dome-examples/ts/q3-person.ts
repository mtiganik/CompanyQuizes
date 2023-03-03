class Person{
    hair: string;
    height: string;
    eyeColor: string;
}

let first = {hair:"brunette", height: "173cm"};
let second = {eyeColor:"blue", height:"192cm"};
let third = {hair:"blonde"};

let person: Person = {...first,...second, ...third};
console.log(person)
const array = [10, 11, 12, 13];

function reducer(accumulator, currentValue, index){
    const returns = accumulator + currentValue;
    return returns
}

console.log(array.reduce(reducer))

for(const s in array){
    console.log(array[s])
}
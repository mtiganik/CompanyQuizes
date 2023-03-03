
const data = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

function shift(item){
    item.unshift(item.pop())
    return item
}

const result = data.map(shift)
console.log(result)
// result.forEach(console.log)

const data = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

const resultArr = []
for(const s of data){
    console.log(s)
    const switched = s.unshift(s.pop())
    console.log(`s: ${s}, switched: ${switched}`)
    resultArr.push(switched)
}
resultArr.forEach(element => {
    console.log(element)
});

// const arr = [1,2,3,4,5]
// arr.push(arr.shift())
// arr.shift(arr.push())
// console.log(arr.unshift(arr.pop(),6))
// console.log(arr)

// const switched = data.map(n => n.push(n.shift()));
// switched.forEach(n => console.log(n))
// data.forEach(n => n.push(n.shift()))
// const doubled = data.map(n => n.map(a => a * 2))
// doubled.forEach(item => console.log(item))

function rotateLeft(d, arr) {
    for(let i= 0; i < d; i++){
        arr.push(arr.shift());
    }
    return arr
}
const arr = [1,2,3,4,5]
const d = 4
console.log(rotateLeft(d,arr))
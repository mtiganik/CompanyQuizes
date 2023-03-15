
function hourglassSum(arr) {
    let hourRow = []
    for(let i = 1; i < arr[0].length -1; i++){
        for(let j = 1;j < arr.length -1 ; j++){
            let sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]+arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            hourRow.push(sum)
        }
    }
    return Math.max.apply(null, hourRow);
}
var arr1 = [
[-9, -9, -9,  1, 1, 1 ],
[0, -9,  0,  4, 3, 2],
[-9, -9, -9,  1, 2, 3],
[0,  0,  8, 6, 6, 0],
[0,  0,  0, -2, 0, 0],
[0,  0,  1,  2, 4, 0]]
var arr2=[
[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]
]
console.log(hourglassSum(arr1))
console.log(hourglassSum(arr2))




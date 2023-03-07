function sockMerchant(n, ar) {
    // Write your code here

}


n = 9
ar = [10,20,20,10,10,30,50,10,20]


const countObj = {}
ar.forEach(function(i){countObj[i] = (countObj[i]||0) +1;})
const sum = Object.values(countObj).map((n) => Math.floor(n / 2));
const sum2 = Object.values(countObj).reduce((acc,n) => Math.floor(acc/2)+n,n)
console.log(sum2)
// const keys = Object.keys(countObj)
// console.log(keys)

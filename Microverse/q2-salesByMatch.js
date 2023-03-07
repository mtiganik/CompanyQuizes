function sockMerchant(n, ar) {
    const countObj = {}
    ar.forEach(function(i){countObj[i] = (countObj[i]||0) +1;})

    return Object.values(countObj)
    .map((i) => Math.floor(i/2))
    .reduce((partialSum,a) => partialSum + a, 0)
}


n = 9
ar = [10,20,20,10,10,30,50,10,20]
console.log(sockMerchant(n,ar))

n= 10
ar = [1,1,3,1,2,1,3,3,3,3]
console.log(sockMerchant(n,ar))

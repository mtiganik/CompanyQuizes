function dynamicArray(n, queries) {
    var lastAnswer = 0, lastAnswerList = []
    const arr = new Array(n).fill(0).map(() => new Array().fill(0));
    for(let i = 0; i<queries.length; i++){
        var query = queries[i]
        var idx = (query[1]^lastAnswer) % n

        if(query[0] == 1){
            arr[idx].push(query[2])
        }else {
            lastAnswer = arr[idx][query[2] % arr[idx].length]
            lastAnswerList.push(lastAnswer)
        }
    }
    return lastAnswerList
}
function splitIntegerStringToIntArray(stringOfIntegers){
    return stringOfIntegers.split(' ').map(function(item) {
        return parseInt(item, 10);
    });
}
var inp = 2
var queries = [
    [1, 0, 5],
    [1, 1, 7],
    [1, 0, 3],
    [2, 1, 0],
    [2, 1, 1]
]
console.log(dynamicArray(inp,queries))
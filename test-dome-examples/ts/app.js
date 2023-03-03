function filterNumbersFromArray(arr) {
    var result = [];
    for (var i = 0; i < arr.length; i++) {
        if (typeof arr[i] !== 'number') {
            arr.splice(i, i);
            i = i - 1;
        }
    }
}
var arr = [1, 'a', 'b', 2];
filterNumbersFromArray(arr);
console.log(arr);

function countingValleys(steps, path) {
    var level = 0, valleyCnt = 0

    for(var i=0; i < steps; i++){
        if(path[i] == 'U'){
            level++;
            if (level == 0) valleyCnt++ 
        }else level--
    }
    return valleyCnt
    
}

const steps = 8
const path = "UDDDUDUU"
console.log(countingValleys(steps,path))
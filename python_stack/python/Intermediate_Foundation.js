function sigma(num){

    var sum = 0;
    for (i=0; i <=num; i++){
        if (i > 0){
            sum += i;
        }
    }
    return sum;
}

//var test = sigma(100);
//console.log(test);

function factorial(num){
    var product = 1;
    for (i=1; i <=num; i++){
        if (i > 0){
            product *= i;
        }
    }
    return product;
}

//var test = factorial(5);
//console.log(test);

function fib(num){
    var fibN = [];
    
    fibN[0] = 0;
    fibN[1] = 1;
    
    for (i=2; i <= num; i++){
        if (num == 0 || num == 1){
            return num
        }
        fibN[i] = (fibN[i-2]) + (fibN[i-1]);
    }
    return fibN[num];
}

//var test = fib(2);
//console.log(test);


function secondToLast(arr){
    if (arr.length < 2){
        return null;
    }
    return arr[arr.length-2];
}

//var test = secondToLast([42, true, 4, "Liam", 7]);
//console.log(test);


function nthToLast(arr, num){
    if (arr.length < 2){
        return null;
    }
    return arr[arr.length-3];
}

//var test = nthToLast([5,2,3,6,4,9,7],3);
//console.log(test);


function secondLargest(arr){
    if (arr.length < 2){
        return null;
    }

    return arr[arr.length-3];
}

//var test = nthToLast([5,2,3,6,4,9,7],3);
//console.log(test);


function secondLargest(arr){
    arr.sort(function(a,b) {return a-b});
    //console.log(arr);
    return (arr[arr.length-2]);  
}

//var test = secondLargest([40,100,1,5,25,10,35,-10,55,60,65]);
//console.log(test);


function doubleTrouble(arr){
    newarr = []
    for (i=0; i<arr.length; i++) {
        newarr.push(arr[i]);
        newarr.push(arr[i]);
    }
    return newarr;  
}

//var test = doubleTrouble([4, "Ulysses", 42, false]);
//console.log(test);



function fib(n){
    
    if (n == 0 || n == 1){
        return n
    }
    return (fib(n-1) + fib(n-2));
}

var fibN = fib(45);
console.log(fibN);

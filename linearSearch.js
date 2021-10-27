//linear Search using Js
//find 67, and count to know number of steps ( Algorithm : O(n))

const FIND = 67;
let count  = 0;

let list = [1,3,4,6,78,53,78,2,67,34,100];

if(list.find(listItem => {count++; return listItem === FIND;})){
    console.log(`Found!!! and count is ${count}`);
}else{
    console.log("Not Found!!!");
}
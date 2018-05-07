const List = require('./linked-list');

let list = new List();

list.addToTail(1);
console.log(JSON.stringify(list, null, 2));
console.log('----------------');
list.addToTail(2);
console.log(JSON.stringify(list, null, 2));
console.log('----------------');
list.addToTail(3);
console.log(JSON.stringify(list, null, 2));
console.log('----------------');
list.addToTail(4);
console.log(JSON.stringify(list, null, 2));
console.log('----------------');
list.addToTail(5);
console.log(JSON.stringify(list, null, 2));
console.log('----------------');


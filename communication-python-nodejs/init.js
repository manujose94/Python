//init.js
var spawn = require('child_process').spawn,
    py    = spawn('python3', ['compute_input.py']),
    data = [3,4],
    dataString = '';

py.stdout.on('data', function(data){
  dataString += data.toString();
  console.log(data.toString())
});
py.stdout.on('end', function(){
  console.log('Sum of numbers=',dataString);
 
  //py.stdin.write(JSON.stringify(data));
});
py.stdin.write(JSON.stringify(data));
py.stdin.end();

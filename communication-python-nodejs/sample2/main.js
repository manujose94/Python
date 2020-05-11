var spawn = require('child_process').spawn;

var child = spawn('python', ['-u', 'child.py']);

child.stdout.on('data', function(data) {
  process.stdout.write(data);
});

child.stdout.on('close', function() {
  process.stdout.write('close');
});

child.kill();

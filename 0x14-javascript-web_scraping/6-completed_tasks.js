#!/usr/bin/node

const process = require('process');
const request = require('request');

let apiUrl = process.argv.slice(2, 3);

if (apiUrl.length) {
  apiUrl = apiUrl.toString();
} else {
  console.error('Usage: ./6-completed_tasks.js API_URL');
  process.exit(1);
}

request.get(apiUrl, { json: true }, (err, res, todosBody) => {
  try {
    if (err) throw err;

    const usrsCompletedTasks = {};
    let count = 0;
    todosBody.forEach(todo => {
      if (todo.userId === undefined && todo.completed) count = 1;
      else if (todo.completed) count++;

      usrsCompletedTasks[todo.userId] = count;
    });

    console.log(usrsCompletedTasks);
  } catch {
    console.error(err);
  }
});

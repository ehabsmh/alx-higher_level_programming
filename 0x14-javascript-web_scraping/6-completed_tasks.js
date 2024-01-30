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

request.get(apiUrl, { json: true }, (err, res, todos) => {
  try {
    if (err) throw err;

    const usrsCompletedTasks = {};

    todos.forEach((todo) => {
      if (todo.completed && usrsCompletedTasks[todo.userId] === undefined) {
        usrsCompletedTasks[todo.userId] = 1;
      } else if (todo.completed) {
        usrsCompletedTasks[todo.userId] += 1;
      }
    });

    console.log(usrsCompletedTasks);
  } catch {
    console.error(err);
  }
});

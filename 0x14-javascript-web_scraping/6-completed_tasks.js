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

request.get('https://jsonplaceholder.typicode.com/users',
  { json: true },
  (err, res, usrsBody) => {
    if (err) console.log(err);
    request.get(apiUrl, { json: true }, (err, res, todosBody) => {
      try {
        if (err) throw err;

        const usrsCompletedTasks = {};
        let count = 0;

        usrsBody.forEach(usr => {
          todosBody.forEach(todo =>
            todo.userId === usr.id && todo.completed ? count++ : count
          );

          usrsCompletedTasks[usr.id] = count;
          count = 0;
        });

        console.log(usrsCompletedTasks);
      } catch {
        console.error(err);
      }
    });
  });

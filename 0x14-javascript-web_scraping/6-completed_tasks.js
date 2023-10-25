#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.log('Please provide the API URL as an argument');
  process.exit(-1);
}

const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    for (const todo of todos) {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId] += 1;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    }

    if (completedTasks) {
      console.log(completedTasks);
    }
  } else {
    console.log(error); // Print the error if one occurred
  }
});

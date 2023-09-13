#!/usr/bin/node
exports.esrever = function (list) {
  const b = [];
  for (let i = list.length - 1; i >= 0; i--) {
    b.push(list[i]);
  }
  return b;
};

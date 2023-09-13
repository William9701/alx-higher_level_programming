#!/usr/bin/node
const file = require('file');
const fargs = readFileSync(process.argv[2]).toString();
const sargs = readFileSync(process.argv[3]).toString();
file.writeFileSync(process.argv[4], fargs + sargs);

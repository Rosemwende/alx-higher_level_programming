#!/usr/bin/node
/* a script that concats 2 files */
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA = fs.readFileSync(fileA, 'utf-8');
const contentB = fs.readFileSync(fileB, 'utf-8');

fs.writeFileSync(fileC, contentA + contentB);

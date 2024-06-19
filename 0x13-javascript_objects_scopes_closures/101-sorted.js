#!/usr/bin/node
/* a script that imports a dictionary of occurrences by
 * user id and computes a dictionary of user ids by occurrence
 */
const { dict } = require('./101-data');

const sortedDict = {};

Object.keys(dict).forEach((key) => {
  const value = dict[key];
  if (!sortedDict[value]) {
    sortedDict[value] = [];
  }
  sortedDict[value].push(key);
});

console.log(sortedDict);

#!/usr/bin/node
/* Write a function that executes x times a function */
function (x, theFunction)
const callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
      theFunction();
    }
};
module.exports = { callMeMoby };

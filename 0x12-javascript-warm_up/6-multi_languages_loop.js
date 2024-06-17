#!/usr/bin/node
/* Write a script that prints 3 lines: (like 1-multi_languages.js)
 * but by using an array of string and a loop
 */
const languages = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

for (const language of languages) {
  console.log(language);
}

function sortStrings(s, t) {
  let sortedString = '';

  let i = 0;
  while (i < t.length) {
    for (let j = 0; j < s.length; j++) {
      if (s[j] === t[i]) {
        sortedString += s[j]
      }
    }
    i++
  }

  return sortedString
}

const goodreadsInfo = {
  currentlyReading: [
    {
      title: "Vox Machina",
      author: "Matthew Mercer"
    }
  ],

  wantToRead: [
    {
      title: "The Mighty Nein",
      author: "Matthew Mercer"
    }
  ]
}

const addNewBook = (books, ...additionalBooks) => {
  return [...books, ...additionalBooks]
};

goodreadsInfo.currentlyReading = addNewBook(
  goodreadsInfo.currentlyReading,
  {title:"Vox Machina", author:"Matthew Mercer"},
);

goodreadsInfo.wantToRead = addNewBook(goodreadsInfo.wantToRead, {
  title: "The Mighty Nein",
  author: "Matthew Mercer"
});

const showGoodreadsInfo = (info) => {
    const currentlyReading = info.currentlyReading;
    const wantToRead = info.wantToRead;

    console.log("Currently Reading:");
    for (let book of currentlyReading) {
        console.log(`- ${book.title} by ${book.author}`);
    }

    console.log("Want to Read:");
    for (let book of wantToRead) {
        console.log(`- ${book.title} by ${book.author}`);
    }
};

showGoodreadsInfo(goodreadsInfo);
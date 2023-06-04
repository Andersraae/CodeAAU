const Genre = require("../models/genre");
const Book = require("../models/book");
const Author = require("../models/author");
const asyncHandler = require("express-async-handler");

// Search with a phrase.
exports.search = asyncHandler(async (req, res, next) => {
  
    // Get books, authors and genres that relate to search phrase
    console.log(req.query.search);
    const search = req.query.search;

    const [books, authors, genres] = await Promise.all([
        Book.find({ title: { $regex: search, $options: "i" } }).populate('author'),//find out what $regex and $options mean
        Author.find({ first_name: { $regex: search, $options: "i" } }),
        Genre.find({ name: { $regex: search, $options: "i" } }),
    ]);

    
    // Render the "search_result.pug" template and pass the search results as data
    res.render("search_result", {
      books: books,
      authors: authors,
      genres: genres,
    });
  });
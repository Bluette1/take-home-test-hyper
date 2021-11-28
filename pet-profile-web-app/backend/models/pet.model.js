const mongoose = require("mongoose");

const Pet = mongoose.model(
  "Role",
  new mongoose.Schema({
    name: String,
    age: Number,
    sex: String,
    weight: Number,
    color: String,
    missing:{
      type: Boolean,
      default: false,
    }
  })
);

module.exports = Pet;
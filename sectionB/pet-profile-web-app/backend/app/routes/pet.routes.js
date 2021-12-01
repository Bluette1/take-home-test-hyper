const { verifyToken } = require("../middlewares");
const controller = require("../controllers/pet.controller");
const multer = require('multer');
const DIR = __dirname +'/uploads/';

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, DIR)
  },
  filename: (req, file, cb) => {
    const fileName = file.originalname.toLowerCase().split(' ').join('-');
      cb(null, fileName + '-' + Date.now())
  }
});


const upload = multer({ storage });

module.exports = function(app) {
  app.use(function(req, res, next) {
    res.header(
      "Access-Control-Allow-Headers",
      "x-access-token, Origin, Content-Type, Accept"
    );
    next();
  });

  app.get("/api/pets", controller.getPets);

  app.get("/api/pet", controller.getPet);
  app.post("/api/pets", upload.single('image'), [verifyToken], controller.addPet);

};
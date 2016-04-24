var express = require('express');
var multer  = require('multer');
var jade = require('jade');
var fs = require('fs');
var printer = require('printer');
const exec = require('child_process').exec;


var storage =   multer.diskStorage({
  destination: function (req, file, callback) {
    callback(null, './public/uploads');
  },
  filename: function (req, file, callback) {

    callback(null,file.originalname);
  }
});
var upload = multer({ storage : storage}).single('userPhoto');




var app = express()
app.set('views', __dirname + '/views');
app.set('view engine', 'jade');

app.use(express.static(__dirname + '/public'));


app.get('/', function(req, res){
  console.log ("serving index");
  try {
     res.render('index');
  }
  catch (e) {
     console.log(e);
  }
});
app.get('/photo', function(req, res){
  fs.readdir("public/uploads", function(err,files){
    console.log(files);
    var randomfile=Math.round((Math.random() * files.length));
    console.log(randomfile);
    console.log (files[randomfile]);
    res.render('getData',{ image: files[randomfile] });
    printFile("public/uploads/"+files[randomfile]);
  })
});


app.post('/', function(req, res){
    console.log(req.body) // form fields
    console.log(req.files) // form files
    res.status(204).end()
});


app.post('/api/photo',function(req,res){
    upload(req,res,function(err) {
        if(err) {
            return res.end("Error uploading file.");
        }
        res.end("File is uploaded");
    });
});


var printFile=function(filename){
  exec("lp "+filename+" -o media='Postcard(4x6in)_Type2.FullBleed'",
  (err, stdout, stderr) => {
    if (err ){
      console.error(err);
      return;
    }
    console.log(stdout);

  });

  exec('my.bat', (err, stdout, stderr) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(stdout);
});

}



var port = 3000;
app.listen( port, function(){ console.log('listening on port '+port); } );

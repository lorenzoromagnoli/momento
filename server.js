var express = require('express');
var multer  = require('multer');
var jade = require('jade');
var fs = require('fs');
var gm = require('gm');

// var PDFDocument=require ('pdfkit');
const exec = require('child_process').exec;

var QRCode = require('qrcode');

// QRCode.toDataURL('i am a pony!',function(err,url){
//     console.log(url);
// });
// QRCode.save('public/qr/qr.png','i am a pony!',function(err,url){
//     console.log(url);
// });


PDFDocument = require ('pdfkit')



var showRandomFile=function(req, res){
  fs.readdir("public/uploads", function(err,files){
    filesNumber=files.length;
    var randomfile=Math.round((Math.random() * files.length-1));
    res.render('getData',{ image: files[randomfile] });
  })
}
var printRandomFile=function(){
  fs.readdir("public/qr", function(err,files){
    filesNumber=files.length;
    var randomfile=Math.round((Math.random() * files.length-1));
    printFile("public/qr/"+files[randomfile]);
  })
}

var storage =   multer.diskStorage({
  destination: function (req, file, callback) {
    callback(null, './public/uploads');
  },
  filename: function (req, file, callback) {
    callback(null,file.originalname);
  }
});
var upload = multer({ storage : storage}).single('userPhoto');


var createPDF=function(imagePath){

  doc = new PDFDocument({
  layout: 'portrait',
  size: [1200, 1800] // a smaller document for small badge printers
});

//var newImg= fs.createWriteStream("public/uploads/cropped_"+imagePath);

gm("public/uploads/"+imagePath)
  .resize('1200', '1200', '^')
  .gravity('Center')
  .crop('1200', '1200')
  .write("public/uploads/scaled_"+imagePath, function (err) {
    if (err) {
      console.log(err);
    }
    doc.pipe (fs.createWriteStream('public/qr/'+imagePath+'.pdf'));

     doc.image("public/uploads/scaled_"+imagePath, 0, 0, {width: 1200});
     doc.image("public/assets/emojii.png", 10, 1150);

     doc.end();


  });



}


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
  showRandomFile(req, res);
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
        showRandomFile(req, res);
        printRandomFile();

    });
});


var printFile=function(filename){
  console.log (filename);
  exec("lp '"+filename+"' -o media='Postcard(4x6in)_Type2.FullBleed' -o fit-to-page",
  function(err, stdout, stderr) {
    if (err ){
      console.error(err);
      return;
    }
    console.log(stdout);
  });
}

var blinkLed=function(){
  leds.fill(0xFF, 255, 0x00);
  leds.update();
  setTimeout(function(){
    leds.fill(0x00, 0x00, 0x00);
    leds.update();
  },2000);
}



var port = 3000;
app.listen( port, function(){ console.log('listening on port '+port); } );

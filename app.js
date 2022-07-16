const express = require('express');

const app = express();
 
app.get('/', (req, res) => {
     // index.html is the file we want to serve
        res.sendFile(__dirname + '/index.html');    
    }

);
app.get('/Contact', (req, res) => {
    // index.html is the file we want to serve
       res.sendFile(__dirname + '/contact.html');    
   }

);

app.get('/About', (req, res) => {
    // index.html is the file we want to serve
       res.sendFile(__dirname + '/about.html');    
   }

);

app.get('/Home', (req, res) => {
    // index.html is the file we want to serve
       res.sendFile(__dirname + '/home.html');    
   }

);



app.listen(8080, () => {
        console.log('Example app listening on port 8080!');
    }
    );


    app.get('/snake', (req, res) => {
        res.send('Here is a 🐍');
        }
    );
    
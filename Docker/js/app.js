const express = require('express');




const app = express();
 
app.get('/', (req, res) => {
     // index.html is the file we want to serve
        res.sendFile(__dirname + '/templates/index.html');
}
);




app.get('/Home', (req, res) => {
    // index.html is the file we want to serve
    console.log(req.query.query);

    
    res.sendFile(__dirname + '/templates/index.html');

    }
    );
    
 

    



    



app.listen(8080, () => {
        console.log(' app listening on  http://localhost:8080');
    }
    );


    app.get('/snake', (req, res) => {
        res.send('Here is a 🐍');
        }
    );
    
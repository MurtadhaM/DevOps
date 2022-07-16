const express = require('express');




const app = express();
 
app.get('/', (req, res) => {
     // index.html is the file we want to serve
        res.sendFile(__dirname + '/templates/index.html');
}
);

app.get('/Contact', (req, res) => {
    // index.html is the file we want to serve
    res.sendFile(__dirname + '/templates/contact.html');
}

);

app.get('/About', (req, res) => {
    // index.html is the file we want to serve
    res.sendFile(__dirname + '/templates/about.html');
}

);


function show_image(image_name) {
    var img = document.createElement("img");
    img.src = image_name;
    document.body.appendChild(img);
}


app.get('/Home', (req, res) => {
    // index.html is the file we want to serve
    console.log(req.query.query);

    
    res.sendFile(__dirname + '/templates/home.html');
    
    


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
    
import webbrowser
import os
import re


# styling is applied on the head part
main_head = '''
<!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://bit.ly/2s4oj3T" rel="stylesheet">
    <style>
        body {font-family: Arial, Helvetica, sans-serif;
    margin: 0;
}


.modal {
    display: none;
    position: fixed;
    z-index: 1;
    padding-top: 100px;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0,0,0,0.6);
}


.modal-content {
    background-color: rgba(0,0,0,0.6);
    margin: auto;
    padding: 20px;
    border: 1px solid #888;
    width: 15cm;
}

.close {
    color: #dfd9d9;
    float: right;
    font-size: 25px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: rgb(221, 28, 28);
    text-decoration: none;
    cursor: pointer;
}
.head {
    color: white;
    background-color: black;
    font-family: 'Times New Roman', Times, serif;
    padding: 0.2%;
    width: 35.5cm;
}
.row {
    display: grid;
    grid-template-columns: auto auto auto;
    grid-column-gap: 30px;
    grid-row-gap: 20px;
    padding: 5% 11%;
}
.column1,
.column2,
.column3,
.column4,
.column5,
.column6 {
    padding: 5%;
    border-radius: 8px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    width: 250px;
    height: 380px;
    text-indent: 0;
    float: left;
    color: white;
}

.column1:hover,
.column2:hover,
.column3:hover,
.column4:hover,
.column5:hover,
.column6:hover{
    background: red;
    border-radius: 8px;
    cursor: pointer;
}
.khan{
    text-align: center;
    font-family: 'Noto Sans', sans-serif;
}
@media only screen and (min-width: 0px) and (max-width: 500px){
    .row{
        grid-template-columns: auto;
        padding: 5% 11%;
        grid-column-gap: 30px;
        grid-row-gap: 20px;
    }
}
@media only screen and (min-width: 500px) and (max-width: 900px){
    .row{
        grid-template-columns: auto auto;
        padding: 5% 11%;
        grid-column-gap: 30px;
        grid-row-gap: 20px;
    }
}
    </style>
</head>
    <body>
    <div class="head">
        <h2>
            <b>MOVIE TRAILER</b>
            <img src="https://bit.ly/2GHftOI"
                alt="clapper" width="30" height="30">
        </h2>

    </div>
    <div class="khan">
        <h4>
            Khanon ke Khan
            <i>
                <b>KING KHAN</b>
            </i>
        </h4>
    </div>
    <div class="row">'''
# what is to be displayed is here

display = '''<div class="column1" onclick="changevideo('{trailer_youtube_url}')">
            <img src="{poster_image_url}"
                width="220" height="324">
            <figcaption>{title}</figcaption>
        </div>'''
# the main content of code goes here
content = '''</div>
    <div id="myModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <iframe width="560"
            height="315" id="myFrame" src=""
            frameborder="0" allow="autoplay; encrypted-media"
            allowfullscreen></iframe>
        </div>

    </div>

    <script>
        var modal = document.getElementById('myModal');
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
            modal.style.display = "none";
            var x = document.getElementById("myFrame")
            x.src = "https://www.youtube.com/embed/";

        }
        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
                var x = document.getElementById("myFrame")
                x.src = "https://www.youtube.com/embed/";
            }
        }
        function changevideo(vid) {
            var x = document.getElementById("myFrame")
            x.src = "https://www.youtube.com/embed/" + vid;
            modal.style.display = "block";
        }
    </script>
</body>

</html>
'''
# creation of a new file


def creation(movies):
    content = ''
    for mv in movies:
        content += display.format(
            trailer_youtube_url=mv.trailer_youtube_url,
            poster_image_url=mv.poster_image_url,
            title=mv.title
        )
    return content

# opening my new file


def open_module(movies):
    output = open('mov.html', 'w')
    rendered_content = creation(movies)

    output.write(main_head + rendered_content + content)
    output.close()
    url = os.path.abspath(output.name)
    webbrowser.open('file://' + url, new=2)

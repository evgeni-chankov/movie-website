import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>The Movie Site</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300|Ubuntu" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            font-family: 'Open Sans Condensed', sans-serif;
        }
        .navbar-brand{
            font-size: 2em;
            font-weight: bolder;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile,
        .show-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }

        .movie-tile:hover,
        .show-tile:hover {
            box-shadow: 5px 10px 10px #a8a8a8;
            cursor:pointer;
        }
        
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .movie_title{
            color: #39B3C6;
            font-family: 'Ubuntu', sans-serif;
        }
        .play-icon{
            color: #ffffff;
            position: absolute;
            height: 1em;
            width: 1em;
            margin-top: -0.3em;
            margin-left: -0.3em;
        }
        a{
            color: #39B3C6;
            outline: none !important;
        }
        .hidden{
            display:none;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened for movies
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Start playing the video whenever the trailer modal is opened for shows
        $(document).on('click', '.show-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // When clicking on menu entry shows display only shows and hide movies
        $(document).ready(function (){
            $('#shows').on('click', function(){
            $('.container-movies').addClass('hidden');
            $('.container-shows').removeClass('hidden');
            });  
        });
        // When clicking on menu entry movies display only movies and hide shows
        $(document).ready(function (){
            $('#movies').on('click', function(){
            $('.container-shows').addClass('hidden');
            $('.container-movies').removeClass('hidden');
            });  
        });
        // Change active class in menu
        $(document).ready(function (){
            $(function() {
            $("li").click(function() {
                // remove classes from all
                $("li").removeClass("active");
                // add class to the one we clicked
                $(this).addClass("active");
                });
            });  
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">The Movie Site</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#movies" id="movies">Movies</a></li>
            <li><a href="#shows" id="shows">Shows</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    </div>
    <div class="container container-movies">
      {movie_tiles}
    </div>
    <div class="container container-shows hidden">
      {show_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{movie_trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <i class="fa fa-play-circle-o fa-5x play-icon"></i>
    <img src="{movie_poster_image_url}" class="poster" width="220" height="342">
    <h2 class="movie_title">{movie_title}</h2>
    <h4>Director: {movie_director}</h4>
    <h4>Actors: {movie_main_star}</h4>
    <h4>Metascore Critic Score: {movie_metascore}</h4>
    <h5>{movie_storyline}<h5>
    <h6><a href="{movie_more_info}" target="_blank">More Information</a></h6>
</div>
'''

# A single show entry html template
show_tile_content = '''
<div class="col-md-6 col-lg-4 show-tile text-center" data-trailer-youtube-id="{show_trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <i class="fa fa-play-circle-o fa-5x play-icon"></i>
    <img src="{show_poster_image_url}" class="poster" width="220" height="342">
    <h2 class="movie_title">{show_title}</h2>
    <h4>Director: {show_director}</h4>
    <h4>Actors: {show_main_star}</h4>
    <h4>Metascore Critic Score: {show_metascore}</h4>
    <h4>Seasons: {show_seasons} ({show_start}-{show_end})</h4>
    <h5>{show_storyline}<h5>
    <h6><a href="{show_more_info}" target="_blank">More Information</a></h6>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_director=movie.director,
            movie_main_star=movie.main_star,
            movie_metascore=movie.metascore,
            movie_more_info=movie.more_info,
            movie_poster_image_url=movie.poster_image_url,
            movie_trailer_youtube_id=trailer_youtube_id
        )
    return content

def create_show_tiles_content(shows):
    # The HTML content for this section of the page
    content = ''
    for show in shows:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', show.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', show.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the show with its content filled in
        content += show_tile_content.format(
            show_title=show.title,
            show_storyline=show.storyline,
            show_director=show.director,
            show_main_star=show.main_star,
            show_metascore=show.metascore,
            show_more_info=show.more_info,
            show_poster_image_url=show.poster_image_url,
            show_trailer_youtube_id=trailer_youtube_id,
            show_seasons=show.number_seasons,
            show_start=show.starting_year,
            show_end=show.ending_year
        )
    return content


def open_movies_page(movies,shows):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        show_tiles=create_show_tiles_content(shows))
        

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
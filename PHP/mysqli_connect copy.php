<?php // mysqli_connect.php
  // connect to MySQL
  $dbc = mysqli_connect('localhost', 'brian', 'brian1', 'brianshukwit');

  mysqli_set_charset($dbc, 'utf8');

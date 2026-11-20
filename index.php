<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Source code generated using layoutit.com">
    <meta name="author" content="LayoutIt!">

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}

.topnav .icon {
  display: none;
}

@media screen and (max-width: 600px) {
  .topnav a:not(:first-child) {display: none;}
  .topnav a.icon {
    float: right;
    display: block;
  }
}

@media screen and (max-width: 600px) {
  .topnav.responsive {position: relative;}
  .topnav.responsive .icon {
    position: absolute;
    right: 0;
    top: 0;
  }
  .topnav.responsive a {
    float: none;
    display: block;
    text-align: left;
  }
}
</style>
</head>
<body>

   <div class="container">
	<div class="row">
		<div class="col-md-12">
			<p align="center">
				<img src="images/top1.png" class="d-block w-100" alt="Carousel Bootstrap First" />

			</p>
		</div>
	</div>
    </div>
<div class="container">
<div class="topnav" id="myTopnav">
  <a href="index.html" class="active">Home</a> 
  <a href="Literatures.html">Literatures</a>
  <a href="data.html">Data</a>
  
  <a href="contact.html">Contact</a>

  <a href="javascript:void(0);" class="icon" onclick="myFunction()">
    <i class="fa fa-bars"></i>
  </a>
</div>
</div>

<!--
<div class="container">

	<div class="row">
		<div class="col-md-4">
		<img class="d-block w-100" alt="Carousel Bootstrap First" src="images/p3.jpeg">
		</div>
		<div class="col-md-4">
		<img class="d-block w-100" alt="Carousel Bootstrap First" src="images/p1.jpeg">
		</div>
		<div class="col-md-4">
		<img class="d-block w-100" alt="Carousel Bootstrap First" src="images/p2.jpeg">
		</div>
	</div>
</div>

-->


<div class="container">
	<div class="carousel-inner">
		<div class="carousel-item active">
			<img class="d-block w-100" alt="Carousel Bootstrap First" src="images/cadd1.jpg" width="200" height="200">
		</div>
	</div>
</div>


<div class="container">

	<div class="jumbotron">
<!--
	<P align="center"><font color="red" size="6"><a href="http://neist.res.in/ddh2020/registration/" style="color:red;">REGISTER HERE</a></font></p>
-->
	<div class="row">
		<div class="col-md-12">
			<h2>Some text</h2>
				<form action="prediction.php" method="post" enctype="multipart/form-data">
				  <div class="form-group">
					<label for="fileToUpload">Input</label>
					<input type="file" class="form-control" name="fileToUpload" id="fileToUpload">
				  </div> 
				  <button type="submit" class="btn btn-default">Submit</button>
				</form>
        </div>
    </div>	
	</div>
</div>



<div class="container">
			
</div>

<div class="container">
			<table class="table table-sm table-striped">

					
					<tr style="background-color:#000000">
						<td align="center"><font size="2" color="white">NIPER Guwahati, Assam. All Rights Reserved</font></td>
					</tr>
			</table>
</div>



<script>
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
</script>

</body>
</html>

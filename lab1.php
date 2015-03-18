<?php include('header.php'); ?>
<?php include('navbar.php'); ?>

<?php
	print '
	<div class="page-header">
  	<h1>XSS: <small>Between tags</small></h1>
	</div>
	';


?>

	<form name="XSS" action="lab1.php" method="post">
	<div class="input-group">
		<input type="text" class="form-control" placeholder="Input text"  name="input" aria-describedby="basic-addon1">
		<span class="input-group-btn">
			<button class="btn btn-default" type="submit">Search</button>
		</span>
	</div>
	</form>
	<br>
	<?php
			 
		if ($_POST["input"]== ""){
			
		}
		else{
			$texto = $_POST["input"];
			print $texto;	

			print '
			    <p>
				<div class="panel panel-danger">
				<div class="panel-heading">
				 Incerted input incorrectly escaped.
				</div>
				<div class="panel-body">
				';
			
			print "<pre><i>".htmlspecialchars($texto)."</i></pre>";
			
			print '
					</div>
						
					   </div>

					<div class="panel panel-success">
						<div class="panel-heading">	
					Incerted input correctly escaped.
					    </div>
					    <div class="panel-body">
				  ';
			
			print "<pre><i>".htmlspecialchars(htmlspecialchars($texto))."</i></pre>";
			print "</div>	
				   </div>
				   </p>
				  ";
		}
	?>

<?php include('footer.php'); ?>
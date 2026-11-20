<?php

$target_dir = "server-test/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
/*
$flag=0;
$sdfFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if file already exists
if (file_exists($target_file)) {
  echo " file already exists.";
  $uploadOk = 1;
}

// Allow certain file formats
if($sdfFileType != "sdf" ) {
  echo "Sorry, only sdf file is allowed.";
  $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
  echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
}else{
	if (move_uploaded_file('/opt/lampp/temp/', $target_file)) {
		echo "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded.";
		$flag=1;
		
	}else {
		echo "Sorry, there was an error uploading your file.\n";
		echo $_FILES["fileToUpload"]["tmp_name"];
	}
}
*/
$flag=1;
$target_dir='server_test/';
$o_file='Acebutolol';
if($flag==1){
	#echo "Good to go";
	#shell_exec('chmod 777 $_FILES["fileToUpload"]["tmp_name"]');
	#echo "python script is running please wait";
	$output='testing';
	#$output= shell_exec("python server_test/SOS-predictor1-post-Docking-mod-4.py");
	if($output !='')
		#echo $output;
		#$target_dir = "server_test/";
		$filename='Accesibility_Model_NEW.csv'; ## change if needed
		echo $filename;
		$str='<html><body>
			<table class="table">
			<thead>
				<tr> 
				<th scope="col">Ligand</th>
				<th scope="col">AtomID</th>
				<th scope="col">Pose_No</th>
				<th scope="col">Dock_Score</th>
				<th scope="col">Atom</th>
				<th scope="col">AtomNo</th>
				<th scope="col">Dist_from_Fe</th>
				<th scope="col">BDE</th>
				<th scope="col">BDE_dist</th>
				<th scope="col">Sub-Non_sub</th>
				<th scope="col">SOS</th>
				</tr>
			</thead>';
		$str_rows='';
		$open = fopen($filename, "r");
		while (($line = fgetcsv($open)) !== false) {
			echo "in while";
			$str_rows=$str_rows."<tr>";
			foreach ($line as $cell){
				$str_rows=$str_rows. "<td>" . htmlspecialchars($cell) . "</td>";
			}
			$str_rows=$str_rows."</tr>";
		}
		$final_str=$str.$str_rows."</tbody></table>
		<div><p><img src=\"".$o_file."..png\" class=\"img-fluid\" alt=\"Responsive image\"></p></div>
		</body></html>";
		echo $final_str;
		fclose($open);
	
}
*/
?>

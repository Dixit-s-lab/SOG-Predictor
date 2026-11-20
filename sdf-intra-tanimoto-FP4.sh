for i in $(ls *IN.sdf | sed 's/.sdf//')
do
    echo "Processing molecule: $i"

    # Generate 3D coordinates using the distance geometry method
    echo "Generating 3D coordinates for $i"
    obabel $i.sdf -O $i_3D.sdf --gen3D

    # Calculate molecular fingerprints for the 3D coordinates
    echo "Calculating fingerprints for $i"
    obabel $i_3D.sdf *.sdf -ofpt -xfFP4 | grep -v Possible | awk '{print $1,$6}' > $i-FP4.txt

    # Clean up temporary 3D SDF file
    rm $i_3D.sdf

    echo "Completed processing for $i"
done


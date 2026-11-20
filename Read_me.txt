# Site of Glucuronidation (SOG) Predictor

# 1. Introduction

Glucuronidation is an important Phase II metabolic reaction catalyzed by UDP-glucuronosyltransferase (UGT) enzymes. It plays a major role in drug metabolism and elimination by increasing the polarity and facilitating the excretion of various endogenous and xenobiotic compounds. Therefore, identifying potential UGT substrates and their sites of glucuronidation (SOG) is important in drug discovery, metabolism, and toxicological assessment.

The **SOG Predictor** is a computational tool designed to classify query molecules containing at least one hydroxyl (OH) group as potential UGT substrates or non-substrates. It also identifies potential sites of glucuronidation in molecules classified as substrates.

The SOG Predictor uses the **ACM-VS/HAC_PCA-pKa algorithm**, which integrates molecular accessibility and chemical reactivity parameters through a two-stage prediction approach.

- **Substrate classification:** The ACM-VS/HAC model is used to assess molecular accessibility and classify query molecules as potential UGT substrates or non-substrates.
- **Site-of-glucuronidation prediction:** The RCA-pKa model is used to assess the reactivity of individual hydroxyl groups. The pKa of each OH group is considered as the reactivity parameter for identifying potential glucuronidation sites.

The datasets used for model development, including substrate, non-substrate, and validation datasets, are provided in SDF format.

# Features

* **Substrate Prediction:** Classifies query molecules as potential UGT substrates or non-substrates.
* **Site Identification:** Identifies potential hydroxyl-group sites of glucuronidation in predicted UGT substrates.
* **Accessibility Assessment:** Uses the ACM-VS/HAC model to evaluate molecular accessibility for substrate classification.
* **Reactivity Assessment:** Uses the RCA-pKa model to evaluate hydroxyl-group reactivity based on pKa values.
* **User-Friendly Interface:** Provides an easy-to-use workflow for predicting UGT substrate potential and glucuronidation sites.

# 2. System Requirements

Before you begin, ensure that your system meets the following requirements:

* OS: Linux
* Python 3.6 or later
* Dependencies specified in the `requirements.txt` file

To ensure the seamless operation of the SOG Predictor, all dependencies specified in the `requirements.txt` file must be installed correctly. The required software and libraries should also be available in the user path (`.bashrc` file).

It is recommended to set up a Conda environment containing the required Python libraries. If Conda is not installed, it can be obtained from the official website:

https://www.anaconda.com/

Detailed installation instructions are available on the Conda website.

# 3. Installation

Follow these steps to install the SOG Predictor:

1. Download the Phase-II-prediction-main directory or clone the repository using the command:

   `gh repo clone Dixit-s-lab/Phase-II-prediction`

2. Extract the downloaded archive, if applicable:

   `unzip Phase-II-prediction-main.zip`

3. Navigate to the SOG Predictor directory:

   `cd SOG-Predictor`

4. Install the required dependencies:

   `pip install -r requirements.txt`

Alternatively, the dependencies can be installed manually. If manual installation is performed, ensure that the required software paths are correctly configured in the `.bashrc` file.

# 4. Usage

After installing the required software and dependencies and updating the paths in the `.bashrc` file, follow these steps to perform SOG prediction.

1. Place a single molecule in SDF format inside the `SOG_predictor` directory. For example, `dopamine.sdf`.

2. Ensure that the input molecule contains at least one hydroxyl (OH) group. Molecules without an OH group will not be processed for SOG prediction.

3. Execute the following command to run the SOG Predictor:

   `python SOG_single_ligand.py`

4. The SOG Predictor will first classify the input molecule as a potential UGT substrate or non-substrate using the ACM-VS/HAC model.

5. For molecules classified as potential UGT substrates, the RCA-pKa model will assess the reactivity of individual hydroxyl groups using their pKa values and identify potential sites of glucuronidation.

6. The tool will generate a `Results` directory inside the SOG Predictor folder. The prediction results will be saved in CSV format and displayed on the terminal.

The output includes the following information:

* **Ligand:** Name or identifier of the input molecule.
* **AtomNo:** Atom number corresponding to the evaluated hydroxyl group.
* **Substrate/Non-substrate:** Predicted UGT substrate classification.
* **Site_of_glucuronidation:** Predicted glucuronidation site for potential UGT substrates.

# 5. License

The SOG Predictor is available under the Creative Commons license and is free for academic research groups working in degree-granting universities or institutes.

Any work, report, thesis, research article, or review article resulting from the use of the SOG Predictor should appropriately cite the software and its associated publication.

For commercial use of the SOG Predictor, please contact:

vaibhavadixit@gmail.com  
vaibhav@niperguwahati.in

# 6. Developer

This tool was developed by **Shivam Kumar Vyas (PhD Research Scholar)** under the supervision of **Dr. Vaibhav A. Dixit, Assistant Professor, Department of Medicinal Chemistry, NIPER Guwahati**, at the Advanced Center of Computer-Aided Drug Design (A-CADD).

The SOG Predictor, its GUI, websites, tools, layouts, and logos are subject to copyright protection and are the exclusive property of the Department of Medicinal Chemistry, NIPER Guwahati.

The name and logos of NIPER Guwahati must not be associated with publicity or business promotion without prior written approval from NIPER Guwahati.

# 7. Troubleshooting

If you encounter any issues or errors during installation or usage, please contact:

vyasshivam16@gmail.com  
vaibhavadixit@gmail.com
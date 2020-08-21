{
// Reads the XRF absorbtion data as well as mass attenuation coefficients from
// input file,
// Calculates the thickness of absorber foil

gROOT->Reset();

ifstream spectrum;
char filename[128];
std::string LineBuffer;

Int_t i,j,k, ncal=0;
Float_t mac[10], E[10];
Float_t t, E0, I0=0, I1=0, ln_mac=0, ur=0;

const int numbins = 4096;

// **************************** //
// Reading input file data
// **************************** //

sprintf(filename,"C:/KLASSE/Fis384/XRF_data2019/Cr_mac_gr2.txt");
spectrum.open(filename);

if(spectrum.is_open()){
	cout << "starts mca conversion" << endl;
//	cout << " input: " << filename << "\n output: " << fileout << endl;
	spectrum >> LineBuffer;
	spectrum >> E0;
	spectrum >> I0;
	spectrum >> I1;
	spectrum >> LineBuffer;
	spectrum >> LineBuffer;
	i=0;
	while(! spectrum.eof()){
		spectrum >> E[i];
		spectrum >> mac[i];
		printf("E: %f \t MAC: %f \n",E[i],mac[i]);
		i++;
	}
	ncal=i;
}	
else cout<< "Nope! File not opened!"<<endl;

// ********************************************************************* //
// Calculate mass attenuation coefficient at E0 energy
// ********************************************************************* //
Float_t X[ncal];
Float_t Y[ncal];

for(int k=0;k<ncal;k++){
	X[k]=log(E[k]);
	Y[k]=log(mac[k]);
}	

TGraph *gr = new TGraph(ncal,X,Y);
gr->Draw("A*");
gr->Fit("pol1");

Double_t *par;
par = pol1->GetParameters();

ln_mac = par[1]*log(E0)+par[0];
ur = exp(ln_mac);

printf("Mass att. coeff. at %f keV : %f cm2/mg \n",E0,ur);

// ********************************************************************* //
// Calculate density thickness
// ********************************************************************* //
t = -log(I1/I0)/ur;

printf("Thickness of foil: %f mg/cm2 \n",t);

}
